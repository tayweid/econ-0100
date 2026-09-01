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


class Episode0(Scene):
    """Episode 0 | Economics isn't about money."""

    def construct(self):
        self.notes = NotesPanel()
        self.b01_title()
        self.b02_unemployment()
        self.b04_wealth()
        self.b05_cities()
        self.b07_preferences()
        self.b11_scarcity()
        self.b15_choices()
        self.b16_opportunity_cost()
        self.b18_social()
        self.b22_what_is_micro()
        self.b23_next_time()
        self.b24_six_parts()

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
        self.notes.add(self, 'Where did all that wealth go?')
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
        self.notes.add(self, f'Why are people crammed together, right on the oceans? ({n_port} of {n} are ports)')
        self.wait(2)
        self.play(FadeOut(key), FadeOut(dots), FadeOut(earth))

    # ------------------------------------------------------------ B07-B10
    def b07_preferences(self):
        beat(self, 'B07_cakes')
        self.behavior_title = on_model(title('This class is about behavior.'))
        self.play(FadeIn(self.behavior_title))

        cakes = on_model(tex_row(['Carrot Cake', '$\\succ$', 'Chocolate Cake']))
        self.play(FadeIn(cakes, lag_ratio=0.3))
        self.wait()
        self.play(FadeOut(cakes))

        beat(self, 'B08_coffee')
        coffee = on_model(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast']))
        self.play(FadeIn(coffee, lag_ratio=0.3))
        self.wait()

        beat(self, 'B09_transitivity')
        coffee3 = on_model(tex_row(['Dark Roast', '$\\succ$', 'Medium Roast', '$\\succ$', 'Light Roast']))
        self.play(Transform(coffee, coffee3))
        self.wait()
        # transitivity: dark > light
        arc = ArcBetweenPoints(coffee3[0].get_top() + 0.1 * UP, coffee3[4].get_top() + 0.1 * UP,
                               angle=-TAU / 4).set_color(FOCUS)
        self.play(Create(arc))
        self.wait()
        self.play(FadeOut(arc))

        # rankings on a number line
        pref_line = on_model(NumberLine(x_range=[-10, 10, 2], length=9, color=MUTED,
                                        include_numbers=True, label_direction=UP).to_edge(DOWN, buff=1))
        dots, names = VGroup(), VGroup()
        for name, p in zip(['Dark Roast', 'Medium Roast', 'Light Roast'], [9, 0, -9]):
            d = Dot(pref_line.number_to_point(p), color=GUIDE, z_index=10)
            dots.add(d)
            names.add(Tex(name).next_to(d, UP, buff=1))
        self.play(FadeIn(pref_line))
        self.play(FadeIn(dots), Transform(coffee, names))
        self.wait()

        beat(self, 'B10_preferences_are_rankings')
        card = on_model(definition('Preferences', 'are rankings.'))
        self.play(AddTextWordByWord(card))
        self.wait()
        self.play(FadeOut(coffee), FadeOut(dots), FadeOut(pref_line))
        self.notes.file(self, card, 'Preferences are rankings.', term='Preferences')

    # ------------------------------------------------------------ B11-B14
    def b11_scarcity(self):
        beat(self, 'B11_cant_always')
        q1 = on_model(Tex("We can't always have what we want most."))
        self.play(AddTextWordByWord(q1))
        self.wait()
        self.notes.file(self, q1, "We can't always have what we want most.")

        beat(self, 'B12_scarcity_basic')
        q2 = on_model(definition('Scarcity', 'is more basic than money.'))
        self.play(Write(q2))
        self.wait()
        self.notes.file(self, q2, 'Scarcity is more basic than money.', term='Scarcity')

        beat(self, 'B13_tesla_vs_food')
        left = Tex('Everyone gets a Tesla').move_to(MODEL_CENTER + 3 * LEFT)
        vs = Tex('vs').move_to(MODEL_CENTER)
        right = Tex('Everyone gets food').move_to(MODEL_CENTER + 3 * RIGHT)
        self.play(FadeIn(left))
        self.play(FadeIn(vs))
        self.play(FadeIn(right))
        self.wait()
        self.play(FadeOut(left), FadeOut(vs), FadeOut(right))

        beat(self, 'B14_tradeoffs')
        q3 = on_model(Tex('With preferences in the face of scarcity,'))
        q4 = Tex('we must make choices requiring tradeoffs.').next_to(q3, DOWN)
        self.play(AddTextWordByWord(q3))
        self.play(AddTextWordByWord(q4))
        self.wait()
        self.notes.file(self, VGroup(q3, q4), 'With preferences in the face of scarcity, we must make choices requiring tradeoffs.')

    # ------------------------------------------------------------ B15
    def b15_choices(self):
        beat(self, 'B15_choices_equation')
        eq = on_model(tex_row(['Preferences', '$+$', 'Scarcity', '$\\Rightarrow$', 'Choices'], color=DEFINITION, buff=0.4))
        for piece in eq:
            self.play(FadeIn(piece), run_time=0.6)
        self.wait()
        self.notes.file(self, eq)

    # ------------------------------------------------------------ B16-B17
    def b16_opportunity_cost(self):
        beat(self, 'B16_A_or_B')
        OR = on_model(Tex(' or ').scale(1.5))
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(A))
        self.wait()
        self.play(FadeIn(OR))
        self.wait()
        self.play(FadeIn(B))
        self.wait()

        beat(self, 'B17_opportunity_cost')
        box_a = SurroundingRectangle(A, buff=0.3).set_color(EFFICIENT)
        box_b = SurroundingRectangle(B, buff=0.3).set_color(NASH)
        self.play(Create(box_a))
        self.wait()
        self.play(Create(box_b))
        self.wait()

        cost = (Tex('Opportunity Cost({{A}}) = {{B}}').scale(1.5).next_to(OR, DOWN, buff=2)
                .set_color_by_tex_to_color_map({'A': EFFICIENT, 'B': NASH}))
        self.play(Write(cost))
        self.wait()

        cost2 = (Tex('Opportunity Cost({{B}}) = {{A}}').scale(1.5).next_to(OR, DOWN, buff=2)
                 .set_color_by_tex_to_color_map({'A': NASH, 'B': EFFICIENT}))
        self.play(box_a.animate.move_to(B), box_b.animate.move_to(A), Transform(cost, cost2))
        self.wait()
        self.play(FadeOut(VGroup(A, OR, B, box_a, box_b, cost)))

        oc = on_model(definition('Opportunity Cost', 'is the value of the next best alternative.'))
        self.play(AddTextWordByWord(oc))
        self.wait()
        self.notes.file(self, oc, 'Opportunity Cost is the value of the next best alternative.', term='Opportunity Cost')
        self.play(FadeOut(self.behavior_title))

    # ------------------------------------------------------------ B18-B21
    def b18_social(self):
        beat(self, 'B18_autarky')
        social_title = on_model(title('This class is about social environments.'))
        self.play(FadeIn(social_title))
        aut = on_model(definition('Autarky', 'is a state of economic self-sufficiency.'))
        self.play(AddTextWordByWord(aut))
        self.wait()
        self.notes.file(self, aut, 'Autarky is a state of economic self-sufficiency.', term='Autarky')

        beat(self, 'B19_dating_game')
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

        beat(self, 'B20_their_choices_your_choices')
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

        beat(self, 'B21_walk_the_cells')
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

    # ------------------------------------------------------------ B22
    def b22_what_is_micro(self):
        beat(self, 'B22_what_is_micro')
        head = title('What is Microeconomics about?', scale=1.5)
        lines = VGroup(
            Tex("It's a cognitive tool that lets us see"),
            Tex("that there's a {{reason to coordinate}},"),
            Tex('that {{markets work sometimes}},'),
            Tex("and that there's a {{framework to tell when}}."),
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

    # ------------------------------------------------------------ B23
    def b23_next_time(self):
        beat(self, 'B23_next_time')
        head = title('Next time...', scale=1.5)
        topic = Tex('A trip back to 1800s British philosophy.').scale(1.2)
        self.add(head, topic)
        framebox_reveal(self, topic)
        self.wait()
        self.play(FadeOut(head), FadeOut(topic))

    # ------------------------------------------------------------ B24
    def b24_six_parts(self):
        beat(self, 'B24_six_parts')
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
