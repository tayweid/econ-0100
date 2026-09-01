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



# ---------------------------------------------------------------- the ladder
# Choices are rungs at heights; higher is preferred. Episode-local choreography.
class Ladder(VGroup):
    """items: names top -> bottom. Rungs are evenly spaced on a muted rail."""

    def __init__(self, items, height=4.2, width=2.4, label=None, label_scale=0.7, **kwargs):
        super().__init__(**kwargs)
        self.h, self.w = height, width
        self.rail = Line(DOWN * height / 2, UP * height / 2, color=MUTED, stroke_width=2).shift(LEFT * width / 2)
        self.rungs = {}
        self.order = list(items)
        self.label_scale = label_scale
        self.add(self.rail)
        for i, name in enumerate(items):
            r = self._make_rung(name)
            r.move_to(self.rail.get_center() + RIGHT * self.w / 2 + UP * self.y_of(i))
            self.rungs[name] = r
            self.add(r)
        self.title = None
        if label is not None:
            self.title = Tex(label).scale(0.8).set_color(MUTED).next_to(self.rail, UP, buff=0.25)
            self.add(self.title)
        self.scale_numbers = None

    def _make_rung(self, name):
        line = Line(LEFT * self.w / 2, RIGHT * self.w / 2, color=INK, stroke_width=3)
        text = Tex(name).scale(self.label_scale).next_to(line, UP, buff=0.08)
        return VGroup(line, text)

    def y_of(self, i):
        n = max(len(self.order), 2)
        step = self.h / (n + 0.5)
        return self.h / 2 - step * (i + 0.75)

    def rung(self, name):
        return self.rungs[name]

    def target_for(self, name, order=None):
        order = order or self.order
        return self.rail.get_center() + RIGHT * self.w / 2 + UP * self.y_of(order.index(name))

    def reorder(self, new_order):
        """Animations moving existing rungs to a new order (and adding/removing)."""
        anims = []
        for name in list(self.rungs):
            if name not in new_order:
                anims.append(FadeOut(self.rungs[name]))
                self.remove(self.rungs[name]); del self.rungs[name]
        self.order = list(new_order)
        for name in new_order:
            if name in self.rungs:
                anims.append(self.rungs[name].animate.move_to(self.target_for(name)))
            else:
                r = self._make_rung(name).move_to(self.target_for(name))
                self.rungs[name] = r; self.add(r)
                anims.append(FadeIn(r, shift=0.2 * DOWN))
        if self.scale_numbers is not None:
            anims += self._scale_anims()
        return anims

    def relabel(self, new_names):
        """Swap the text on each rung in place (same heights). Returns animations."""
        anims = []
        for old, new in zip(self.order, new_names):
            r = self.rungs.pop(old)
            t = Tex(new).scale(self.label_scale).move_to(r[1])
            anims.append(Transform(r[1], t))
            self.rungs[new] = r
        self.order = list(new_names)
        return anims

    # -- number scale beside the ladder (utility)
    def add_scale(self, values, side=LEFT, color=MUTED):
        """values: number per rung, top -> bottom. Returns the VGroup to FadeIn."""
        self.values = list(values)
        nums = VGroup()
        for name, v in zip(self.order, values):
            n = Integer(v, group_with_commas=False).scale(0.6).set_color(color)
            n.next_to(self.rungs[name][0], side, buff=0.25)
            nums.add(n)
        self.scale_numbers = nums
        self.add(nums)
        return nums

    def _scale_anims(self):
        return [n.animate.next_to(self.rungs[name][0], LEFT, buff=0.25)
                for n, name in zip(self.scale_numbers, self.order)]

    def relabel_scale(self, values):
        anims = []
        for n, v in zip(self.scale_numbers, values):
            anims.append(n.animate.set_value(v))
        self.values = list(values)
        return anims

    def remove_scale(self):
        nums = self.scale_numbers
        self.scale_numbers = None
        self.remove(nums)
        return FadeOut(nums)

    # -- brackets: benefit / cost as heights
    def height_bracket(self, name, text, color=INK, side=RIGHT):
        """A brace from the rail's foot up to the rung, labelled. Height = value."""
        foot = self.rail.get_bottom()
        top = np.array([foot[0], self.rungs[name][0].get_center()[1], 0])
        x = self.rail.get_center()[0] + (self.w / 2) + (self.w / 2 + 0.35) * side[0]
        seg = Line([x, foot[1], 0], [x, top[1], 0])
        brace = Brace(seg, side, buff=0.1).set_color(color)
        lab = brace.get_text(text).scale(0.7).set_color(color)
        return VGroup(brace, lab)

    def next_best_arrow(self, src, dst, color=MUTED):
        a = self.rungs[src][0].get_right() + RIGHT * 0.15
        b = self.rungs[dst][0].get_right() + RIGHT * 0.15
        return CurvedArrow(a, b, angle=-TAU / 6, color=color)


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
        self.notes = NotesPanel()
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
        self.b43_next_time()
        self.b44_six_parts()

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
        ax = on_model(style_axes([0, WINDOW], [0, y_max]))
        labels = axis_caption(ax, 'Unemployment rate (\\%)')

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
        axes = on_model(style_axes([1920, 1940, 5], [0, 600, 100]))
        x_nums = VGroup(*[Integer(y, group_with_commas=False).scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(y, 0), DOWN) for y in range(1920, 1941, 5)])
        y_nums = VGroup(*[Tex(f'\\${v}').scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(1920, v), LEFT) for v in (100, 200, 300, 400, 500, 600)])
        ylab = axis_caption(axes, 'U.S. private wealth (billions)')

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
        trough = Dot(axes.c2p(1933, w[i33]), color=GUIDE, z_index=10)
        trough_label = Tex(f'1933: \\${w[i33]:.0f}bn').scale(0.8).next_to(trough, DOWN)
        self.play(FadeIn(trough), FadeIn(trough_label))
        self.wait()
        self.play(Create(after), run_time=2, rate_func=linear)
        self.notes.add(self, 'Where did the wealth go?')
        self.wait(2)
        self.play(FadeOut(VGroup(axes, x_nums, y_nums, ylab, rise, fall, after,
                                 peak, peak_label, trough, trough_label)))

    # ------------------------------------------------------------ B05 [new]
    def b05_cities(self):
        """NASA Black Marble with the 30 largest cities overlaid; ports vs inland."""
        beat(self, 'B05_cities')
        earth = ImageMobject(NIGHT_MAP)
        earth.set_width(MODEL_WIDTH).move_to(MODEL_CENTER)   # 2:1 image fills the model region
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
        ).arrange(RIGHT, buff=0.6).next_to(earth, DOWN, buff=0.2).align_to(earth, LEFT)
        self.play(FadeIn(key))
        self.notes.add(self, f'Why do we crowd the coasts? ({n_port} of {n} cities are ports)')
        self.wait(2)
        self.play(FadeOut(key), FadeOut(dots), FadeOut(earth))


    # ------------------------------------------------------------ B10-B15  preferences
    def b10_preferences(self):
        beat(self, 'B10_cakes')
        self.behavior_title = on_model(title('This class is about behavior.'))
        self.play(FadeIn(self.behavior_title))

        cakes = on_model(tex_row(['Carrot Cake', '$\\succ$', 'Chocolate Cake']))
        self.play(FadeIn(cakes, lag_ratio=0.3))
        self.wait()
        self.play(FadeOut(cakes))

        beat(self, 'B11_coffee')
        coffee = on_model(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast']))
        self.play(FadeIn(coffee, lag_ratio=0.3))
        self.wait()

        beat(self, 'B12_transitivity')
        coffee3 = on_model(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast', '$\\succ$', 'Light Roast']))
        self.play(Transform(coffee, coffee3))
        self.wait()
        arc = ArcBetweenPoints(coffee3[0].get_top() + 0.1 * UP, coffee3[4].get_top() + 0.1 * UP,
                               angle=-TAU / 4).set_color(FOCUS)
        self.play(Create(arc))
        self.wait()
        self.play(FadeOut(arc))

        beat(self, 'B13_chain_stands_up')
        # the chain stands up into the ladder
        self.ladder = Ladder(['Dark Roast', 'Medium Roast', 'Light Roast']).move_to(MODEL_CENTER + DOWN * 0.3)
        self.play(
            Transform(coffee[0], self.ladder.rung('Dark Roast')[1]),
            Transform(coffee[2], self.ladder.rung('Medium Roast')[1]),
            Transform(coffee[4], self.ladder.rung('Light Roast')[1]),
            FadeOut(coffee[1]), FadeOut(coffee[3]),
            Create(self.ladder.rail),
            *[Create(self.ladder.rung(n)[0]) for n in self.ladder.order],
            run_time=1.5,
        )
        self.remove(coffee)
        self.add(self.ladder)
        self.wait()
        self.play(*self.ladder.reorder(['Espresso', 'Dark Roast', 'Medium Roast', 'Light Roast', 'Decaf']))
        self.wait()

        beat(self, 'B14_rank_anything')
        self.play(*self.ladder.relabel(['Fall', 'Spring', 'Summer', 'Winter', 'Mud season']))
        self.wait()
        self.play(*self.ladder.relabel(['Mushroom', 'Pepperoni', 'Plain', 'Olive', 'Pineapple']))
        self.wait()
        self.play(*self.ladder.relabel(['Espresso', 'Dark Roast', 'Medium Roast', 'Light Roast', 'Decaf']))

        beat(self, 'B15_preferences_are_rankings')
        card = on_model(definition('Preferences', 'are rankings.')).to_edge(DOWN, buff=0.6)
        self.play(AddTextWordByWord(card))
        self.wait()
        self.notes.file(self, card, 'Preferences are rankings.', term='Preferences')

    # ------------------------------------------------------------ B16-B21  utility
    def b16_utility(self):
        beat(self, 'B16_numbers')
        L = self.ladder
        self.play(L.animate.shift(LEFT * 1.8))
        nums = L.add_scale([9, 7, 5, 3, 1])
        self.play(FadeIn(nums, lag_ratio=0.2))
        self.wait()

        beat(self, 'B17_utility_definition')
        card = on_model(definition('Utility', 'is a number that does the ranking for us.')).to_edge(DOWN, buff=0.6)
        self.play(AddTextWordByWord(card))
        self.wait()
        self.notes.file(self, card, 'Utility: a number that ranks for us.', term='Utility')

        beat(self, 'B18_mine_and_yours')
        me = Tex('Me').scale(0.8).set_color(MUTED).next_to(L.rail, UP, buff=0.3)
        yours = Ladder(['Light Roast', 'Decaf', 'Medium Roast', 'Espresso', 'Dark Roast'])
        yours.move_to(L.rail.get_center() + RIGHT * 4.2)
        ynums = yours.add_scale([8, 6, 5, 2, 1])
        you = Tex('You').scale(0.8).set_color(MUTED).next_to(yours.rail, UP, buff=0.3)
        self.play(FadeIn(me), FadeIn(yours), FadeIn(you))
        self.wait()

        beat(self, 'B19_benefits')
        cap = Tex('benefit').scale(0.7).set_color(MUTED).rotate(PI / 2).next_to(L.rail, LEFT, buff=0.9)
        arrow = Arrow(L.rail.get_bottom() + LEFT * 1.4, L.rail.get_top() + LEFT * 1.4, color=MUTED, buff=0, stroke_width=2, max_tip_length_to_length_ratio=0.06)
        self.play(FadeOut(nums), FadeOut(ynums), FadeIn(arrow), FadeIn(cap))
        self.wait()
        self.play(FadeOut(arrow), FadeOut(cap), FadeIn(nums), FadeIn(ynums))

        beat(self, 'B20_times_100')
        self.play(*L.relabel_scale([900, 700, 500, 300, 100]), *yours.relabel_scale([800, 600, 500, 200, 100]))
        self.wait()
        self.play(*L.relabel_scale([9, 7, 5, 3, 1]), *yours.relabel_scale([8, 6, 5, 2, 1]))
        self.wait()

        beat(self, 'B21_preferences_change')
        self.play(FadeOut(yours), FadeOut(you), FadeOut(me), L.remove_scale())
        self.play(L.animate.move_to(MODEL_CENTER + DOWN * 0.3))
        self.play(*L.reorder(['Coffee', 'Tea']))
        self.wait()
        self.play(*L.reorder(['Tea', 'Coffee']), run_time=1.5)
        self.wait()
        self.play(FadeOut(L), FadeOut(self.behavior_title))
        self.ladder = None

    # ------------------------------------------------------------ B22-B25  scarcity
    def b22_scarcity(self):
        beat(self, 'B22_cant_always')
        self.scarcity_title = on_model(title('This class is about scarcity.'))
        self.play(FadeIn(self.scarcity_title))
        q1 = on_model(Tex("We can't always have what we want most."))
        self.play(AddTextWordByWord(q1))
        self.wait()
        self.notes.file(self, q1, "We can't always have what we want most.")

        beat(self, 'B23_scarcity_basic')
        q2 = on_model(definition('Scarcity', 'is more basic than money.'))
        self.play(Write(q2))
        self.wait()
        self.notes.file(self, q2, 'Scarcity is more basic than money.', term='Scarcity')

        beat(self, 'B24_house_or_movies')
        big = VGroup(house(1.6), tickets(2)).arrange(DOWN, buff=0.35)
        big_lab = Tex('near the park, fewer movies').scale(0.6).set_color(MUTED).next_to(big, DOWN, buff=0.25)
        small = VGroup(house(0.9), tickets(6)).arrange(DOWN, buff=0.35)
        small_lab = Tex('far from the park, more movies').scale(0.6).set_color(MUTED).next_to(small, DOWN, buff=0.25)
        OR = Tex('or').scale(1.2)
        A = VGroup(big, big_lab); B = VGroup(small, small_lab)
        row = VGroup(A, OR, B).arrange(RIGHT, buff=1.2)
        on_model(row).shift(DOWN * 0.2)
        self.play(FadeIn(A))
        self.play(FadeIn(OR))
        self.play(FadeIn(B))
        self.wait()
        self.play(FadeOut(row))

        beat(self, 'B25_who_gets_the_house')
        h = house(1.8).move_to(MODEL_CENTER + DOWN * 0.2)
        who = Tex('Taylor').scale(0.9).next_to(h, DOWN, buff=0.3)
        caption = Tex('who gets the nice house?').scale(0.7).set_color(MUTED).next_to(h, UP, buff=0.5)
        self.play(FadeIn(h), FadeIn(who), FadeIn(caption))
        self.wait()
        for name in ['Andrew', 'Taylor', 'Andrew']:
            self.play(Transform(who, Tex(name).scale(0.9).move_to(who)), run_time=0.6)
            self.wait(0.4)
        self.play(FadeOut(h), FadeOut(who), FadeOut(caption), FadeOut(self.scarcity_title))

    # ------------------------------------------------------------ B26-B27  choices
    def b26_choices(self):
        beat(self, 'B26_choices_because')
        q = on_model(Tex('We make choices because of preferences and scarcity.'))
        self.play(AddTextWordByWord(q))
        self.wait()
        self.notes.file(self, q, 'Preferences and scarcity force choices.')

        beat(self, 'B27_choices_equation')
        eq = on_model(tex_row(['Preferences', '$+$', 'Scarcity', '$\\Rightarrow$', 'Choices'], color=DEFINITION, buff=0.4))
        for piece in eq:
            self.play(FadeIn(piece), run_time=0.6)
        self.wait()
        self.notes.file(self, eq)

    # ------------------------------------------------------------ B28-B32  tradeoffs
    def b28_tradeoffs(self):
        beat(self, 'B28_A_or_B')
        self.tradeoff_title = on_model(title('This class is about tradeoffs.'))
        self.play(FadeIn(self.tradeoff_title))
        OR = Tex(' or ').scale(1.5).move_to(MODEL_CENTER)
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(A)); self.wait(0.5)
        self.play(FadeIn(OR)); self.wait(0.5)
        self.play(FadeIn(B)); self.wait()
        # one or the other, never both
        box = SurroundingRectangle(A, buff=0.3).set_color(FOCUS)
        self.play(Create(box))
        for target in [B, A, B, A]:
            self.play(box.animate.move_to(target), run_time=0.5)
            self.wait(0.3)

        beat(self, 'B29_benefit')
        self.play(box.animate.set_color(EFFICIENT))
        self.wait()
        # lift onto a two-rung ladder
        L = Ladder(['A', 'B'], height=3.6, width=1.6, label_scale=1.0).move_to(MODEL_CENTER + DOWN * 0.4)
        self.play(
            FadeOut(OR), FadeOut(box),
            Transform(A, L.rung('A')[1]), Transform(B, L.rung('B')[1]),
            Create(L.rail), Create(L.rung('A')[0]), Create(L.rung('B')[0]),
        )
        self.remove(A, B); self.add(L)
        ben = L.height_bracket('A', 'benefit', color=EFFICIENT, side=LEFT)
        self.play(FadeIn(ben))
        self.wait()

        beat(self, 'B30_cost')
        cost = L.height_bracket('B', 'cost', color=NASH, side=RIGHT)
        self.play(FadeIn(cost))
        note = Tex('cost of {{A}} = value of {{B}}').scale(0.8).set_color_by_tex_to_color_map({'A': EFFICIENT, 'B': NASH})
        note.next_to(L, DOWN, buff=0.5)
        self.play(Write(note))
        self.wait()

        beat(self, 'B31_opportunity_cost_definition')
        oc = on_model(definition('Opportunity Cost', 'is the value of the next best alternative.')).to_edge(UP, buff=1.6)
        self.play(FadeOut(self.tradeoff_title), AddTextWordByWord(oc))
        self.wait()
        self.notes.file(self, oc, 'Opportunity Cost: the value of the next best alternative.', term='Opportunity Cost')

        beat(self, 'B32_switch')
        eq1 = Tex('OC({{A}}) = {{B}}').scale(0.9).set_color_by_tex_to_color_map({'A': EFFICIENT, 'B': NASH}).next_to(L, RIGHT, buff=1.6)
        self.play(Transform(note, eq1))
        self.wait()
        self.play(*L.reorder(['B', 'A']), FadeOut(ben), FadeOut(cost), run_time=1.2)
        ben2 = L.height_bracket('B', 'benefit', color=EFFICIENT, side=LEFT)
        cost2 = L.height_bracket('A', 'cost', color=NASH, side=RIGHT)
        eq2 = Tex('OC({{B}}) = {{A}}').scale(0.9).set_color_by_tex_to_color_map({'B': EFFICIENT, 'A': NASH}).move_to(eq1)
        self.play(FadeIn(ben2), FadeIn(cost2), Transform(note, eq2))
        self.wait()
        self.play(FadeOut(L), FadeOut(ben2), FadeOut(cost2), FadeOut(note))

    # ------------------------------------------------------------ B33-B34  grocery
    def b33_grocery(self):
        beat(self, 'B33_apple_or_banana')
        head = on_model(title('Forbes Ave Grocery'))
        self.play(FadeIn(head))
        ap = VGroup(apple(), Tex('apple \\$1').scale(0.7)).arrange(DOWN, buff=0.25)
        ba = VGroup(banana(), Tex('banana \\$1').scale(0.7)).arrange(DOWN, buff=0.25)
        OR = Tex('or')
        row = on_model(VGroup(ap, OR, ba).arrange(RIGHT, buff=1.2))
        self.play(FadeIn(row))
        self.wait()
        pick = SurroundingRectangle(ap, buff=0.25).set_color(EFFICIENT)
        self.play(Create(pick), ba.animate.set_color(MUTED))
        oc = Tex('OC(apple) = banana').scale(0.8).next_to(row, DOWN, buff=0.6)
        self.play(Write(oc))
        self.wait()
        self.play(FadeOut(row), FadeOut(pick), FadeOut(oc))

        beat(self, 'B34_cost_of_a_dollar')
        L = Ladder(['Apple', 'Orange', 'Chocolate', 'Bike share'], height=3.8).move_to(MODEL_CENTER + DOWN * 0.3)
        c = coin().next_to(L.rail, DOWN, buff=0.2)
        q = Tex('what can a dollar get?').scale(0.7).set_color(MUTED).next_to(L, UP, buff=0.3)
        self.play(FadeIn(c), FadeIn(q))
        self.play(Create(L.rail), *[FadeIn(L.rung(n), shift=0.2 * DOWN) for n in L.order], lag_ratio=0.2)
        self.wait()
        top = L.height_bracket('Apple', 'OC(\\$1) = max', color=NASH, side=RIGHT)
        self.play(FadeIn(top))
        self.wait()
        # chocolate climbs
        self.play(FadeOut(top))
        self.play(*L.reorder(['Chocolate', 'Apple', 'Orange', 'Bike share']), run_time=1.5)
        top2 = L.height_bracket('Chocolate', 'OC(\\$1) = max', color=NASH, side=RIGHT)
        flip = Tex('the choice flips').scale(0.7).set_color(FOCUS).next_to(L, LEFT, buff=0.8)
        self.play(FadeIn(top2), FadeIn(flip))
        self.wait()
        self.play(FadeOut(L), FadeOut(c), FadeOut(q), FadeOut(top2), FadeOut(flip), FadeOut(head))

    # ------------------------------------------------------------ B35-B36  bakery
    def b35_bakery(self):
        beat(self, 'B35_pie_or_bread')
        head = on_model(title('The bakery'))
        self.play(FadeIn(head))
        L = Ladder(['Apple pie', 'Banana bread'], height=3.6, width=2.8).move_to(MODEL_CENTER + LEFT * 1.2 + DOWN * 0.3)
        self.play(Create(L.rail), *[FadeIn(L.rung(n)) for n in L.order])
        a1 = L.next_best_arrow('Apple pie', 'Banana bread')
        oc1 = Tex('OC(pie) = banana bread').scale(0.8).next_to(L, RIGHT, buff=1.6)
        self.play(Create(a1), Write(oc1))
        self.wait()

        beat(self, 'B36_carrot_cake')
        self.play(FadeOut(a1), FadeOut(oc1))
        self.play(*L.reorder(['Carrot cake', 'Apple pie', 'Banana bread']), run_time=1.2)
        self.wait()
        arrows = VGroup(
            L.next_best_arrow('Apple pie', 'Carrot cake'),
            L.next_best_arrow('Banana bread', 'Carrot cake'),
            L.next_best_arrow('Carrot cake', 'Apple pie'),
        )
        table = VGroup(
            Tex('OC(cake) = pie'),
            Tex('OC(pie) = cake'),
            Tex('OC(bread) = cake'),
        ).arrange(DOWN, buff=0.3, aligned_edge=LEFT).scale(0.8).next_to(L, RIGHT, buff=1.8)
        for arrow, line in zip([arrows[2], arrows[0], arrows[1]], table):
            self.play(Create(arrow), Write(line))
            self.wait(0.5)
        self.wait()
        self.play(FadeOut(L), FadeOut(arrows), FadeOut(table), FadeOut(head))

    # ------------------------------------------------------------ B37  marginal
    def b37_marginal(self):
        beat(self, 'B37_one_more_apple')
        head = on_model(title('One more apple?'))
        self.play(FadeIn(head))
        benefits = [9, 7, 5, 3, 1]
        cost = 4
        unit = 0.32
        base_y = MODEL_CENTER[1] - 1.6
        cols = VGroup()
        for i, b in enumerate(benefits):
            bar = Rectangle(width=0.7, height=b * unit, color=EFFICIENT, fill_color=EFFICIENT, fill_opacity=AREA_OPACITY, stroke_width=2)
            bar.move_to([0, base_y + b * unit / 2, 0])
            glyph = apple(0.22).next_to(bar, DOWN, buff=0.15)
            cols.add(VGroup(bar, glyph))
        cols.arrange(RIGHT, buff=0.45, aligned_edge=DOWN)
        cols.move_to([MODEL_CENTER[0], cols.get_center()[1], 0])
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
        line = on_model(Tex('{{Marginal}} means one more.').set_color_by_tex_to_color_map({'Marginal': DEFINITION})).to_edge(DOWN, buff=0.5)
        self.play(Write(line))
        self.wait()
        self.notes.file(self, line, 'Marginal means one more.', term='Marginal')
        self.play(FadeOut(cols), FadeOut(cost_line), FadeOut(cost_lab), FadeOut(mb_lab), FadeOut(marks), FadeOut(head))

    # ------------------------------------------------------------ B38-B41
    def b38_social(self):
        beat(self, 'B38_autarky')
        social_title = on_model(title('This class is about social environments.'))
        self.play(FadeIn(social_title))
        aut = on_model(definition('Autarky', 'is a state of economic self-sufficiency.'))
        self.play(AddTextWordByWord(aut))
        self.wait()
        self.notes.file(self, aut, 'Autarky: economic self-sufficiency.', term='Autarky')

        beat(self, 'B39_dating_game')
        # rows = you, columns = your love interest
        table = Table(
            [['10', '$-1$'],
             ['$-1$', '8']],
            row_labels=[Tex('Movie'), Tex('Theater')],
            col_labels=[Tex('Movie').set_color(COL_PLAYER), Tex('Theater').set_color(COL_PLAYER)],
            element_to_mobject=Tex,
        ).scale(0.8).move_to(MODEL_CENTER)
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
        self.wait()
        self.notes.hide(self)

    # ------------------------------------------------------------ B42
    def b42_what_is_micro(self):
        beat(self, 'B42_what_is_micro')
        head = title('What is Microeconomics about?', scale=1.5)
        lines = VGroup(
            Tex("It's a cognitive tool that lets us see"),
            Tex("that there's a {{reason to coordinate}},"),
            Tex('that {{markets work sometimes}},'),
            Tex("and that there's a {{framework to tell when}} other tools work better."),
        ).arrange(DOWN, buff=0.4)
        for l in lines[1:]:
            l.set_color_by_tex_to_color_map({
                'reason to coordinate': DEFINITION,
                'markets work sometimes': DEFINITION,
                'framework to tell when': DEFINITION,
            })
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
        for i, p in enumerate(parts):
            self.play(FadeIn(Tex(p).to_edge(LEFT).shift(UP + DOWN * i * 2 / 3)
                             .set_color_by_tex_to_color_map(cmap)))
            self.wait()
        self.wait(2)
