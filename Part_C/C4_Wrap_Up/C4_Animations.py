# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-02T23:47:58Z"
# ///

# maniml C4_Animations.py C4
# Storyboard: C4_Notes.md. All lesson choreography stays in construct().
# The Part C wrap-up: one rule for deadweight loss across negative and positive externalities,
# taxes and subsidies, taught in three stages: the close-up of one unit; the same unit on the
# market graph, drawn as the close-up compressed around one line up from its quantity (small
# floating bars pointing at the dots on the line, the comparison brackets left and right); then
# every unit between Q and Q*. Ends with every welfare measure in the corrected markets.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../../Part_B/Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects


class C4(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        self.set_camera_orientation(phi=0, theta=0, gamma=0)
        self.camera.frame.move_to(ORIGIN).set_height(8)
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        EXTERNAL = 2
        BAR_GAP = 0.08
        BASE_OPACITY, SURPLUS_OPACITY, STRIP_OPACITY = 0.16, 0.65, 0.8
        ORIGIN_X, ORIGIN_Y = -5.7, -2.25
        # Top-level z order (the engine sorts top-level mobjects by z_index): fills under curves,
        # loss strips, area and curve words, guides, policy line, dots, then the stage-2 unit and
        # its words. The engine's set_z_index sets a group's own z only, not its children's.
        FILL_LAYER, STRIP_LAYER, WORD_LAYER, GUIDE_LAYER, POLICY_LAYER, DOT_LAYER = -1, 1, 6, 10, 13, 30
        BAR_LAYER, GAP_LAYER, EDGE_LAYER, TOP_LAYER = 43, 46, 47, 50
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        # Stage 2: the market fades to these while one unit is inspected (curves keep their shape).
        DIM_CURVES, DIM_REST = 0.15, 0.15
        FRAME_LEFT = -8 + 0.12                     # The frame is 16 units wide at height 8.
        # Stage 2: the close-up's columns as small bars beside the unit's line.
        GAP, BAR_W, NEAR, BAR_FILL, BAR_FADE_TOP = 0.40, 0.34, 0.10, 0.22, 0.45
        SURPLUS_FILL = 0.55                        # A traded unit's CS and PS, between price and value.
        # One type size for the unit's numbers and one for its words; one line weight for its
        # structure (the line, flanges, brackets, price segments) and one for annotation (leaders).
        NUMBER_SCALE, LABEL_SCALE = 0.50, 0.44
        STRUCTURE, ANNOTATION = 2.5, 1.2
        NAME_GAP = 0.06                            # A name's edge from the flange it belongs to.
        DETAIL_BASE, DETAIL_SCALE = -2.05, 0.68
        detail_y = lambda value: DETAIL_BASE + DETAIL_SCALE * value

        # The model, as one-line functions of quantity.
        mb = lambda q: 12 - q / 5
        mc = lambda q: 2 + q / 20
        msc = lambda q: mc(q) + EXTERNAL
        msb = lambda q: mb(q) + EXTERNAL
        zero = lambda q: 0
        level = lambda value: (lambda q: value)

        # Each system: society's benefit and cost curves, the efficient and traded quantities, any
        # policy prices (top, bottom) with their names, the two stacks the close-up draws (buyer's
        # and seller's: pieces of (curve, fill color, edge color, name), bottom up), and which two
        # names society compares.
        negative = dict(benefit=mb, cost=msc, q_star=32, q_market=40, prices=None, price_names=(),
                        buyer=[(mb, DEMAND, DEMAND, 'MB')], seller=[(mc, SUPPLY, SUPPLY, 'MC'), (msc, EXT, SUPPLY, 'MSC')],
                        society=('MB', 'MSC'))
        positive = dict(benefit=msb, cost=mc, q_star=48, q_market=40, prices=None, price_names=(),
                        buyer=[(mb, DEMAND, DEMAND, 'MB'), (msb, EXT, DEMAND, 'MSB')], seller=[(mc, SUPPLY, SUPPLY, 'MC')],
                        society=('MSB', 'MC'))
        taxed = dict(benefit=mb, cost=mc, q_star=40, q_market=32, prices=(5.6, 3.6), price_names=('P_b', 'P_s'),
                     buyer=[(mb, DEMAND, DEMAND, 'MB')], seller=[(mc, SUPPLY, SUPPLY, 'MC')], society=('MB', 'MC'))
        subsidized = dict(benefit=mb, cost=mc, q_star=40, q_market=48, prices=(4.4, 2.4), price_names=('P_s', 'P_b'),
                          buyer=[(mb, DEMAND, DEMAND, 'MB')], seller=[(mc, SUPPLY, SUPPLY, 'MC')], society=('MB', 'MC'))

        teaching = lambda text: fixed(Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                      .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))

        def ordinal(n):
            suffix = 'th' if 10 <= n % 100 <= 20 else {1: 'st', 2: 'nd', 3: 'rd'}.get(n % 10, 'th')
            return rf'{n}\textsuperscript{{{suffix}}}'

        # ---- The market graph, shared by every section. MSC and MSB are solid in this episode.
        ax = style_axes([0, 60, 10], [0, 14, 2], x_length=8.2, y_length=4.7)
        ax.shift(np.array([ORIGIN_X, ORIGIN_Y, 0]) - ax.c2p(0, 0))
        fixed(ax)
        y_at = lambda value: ax.c2p(0, value)[1]
        x_at = lambda q: ax.c2p(q, 0)[0]
        price_word = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, 14), LEFT, buff=0.23)
        axis_words = fixed(VGroup(
            price_word,
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(price_word, DOWN, buff=0.08),
            Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(60, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(60, 0), DOWN, buff=0.73)))
        demand = fixed(Line(ax.c2p(0, 12), ax.c2p(60, 0), color=DEMAND, stroke_width=3))
        supply = fixed(Line(ax.c2p(0, 2), ax.c2p(60, 5), color=SUPPLY, stroke_width=3))
        social_cost = fixed(Line(ax.c2p(0, 4), ax.c2p(60, 7), color=SUPPLY, stroke_width=3))
        social_benefit = fixed(Line(ax.c2p(0, 14), ax.c2p(60, 2), color=DEMAND, stroke_width=3))
        mb_word = fixed(Tex('MB', color=INK).scale(0.7).next_to(ax.c2p(60, 0), UR, buff=0.12).set_z_index(WORD_LAYER))
        mc_word = fixed(Tex('MC', color=INK).scale(0.7).next_to(ax.c2p(60, 5), RIGHT, buff=0.12).set_z_index(WORD_LAYER))
        msc_word = fixed(Tex('MSC', color=INK).scale(0.7).next_to(ax.c2p(60, 7), RIGHT, buff=0.12).set_z_index(WORD_LAYER))
        msb_word = fixed(Tex('MSB', color=INK).scale(0.7).next_to(ax.c2p(60, 2), RIGHT, buff=0.12).set_z_index(WORD_LAYER))

        def unit_slice(axes, q, low, high, color, opacity, right=None, left=None):
            left = q + BAR_GAP / 2 if left is None else left
            right = q + 1 - BAR_GAP / 2 if right is None else right
            return fixed(Polygon(axes.c2p(left, low(left)), axes.c2p(right, low(right)),
                                 axes.c2p(right, high(right)), axes.c2p(left, high(left)),
                                 stroke_width=0, fill_color=color, fill_opacity=opacity))

        def strips(low, high, color, opacity, first, last, axes=ax):
            return fixed(VGroup(*[unit_slice(axes, q, low, high, color, opacity) for q in range(first, last)]))

        def point_mark(q, p, color, radius=0.065):
            """A dot on the curves with its drop to the axis. Hidden, not dimmed, during stage 2."""
            mark = fixed(VGroup(DashedLine(ax.c2p(q, 0), ax.c2p(q, p), color=color, stroke_width=2),
                                Dot(ax.c2p(q, p), radius=radius, color=color)).set_z_index(DOT_LAYER))
            mark.hides_in_stage = True
            return mark

        def quantity_word(q, symbol, color, symbol_scale=QUANTITY_LABEL_SCALE):
            return fixed(VGroup(
                Tex(str(q), color=color).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(q, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                Tex(symbol, color=color).scale(symbol_scale).move_to(ax.c2p(q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
            ).set_z_index(GUIDE_LAYER))

        def price_guides(q, prices, names):
            """Both policy prices: dashed lines from the axis to Q, and their values on the axis."""
            guides = VGroup()
            for p, name in zip(prices, names):
                guides.add(DashedLine(ax.c2p(0, p), ax.c2p(q, p), color=GUIDE, stroke_width=2),
                           Tex(rf'${name}={p:.2f}$', color=GUIDE).scale(0.62).next_to(ax.c2p(0, p), LEFT, buff=0.15))
            return fixed(guides.set_z_index(GUIDE_LAYER))

        def price_points(q, prices):
            """The two price dots on the curves, and the drop from the lower price to the axis."""
            top, bottom = prices
            points = fixed(VGroup(DashedLine(ax.c2p(q, 0), ax.c2p(q, bottom), color=GUIDE, stroke_width=2),
                                  Dot(ax.c2p(q, top), radius=0.065, color=GUIDE),
                                  Dot(ax.c2p(q, bottom), radius=0.065, color=GUIDE)).set_z_index(DOT_LAYER))
            points.hides_in_stage = True
            return points

        def wedge_at(q, low, high, word, side, corner):
            """The tax or subsidy as a thin green line at Q between the two prices, labeled on a pad.
            `side` nudges it just off Q (-1 left, +1 right) and `corner` says where its label ('$2'
            over the word) hangs below its lower end."""
            x = ax.c2p(q, 0)[0] + side * 0.025
            line = Polygon([x - 0.025, y_at(low), 0], [x + 0.025, y_at(low), 0],
                           [x + 0.025, y_at(high), 0], [x - 0.025, y_at(high), 0],
                           stroke_width=0, fill_color=GOV, fill_opacity=1)
            text = VGroup(Tex(r'\$2', color=GOV), Tex(word, color=GOV)).arrange(DOWN, buff=0.05).scale(0.55)
            text.next_to(line.get_bottom(), corner, buff=0.06)
            pad = Rectangle(width=text.width + 0.08, height=text.height + 0.06, stroke_width=0,
                            fill_color=BG, fill_opacity=0.9).move_to(text)
            return fixed(VGroup(line, pad, text).set_z_index(POLICY_LAYER))

        def axis_wedge(low, high, word, guides):
            """The same $2, measured beside the price axis, just left of the price labels in
            `guides`, so it never crowds the unit."""
            x = min(guides[1].get_left()[0], guides[3].get_left()[0]) - 0.15
            line = Line([x, y_at(low), 0], [x, y_at(high), 0], color=GOV, stroke_width=5)
            text = VGroup(Tex(r'\$2', color=GOV), Tex(word, color=GOV)).arrange(DOWN, buff=0.04).scale(0.5)
            text.next_to(line, LEFT, buff=0.1)
            room = x - 0.1 - FRAME_LEFT                # Keep the word inside the frame.
            if 0 < room < text.width:
                text.scale(room / text.width, about_point=text.get_right())
            return fixed(VGroup(line, text).set_z_index(POLICY_LAYER))

        # ---- The five steps, kept beside the graph in a corner card.
        card_head = Tex(r'\textsf{Finding DWL}', color=TITLE).scale(0.62)
        steps = VGroup(
            Tex(r"1. Society's curves", color=CAPTION),
            Tex(r"2. $Q^*$: where society's curves cross", color=CAPTION),
            Tex(r'3. $Q$: what the market trades', color=CAPTION),
            Tex(r'4. One unit: social benefit vs. social cost', color=CAPTION),
            Tex(r'5. Every unit between $Q$ and $Q^*$', color=CAPTION)).scale(0.55).arrange(DOWN, aligned_edge=LEFT, buff=0.24)
        card = fixed(VGroup(card_head, steps).arrange(DOWN, aligned_edge=LEFT, buff=0.3))
        if card.width > 3.9:
            card.scale(3.9 / card.width)
        card.move_to([3.85, 2.65, 0], aligned_edge=UL)

        def focus(*active):
            return [step.animate.set_color(DEFINITION if k + 1 in active else CAPTION) for k, step in enumerate(steps)]

        # ---- Stage 2: the close-up compressed around one line up from the unit's quantity.
        def check_icon():
            return VMobject(color=EFFICIENT, stroke_width=5).set_points_as_corners(
                [[-0.28, 0, 0], [-0.08, -0.20, 0], [0.32, 0.27, 0]]).scale(0.85)

        def cross_icon():
            return VGroup(Line([-0.22, -0.22, 0], [0.22, 0.22, 0], color=GUIDE, stroke_width=5),
                          Line([-0.22, 0.22, 0], [0.22, -0.22, 0], color=GUIDE, stroke_width=5)).scale(0.85)

        def exchange_questions():
            return fixed(VGroup(
                Tex('Will they exchange?', color=DEFINITION).scale(0.60).move_to([-4.8, -3.05, 0]),
                Tex('Is it good for society?', color=DEFINITION).scale(0.60).move_to([4.8, -3.05, 0])).set_z_index(TOP_LAYER))

        def layered(group, z):
            """A fixed group at layer z, its children too, so a child animated on its own keeps it."""
            group.set_z_index(z)
            for m in group:
                m.set_z_index(z)
            return fixed(group)

        def bracket(x, lo, hi, color, toward):
            """A comparison bracket: a vertical span with small end ticks toward the unit."""
            tick = 0.07 * (1 if toward is RIGHT else -1)
            return VGroup(Line([x, y_at(lo), 0], [x, y_at(hi) + 1e-6, 0], color=color, stroke_width=STRUCTURE),
                          Line([x, y_at(lo), 0], [x + tick, y_at(lo), 0], color=color, stroke_width=STRUCTURE),
                          Line([x, y_at(hi), 0], [x + tick, y_at(hi), 0], color=color, stroke_width=STRUCTURE))

        def leader(x0, x1, v, color, avoid=()):
            """A dashed lead at value v from x0 to x1, broken around any text in `avoid` it would cross."""
            y, lo, hi = y_at(v), min(x0, x1), max(x0, x1)
            cuts = sorted((b.get_left()[0] - 0.05, b.get_right()[0] + 0.05) for b in avoid
                          if b.get_bottom()[1] - 0.03 < y < b.get_top()[1] + 0.03)
            runs, start = [], lo
            for a, b in cuts + [(hi, hi)]:
                if a > start:
                    runs.append((start, min(a, hi)))
                start = max(start, b)
            # Built from x0 toward x1, so Create draws the lead out of the value into the bracket.
            pieces = VGroup()
            for a, b in (runs if x0 <= x1 else [(b, a) for a, b in reversed(runs)]):
                pieces.add(DashedLine([a, y, 0], [b, y, 0], color=color, stroke_width=ANNOTATION, dash_length=0.07))
            return pieces

        def price_stub(x, p):
            """A short solid piece of a price line at a bracket's end, past its tick, toward the unit."""
            return Line([x + 0.07, y_at(p), 0], [x + 0.32, y_at(p), 0], color=GUIDE, stroke_width=STRUCTURE)

        def block(xl, xr, lo, hi, color, opacity):
            return Polygon([xl, y_at(lo), 0], [xr, y_at(lo), 0], [xr, y_at(hi), 0], [xl, y_at(hi), 0],
                           stroke_width=0, fill_color=color, fill_opacity=opacity)

        def fade_mask(xl, xr, lo, hi, steps=12):
            """Background strips that fade a bar out toward its bottom, so it floats above the axis."""
            g = VGroup()
            for k in range(steps):
                a, b = lo + (hi - lo) * k / steps, lo + (hi - lo) * (k + 1) / steps
                g.add(Polygon([xl, y_at(a), 0], [xr, y_at(a), 0], [xr, y_at(b), 0], [xl, y_at(b), 0],
                              stroke_width=0, fill_color=BG, fill_opacity=1 - (k + 0.5) / steps))
            return g

        def clear_of(text, x, spans):
            """Move a name straight down until it overlaps none of the (bottom, top) spans in its column."""
            moved = True
            while moved:
                moved = False
                for lo, hi in spans:
                    if text.get_bottom()[1] < hi + 0.03 and text.get_top()[1] > lo - 0.03:
                        text.move_to([x, lo - NAME_GAP - text.height / 2, 0])
                        moved = True
            return text

        def unit_stage(system, u):
            """The u-th unit on the graph: one white line up from Q = u with its ordinal under it,
            the close-up's two columns as small bars standing a little off either side of it, each
            bar's top edge running inward to a dot on the line, names on the bars, values outside,
            under a policy each party's price as a short solid line across its own bar (with the
            bar filled more solidly between price and value on a traded unit: its CS, its PS), the
            social gap on the taller bar, and the comparison brackets left (market) and right
            (society) with their verdicts. Every piece is returned by name so the beats can stage
            them in the order they are found."""
            x_u = x_at(u)
            pt = lambda v: np.array([x_u, y_at(v), 0])
            market_yes = u <= system['q_market']
            society_yes = u <= system['q_star']
            values = {}
            for pieces in (system['buyer'], system['seller']):
                for f, _, _, name in pieces:
                    values[name] = round(f(u), 2)
            prices = dict(zip(system['price_names'], system['prices'] or ()))
            party_price = {-1: prices.get('P_b'), +1: prices.get('P_s')}
            party_value = {-1: 'MB', +1: 'MC'}
            curve_top = max(values.values())
            top = max([curve_top] + list(prices.values()))
            line = VGroup(Line(pt(0), pt(curve_top), color=INK, stroke_width=STRUCTURE),
                          Tex(ordinal(u), color=INK).scale(QUANTITY_NUMBER_SCALE)
                          .move_to(ax.c2p(u, 0) + DOWN * QUANTITY_NUMBER_OFFSET))
            bars, masks, edges, dots, names, value_words = (VGroup() for _ in range(6))
            price_marks, surplus, gap = VGroup(), VGroup(), VGroup()
            span, outer_x, name_spots, ext_span, ext_hidden = {}, {}, {}, None, False
            # Screen spans a name must stay clear of, per column, tagged with the beat they arrive in:
            # 0 the price segments, 1 the MC leader, 2 the fills, 3 the benefit projection, 4 the gap.
            events = {-1: [], +1: []}
            for side, pieces in ((-1, system['buyer']), (+1, system['seller'])):
                inner, outer = x_u + side * GAP, x_u + side * (GAP + BAR_W)
                xl, xr = min(inner, outer), max(inner, outer)
                span[side], outer_x[side] = (xl, xr), outer
                low = 0
                for k, (f, fill_color, edge_color, name) in enumerate(pieces):
                    high = values[name]
                    bars.add(block(xl, xr, low, high, fill_color, BAR_FILL))
                    if k == 0:
                        masks.add(fade_mask(xl, xr, 0.0, min(BAR_FADE_TOP * high, high - 0.3)))
                    edges.add(Line([outer, y_at(high), 0], [x_u + side * NEAR, y_at(high), 0],
                                   color=edge_color, stroke_width=STRUCTURE))
                    dots.add(Dot(pt(high), radius=0.065, color=edge_color))
                    # The first piece's name hangs under its flange, a stacked piece's sits above; EXT mid-piece.
                    name_spots[name] = (side, y_at(high), -1 if k == 0 else +1, edge_color)
                    if fill_color == EXT:
                        name_spots['EXT'] = (side, y_at(low + 0.3 * (high - low)), 0, EXT)
                        ext_span = (side, low, high)
                    low = high
            for side, pieces in ((-1, system['buyer']), (+1, system['seller'])):
                for f, _, edge_color, name in pieces:
                    text = Tex(rf'\${values[name]:.2f}', color=edge_color).scale(NUMBER_SCALE)
                    text.next_to([outer_x[side], y_at(values[name]), 0], LEFT if side < 0 else RIGHT, buff=0.12)
                    value_words.add(text)
            word_of = dict(zip([n for _, _, _, n in system['buyer'] + system['seller']], value_words))
            # Under a policy each party's price crosses its own bar as a short solid line, named at
            # the outer end (nudged off the value there if the two would touch). On a traded unit the
            # bar fills more solidly between the price and the party's value: its CS, its PS.
            p_words, fill_spans = {}, {}
            if top > curve_top + 1e-9:
                price_marks.add(Line(pt(curve_top), pt(top), color=INK, stroke_width=STRUCTURE))
            for side in (-1, +1):
                p = party_price[side]
                if p is None:
                    continue
                xl, xr = span[side]
                ends = (xl - 0.06, xr + 0.06)
                price_marks.add(Line([ends[0], y_at(p), 0], [ends[1], y_at(p), 0], color=GUIDE, stroke_width=STRUCTURE))
                name = 'P_b' if side < 0 else 'P_s'
                word = Tex(f'${name}$', color=GUIDE).scale(LABEL_SCALE)
                word.next_to([ends[0] if side < 0 else ends[1], y_at(p), 0], LEFT if side < 0 else RIGHT, buff=0.08)
                value, v = word_of[party_value[side]], values[party_value[side]]
                if word.get_bottom()[1] < value.get_top()[1] + 0.03 and word.get_top()[1] > value.get_bottom()[1] - 0.03:
                    away = 1 if p >= v else -1
                    edge = value.get_top()[1] if away > 0 else value.get_bottom()[1]
                    word.set_y(edge + away * (0.03 + word.height / 2))
                price_marks.add(word)
                p_words[side] = word
                events[side].append((0, (y_at(p) - 0.02, y_at(p) + 0.02)))
                if market_yes:
                    surplus.add(block(xl, xr, min(p, v), max(p, v), DEMAND if side < 0 else SUPPLY, SURPLUS_FILL))
                    fill_spans[side] = (min(p, v), max(p, v))
                    events[side].append((2, tuple(sorted((y_at(p), y_at(v))))))
            benefit_name, cost_name = system['society']
            benefit_v, cost_v = values[benefit_name], values[cost_name]
            # Lines that cross a column on their way to a bracket: the MC leader crosses the buyer's,
            # society's benefit projection the seller's.
            events[-1].append((1, (y_at(values['MC']) - 0.02, y_at(values['MC']) + 0.02)))
            events[+1].append((3, (y_at(benefit_v) - 0.02, y_at(benefit_v) + 0.02)))
            # The social gap on the taller bar, between the two social values; where that bar's own
            # surplus fill lies inside it, the gap leaves the fill showing. Both-no units show nothing.
            if market_yes or society_yes:
                lo, hi = sorted((benefit_v, cost_v))
                gap_side = +1 if cost_v > benefit_v else -1
                pieces = [(lo, hi)]
                if gap_side in fill_spans and lo <= fill_spans[gap_side][0] and fill_spans[gap_side][1] <= hi:
                    a, b = fill_spans[gap_side]
                    pieces = [q for q in ((lo, a), (b, hi)) if q[1] - q[0] > 1e-9]
                for s, e in pieces:
                    gap.add(block(*span[gap_side], s, e, DWL if market_yes != society_yes else TOTAL, STRIP_OPACITY))
                if ext_span and ext_span[0] == gap_side and lo <= ext_span[1] and hi >= ext_span[2]:
                    ext_hidden = True              # The gap says it all when it hides the whole piece.
                events[gap_side].append((4, (y_at(lo), y_at(hi))))
            # Names: under their flange (above, for a stacked piece), then straight down past whatever
            # has arrived in their column by each beat, so a name moves only when something lands
            # under it (and EXT leaves when the gap covers its whole piece).
            name_tex = {name: Tex(name, color=color).scale(LABEL_SCALE) for name, (_, _, _, color) in name_spots.items()}

            def placements(k):
                spans = {s: [sp for b, sp in events[s] if b <= k] for s in (-1, +1)}
                out = {}
                for name, (side, y, anchor, color) in name_spots.items():
                    if name == 'EXT' and ext_hidden and k >= 4:
                        continue
                    text, x = name_tex[name], sum(span[side]) / 2
                    if anchor < 0:
                        text.move_to([x, y - NAME_GAP - text.height / 2, 0])
                    elif anchor > 0:
                        text.move_to([x, y + NAME_GAP + text.height / 2, 0])
                    else:
                        text.move_to([x, y, 0])
                    if anchor <= 0:
                        clear_of(text, x, spans[side])
                        spans[side].append((text.get_bottom()[1], text.get_top()[1]))
                    out[name] = text.get_center().copy()
                return out

            name_at = [placements(k) for k in range(5)]
            for name, text in name_tex.items():
                text.move_to(name_at[0][name])
                names.add(text)
            # Comparisons. The market's: MB against MC, or under a policy each party against its price.
            # Society's: the two social values. A near value is led from its label, a far one projected
            # from its dot (or its price segment) in its own color.
            all_text = list(value_words) + list(p_words.values())
            all_words = all_text
            left_x = min(w.get_left()[0] for w in all_words) - 0.55
            max_right = max(w.get_right()[0] for w in all_words)
            right_x = min(max_right + 0.55, max(x_at(60) + 0.3, max_right + 0.18))
            mb_value = word_of['MB']
            market_marks, market_answers = VGroup(), []
            if prices:
                p_buyer, p_seller = prices['P_b'], prices['P_s']
                # When the seller's span lies inside the buyer's, it gets its own column further out.
                nested = max(min(values['MB'], p_buyer), min(values['MC'], p_seller)) < \
                         min(max(values['MB'], p_buyer), max(values['MC'], p_seller))
                seller_x = left_x - 0.85 if nested else left_x
                market_marks.add(bracket(left_x, values['MB'], p_buyer, DEMAND, RIGHT),
                                 leader(mb_value.get_left()[0] - 0.04, left_x, values['MB'], DEMAND, all_text),
                                 price_stub(left_x, p_buyer))
                market_marks.add(bracket(seller_x, values['MC'], p_seller, SUPPLY, RIGHT),
                                 leader(x_u - NEAR, seller_x, values['MC'], SUPPLY, all_text),
                                 price_stub(seller_x, p_seller))
                # Each party's verdict sits beside its bracket at the price it faces.
                for x, p, yes in ((left_x, p_buyer, values['MB'] >= p_buyer), (seller_x, p_seller, values['MC'] <= p_seller)):
                    icon = (check_icon() if yes else cross_icon()).scale(0.8)
                    market_answers.append(fixed(icon.move_to([x - 0.38, y_at(p), 0]).set_z_index(TOP_LAYER)))
                market_yes_drawn = values['MB'] >= p_buyer and values['MC'] <= p_seller
            else:
                market_marks.add(bracket(left_x, values['MB'], values['MC'], TOTAL, RIGHT),
                                 leader(mb_value.get_left()[0] - 0.04, left_x, values['MB'], DEMAND, all_text),
                                 leader(x_u - NEAR, left_x, values['MC'], SUPPLY, all_text))
                icon = (check_icon() if values['MB'] >= values['MC'] else cross_icon()).scale(0.8)
                market_answers.append(fixed(icon.move_to([left_x - 0.38, (y_at(values['MB']) + y_at(values['MC'])) / 2, 0]).set_z_index(TOP_LAYER)))
                market_yes_drawn = values['MB'] >= values['MC']
            assert market_yes_drawn == market_yes
            assert (benefit_v >= cost_v) == society_yes
            # The cost value sits on the seller's side, near the right bracket; the benefit is projected.
            near_name, far_name = cost_name, benefit_name
            society_marks = VGroup(bracket(right_x, benefit_v, cost_v, TOTAL, LEFT),
                                   leader(word_of[near_name].get_right()[0] + 0.04, right_x, values[near_name], SUPPLY, all_text),
                                   leader(x_u + NEAR, right_x, values[far_name], DEMAND, all_text))
            verdict = VGroup((check_icon() if society_yes else cross_icon()).scale(0.8))
            if market_yes or society_yes:
                verdict.add(Tex('TS' if society_yes else 'DWL', color=TOTAL if society_yes else INK).scale(LABEL_SCALE))
            verdict.arrange(DOWN, buff=0.1).move_to([right_x + 0.45, (y_at(benefit_v) + y_at(cost_v)) / 2, 0])
            # Under a policy past its quantity, the market's faint price lines continue out to the unit.
            extension = VGroup()
            if prices and u > system['q_market']:
                for p in prices.values():
                    extension.add(DashedLine(ax.c2p(system['q_market'], p), pt(p), color=GUIDE, stroke_width=2)
                                  .set_opacity(DIM_REST))
            return dict(system=system, unit=u, verdicts=(market_yes, society_yes),
                        line=layered(line, BAR_LAYER),
                        bars=layered(bars, BAR_LAYER),
                        masks=layered(masks, BAR_LAYER + 1),
                        surplus=layered(surplus, BAR_LAYER + 2),
                        gap=layered(gap, GAP_LAYER),
                        edges=layered(edges, EDGE_LAYER),
                        price_marks=layered(price_marks, EDGE_LAYER),
                        dots=layered(dots, EDGE_LAYER + 1),
                        names=layered(names, TOP_LAYER),
                        values=layered(value_words, TOP_LAYER),
                        prices=layered(extension, GUIDE_LAYER),
                        market_marks=layered(market_marks, TOP_LAYER),
                        market_answers=market_answers,
                        society_marks=layered(society_marks, TOP_LAYER),
                        society_answer=layered(verdict, TOP_LAYER),
                        name_tex=name_tex, name_at=name_at)

        STAGE_KEYS = ('line', 'bars', 'masks', 'surplus', 'gap', 'edges', 'price_marks', 'dots', 'names', 'values',
                      'prices', 'market_marks', 'society_marks', 'society_answer')

        def stage_parts(stage):
            return [stage[k] for k in STAGE_KEYS if len(stage[k])] + stage['market_answers']

        curve_words = (mb_word, mc_word, msc_word, msb_word)
        hides = lambda m: m in curve_words or getattr(m, 'hides_in_stage', False)

        def market_fade(pieces, curves, on):
            """The market goes faint while one unit is inspected; its curve names and its dots and
            drops hide outright, so nothing sits under a verdict or inside a bar. The card does not
            change."""
            return ([m.animate.set_opacity(DIM_CURVES if on else 1) for m in curves] +
                    [m.animate.set_opacity((0 if hides(m) else DIM_REST) if on else 1) for m in pieces])

        def reveal_unit(stage, pause_prefix=None):
            """The unit's picture in the order it is found, once the line stands at the quantity and
            the dots sit where it meets the curves: the flanges pop out from the dots, then the
            numbers and names (and any prices), then the bars drop from the flanges."""
            if pause_prefix:
                pieces = stage['system']['buyer'] + stage['system']['seller']
                for i, (_, fill_color, _, name) in enumerate(pieces):
                    self.play(GrowFromPoint(stage['edges'][i], stage['dots'][i].get_center()), run_time=0.35)
                    labels = [stage['name_tex'][name], stage['values'][i]]
                    if fill_color == EXT:
                        labels.append(stage['name_tex']['EXT'])
                    self.play(*[FadeIn(m) for m in labels], run_time=0.35)
                    self.pause(f'{pause_prefix}.{name.lower()}')
                self.add(stage['edges'], stage['names'], stage['values'])
                prices = [stage[k] for k in ('prices', 'price_marks') if len(stage[k])]
                if prices:
                    self.play(*[FadeIn(m) for m in prices], run_time=0.35)
            else:
                self.play(*[GrowFromPoint(e, d.get_center()) for e, d in zip(stage['edges'], stage['dots'])], run_time=0.35)
                self.add(stage['edges'])
                words = [stage[k] for k in ('names', 'values', 'prices', 'price_marks') if len(stage[k])]
                self.play(*[FadeIn(m) for m in words], run_time=0.35)
            bars = stage['bars']
            bars.save_state()
            for bar in bars:
                bar.stretch(0.001, 1, about_edge=UP)
            self.play(Restore(bars), FadeIn(stage['masks']), run_time=0.45)

        def name_moves(stage, k):
            """Animations that move the names to their places once beat k's pieces are in, and fade
            a name the gap hides. The group is re-added after the play to regroup the moved names."""
            anims = []
            for name, text in list(stage['name_tex'].items()):
                target = stage['name_at'][k].get(name)
                if target is None:
                    anims.append(FadeOut(text))
                    del stage['name_tex'][name]
                    stage['names'].remove(text)
                elif np.linalg.norm(text.get_center() - target) > 1e-4:
                    anims.append(text.animate.move_to(target))
            return anims

        def settle_names(stage, k):
            """The names at their beat-k places at once, for a unit that arrives already decided."""
            for name, text in list(stage['name_tex'].items()):
                target = stage['name_at'][k].get(name)
                if target is None:
                    del stage['name_tex'][name]
                    stage['names'].remove(text)
                else:
                    text.move_to(target)

        def decide_unit(stage, lines, pause_prefix=None):
            """Then the values decide, in the close-up's beats: the market's comparison, its verdict
            (a traded unit's CS and PS with it), society's comparison, its verdict with the gap.
            With a pause prefix each beat gets its pausepoint; without one they run straight through."""
            pause = (lambda name: self.pause(f'{pause_prefix}.{name}')) if pause_prefix else (lambda name: None)
            self.play(*[Create(m) for m in stage['market_marks']], *name_moves(stage, 1), run_time=0.6)
            self.add(stage['market_marks'], stage['names'])      # Regroup the drawn pieces at their layer.
            pause('private.compare')
            self.play(*[FadeIn(m) for m in stage['market_answers']],
                      *([FadeIn(stage['surplus'])] if len(stage['surplus']) else []), *name_moves(stage, 2), run_time=0.4)
            self.add(stage['names'])
            pause('private')
            self.play(*[Create(m) for m in stage['society_marks']], *name_moves(stage, 3), run_time=0.6)
            self.add(stage['society_marks'], stage['names'])
            pause('social.compare')
            stage['note'] = teaching(lines)
            self.play(*([FadeIn(stage['gap'])] if len(stage['gap']) else []), FadeIn(stage['society_answer']),
                      FadeIn(stage['note']), *name_moves(stage, 4), run_time=0.5)
            self.add(stage['names'])

        def show_unit(system, u, pause_prefix, lines, faded, curves, moving_wedge=()):
            """Stage 2 without a close-up: the market fades as the line rises at the quantity, the
            dots land where it meets the curves, the picture fills in, then the beats decide."""
            stage = unit_stage(system, u)
            stage.update(questions=exchange_questions(), first=u, faded=faded, curves=curves)
            self.play(*market_fade(faded, curves, True), *moving_wedge, FadeIn(stage['questions']), *focus(4),
                      GrowFromEdge(stage['line'][0], DOWN), FadeIn(stage['line'][1]), run_time=1.0)
            self.add(stage['line'])
            self.play(*[GrowFromCenter(d) for d in stage['dots']], run_time=0.3)
            self.add(stage['dots'])
            reveal_unit(stage)
            self.pause(f'{pause_prefix}.values')
            decide_unit(stage, lines, pause_prefix)
            return stage

        def jump_unit(stage, u, lines, pause_prefix, explain_values=False):
            """The unit moves to another quantity: the picture clears down to the line and the dots,
            which slide along the curves to the new quantity (the ordinal counting with them); the
            picture fills back in there and the beats decide. The first two moves pause at the
            quantity and reveal each marginal value separately; later moves reveal them together."""
            new = unit_stage(stage['system'], u)
            new.update(questions=stage['questions'], first=stage['first'], faded=stage['faded'], curves=stage['curves'])
            leaving = [stage[k] for k in STAGE_KEYS if k not in ('line', 'dots') and len(stage[k])]
            self.play(*[FadeOut(m) for m in leaving + stage['market_answers'] + [stage['note']]], run_time=0.4)
            # The ordinal counts through the units under the moving line (a glyph morph would melt).
            old_u = stage['unit']
            lo_u, hi_u = min(old_u, u), max(old_u, u)
            counter = layered(VGroup(*[Tex(ordinal(q), color=INK).scale(QUANTITY_NUMBER_SCALE)
                                       for q in range(lo_u, hi_u + 1)]), BAR_LAYER)

            def count(group, alpha):
                q = old_u + (u - old_u) * smooth(alpha)   # The updater gets raw alpha; ease it like the Transforms.
                for k, word in enumerate(group):
                    on = lo_u + k == int(round(q))
                    word.set_opacity(1 if on else 0)
                    if on:
                        word.move_to(ax.c2p(q, 0) + DOWN * QUANTITY_NUMBER_OFFSET)

            fns = [f for f, *_ in stage['system']['buyer'] + stage['system']['seller']]

            def slide(line_mob, alpha):
                q = old_u + (u - old_u) * smooth(alpha)
                line_mob.put_start_and_end_on(ax.c2p(q, 0), ax.c2p(q, max(f(q) for f in fns)))

            count(counter, 0)
            self.remove(stage['line'][1])
            self.add(counter)
            self.play(UpdateFromAlphaFunc(stage['line'][0], slide), UpdateFromAlphaFunc(counter, count),
                      Transform(stage['dots'], new['dots'].copy()), run_time=1.0)
            self.remove(stage['line'][0], counter, stage['dots'])
            self.add(new['line'], new['dots'])
            if explain_values:
                self.pause(f'{pause_prefix}.quantity')
            reveal_unit(new, pause_prefix if explain_values else None)
            self.pause(f'{pause_prefix}.values')
            decide_unit(new, lines)
            return new

        def stack_units(stage, line, word_at):
            """Stage 3: every unit between the two quantities, as bars between society's curves,
            building outward from the first unit shown in stage 2, with the market back."""
            system = stage['system']
            low, high = sorted((system['q_star'], system['q_market']))
            benefit, cost = system['benefit'], system['cost']
            order = sorted(range(low, high), key=lambda q: abs(q - (stage['first'] - 1)))
            loss = fixed(VGroup(*[unit_slice(ax, q, lambda x: min(benefit(x), cost(x)), lambda x: max(benefit(x), cost(x)),
                                             DWL, STRIP_OPACITY) for q in range(low, high)]).set_z_index(STRIP_LAYER))
            word = fixed(Tex('DWL', color=INK).scale(0.6).move_to(word_at).set_z_index(WORD_LAYER))
            self.play(*[FadeOut(m) for m in stage_parts(stage)], FadeOut(stage['questions']), FadeOut(stage['note']),
                      *market_fade(stage['faded'], stage['curves'], False), *focus(5))
            note = teaching(line)
            self.play(LaggedStart(*[FadeIn(loss[q - low]) for q in order], lag_ratio=0.3),
                      FadeIn(word), FadeIn(note), run_time=1.8)
            self.remove(*loss)
            self.add(loss)
            return loss, word, note

        # ---- 0.a · Shared bumper. Thesis line left for Taylor.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'C', 4)
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode))
        self.clear()

        # ---- 1.a · One plain market and the question.
        head = fixed(title('Finding Deadweight Loss'))
        context = fixed(subtitle(head, 'Four markets, one rule.'))
        market_mark = point_mark(40, 4, GUIDE)
        market_word = quantity_word(40, r'$\hat{Q}$', GUIDE)
        note = teaching('Where is the deadweight loss?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(ax), FadeIn(axis_words),
                  FadeIn(demand), FadeIn(supply), FadeIn(mb_word), FadeIn(mc_word))
        self.play(FadeIn(market_mark), FadeIn(market_word), FadeIn(note))
        self.pause('1.a')

        # ---- 1.b · The five steps, one at a time, in the corner card.
        self.remove(note)
        note = teaching('The same five steps find it in every market in Part C.')
        self.play(FadeIn(card_head), FadeIn(note))
        self.play(LaggedStart(*[FadeIn(step, shift=RIGHT * 0.2) for step in steps], lag_ratio=0.5), run_time=2.5)
        self.remove(card_head, *steps)
        self.add(card)
        self.pause('1.b')

        # ---- 2.a · Negative externality, step 1: society counts the external cost, unit by unit.
        self.remove(head, context, note)
        head = fixed(title('Negative Externalities'))
        cost_bars = strips(mc, msc, EXT, 0.45, 0, 60).set_z_index(FILL_LAYER)
        note = teaching('Society counts the external cost: MSC = MC + EXT.')
        self.play(FadeIn(head), FadeIn(cost_bars), FadeIn(note), *focus(1))
        self.play(FadeIn(social_cost), FadeIn(msc_word))
        self.play(FadeOut(cost_bars))
        self.pause('2.a')

        # ---- 2.a.quantities · Steps 2 and 3: Q* where MB meets MSC; the market still trades 40.
        efficient_mark = point_mark(32, 5.6, FOCUS, radius=0.085)
        efficient_word = quantity_word(32, '$Q^*$', FOCUS)
        self.remove(note)
        note = teaching(r'$Q^* = 32$, where MB meets MSC. The market ignores EXT and trades $\hat{Q} = 40$.')
        self.play(FadeIn(efficient_mark), FadeIn(efficient_word), *focus(2))
        self.play(Indicate(market_mark[1], color=GUIDE, scale_factor=1.6), FadeIn(note), *focus(3))
        self.pause('2.a.quantities')

        # ---- 2.b.select · Stage 1 starts from one unit between the two quantities.
        graph = fixed(VGroup(ax, axis_words, demand, supply, social_cost, market_word, efficient_word))
        marks = [market_mark, efficient_mark, mb_word, mc_word, msc_word]
        self.remove(*graph)
        self.add(graph)
        pair = fixed(VGroup(unit_slice(ax, 35, zero, mb, DEMAND, BASE_OPACITY),
                            unit_slice(ax, 35, zero, mc, SUPPLY, BASE_OPACITY),
                            unit_slice(ax, 35, mc, msc, EXT, BASE_OPACITY)))
        pair_box = fixed(SurroundingRectangle(pair, color=FOCUS, buff=0.025, stroke_width=2))
        self.remove(note)
        note = teaching(r'Take one unit between $Q^*$ and $\hat{Q}$: the 36th.')
        self.play(FadeIn(pair), FadeIn(pair_box), FadeIn(note), *focus(4))
        self.pause('2.b.select')

        # ---- 2.b.values · The close-up: private values and the external cost, C1's layout.
        pair_target = fixed(VGroup())
        for x, low, high, color in [(-1.16, 0, 4.8, DEMAND), (0.06, 0, 3.8, SUPPLY), (0.06, 3.8, 5.8, EXT)]:
            pair_target.add(fixed(Polygon([x, detail_y(low), 0], [x + 1.1, detail_y(low), 0],
                                          [x + 1.1, detail_y(high), 0], [x, detail_y(high), 0],
                                          stroke_width=0, fill_color=color, fill_opacity=BASE_OPACITY)))
        self.play(FadeOut(graph), *[FadeOut(m) for m in marks], FadeOut(card), FadeOut(pair_box), FadeOut(note),
                  Transform(pair, pair_target), run_time=1.6)
        detail_edges = fixed(VGroup(
            *[Line(bar.get_corner(UL), bar.get_corner(UR), color=color, stroke_width=3)
              for bar, color in zip(pair_target, [DEMAND, SUPPLY, SUPPLY])])).set_z_index(3)
        detail_floor = fixed(Line([-1.3, DETAIL_BASE, 0], [1.3, DETAIL_BASE, 0], color=MUTED).set_z_index(3))
        detail_values = fixed(VGroup(
            Tex(r'\$4.80', color=DEMAND).scale(0.72).next_to([-1.16, detail_y(4.8), 0], LEFT, buff=0.25),
            Tex(r'\$3.80', color=SUPPLY).scale(0.72).next_to([1.16, detail_y(3.8), 0], RIGHT, buff=0.25),
            Tex(r'\$5.80', color=SUPPLY).scale(0.72).next_to([1.16, detail_y(5.8), 0], RIGHT, buff=0.25))).set_z_index(4)
        detail_names = fixed(VGroup(
            Tex('MB', color=DEMAND).scale(0.58).next_to([-0.61, detail_y(4.8), 0], DOWN, buff=0.10),
            Tex('MC', color=SUPPLY).scale(0.58).next_to([0.61, detail_y(3.8), 0], DOWN, buff=0.10),
            Tex('MSC', color=SUPPLY).scale(0.58).next_to([0.61, detail_y(5.8), 0], UP, buff=0.10),
            Tex('EXT', color=EXT).scale(0.58).move_to([0.61, detail_y(4.8), 0]))).set_z_index(4)
        detail_people = fixed(Group())
        for x, color, name in [(-1.45, DEMAND, 'Buyer'), (1.45, SUPPLY, 'Seller')]:
            detail_people.add(fixed(Ellipse(width=0.42, height=0.05, stroke_width=0,
                fill_color=color, fill_opacity=0.28).move_to([x, DETAIL_BASE - 0.60, 0])))
            detail_people.add(fixed(Sphere(radius=0.18, color=color, opacity=1, resolution=(32, 24))
                .move_to([x, DETAIL_BASE - 0.35, 0])).apply_depth_test())
            detail_people.add(fixed(Tex(name, color=INK).scale(0.60).move_to([x, DETAIL_BASE - 0.94, 0])))
        unit_context = fixed(subtitle(head, r'The 36th unit: between $Q^*$ and $\hat{Q}$.'))
        questions = exchange_questions()
        self.add(detail_people)
        self.play(FadeIn(detail_edges), FadeIn(detail_floor), FadeIn(detail_values), FadeIn(detail_names),
                  FadeIn(unit_context), FadeIn(questions))
        self.pause('2.b.values')

        # ---- 2.b.private · The market's answer: MB above MC, so they exchange.
        private_guides = fixed(VGroup(
            Line([-3.65, detail_y(3.8), 0], [-3.65, detail_y(4.8), 0], color=TOTAL, stroke_width=3),
            DashedLine(detail_values[0].get_left() + LEFT * 0.12, [-3.65, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([0.06, detail_y(3.8), 0], [-3.65, detail_y(3.8), 0], color=TOTAL, stroke_width=1.4)))
        private_answer = fixed(check_icon().next_to([-3.65, detail_y(4.3), 0], LEFT, buff=0.3))
        self.play(FadeIn(private_guides))
        self.pause('2.b.private.compare')
        self.play(FadeIn(private_answer))
        self.pause('2.b.private')

        # ---- 2.b.social · Society's answer: MSC above MB, so the exchange costs society $1.
        social_guides = fixed(VGroup(
            Line([3.65, detail_y(4.8), 0], [3.65, detail_y(5.8), 0], color=TOTAL, stroke_width=3),
            DashedLine(detail_values[2].get_right() + RIGHT * 0.12, [3.65, detail_y(5.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([-0.06, detail_y(4.8), 0], [0.06, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4),
            DashedLine([1.16, detail_y(4.8), 0], [3.65, detail_y(4.8), 0], color=TOTAL, stroke_width=1.4)))
        social_answer = fixed(VGroup(cross_icon(), Tex('DWL', color=INK)).arrange(DOWN, buff=0.16).scale(0.70)
                              .next_to([3.65, detail_y(5.3), 0], RIGHT, buff=0.3))
        detail_loss = fixed(Polygon([0.06, detail_y(4.8), 0], [1.16, detail_y(4.8), 0],
                                    [1.16, detail_y(5.8), 0], [0.06, detail_y(5.8), 0],
                                    stroke_width=0, fill_color=DWL, fill_opacity=STRIP_OPACITY).set_z_index(1))
        self.play(FadeIn(social_guides))
        self.pause('2.b.social.compare')
        note = teaching(r'Trading the 36th unit costs society \$1: its deadweight loss.')
        self.play(FadeIn(detail_loss), FadeIn(social_answer), FadeIn(note),
                  detail_names[3].animate.move_to([0.61, detail_y(4.3), 0]))
        self.pause('2.b.social')

        # ---- 2.c · Stage 2: the close-up compresses onto the market around the 36th unit's line.
        # Every close-up piece lands on its counterpart: columns on the bars, edges on the flanged
        # edges, values and names on theirs, brackets on brackets, icons on icons, the grey loss on
        # the gap. The market returns faint behind it.
        stage = unit_stage(negative, 36)
        stage.update(questions=questions, first=36, faded=[graph] + marks, curves=[demand, supply, social_cost])
        settle_names(stage, 4)
        for m, z in ((pair, BAR_LAYER), (detail_loss, GAP_LAYER), (detail_edges, EDGE_LAYER),
                     (detail_values, TOP_LAYER), (detail_names, TOP_LAYER), (private_guides, TOP_LAYER),
                     (social_guides, TOP_LAYER), (private_answer, TOP_LAYER), (social_answer, TOP_LAYER)):
            m.set_z_index(z)
        for m in [graph] + marks:
            m.set_opacity(0 if hides(m) else DIM_REST)
        for m in (demand, supply, social_cost):
            m.set_opacity(DIM_CURVES)
        self.remove(detail_people[1], detail_people[4])        # The spheres cannot fade; the rest can.
        self.play(FadeOut(detail_floor), FadeOut(unit_context), FadeOut(note),
                  *[FadeOut(detail_people[k]) for k in (0, 2, 3, 5)], run_time=0.3)
        self.remove(detail_people)
        # Solid shapes morph onto their counterparts; the dashed guides and brackets, whose dash
        # counts and parts differ, crossfade instead.
        self.play(Transform(pair, stage['bars'].copy()),
                  Transform(detail_edges, stage['edges'].copy()),
                  Transform(detail_values, stage['values'].copy()),
                  Transform(detail_names, stage['names'].copy()),
                  Transform(detail_loss, stage['gap'][0].copy()),
                  Transform(private_answer, stage['market_answers'][0].copy()),
                  Transform(social_answer, stage['society_answer'].copy()),
                  FadeOut(private_guides), FadeOut(social_guides),
                  FadeIn(stage['market_marks']), FadeIn(stage['society_marks']),
                  FadeIn(graph), *[FadeIn(m) for m in marks], FadeIn(card),
                  FadeIn(stage['line']), FadeIn(stage['masks']), FadeIn(stage['dots']), run_time=1.6)
        self.remove(pair, detail_edges, detail_values, detail_names, detail_loss, private_guides, social_guides,
                    private_answer, social_answer)
        self.add(*[stage[k] for k in STAGE_KEYS if len(stage[k])], *stage['market_answers'])
        stage['note'] = teaching(r'The 36th unit: they exchange, but it costs society \$1.')
        self.play(FadeIn(stage['note']), run_time=0.4)
        self.pause('2.c')

        # ---- 2.d.inside · Jump to a unit both answers accept: its gap is surplus, not loss.
        stage = jump_unit(stage, 28, 'The 28th unit: both answers are yes, so its gap is surplus, not loss.', '2.d.inside', explain_values=True)
        self.pause('2.d.inside')

        # ---- 2.d.outside · Jump past both quantities: never traded, nothing lost.
        stage = jump_unit(stage, 44, 'The 44th unit: both answers are no. It is never traded, so nothing is lost.', '2.d.outside', explain_values=True)
        self.pause('2.d.outside')

        # ---- 2.d · Stage 3: every unit between the two quantities, starting from the 36th.
        loss, loss_word, note = stack_units(
            stage, r'DWL: every unit between $Q^*$ and $\hat{Q}$, from MB up to MSC.',
            ax.c2p(40, 5) + RIGHT * 0.38)
        self.pause('2.d')

        # ---- 3.a · Positive externality, step 1: society counts the external benefit, unit by unit.
        self.remove(head, note)
        head = fixed(title('Positive Externalities'))
        benefit_bars = strips(mb, msb, EXT, 0.45, 0, 60).set_z_index(FILL_LAYER)
        note = teaching('Society counts the external benefit: MSB = MB + EXT.')
        self.play(FadeOut(social_cost), FadeOut(msc_word), FadeOut(loss), FadeOut(loss_word),
                  FadeOut(efficient_mark), FadeOut(efficient_word),
                  FadeIn(head), FadeIn(benefit_bars), FadeIn(note), *focus(1))
        self.play(FadeIn(social_benefit), FadeIn(msb_word))
        self.play(FadeOut(benefit_bars))
        self.pause('3.a')

        # ---- 3.a.quantities · Steps 2 and 3: Q* = 48; the market still trades 40.
        efficient_mark = point_mark(48, 4.4, FOCUS, radius=0.085)
        efficient_word = quantity_word(48, '$Q^*$', FOCUS)
        self.remove(note)
        note = teaching(r'$Q^* = 48$, where MSB meets MC. The market ignores EXT and trades $\hat{Q} = 40$.')
        self.play(FadeIn(efficient_mark), FadeIn(efficient_word), *focus(2))
        self.play(Indicate(market_mark[1], color=GUIDE, scale_factor=1.6), FadeIn(note), *focus(3))
        self.pause('3.a.quantities')

        # ---- 3.b · Stage 2 at the 44th unit, in the close-up's beats.
        self.play(FadeOut(note), run_time=0.3)
        stage = show_unit(positive, 44, '3.b', r'The 44th unit: the market skips it, but it is worth \$1 to society.',
                          faded=[ax, axis_words, market_word, efficient_word, market_mark, efficient_mark, mb_word, mc_word, msb_word],
                          curves=[demand, supply, social_benefit])
        self.pause('3.b')

        # ---- 3.c.inside · Jump to a unit both answers accept.
        stage = jump_unit(stage, 36, 'The 36th unit: both answers are yes, so its gap is surplus, not loss.', '3.c.inside')
        self.pause('3.c.inside')

        # ---- 3.c.outside · Jump past both quantities.
        stage = jump_unit(stage, 52, 'The 52nd unit: both answers are no. It is never traded, so nothing is lost.', '3.c.outside')
        self.pause('3.c.outside')

        # ---- 3.c · Stage 3: every forgone unit, starting from the 44th.
        loss, loss_word, note = stack_units(
            stage, r'DWL: every unit between $\hat{Q}$ and $Q^*$, from MC up to MSB.',
            ax.c2p(47, 5.9))
        self.pause('3.c')

        # ---- 4.a.start · Tax with no externality: society's curves are MB and MC, so Q* = 40.
        self.remove(head, note)
        head = fixed(title('Taxes'))
        efficient_center = point_mark(40, 4, FOCUS, radius=0.085)
        efficient_center_word = quantity_word(40, '$Q^*$', FOCUS)
        note = teaching(r'No externality: society counts MB and MC, so $Q^* = 40$.')
        self.play(FadeOut(social_benefit), FadeOut(msb_word), FadeOut(loss), FadeOut(loss_word),
                  FadeOut(efficient_mark), FadeOut(efficient_word),
                  FadeIn(head), FadeIn(note), *focus(1))
        self.play(FadeOut(market_mark), FadeOut(market_word),
                  FadeIn(efficient_center), FadeIn(efficient_center_word), *focus(2))
        self.pause('4.a.start')

        # ---- 4.a · Step 3: the $2 tax sits between the two prices at 32.
        tax_wedge = wedge_at(32, 3.6, 5.6, 'tax', -1, DR)
        tax_guides = price_guides(32, taxed['prices'], ('P_b', 'P_s'))
        tax_points = price_points(32, taxed['prices'])
        tax_word = quantity_word(32, r'$Q^{tax}$', GUIDE)
        self.remove(note)
        note = teaching('The tax market trades 32. Society wants 40.')
        self.play(FadeIn(tax_wedge), FadeIn(tax_guides), FadeIn(tax_points), FadeIn(tax_word), FadeIn(note), *focus(3))
        self.pause('4.a')

        # ---- 4.b · Stage 2 at the 36th unit. The $2 moves to the price axis, out of the unit's way.
        self.play(FadeOut(note), run_time=0.3)
        tax_axis = axis_wedge(3.6, 5.6, 'tax', tax_guides)
        stage = show_unit(taxed, 36, '4.b', r'The 36th unit: the tax stops an exchange worth \$1 to society.',
                          faded=[ax, axis_words, efficient_center_word, efficient_center, mb_word, mc_word, tax_points, tax_word, tax_guides],
                          curves=[demand, supply],
                          moving_wedge=[Transform(tax_wedge[0], tax_axis[0]), FadeOut(tax_wedge[1]), FadeOut(tax_wedge[2]),
                                        FadeIn(tax_axis[1])])
        self.pause('4.b')

        # ---- 4.c.inside · Jump to a unit both answers accept.
        stage = jump_unit(stage, 28, 'The 28th unit: both answers are yes, so its gap is surplus, not loss.', '4.c.inside')
        self.pause('4.c.inside')

        # ---- 4.c.outside · Jump past both quantities.
        stage = jump_unit(stage, 44, 'The 44th unit: both answers are no. It is never traded, so nothing is lost.', '4.c.outside')
        self.pause('4.c.outside')

        # ---- 4.c · Stage 3: every unit the tax stops, starting from the 36th.
        loss, loss_word, note = stack_units(
            stage, r'DWL: every unit between $Q^{tax}$ and $Q^*$, from MC up to MB.',
            ax.c2p(37.5, 5.85))
        self.pause('4.c')

        # ---- 5.a · Subsidy: the $2 subsidy sits between the two prices at 48.
        self.remove(head, note)
        head = fixed(title('Subsidies'))
        subsidy_wedge = wedge_at(48, 2.4, 4.4, 'subsidy', 1, DL)
        subsidy_guides = price_guides(48, subsidized['prices'], ('P_s', 'P_b'))
        subsidy_points = price_points(48, subsidized['prices'])
        subsidy_word = quantity_word(48, r'$Q^{subsidy}$', GUIDE, symbol_scale=0.45)
        note = teaching('The subsidy market trades 48. Society still wants 40.')
        self.play(FadeOut(tax_wedge[0]), FadeOut(tax_axis[1]), FadeOut(tax_guides), FadeOut(tax_points), FadeOut(tax_word),
                  FadeOut(loss), FadeOut(loss_word), FadeIn(head))
        self.play(FadeIn(subsidy_wedge), FadeIn(subsidy_guides), FadeIn(subsidy_points), FadeIn(subsidy_word),
                  FadeIn(note), *focus(3))
        self.pause('5.a')

        # ---- 5.b · Stage 2 at the 44th unit. The $2 moves to the price axis.
        self.play(FadeOut(note), run_time=0.3)
        subsidy_axis = axis_wedge(2.4, 4.4, 'subsidy', subsidy_guides)
        stage = show_unit(subsidized, 44, '5.b', r'The 44th unit: the subsidy adds an exchange that costs society \$1.',
                          faded=[ax, axis_words, efficient_center_word, efficient_center, mb_word, mc_word, subsidy_points, subsidy_word, subsidy_guides],
                          curves=[demand, supply],
                          moving_wedge=[Transform(subsidy_wedge[0], subsidy_axis[0]), FadeOut(subsidy_wedge[1]),
                                        FadeOut(subsidy_wedge[2]), FadeIn(subsidy_axis[1])])
        self.pause('5.b')

        # ---- 5.c.inside · Jump to a unit both answers accept.
        stage = jump_unit(stage, 36, 'The 36th unit: both answers are yes, so its gap is surplus, not loss.', '5.c.inside')
        self.pause('5.c.inside')

        # ---- 5.c.outside · Jump past both quantities.
        stage = jump_unit(stage, 52, 'The 52nd unit: both answers are no. It is never traded, so nothing is lost.', '5.c.outside')
        self.pause('5.c.outside')

        # ---- 5.c · Stage 3: every unit the subsidy adds, starting from the 44th.
        loss, loss_word, note = stack_units(
            stage, r'DWL: every unit between $Q^*$ and $Q^{subsidy}$, from MB up to MC.',
            ax.c2p(44, 5.0))
        self.pause('5.c')

        # ---- 6.a · All four side by side: too much in the left column, too little in the right.
        main_graph = fixed(VGroup(ax, axis_words, demand, supply, mb_word, mc_word, efficient_center,
                                  efficient_center_word, subsidy_wedge[0], subsidy_axis[1], subsidy_guides, subsidy_points,
                                  subsidy_word, loss, loss_word))
        self.remove(*main_graph)
        self.add(main_graph)
        self.remove(head, note)
        head = fixed(title('Four Markets, One Rule'))
        grid = fixed(VGroup(
            Tex(r'\textsf{Too much}', color=INK).scale(0.62).move_to([-3.7, 2.7, 0]),
            Tex(r'\textsf{Too little}', color=INK).scale(0.62).move_to([0.5, 2.7, 0]),
            Tex(r'\textsf{Externality}', color=CAPTION).scale(0.55).move_to([-6.55, 1.2, 0]),
            Tex(r'\textsf{Policy}', color=CAPTION).scale(0.55).move_to([-6.55, -1.65, 0])))
        cells = [(negative, 0, 0, 'Negative externality'), (positive, 1, 0, 'Positive externality'),
                 (subsidized, 0, 1, 'Subsidy'), (taxed, 1, 1, 'Tax')]
        for system, col, row, name in cells:
            small = style_axes([0, 60, 10], [0, 14, 2], x_length=3.5, y_length=2.25)
            small.shift(np.array([-5.45 + col * 4.2, 0.1 - row * 2.85, 0]) - small.c2p(0, 0))
            cell = VGroup(small,
                          Line(small.c2p(0, 12), small.c2p(60, 0), color=DEMAND, stroke_width=2),
                          Line(small.c2p(0, 2), small.c2p(60, 5), color=SUPPLY, stroke_width=2))
            if system is negative:
                cell.add(Line(small.c2p(0, 4), small.c2p(60, 7), color=SUPPLY, stroke_width=2))
            if system is positive:
                cell.add(Line(small.c2p(0, 14), small.c2p(60, 2), color=DEMAND, stroke_width=2))
            low, high = sorted((system['q_star'], system['q_market']))
            benefit, cost = system['benefit'], system['cost']
            cell.add(*strips(lambda q, b=benefit, c=cost: min(b(q), c(q)), lambda q, b=benefit, c=cost: max(b(q), c(q)),
                             DWL, STRIP_OPACITY, low, high, axes=small))
            if system['prices']:
                # The policy row shows its wedge, as the externality row shows its social curve.
                away = LEFT if system['q_market'] < system['q_star'] else RIGHT
                cell.add(Line(small.c2p(system['q_market'], system['prices'][1]),
                              small.c2p(system['q_market'], system['prices'][0]), color=GOV, stroke_width=4).shift(away * 0.015))
            for q, color, word in [(system['q_star'], FOCUS, '$Q^*$'), (system['q_market'], GUIDE, '$Q$')]:
                cell.add(Dot(small.c2p(q, 0), radius=0.045, color=color),
                         Tex(word, color=color).scale(0.5).next_to(small.c2p(q, 0), DOWN, buff=0.08))
            cell.add(Tex(rf'\textsf{{{name}}}', color=INK).scale(0.48).move_to(small.c2p(60, 14), aligned_edge=UR))
            grid.add(fixed(cell))
        note = teaching(r"Same shape every time: between society's curves, from $Q$ to $Q^*$.")
        self.play(FadeOut(main_graph), FadeIn(head), *[step.animate.set_color(INK) for step in steps])
        self.play(LaggedStart(*[FadeIn(cell) for cell in grid], lag_ratio=0.2), FadeIn(note), run_time=2.0)
        self.pause('6.a')

        # ---- 7.a · Corrected markets: a $2 tax on a $2 external cost brings Q to Q*.
        self.remove(head, note)
        head = fixed(title('Corrected Markets'))
        context = fixed(subtitle(head, r'A \$2 tax on a \$2 external cost.'))
        corrected = fixed(VGroup(
            wedge_at(32, 3.6, 5.6, 'tax', 1, DR),
            price_guides(32, taxed['prices'], ('P_b', 'P_s')),
            price_points(32, taxed['prices']),
            quantity_word(32, r'$Q^{tax}=Q^*$', GUIDE, symbol_scale=0.5),
            Dot(ax.c2p(32, 5.6), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER + 1)))
        note = teaching(r'The tax brings $Q$ to $Q^*$: no deadweight loss.')
        self.play(FadeOut(grid), FadeOut(card), FadeIn(head), FadeIn(context))
        self.play(FadeIn(ax), FadeIn(axis_words), FadeIn(demand), FadeIn(supply), FadeIn(social_cost),
                  FadeIn(mb_word), FadeIn(mc_word), FadeIn(msc_word))
        self.play(*[FadeIn(m) for m in corrected], FadeIn(note))
        self.pause('7.a')

        # ---- 7.b · CS, PS and GOV, one at a time; they do not overlap.
        cs_fill = strips(level(5.6), mb, DEMAND, SURPLUS_OPACITY, 0, 32).set_z_index(FILL_LAYER)
        ps_fill = strips(mc, level(3.6), SUPPLY, SURPLUS_OPACITY, 0, 32).set_z_index(FILL_LAYER)
        gov_fill = strips(level(3.6), level(5.6), GOV, SURPLUS_OPACITY, 0, 32).set_z_index(FILL_LAYER)
        cs_word = fixed(Tex('CS', color=INK).scale(0.6).move_to(ax.c2p(10.7, 7.7)).set_z_index(WORD_LAYER))
        ps_word = fixed(Tex('PS', color=INK).scale(0.55).move_to(ax.c2p(8, 3.1)).set_z_index(WORD_LAYER))
        gov_word = fixed(Tex('GOV', color=INK).scale(0.55).move_to(ax.c2p(6, 5.0)).set_z_index(WORD_LAYER))
        self.remove(note)
        self.play(FadeIn(cs_fill), FadeIn(cs_word))
        self.play(FadeIn(ps_fill), FadeIn(ps_word))
        note = teaching('Buyers keep CS, sellers keep PS, and the government collects GOV.')
        self.play(FadeIn(gov_fill), FadeIn(gov_word), FadeIn(note))
        self.pause('7.b')

        # ---- 7.c · The external cost: the tax revenue lands exactly on it.
        ext_fill = strips(mc, msc, EXT, SURPLUS_OPACITY, 0, 32)
        ext_word = fixed(Tex('EXT', color=INK).scale(0.55).move_to(ax.c2p(20, 4.3)).set_z_index(WORD_LAYER))
        gov_copy = gov_fill.copy().set_z_index(FILL_LAYER)
        self.remove(note)
        self.add(gov_copy)
        self.play(FadeOut(cs_fill), FadeOut(cs_word), FadeOut(ps_fill), FadeOut(ps_word), FadeOut(gov_word),
                  gov_fill.animate.set_fill(opacity=0.2))
        note = teaching('The tax collects exactly the external cost.')
        self.play(Transform(gov_copy, ext_fill), FadeIn(ext_word), FadeIn(note), run_time=1.8)
        self.pause('7.c')

        # ---- 7.d · Total surplus: the area between society's curves, up to Q.
        ts_fill = strips(msc, mb, TOTAL, SURPLUS_OPACITY, 0, 32).set_z_index(FILL_LAYER)
        ts_word = fixed(Tex('TS', color=INK).scale(0.6).move_to(ax.c2p(10.7, 7.2)).set_z_index(WORD_LAYER))
        ts_equation = fixed(VGroup(
            Tex('TS', color=TOTAL), Tex('$=$', color=INK), Tex('CS', color=DEMAND), Tex('$+$', color=INK),
            Tex('PS', color=SUPPLY), Tex('$+$', color=INK), Tex('GOV', color=GOV), Tex('$-$', color=INK),
            Tex('EXT', color=EXT)).arrange(RIGHT, buff=0.14).scale(0.75).move_to([5.1, 1.2, 0]))
        self.remove(note)
        self.play(FadeOut(gov_copy), FadeOut(gov_fill), FadeOut(ext_word))
        note = teaching(r"Total surplus: between society's curves, from 0 to $Q$.")
        self.play(FadeIn(ts_fill), FadeIn(ts_word), FadeIn(ts_equation), FadeIn(note))
        self.pause('7.d')

        # ---- 7.e · The mirror: a $2 subsidy on a $2 external benefit brings Q to 48.
        self.remove(context, note)
        context = fixed(subtitle(head, r'A \$2 subsidy on a \$2 external benefit.'))
        corrected_subsidy = fixed(VGroup(
            wedge_at(48, 2.4, 4.4, 'subsidy', 1, DL),
            price_guides(48, subsidized['prices'], ('P_s', 'P_b')),
            price_points(48, subsidized['prices']),
            quantity_word(48, r'$Q^{subsidy}=Q^*$', GUIDE, symbol_scale=0.45),
            Dot(ax.c2p(48, 4.4), radius=0.085, color=FOCUS).set_z_index(DOT_LAYER + 1)))
        note = teaching(r'The subsidy brings $Q$ to $Q^*$: no deadweight loss.')
        self.play(FadeOut(ts_fill), FadeOut(ts_word), FadeOut(ts_equation), *[FadeOut(m) for m in corrected],
                  FadeOut(social_cost), FadeOut(msc_word), FadeIn(context))
        self.play(FadeIn(social_benefit), FadeIn(msb_word), *[FadeIn(m) for m in corrected_subsidy], FadeIn(note))
        self.pause('7.e')

        # ---- 7.f · CS, PS and government spending overlap, so one at a time.
        cs_fill = strips(level(2.4), mb, DEMAND, SURPLUS_OPACITY, 0, 48).set_z_index(FILL_LAYER)
        ps_fill = strips(mc, level(4.4), SUPPLY, SURPLUS_OPACITY, 0, 48).set_z_index(FILL_LAYER)
        spend_fill = strips(level(2.4), level(4.4), GOV, SURPLUS_OPACITY, 0, 48).set_z_index(FILL_LAYER)
        cs_word = fixed(Tex('CS', color=INK).scale(0.6).move_to(ax.c2p(16, 5.6)).set_z_index(WORD_LAYER))
        ps_word = fixed(Tex('PS', color=INK).scale(0.55).move_to(ax.c2p(16, 3.6)).set_z_index(WORD_LAYER))
        spend_word = fixed(Tex('GOV', color=INK).scale(0.55).move_to(ax.c2p(10, 3.45)).set_z_index(WORD_LAYER))
        self.remove(note)
        note = teaching('Buyers keep CS.')
        self.play(FadeIn(cs_fill), FadeIn(cs_word), FadeIn(note))
        self.pause('7.f.cs')
        self.remove(note)
        note = teaching('Sellers keep PS.')
        self.play(FadeOut(cs_fill), FadeOut(cs_word), FadeIn(ps_fill), FadeIn(ps_word), FadeIn(note))
        self.pause('7.f.ps')
        self.remove(note)
        note = teaching(r'The government pays \$2 on every unit: GOV is spending.')
        self.play(FadeOut(ps_fill), FadeOut(ps_word), FadeIn(spend_fill), FadeIn(spend_word), FadeIn(note))
        self.pause('7.f')

        # ---- 7.g · The external benefit: the spending lands exactly on it.
        ext_fill = strips(mb, msb, EXT, SURPLUS_OPACITY, 0, 48)
        ext_word = fixed(Tex('EXT', color=INK).scale(0.55).move_to(ax.c2p(24, 8.2)).set_z_index(WORD_LAYER))
        spend_copy = spend_fill.copy().set_z_index(FILL_LAYER)
        self.remove(note)
        self.add(spend_copy)
        self.play(FadeOut(spend_word), spend_fill.animate.set_fill(opacity=0.2))
        note = teaching('The subsidy pays exactly the external benefit.')
        self.play(Transform(spend_copy, ext_fill), FadeIn(ext_word), FadeIn(note), run_time=1.8)
        self.pause('7.g')

        # ---- 7.h · Total surplus again: between society's curves, up to Q.
        ts_fill = strips(mc, msb, TOTAL, SURPLUS_OPACITY, 0, 48).set_z_index(FILL_LAYER)
        ts_word = fixed(Tex('TS', color=INK).scale(0.6).move_to(ax.c2p(16, 6.8)).set_z_index(WORD_LAYER))
        ts_equation = fixed(VGroup(
            Tex('TS', color=TOTAL), Tex('$=$', color=INK), Tex('CS', color=DEMAND), Tex('$+$', color=INK),
            Tex('PS', color=SUPPLY), Tex('$-$', color=INK), Tex('GOV', color=GOV), Tex('$+$', color=INK),
            Tex('EXT', color=EXT)).arrange(RIGHT, buff=0.14).scale(0.75).move_to([5.1, 1.2, 0]))
        self.remove(note)
        self.play(FadeOut(spend_copy), FadeOut(spend_fill), FadeOut(ext_word))
        note = teaching(r"Total surplus: between society's curves, from 0 to $Q$.")
        self.play(FadeIn(ts_fill), FadeIn(ts_word), FadeIn(ts_equation), FadeIn(note))
        self.pause('7.h')

        # ---- 8.a · Close on the five steps alone. Bottom line left for Taylor.
        self.play(*[FadeOut(m) for m in self.mobjects])
        self.clear()
        card.scale(1.35).move_to(ORIGIN)
        self.play(FadeIn(card))
        self.pause('8.a')
