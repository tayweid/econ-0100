# maniml 03_Code.py Episode0
#
# Episode 0 | Economics isn't about money
# One scene; beats follow 02_Storyboard.md (B01...B44). Talking-head beats
# (B06, B45) are gaps between sections.

from manim import *
import numpy as np
import pandas as pd
import os
import sys
import warnings

warnings.filterwarnings('ignore')

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *          # palette tokens, frame config, title(), bumper(), ...
from style import axes as style_axes

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


def choice_boxes(a, b, buff=0.3):
    """Green (chosen) and red (given up) boxes of the same size around two mobjects."""
    w = max(a.get_width(), b.get_width()) + 2 * buff
    h = max(a.get_height(), b.get_height()) + 2 * buff
    box_a = Rectangle(width=w, height=h, color=EFFICIENT).move_to(a)
    box_b = Rectangle(width=w, height=h, color=NASH).move_to(b)
    return box_a, box_b


# The value line: choices as dots on a number line; the arrow tip marks
# the preferred direction.
# Marks are plain VGroup(dot, label)s; re-rank one by shifting it:
# mark.animate.shift(line.n2p(new) - line.n2p(old)).
def value_line(v_range=(0, 10), length=10):
    return NumberLine([v_range[0], v_range[1], 1], length=length, color=MUTED, include_numbers=False, include_tip=True)


def value_mark(line, name, v, side=UP, scale=0.7):
    dot = Dot(line.n2p(v), color=GUIDE, z_index=10)
    lab = Tex(name).scale(scale).next_to(dot, side, buff=0.25 if side[1] > 0 else 0.6)
    return VGroup(dot, lab)


def value_marks(line, items, scale=0.7, stagger=True):
    """name -> mark, labels alternating above/below the line when staggered."""
    sides = [UP, DOWN] if stagger else [UP, UP]
    return {name: value_mark(line, name, v, sides[i % 2], scale)
            for i, (name, v) in enumerate(items.items())}


def value_numbers(line, factor=1):
    return VGroup(*[Integer(v * factor, group_with_commas=False).scale(0.5).set_color(MUTED)
                    .next_to(line.n2p(v), DOWN, buff=0.2) for v in (1, 5, 10)])


class Episode0(Scene):
    """Episode 0 | Economics isn't about money.

    One flat construct(). Each `# Bxx` section is self-contained: it clears
    the previous beat's objects, builds its own, and ends at the pause()
    the viewer parks on before the next section.
    """

    def construct(self):

        # B01 ---------------------------------------------------------

        squares = bumper_raster(self)

        # B01b --------------------------------------------------------

        flicker(self, squares)

        # B01c --------------------------------------------------------

        label = bumper_title(self, squares, 'A', 0)
        thesis = Tex("\\textit{Economics is not} about \\textit{money}").scale(1.2).set_color(MUTED).next_to(label, DOWN, buff=0.5)
        self.play(FadeIn(thesis))
        self.pause()

        # B02 ---------------------------------------------------------

        FadeAll(self)
        y_max = float(np.ceil(RATES.max()))
        ax = style_axes([0, WINDOW], [0, y_max]).move_to(DOWN * 0.3)
        labels = VGroup(title('Unemployment'), axis_caption(ax, 'rate (\\%)'))

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
        year_r.add_updater(lambda m: m.set_value(YEARS[min(int(t.get_value()), N_MONTHS - 1)]).next_to(ax.c2p(WINDOW, 0), DOWN))
        year_l = Integer(0, group_with_commas=False)
        year_l.add_updater(lambda m: m.set_value(YEARS[int(window()[1])]).next_to(ax.c2p(0, 0), DOWN))

        self.add(ax, labels, year_l, year_r, rate_label, hline, dot)

        self.play(FadeIn(series), run_time=1 / 2)
        self.play(t.animate.set_value(MONTH_2008), run_time=8, rate_func=smooth)
        self.pause()

        # B03 ---------------------------------------------------------

        self.play(t.animate.set_value(N_MONTHS - 1), run_time=4.5, rate_func=smooth)
        self.pause()

        # B04 ---------------------------------------------------------

        FadeAll(self)

        # US private wealth, nominal $bn (Piketty-Zucman Table US.1)
        yrs = WEALTH.year.to_numpy()
        w = WEALTH.private_wealth_nominal_bn.to_numpy()
        axes = style_axes([1920, 1940, 5], [0, 600, 100]).move_to(UP * 0.2)
        x_nums = VGroup(*[Integer(y, group_with_commas=False).scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(y, 0), DOWN) for y in range(1920, 1941, 5)])
        y_nums = VGroup(*[Tex(f'\\${v}').scale(0.7).set_color(MUTED)
                          .next_to(axes.c2p(1920, v), LEFT) for v in (100, 200, 300, 400, 500, 600)])
        ylab = VGroup(title('Wealth in the Great Depression'), axis_caption(axes, 'U.S. private wealth, billions'))

        i29 = int(np.where(yrs == 1929)[0][0])
        i33 = int(np.where(yrs == 1933)[0][0])
        rise = polyline([axes.c2p(yrs[i], w[i]) for i in range(0, i29 + 1)], color=DEMAND)
        fall = polyline([axes.c2p(yrs[i], w[i]) for i in range(i29, i33 + 1)], color=DEMAND).set_stroke(GUIDE)

        self.play(FadeIn(axes), FadeIn(x_nums), FadeIn(y_nums), FadeIn(ylab))
        self.play(Create(rise), run_time=3, rate_func=smooth)
        peak = Dot(axes.c2p(1929, w[i29]), color=GUIDE, z_index=10)
        peak_label = Tex(f'1929: \\${w[i29]:.0f}bn').scale(0.8).next_to(peak, UR, buff=0.15)
        self.play(FadeIn(peak), FadeIn(peak_label))

        self.play(Create(fall), run_time=2.5, rate_func=smooth)

        trough = Dot(axes.c2p(1933, w[i33]), color=GUIDE, z_index=10)
        trough_label = Tex(f'1933: \\${w[i33]:.0f}bn').scale(0.8).next_to(trough, DOWN)
        self.play(FadeIn(trough), FadeIn(trough_label))

        q = Tex('Where did all that wealth go?').set_color(DEFINITION).to_edge(DOWN, buff=0.35)
        self.play(FadeIn(q))

        self.pause()

        # B05 ---------------------------------------------------------

        FadeAll(self)
        earth = ImageMobject(NIGHT_MAP)
        earth.set_height(FRAME_HEIGHT * 1.02)   # full bleed; 2:1 image, slight overscan so no background shows
        self.play(FadeIn(earth), run_time=2)
        self.pause()

        # B05b --------------------------------------------------------

        map_title = title('The 30 largest cities in the world.')
        backing = BackgroundRectangle(map_title, color=BG, fill_opacity=0.7, buff=0.15)
        self.play(FadeIn(backing), FadeIn(map_title))

        port_color, inland_color = FOCUS, DEMAND
        dots = VGroup()
        for row in CITIES.itertuples():
            # equirectangular: linear in both axes, centred on (0, 0)
            p = earth.get_center() + np.array([(row.lon / 180) * earth.get_width() / 2,
                                               (row.lat / 90) * earth.get_height() / 2, 0])
            r = 0.035 * np.sqrt(row.pop_millions_2018)
            dots.add(Dot(p, radius=r, color=port_color if row.port else inland_color,
                         fill_opacity=0.85, z_index=10))
        self.play(LaggedStart(*[GrowFromCenter(d) for d in dots], lag_ratio=0.08), run_time=4)

        key = VGroup(
            VGroup(Dot(color=port_color), Tex('port').scale(0.8)).arrange(RIGHT, buff=0.15),
            VGroup(Dot(color=inland_color), Tex('inland').scale(0.8)).arrange(RIGHT, buff=0.15),
        ).arrange(RIGHT, buff=0.6).to_corner(DL, buff=0.9)
        self.play(FadeIn(key))
        n_port = int(CITIES.port.sum())
        tally = Tex(f'{n_port} of the {len(CITIES)} are ports.').set_color(DEFINITION).next_to(map_title, DOWN, buff=0.3).align_to(map_title, LEFT)
        backing2 = BackgroundRectangle(tally, color=BG, fill_opacity=0.7, buff=0.15)
        self.pause()
        self.play(FadeIn(backing2), Write(tally))
        self.pause()

        # B10 ---------------------------------------------------------

        FadeAll(self)
        behavior_title = title('This class is about behavior.')
        self.play(FadeIn(behavior_title))
        sub = subtitle(behavior_title, 'Behavior involves preferences.')
        self.play(FadeIn(sub))

        # each piece flies in from the side and the row re-centres
        cakes = VGroup(Tex(''))
        for s in ['Carrot Cake', '$\\prec$', 'Chocolate Cake']:   # reads: Chocolate Cake < Carrot Cake
            piece = Tex(s).next_to(cakes, LEFT)
            cakes.add(piece)
            self.play(FadeIn(piece), cakes.animate.move_to(ORIGIN))

        card = centered(definition('Preferences', 'are rankings.')).to_edge(DOWN, buff=0.6)
        self.play(Write(card))
        self.pause()

        # B11 ---------------------------------------------------------

        self.play(FadeOut(card, cakes))
        coffee = VGroup(Tex(''))
        for s in ['Dark Roast', '$\\prec$', 'Light Roast']:       # reads: Light Roast < Dark Roast
            piece = Tex(s).next_to(coffee, LEFT)
            coffee.add(piece)
            self.play(FadeIn(piece), coffee.animate.move_to(ORIGIN))
        dark, lt, light = coffee[1], coffee[2], coffee[3]
        self.pause()

        # B12 ---------------------------------------------------------

        mid = VGroup(Tex('Medium Roast'), Tex('$\\prec$')).arrange(RIGHT, buff=0.25)
        full = VGroup(light.copy(), lt.copy(), mid, dark.copy()).arrange(RIGHT, buff=0.25).move_to(ORIGIN)
        mid.move_to(full[2])
        self.play(light.animate.move_to(full[0]), lt.animate.move_to(full[1]), dark.animate.move_to(full[3]),
                  FadeIn(mid, shift=0.4 * DOWN))
        chain = VGroup(light, lt, mid[0], mid[1], dark)
        self.pause()

        # B13 ---------------------------------------------------------

        vline = value_line().move_to(DOWN * 0.3)
        marks = value_marks(vline, {'Light Roast': 2, 'Medium Roast': 5, 'Dark Roast': 8})
        self.play(
            Transform(light, marks['Light Roast'][1].copy()),
            Transform(mid[0], marks['Medium Roast'][1].copy()),
            Transform(dark, marks['Dark Roast'][1].copy()),
            FadeOut(lt), FadeOut(mid[1]),
            FadeIn(vline), run_time=1.5,
        )
        self.remove(chain, light, mid, dark)
        self.add(*marks.values())
        self.pause()

        # B13b --------------------------------------------------------

        marks['Espresso'] = value_mark(vline, 'Espresso', 9.5)
        marks['Decaf'] = value_mark(vline, 'Decaf', 0.5, DOWN)
        self.play(FadeIn(marks['Espresso']), FadeIn(marks['Decaf']))
        self.pause()

        # B14 ---------------------------------------------------------

        self.play(FadeOut(VGroup(*marks.values())), run_time=0.6)
        marks = value_marks(vline, {'Slush': 1, 'Winter': 3, 'Summer': 6.5, 'Spring': 8, 'Fall': 9.5})
        self.play(FadeIn(VGroup(*marks.values()), lag_ratio=0.1), run_time=0.8)
        self.pause()

        # B14b --------------------------------------------------------

        self.play(FadeOut(VGroup(*marks.values())), run_time=0.6)
        marks = value_marks(vline, {'Pineapple': 0.5, 'Olive': 4, 'Plain': 5.5, 'Pepperoni': 7.5, 'Mushroom': 9})
        self.play(FadeIn(VGroup(*marks.values()), lag_ratio=0.1), run_time=0.8)
        self.pause()

        # B14c --------------------------------------------------------

        self.play(FadeOut(VGroup(*marks.values())), run_time=0.6)
        marks = value_marks(vline, {'Light Roast': 2, 'Decaf': 0.5, 'Medium Roast': 5, 'Dark Roast': 8, 'Espresso': 9.5})
        self.play(FadeIn(VGroup(*marks.values()), lag_ratio=0.1), run_time=0.8)
        self.pause()

        # B15 ---------------------------------------------------------



        # B16 ---------------------------------------------------------

        nums = value_numbers(vline)
        self.play(FadeIn(nums, lag_ratio=0.1))
        self.pause()

        # B17 ---------------------------------------------------------

        card1 = centered(definition('Preferences', 'are rankings.')).to_edge(DOWN, buff=0.8)
        self.play(Write(card1))
        card2 = centered(definition('Utility', 'is a number that does the ranking for us.')).to_edge(DOWN, buff=0.3)
        self.play(Write(card2))
        self.pause()

        # B20 ---------------------------------------------------------

        self.play(Transform(nums, value_numbers(vline, 100)))
        self.pause()

        # B20b --------------------------------------------------------

        self.play(Transform(nums, value_numbers(vline)))
        self.pause()

        # B18 ---------------------------------------------------------

        self.play(FadeOut(card1, card2))
        self.play(vline.animate.shift(UP * 1.2), nums.animate.shift(UP * 1.2), *[m.animate.shift(UP * 1.2) for m in marks.values()])
        me = Tex('Me').scale(0.8).set_color(MUTED).next_to(vline, LEFT, buff=0.4)
        yline = value_line().move_to(DOWN * 1.8)
        ymarks = value_marks(yline, {'Light Roast': 8.5, 'Decaf': 6.5, 'Medium Roast': 5, 'Espresso': 2.5, 'Dark Roast': 1})
        ynums = value_numbers(yline)
        you = Tex('You').scale(0.8).set_color(MUTED).next_to(yline, LEFT, buff=0.4)
        self.play(FadeIn(me), FadeIn(yline), FadeIn(VGroup(*ymarks.values())), FadeIn(ynums), FadeIn(you))
        card = centered(definition('Preferences', 'are individual.')).to_edge(DOWN, buff=0.3)
        self.play(Write(card))
        self.pause()

        # B21 ---------------------------------------------------------

        self.play(FadeOut(VGroup(yline, *ymarks.values(), ynums, you, me, nums), card), run_time=0.8)
        esp = marks['Espresso']
        self.play(FadeOut(VGroup(*[m for k, m in marks.items() if k != 'Espresso'])), run_time=0.6)
        self.play(vline.animate.shift(DOWN * 1.2), esp.animate.shift(DOWN * 1.2))
        tea = value_mark(vline, 'Tea', 3)
        self.play(FadeIn(tea))

        self.play(esp.animate.shift(vline.n2p(3) - vline.n2p(9.5)),
                  tea.animate.shift(vline.n2p(9.5) - vline.n2p(3)), run_time=2, rate_func=smooth)
        card = centered(definition('Preferences', 'can change.')).to_edge(DOWN, buff=0.3)
        self.play(Write(card))
        self.pause()

        # B22 ---------------------------------------------------------

        FadeAll(self)
        scarcity_title = title('This class is about scarcity.')
        self.play(FadeIn(scarcity_title))
        q1 = centered(Tex("We can't always have what we want most."))
        self.play(Write(q1))
        self.play(FadeOut(q1))
        self.pause()

        # B23 ---------------------------------------------------------

        q2 = centered(definition('Scarcity', 'is more basic than money.'))
        self.play(Write(q2))
        sub = subtitle(scarcity_title, 'Scarcity is more basic than money.')
        self.play(Transform(q2,sub))
        self.pause()

        # B24 ---------------------------------------------------------
        
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

        big = VGroup(house(1.6), tickets(2)).arrange(DOWN, buff=0.35)
        big_lab = Tex('near the park, fewer movies').scale(0.6).set_color(MUTED).next_to(big, DOWN, buff=0.25)
        small = VGroup(house(0.9), tickets(6)).arrange(DOWN, buff=0.35)
        small_lab = Tex('far from the park, more movies').scale(0.6).set_color(MUTED).next_to(small, DOWN, buff=0.25)
        OR = Tex('or').scale(1.2)
        A = VGroup(big, big_lab)
        B = VGroup(small, small_lab)
        row = VGroup(A, OR, B).arrange(RIGHT, buff=1.2)
        centered(row).shift(DOWN * 0.2)
        self.play(FadeIn(A))
        self.play(FadeIn(OR, B))
        self.pause()

        # B24b --------------------------------------------------------

        box_a, box_b = choice_boxes(A, B)
        self.play(FadeIn(box_a))
        self.play(FadeIn(box_b))
        self.pause()

        # B24c --------------------------------------------------------

        self.play(box_a.animate.move_to(B), box_b.animate.move_to(A))
        self.pause()

        # B25 ---------------------------------------------------------

        self.play(FadeOut(row), FadeOut(box_a), FadeOut(box_b))
        h1 = VGroup(house(1.6), Tex('Taylor gets the house').scale(0.7)).arrange(DOWN, buff=0.3)
        h2 = VGroup(house(1.6), Tex('Andrew gets the house').scale(0.7)).arrange(DOWN, buff=0.3)
        OR = Tex('or').scale(1.2)
        row = centered(VGroup(h1, OR, h2).arrange(RIGHT, buff=1.2)).shift(DOWN * 0.2)
        self.play(FadeIn(h1))
        self.play(FadeIn(OR, h2))
        self.pause()

        # B25b --------------------------------------------------------

        box_a, box_b = choice_boxes(h1, h2)
        self.play(FadeIn(box_a))
        self.play(FadeIn(box_b))
        self.pause()

        # B25c --------------------------------------------------------

        self.play(box_a.animate.move_to(h2), box_b.animate.move_to(h1))
        self.pause()

        # B26 ---------------------------------------------------------

        FadeAll(self)
        q = centered(Tex('We make choices because of preferences and scarcity.')).shift(UP * 0.6)
        self.play(Write(q))

        eq = centered(tex_row(['Preferences', '$+$', 'Scarcity', '$=$', 'Choices'], color=DEFINITION, buff=0.4)).next_to(q, DOWN, buff=0.8)
        for piece in eq:
            self.play(FadeIn(piece), run_time=0.6)
        self.pause()

        # B28 ---------------------------------------------------------

        FadeAll(self)
        tradeoff_title = title('We measure choices by their tradeoffs.')
        self.play(FadeIn(tradeoff_title))
        sub = subtitle(tradeoff_title, 'What could we have had instead?')
        self.play(FadeIn(sub))
        OR = Tex(' or ').scale(1.5)
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(A))
        self.play(FadeIn(OR))
        self.play(FadeIn(B))
        self.pause()

        # B28b --------------------------------------------------------

        box_a, box_b = choice_boxes(A, B)
        self.play(FadeIn(box_a))
        self.play(FadeIn(box_b))
        self.pause()

        # B28c --------------------------------------------------------

        for _ in range(1):
            self.play(box_a.animate.move_to(B), box_b.animate.move_to(A), run_time=0.6)
            self.play(box_a.animate.move_to(A), box_b.animate.move_to(B), run_time=0.6)
        self.pause()

        # B31 ---------------------------------------------------------

        eq = (Tex('Opportunity Cost({{A}}) = {{B}}').scale(1.2).next_to(OR, DOWN, buff=0.9)
              .set_color_by_tex_to_color_map({'A': EFFICIENT, 'B': NASH}))
        self.play(Write(eq))
        self.pause()

        # B31b --------------------------------------------------------

        oc = centered(definition('Opportunity Cost', 'is the value of the next best alternative.')).to_edge(DOWN, buff=0.4)
        self.play(Write(oc))
        self.pause()

        # B33 ---------------------------------------------------------

        FadeAll(self)
        
        head = title('Forbes Ave Market')
        sub = subtitle(head, 'How should you spend 1 dollar?')
        self.play(FadeIn(head))
        self.play(FadeIn(sub))

        ap = Tex('Apple').scale(1.2)
        ba = Tex('Banana').scale(1.2)
        OR = Tex('or').scale(1.2)
        row = centered(VGroup(ap, OR, ba).arrange(RIGHT, buff=1.5)).shift(UP * 0.5)
        self.play(FadeIn(row))
        self.pause()

        # B33b --------------------------------------------------------

        box_a, box_b = choice_boxes(ap, ba)
        self.play(FadeIn(box_a))
        self.play(FadeIn(box_b))
        self.pause()

        # B33c --------------------------------------------------------

        oc = Tex('Opportunity Cost(Apple) = Banana').scale(0.9).next_to(row, DOWN, buff=0.9)
        self.play(Write(oc))
        self.pause()

        # B35 ---------------------------------------------------------

        FadeAll(self)
        head = title('Your Neighborhood Bakery')
        sub = subtitle(head, 'You get one free item.')
        self.play(FadeIn(head, sub))
        vline = value_line().move_to(DOWN * 0.6)
        marks = value_marks(vline, {'Banana bread': 3, 'Apple pie': 6}, stagger=False)
        self.play(Create(vline), FadeIn(VGroup(*marks.values())))
        table = VGroup().to_edge(DOWN, buff=0.7)
        self.pause()

        # B35b --------------------------------------------------------

        def oc_arrow(src, dst):
            # curved arrow from the choice to its next best, bulging below the line
            a = marks[src][0].get_center() + DOWN * 0.15
            b = marks[dst][0].get_center() + DOWN * 0.15
            return CurvedArrow(a, b, angle=(TAU / 5 if b[0] > a[0] else -TAU / 5), color=GUIDE)

        arr = oc_arrow('Apple pie', 'Banana bread')
        self.play(Create(arr))
        line = Tex('OC(Apple pie) = Banana bread').scale(0.8).set_color(YELLOW).next_to(sub, DOWN*3, buff=0.35).align_to(sub, LEFT)
        self.play(Write(line))
        table.add(line)
        self.play(FadeOut(arr))
        self.pause()

        # B36 ---------------------------------------------------------

        marks['Carrot cake'] = value_mark(vline, 'Carrot cake', 9)
        self.play(FadeIn(marks['Carrot cake']))
        
        self.pause()

        # B36b --------------------------------------------------------

        arr = oc_arrow('Apple pie', 'Carrot cake')
        self.play(Create(arr))
        new_line = Tex('OC(Apple pie) = Carrot cake').scale(0.8).set_color(YELLOW).move_to(line).align_to(line, LEFT)
        self.play(Transform(line, new_line))
        self.play(FadeOut(arr))
        self.pause()

        # B36c-B36d ---------------------------------------------------

        # then the cake, then the bread, one arrow at a time
        for src, dst, text in [('Carrot cake', 'Apple pie', 'OC(cake) = pie'), ('Banana bread', 'Carrot cake', 'OC(bread) = cake')]:
            arr = oc_arrow(src, dst)
            self.play(Create(arr))
            t = Tex(text).scale(0.8).set_color(YELLOW).next_to(table[-1], DOWN, buff=0.2).align_to(head, LEFT)
            self.play(Write(t))
            table.add(t)
            self.play(FadeOut(arr))
            self.pause()

        # B38 ---------------------------------------------------------

        FadeAll(self)
        social_title = title('Microeconomics is about social environments.')
        self.play(FadeIn(social_title))
        self.pause()

        # B38b --------------------------------------------------------

        aut = centered(definition('Autarky', 'is a state of economic self-sufficiency.'))
        self.play(Write(aut))
        self.pause()

        # B39 ---------------------------------------------------------

        sub = subtitle(social_title, 'Usually our choices depend on and are influenced by others.')
        self.play(Transform(aut, sub))
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
        self.pause()

        # B40 ---------------------------------------------------------

        col_box = SurroundingRectangle(table.get_columns()[1], buff=0.2).set_color(COL_PLAYER)
        self.play(Create(col_box))
        col_box2 = SurroundingRectangle(table.get_columns()[2], buff=0.2).set_color(COL_PLAYER)
        self.play(Transform(col_box, col_box2))
        self.pause()

        # B40b --------------------------------------------------------

        self.play(FadeOut(col_box))
        row_box = SurroundingRectangle(table.get_rows()[1], buff=0.2).set_color(YELLOW)
        self.play(Create(row_box))
        row_box2 = SurroundingRectangle(table.get_rows()[2], buff=0.2).set_color(YELLOW)
        self.play(Transform(row_box, row_box2))
        self.pause()

        # B41 ---------------------------------------------------------

        self.play(FadeOut(row_box))
        cell = SurroundingRectangle(table.get_entries((2, 2)), buff=0.25).set_color(EFFICIENT)
        self.play(Create(cell))
        self.pause()

        # B41b --------------------------------------------------------

        self.play(Transform(cell, SurroundingRectangle(table.get_entries((3, 2)), buff=0.25).set_color(NASH)))
        self.pause()

        # B41c --------------------------------------------------------

        self.play(Transform(cell, SurroundingRectangle(table.get_entries((2, 3)), buff=0.25).set_color(NASH)))
        self.pause()

        # B41d --------------------------------------------------------

        self.play(Transform(cell, SurroundingRectangle(table.get_entries((3, 3)), buff=0.25).set_color(EFFICIENT)))
        self.pause()

        # B42 ---------------------------------------------------------

        FadeAll(self)
        head = title('Microeconomics tells us...')
        clauses = [
            ("there's a deep fundamental {{reason}} why it pays", ['reason']),
            ('\\quad to {{coordinate}} with each other,', ['coordinate']),
            ('that {{markets}} can serve as an effective coordination device {{sometimes}},', ['markets', 'sometimes']),
            ('that markets {{often fail}},', ['often fail']),
            ('gives us a {{framework}} for when,', ['framework']),
            ('and provides some {{alternatives}} for doing better.', ['alternatives']),
        ]
        lines = VGroup()
        for text, keys in clauses:
            l = Tex(text).scale(0.95).set_color_by_tex_to_color_map({k: DEFINITION for k in keys})
            lines.add(l)
        lines.arrange(DOWN, buff=0.5, aligned_edge=LEFT).next_to(head, DOWN, buff=0.8).align_to(head, LEFT)
        self.play(FadeIn(head))
        self.pause()

        # B42b --------------------------------------------------------

        for i, l in enumerate(lines):
            self.play(Write(l))
            if i != 0:   # lines 0+1 are one phrase, so they share a press
                self.pause()

        # B44 ---------------------------------------------------------

        FadeAll(self)
        head = title('This class contains six parts.', scale=1.5)
        self.play(FadeIn(head))
        parts = [
            ('A', 'The Landscape:', 'Better choices can benefit everyone.'),
            ('B', 'Coordination Using Markets:', 'Markets can effectively facilitate coordination.'),
            ('C', 'Externalities:', 'Externalities break the efficiency of markets.'),
            ('D', 'Strategic Interaction:', "Strategic Interaction breaks the efficiency of markets."),
            ('E', 'Sellers:', 'Market power breaks the efficiency of markets.'),
            ('F', 'Buyers:', "Buyers' decisions shape the demand curve."),
        ]
        rows = VGroup()
        for p, name, sub in parts:
            row = VGroup(Tex(f'Part {p}.').set_color(MUTED), Tex(name).set_color(DEFINITION), Tex(sub)).scale(0.85)
            row.arrange(RIGHT, buff=0.3)
            rows.add(row)
        rows.arrange(DOWN, buff=0.42, aligned_edge=LEFT)
        if rows.get_width() > FRAME_W - 1.4:
            rows.scale((FRAME_W - 1.4) / rows.get_width())
        rows.next_to(head, DOWN, buff=0.7).align_to(head, LEFT)
        self.pause()

        # B44b --------------------------------------------------------

        for row in rows:
            self.play(FadeIn(row[0]), run_time=0.5)
            self.play(FadeIn(row[1]), run_time=0.5)
            self.play(FadeIn(row[2]), run_time=0.7)
            self.pause()

        # B43 ---------------------------------------------------------

        FadeAll(self)
        head = title('Next time...', scale=1.5)
        topic = Tex('A trip back to 1800s British philosophy.').scale(1.2)
        self.add(head, topic)
        framebox_reveal(self, topic)
        FadeAll(self)
