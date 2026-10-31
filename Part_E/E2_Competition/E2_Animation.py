# maniml E2_Animation.py EpisodeE2
# Storyboard: E2_Notes.md. All lesson choreography stays in construct().
# Competitive firms: the firm's costs from E1 and the flat price it takes, profit as TR - TC = q(P - ATC),
# MC = MR, then the market beside the firm: entry and exit until profit is zero.
# Model of record (03_Code.py): MC = q, ATC = q/2 + 1000/q, AVC = q/2, FC = 1000, the firm's price 80.
# Market D: P = 100 - Q and S: P = Q/alpha (Q in thousands), so P* = 100/(1 + alpha); long run P = sqrt(2000) = 44.72.
# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "seaborn==0.13.2",
# ]
#
# [tool.uv]
# exclude-newer = "2026-10-02T23:47:58Z"
# ///

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *
from style import axes as style_axes

config.frame_rate = 15


class EpisodeE2(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        PRICE_SCALE, WORD_SCALE, AREA_WORD_SCALE = 0.7, 0.7, 0.72
        PI_NAME_SCALE = 0.9    # The profit box is named π, the equation's symbol, a size up from the word names.
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS = 3, 2, 0.07
        BAR_GAP = 0.08
        # Part E's firm palette (shared_E.md). Profit is the seller's gain (orange), a loss is red.
        MC_COLOR, ATC_COLOR, AVC_COLOR, FC_COLOR = SUPPLY, TOTAL, PINK, MUTED
        PROFIT_COLOR, LOSS_COLOR, AREA_FILL = SUPPLY, GUIDE, AREA_OPACITY
        # Layout. Both graphs share one price scale (0 to 120 $/unit) and one baseline. The firm graph sits
        # centred (section 1), left of a grey divider with the profit panel (section 2), or right of the
        # market graph (1.e and section 3). Both quantity axes run to 120 so readouts clear the axis words.
        ORIGIN_Y = BODY_MID - 2.15
        GRAPH_HEIGHT, FIRM_WIDTH, MARKET_WIDTH = 4.6, 4.2, 2.6
        PRICE_MAX, FIRM_Q_MAX, MARKET_Q_MAX, SUPPLY_TOP = 120, 120, 120, 100
        FIRM_CENTER_X, FIRM_ALONE_X, FIRM_BESIDE_X, MARKET_X = -2.3, -5.6, -1.6, -5.6
        DIVIDER_ALONE_X, DIVIDER_BESIDE_X = 0.45, 4.35
        # 1.b only: the market graph and the checklist centred together; the market returns to MARKET_X after.
        CHECKLIST_SHIFT, CHECKLIST_LEFT = 1.5, 0.4
        PANEL_X, EQUATION_Y, PROFIT_READOUT_Y = 3.9, 2.15, 1.65
        # The bars: slots of SLOT width on a grey floor at the graphs' baseline; BAR_SCALE is height per dollar.
        SLOT, BAR_WIDTH, BAR_SCALE, BAR_FILL = 0.95, 0.6, 0.00044, AREA_OPACITY
        FLOOR_ALONE_X, FLOOR_BESIDE_X = PANEL_X - SLOT, 4.55
        BAR_NUMBER_SCALE, BAR_NAME_SCALE = 0.6, 0.6
        # Top-level z order (the engine sorts top-level mobjects by z_index): fills, words, guides, dots.
        FILL_LAYER, WORD_LAYER, GUIDE_LAYER, DOT_LAYER = -1, 6, 10, 30
        # Taxonomy grid (E4's object): a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4

        # The model, as one-line functions (q one firm's output in units, Q market output in thousands).
        FC = 1000
        mc = lambda q: q
        atc = lambda q: q / 2 + FC / q
        avc = lambda q: q / 2
        FIRM_P, LONG_RUN_P = 80, np.sqrt(2 * FC)                 # 80, and 44.72 where MC = ATC
        ATC_START = (2 * PRICE_MAX - np.sqrt(4 * PRICE_MAX ** 2 - 8 * FC)) / 2   # ATC = 120 at q = 8.8
        market_q = lambda p: 100 - p                              # D: P = 100 - Q
        # S runs through the origin and the equilibrium (100 - P, P), cut at Q = 100 or P = SUPPLY_TOP.
        supply_end = lambda p: (min(MARKET_Q_MAX, SUPPLY_TOP * (100 - p) / p),
                                min(MARKET_Q_MAX, SUPPLY_TOP * (100 - p) / p) * p / (100 - p))

        teaching = lambda text: (Tex(text, color=DEFINITION).scale(DEFINITION_SCALE)
                                 .set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM))

        # ---- 0.a · The shared bumper with E2's header line as the thesis.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 2)
        thesis = Tex(r'\textit{The revenue side}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · The market-structures taxonomy (E4's object), the many-sellers homogeneous cell boxed.
        head = title('Perfect Competition')
        grid_left = TAXONOMY_X - (LABEL_W + 2 * CELL_W) / 2
        grid_right = grid_left + LABEL_W + 2 * CELL_W
        grid_top = BODY_MID + (HEADER_H + 3 * CELL_H) / 2
        column_x = [grid_left + LABEL_W + CELL_W * (i + 0.5) for i in range(2)]
        row_y = [grid_top - HEADER_H - CELL_H * (i + 0.5) for i in range(3)]
        # D1's Table look: rules between rows and columns only, no outer frame. The one-seller row has no
        # column rule: differentiation does not matter with one seller.
        taxonomy_rules = VGroup(
            *[Line([grid_left, grid_top - HEADER_H - CELL_H * i, 0], [grid_right, grid_top - HEADER_H - CELL_H * i, 0],
                   color=MUTED, stroke_width=2) for i in range(3)],
            Line([grid_left + LABEL_W, grid_top, 0], [grid_left + LABEL_W, grid_top - HEADER_H - 3 * CELL_H, 0],
                 color=MUTED, stroke_width=2),
            Line([grid_left + LABEL_W + CELL_W, grid_top, 0], [grid_left + LABEL_W + CELL_W, grid_top - HEADER_H - 2 * CELL_H, 0],
                 color=MUTED, stroke_width=2))
        column_words = VGroup(Tex('Homogeneous', color=GUIDE), Tex('Differentiated', color=GUIDE)).scale(0.75)
        for word, x in zip(column_words, column_x):
            word.move_to([x, grid_top - HEADER_H / 2, 0])
        column_words[1].align_to(column_words[0], UP)
        row_words = VGroup(Tex('Many Sellers', color=GUIDE), Tex('Few Sellers', color=GUIDE),
                           Tex('One Seller', color=GUIDE)).scale(0.75)
        for word, y in zip(row_words, row_y):
            word.move_to([grid_left + LABEL_W / 2, y, 0])
        perfect = Tex(r'Perfect\\Competition').scale(0.75).move_to([column_x[0], row_y[0], 0])
        monopolistic = Tex(r'Monopolistic\\Competition').scale(0.75).move_to([column_x[1], row_y[0], 0])
        oligopoly = Tex('Oligopoly').scale(0.75).move_to([column_x[0], row_y[1], 0])
        monopoly = Tex('Monopoly').scale(0.75).move_to([(column_x[0] + column_x[1]) / 2, row_y[2], 0])
        taxonomy = VGroup(taxonomy_rules, column_words, row_words, perfect, monopolistic, oligopoly, monopoly)
        box = SurroundingRectangle(perfect, buff=0.22, color=NASH)
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a')

        # ---- 1.b.buyers · The checklist in grey beside a small market graph; many buyers lights with demand.
        market_ax = style_axes([0, MARKET_Q_MAX, 10], [0, PRICE_MAX, 20], x_length=MARKET_WIDTH, y_length=GRAPH_HEIGHT)
        market_ax.shift(np.array([MARKET_X, ORIGIN_Y, 0]) - market_ax.c2p(0, 0))
        market_price_word = Tex('P', color=INK).scale(0.8).next_to(market_ax.c2p(0, PRICE_MAX), LEFT, buff=0.23)
        # Unit captions sit under P (C4), right-aligned to it so they clear the axis and the supply curve's top end.
        market_words = VGroup(
            market_price_word,
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(market_price_word, DOWN, buff=0.08)
            .align_to(market_price_word, RIGHT),
            Tex('Q', color=INK).scale(0.8).next_to(market_ax.c2p(MARKET_Q_MAX, 0), DOWN, buff=0.23),
            Tex(r'\textsf{1,000 units}', color=CAPTION).scale(0.55).next_to(market_ax.c2p(MARKET_Q_MAX, 0), DOWN, buff=0.73))
        market_demand = Line(market_ax.c2p(0, 100), market_ax.c2p(100, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        demand_word = Tex('D', color=INK).scale(WORD_SCALE).next_to(market_ax.c2p(100, 0), UR, buff=0.12)
        market_supply = Line(market_ax.c2p(0, 0), market_ax.c2p(*supply_end(FIRM_P)), color=SUPPLY, stroke_width=CURVE_WIDTH)
        supply_word = Tex('S', color=INK).scale(WORD_SCALE).next_to(market_ax.c2p(*supply_end(FIRM_P)), RIGHT, buff=0.12)
        checklist = VGroup(*[Tex(f'{n}. {item}', color=CAPTION) for n, item in enumerate(
            ['Many buyers', 'Many identical sellers', 'A homogeneous good', 'No externalities', 'Low barriers to entry'],
            start=1)]).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        checklist.move_to([0, BODY_MID, 0]).align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        market_picture = VGroup(market_ax, market_words, market_demand, demand_word, market_supply, supply_word)
        market_picture.shift(RIGHT * CHECKLIST_SHIFT)
        self.play(FadeOut(taxonomy), FadeOut(box), run_time=0.6)
        self.play(FadeIn(market_ax), FadeIn(market_words), FadeIn(checklist))
        self.play(checklist[0].animate.set_color(INK), FadeIn(market_demand), FadeIn(demand_word))
        self.pause('1.b.buyers')

        # ---- 1.b.sellers · Many identical sellers lights with supply.
        self.play(checklist[1].animate.set_color(INK), FadeIn(market_supply), FadeIn(supply_word))
        self.pause('1.b.sellers')

        # ---- 1.b.good · A homogeneous good.
        self.play(checklist[2].animate.set_color(INK))
        self.pause('1.b.good')

        # ---- 1.b.externalities · No externalities.
        self.play(checklist[3].animate.set_color(INK))
        self.pause('1.b.externalities')

        # ---- 1.b · Low barriers to entry.
        self.play(checklist[4].animate.set_color(INK))
        self.pause('1.b')

        # ---- 1.c · The firm's costs from E1, centred: MC, ATC and the minimum of ATC in yellow.
        self.play(FadeOut(market_picture), FadeOut(checklist), run_time=0.6)
        market_picture.shift(LEFT * CHECKLIST_SHIFT)
        firm_ax = style_axes([0, FIRM_Q_MAX, 10], [0, PRICE_MAX, 20], x_length=FIRM_WIDTH, y_length=GRAPH_HEIGHT)
        firm_ax.shift(np.array([FIRM_CENTER_X, ORIGIN_Y, 0]) - firm_ax.c2p(0, 0))
        firm_price_word = Tex('P', color=INK).scale(0.8).next_to(firm_ax.c2p(0, PRICE_MAX), LEFT, buff=0.23)
        firm_words = VGroup(
            firm_price_word,
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(firm_price_word, DOWN, buff=0.08)
            .align_to(firm_price_word, RIGHT),
            Tex('q', color=INK).scale(0.8).next_to(firm_ax.c2p(FIRM_Q_MAX, 0), DOWN, buff=0.23),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(firm_ax.c2p(FIRM_Q_MAX, 0), DOWN, buff=0.73))
        mc_line = Line(firm_ax.c2p(0, 0), firm_ax.c2p(FIRM_Q_MAX, mc(FIRM_Q_MAX)), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        atc_curve = polyline([firm_ax.c2p(q, atc(q)) for q in np.geomspace(ATC_START, FIRM_Q_MAX, 240)],
                             ATC_COLOR, CURVE_WIDTH)
        cost_words = VGroup(
            Tex('MC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(FIRM_Q_MAX, mc(FIRM_Q_MAX)), RIGHT, buff=0.15),
            # ATC is named at its upper left, where nothing else ever sits; its right end shares heights with P = MR.
            Tex('ATC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(ATC_START, PRICE_MAX - 4), RIGHT, buff=0.15))
        lowest_atc = Dot(firm_ax.c2p(LONG_RUN_P, LONG_RUN_P), radius=0.085, color=FOCUS)
        firm = VGroup(firm_ax, firm_words, mc_line, atc_curve, cost_words, lowest_atc)
        context = subtitle(head, 'One firm among many.')
        self.play(FadeIn(firm), FadeIn(context))
        self.pause('1.c')

        # ---- 1.d · The demand the firm faces: flat at the market price, which is also its marginal revenue.
        price = ValueTracker(FIRM_P)
        quantity = ValueTracker(60)
        price_line = Line(firm_ax.c2p(0, FIRM_P), firm_ax.c2p(FIRM_Q_MAX, FIRM_P), color=DEMAND, stroke_width=CURVE_WIDTH)
        price_line.add_updater(lambda m: m.put_start_and_end_on(
            firm_ax.c2p(0, price.get_value()), firm_ax.c2p(FIRM_Q_MAX, price.get_value())))
        price_word = Tex('P = MR', color=INK).scale(WORD_SCALE)
        price_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        price_number = DecimalNumber(FIRM_P, num_decimal_places=2, color=DEMAND).scale(PRICE_SCALE)
        price_number.add_updater(lambda m: m.set_value(price.get_value())
                                 .next_to(firm_ax.c2p(0, price.get_value()), LEFT, buff=0.2))
        for m in (price_line, price_word, price_number):
            m.update()
        note = teaching('Competitive firms are what we call price takers.')
        self.play(FadeIn(price_line), FadeIn(price_word), FadeIn(price_number))
        self.play(FadeIn(note))
        self.pause('1.d')

        # ---- 1.e.out · Zoom out: the market returns on the left; a tiny box at its crossing grows into a frame
        # around the firm's graph, so the firm's whole graph is that box.
        zoom_box = Square(side_length=0.24, color=FOCUS, stroke_width=2).move_to(market_ax.c2p(market_q(FIRM_P), FIRM_P))
        zoom_frame = Rectangle(width=FIRM_WIDTH, height=GRAPH_HEIGHT, color=FOCUS, stroke_width=2)
        zoom_frame.move_to([FIRM_BESIDE_X + FIRM_WIDTH / 2, ORIGIN_Y + GRAPH_HEIGHT / 2, 0])
        self.remove(note)
        note = teaching('Zoomed in on one firm, the demand curve looks flat.')
        self.play(firm.animate.shift(RIGHT * (FIRM_BESIDE_X - FIRM_CENTER_X)), FadeIn(market_picture), run_time=1.6)
        self.play(Create(zoom_box))
        self.play(TransformFromCopy(zoom_box, zoom_frame), FadeIn(note), run_time=1.4)
        self.pause('1.e.out')

        # ---- 1.e · Wiggle the firm's quantity: the price it gets does not move.
        firm_dot = Dot(firm_ax.c2p(60, FIRM_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        firm_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), price.get_value())))
        # The quantity guide reaches the price line here; later the top of the profit box, then the MC dot too.
        guide_top = lambda m: max(price.get_value(), atc(quantity.get_value()) if m.with_atc else 0,
                                  mc(quantity.get_value()) if m.with_mc else 0)
        q_drop = DashedLine(firm_ax.c2p(60, 0), firm_ax.c2p(60, FIRM_P), color=GUIDE, stroke_width=GUIDE_WIDTH,
                            z_index=GUIDE_LAYER)
        q_drop.with_atc, q_drop.with_mc = False, False
        q_drop.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), 0), firm_ax.c2p(quantity.get_value(), guide_top(m)) + UP * 1e-6,
            color=GUIDE, stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER).set_style(**m.get_style())))
        q_number = DecimalNumber(60, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        q_number.add_updater(lambda m: m.set_value(float(np.round(quantity.get_value())))
                             .move_to(firm_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        q_symbol = Tex('$q$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        q_symbol.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        for m in (firm_dot, q_drop, q_number, q_symbol):
            m.update()
        self.remove(note)
        note = teaching('This firm changing quantity has no real effect on the price.')
        self.play(FadeIn(firm_dot), FadeIn(q_drop), FadeIn(q_number), FadeIn(q_symbol), FadeIn(note))
        # One eased wiggle: 60 up to 90, down to 30, back to 60.
        self.play(quantity.animate.set_value(90), rate_func=lambda t: np.sin(2 * np.pi * smooth(t)), run_time=3.2)
        quantity.set_value(60)
        self.pause('1.e')

        # ---- 2.a.word · Profit: the firm returns left of a grey divider; the word Profit on the right.
        for m in (firm_dot, q_drop, q_number, q_symbol):
            m.update()
        self.remove(head, context, note)
        head = title('Profit')
        divider = Line([DIVIDER_ALONE_X, -3.0, 0], [DIVIDER_ALONE_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        equation = MathTex(r'{{\pi}} = {{\mathrm{TR}}} - {{\mathrm{TC}}} = q({{P}} - {{\mathrm{ATC}}})').scale(0.85)
        equation.get_part_by_tex(r'\pi').set_color(PROFIT_COLOR)
        equation.get_part_by_tex(r'\mathrm{TR}').set_color(DEMAND)
        equation.get_part_by_tex(r'\mathrm{TC}').set_color(ATC_COLOR)
        equation.get_part_by_tex('P').set_color(DEMAND)
        equation.get_part_by_tex(r'\mathrm{ATC}').set_color(ATC_COLOR)
        equation.move_to([PANEL_X, EQUATION_Y, 0])
        # Glyphs: pi | = TR - TC (six) | = q(P - ATC) (nine), so each part fades in on its own beat.
        equation_pi, equation_first, equation_second = equation[0], equation[1:7], equation[7:]
        profit_word = Tex('Profit', color=INK).scale(0.9).move_to([PANEL_X, EQUATION_Y, 0])
        self.play(FadeOut(market_picture), FadeOut(zoom_box), FadeOut(zoom_frame), FadeOut(firm_dot),
                  FadeOut(q_drop), FadeOut(q_number), FadeOut(q_symbol),
                  firm.animate.shift(RIGHT * (FIRM_ALONE_X - FIRM_BESIDE_X)), run_time=1.6)
        self.play(FadeIn(head), FadeIn(divider), FadeIn(profit_word))
        self.pause('2.a.word')

        # ---- 2.a · Profit becomes pi: profit = TR - TC.
        note = teaching('Profit is everything left over after we’ve paid our costs.')
        self.play(ReplacementTransform(profit_word, equation_pi), run_time=1.2)
        self.play(FadeIn(equation_first), FadeIn(note))
        self.pause('2.a')

        # ---- 2.b.revenue · At q = 40: the quantity guide, then total revenue as 40 one-unit strips up to P.
        START_Q = 40
        quantity.set_value(START_Q)
        q_drop.with_atc = True
        for m in (q_drop, q_number, q_symbol):
            m.update()
        revenue_strips = VGroup(*[Polygon(
            firm_ax.c2p(u + BAR_GAP / 2, 0), firm_ax.c2p(u + 1 - BAR_GAP / 2, 0),
            firm_ax.c2p(u + 1 - BAR_GAP / 2, FIRM_P), firm_ax.c2p(u + BAR_GAP / 2, FIRM_P),
            stroke_width=0, fill_color=DEMAND, fill_opacity=AREA_FILL).set_z_index(FILL_LAYER) for u in range(START_Q)])
        revenue_strips.set_z_index(FILL_LAYER)
        # Area names keep clear of the curves: each goes to the spot nearest its area's centre that keeps
        # WORD_CLEAR from the area's edges, MC and ATC (staying on its area's side of ATC). Every name finds such a
        # spot whenever it is visible; the score below only breaks ties while a name is fading on a thin box.
        WORD_CLEAR = 0.05
        X_UNIT, Y_UNIT = FIRM_WIDTH / FIRM_Q_MAX, GRAPH_HEIGHT / PRICE_MAX

        def area_word_spot(m, right, low, high, prefer):
            w, h = m.half_size[0] / X_UNIT, m.half_size[1] / Y_UNIT
            X = np.linspace(0, max(right, 1e-3), 101)[:, None]
            Y = np.linspace(low, max(high, low + 1e-3), 41)[None, :]
            reach = w + WORD_CLEAR / X_UNIT
            xs = np.clip(X[..., None] + np.linspace(-reach, reach, 31), 0.5, None)
            bottom, top = (Y - h)[..., None], (Y + h)[..., None]
            # The area's edges count four times as much as the curves: a name may graze a curve, not leave its area.
            clear = 4 * np.minimum(np.minimum((X - w) * X_UNIT, (right - X - w) * X_UNIT),
                                   np.minimum((Y - h - low) * Y_UNIT, (high - Y - h) * Y_UNIT))
            atc_gap = bottom - atc(xs) if m.above_atc else atc(xs) - top
            clear = np.minimum(clear, np.min(atc_gap, axis=2) * Y_UNIT)
            mc_gap = np.min(np.maximum(bottom - mc(xs), mc(xs) - top), axis=2) * Y_UNIT
            mc_crosses = (mc(xs) > top).any(axis=2) & (mc(xs) < bottom).any(axis=2)
            clear = np.minimum(clear, np.where(mc_crosses, np.minimum(mc_gap, 0), mc_gap))
            score = np.minimum(clear, WORD_CLEAR) - 0.05 * np.hypot((X - prefer[0]) * X_UNIT, (Y - prefer[1]) * Y_UNIT)
            i, j = np.unravel_index(score.argmax(), score.shape)
            return firm_ax.c2p(X[i, 0], Y[0, j])

        revenue_word = Tex('TR', color=INK).scale(AREA_WORD_SCALE).set_z_index(WORD_LAYER)
        revenue_word.half_size, revenue_word.above_atc = (revenue_word.width / 2, revenue_word.height / 2), True
        revenue_word.move_to(area_word_spot(revenue_word, START_Q, atc(START_Q), FIRM_P,
                                            (START_Q / 2, (FIRM_P + atc(START_Q)) / 2)))
        self.remove(note)
        self.play(FadeIn(q_drop), FadeIn(q_number), FadeIn(q_symbol))
        self.play(LaggedStart(*[FadeIn(strip) for strip in revenue_strips], lag_ratio=0.1), run_time=2)
        self.remove(*revenue_strips)
        self.add(revenue_strips)
        self.play(FadeIn(revenue_word))
        self.pause('2.b.revenue')

        # ---- 2.b.cost · Average total cost at q = 40, then total cost as 40 strips up to ATC.
        atc_guide = DashedLine(firm_ax.c2p(0, atc(START_Q)), firm_ax.c2p(START_Q, atc(START_Q)), color=ATC_COLOR,
                               stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER)
        atc_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(0, atc(quantity.get_value())), firm_ax.c2p(quantity.get_value(), atc(quantity.get_value())),
            color=ATC_COLOR, stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER).set_style(**m.get_style())))
        atc_number = DecimalNumber(atc(START_Q), num_decimal_places=2, color=ATC_COLOR).scale(PRICE_SCALE)
        atc_number.add_updater(lambda m: m.set_value(atc(quantity.get_value()))
                               .next_to(firm_ax.c2p(0, atc(quantity.get_value())), LEFT, buff=0.2))
        atc_number.update()
        cost_strips = VGroup(*[Polygon(
            firm_ax.c2p(u + BAR_GAP / 2, 0), firm_ax.c2p(u + 1 - BAR_GAP / 2, 0),
            firm_ax.c2p(u + 1 - BAR_GAP / 2, atc(START_Q)), firm_ax.c2p(u + BAR_GAP / 2, atc(START_Q)),
            stroke_width=0, fill_color=ATC_COLOR, fill_opacity=AREA_FILL).set_z_index(FILL_LAYER) for u in range(START_Q)])
        cost_strips.set_z_index(FILL_LAYER)
        # TC goes above MC, which crosses its area from the lower-left corner.
        cost_word = Tex('TC', color=INK).scale(AREA_WORD_SCALE).set_z_index(WORD_LAYER)
        cost_word.half_size, cost_word.above_atc = (cost_word.width / 2, cost_word.height / 2), False
        cost_word.move_to(area_word_spot(cost_word, START_Q, 0, atc(START_Q), (START_Q / 3, atc(START_Q) * 2 / 3)))
        note = teaching('Profit is the difference between these two areas.')
        self.play(Create(atc_guide), FadeIn(atc_number))
        self.play(LaggedStart(*[FadeIn(strip) for strip in cost_strips], lag_ratio=0.1), run_time=2)
        self.remove(*cost_strips)
        self.add(cost_strips)
        self.play(FadeIn(cost_word), FadeIn(note))
        self.pause('2.b.cost')

        # ---- 2.b · The two areas pour into two bars right of the graph, one slice per unit.
        bar_floor = Line([FLOOR_ALONE_X, ORIGIN_Y, 0], [FLOOR_ALONE_X + 2 * SLOT, ORIGIN_Y, 0], color=MUTED, stroke_width=2)
        bar_x = lambda i: bar_floor.get_left()[0] + SLOT * (i + 0.5)
        bar_y = lambda dollars: bar_floor.get_y() + dollars * BAR_SCALE
        revenue = lambda: price.get_value() * quantity.get_value()
        total_cost = lambda: quantity.get_value() ** 2 / 2 + FC
        revenue_slices = VGroup(*[Rectangle(width=BAR_WIDTH, height=FIRM_P * BAR_SCALE, stroke_width=0, fill_color=DEMAND,
                                            fill_opacity=AREA_FILL).move_to([bar_x(0), bar_y((u + 0.5) * FIRM_P), 0])
                                  for u in range(START_Q)])
        cost_slices = VGroup(*[Rectangle(width=BAR_WIDTH, height=atc(START_Q) * BAR_SCALE, stroke_width=0,
                                         fill_color=ATC_COLOR, fill_opacity=AREA_FILL)
                               .move_to([bar_x(1), bar_y((u + 0.5) * atc(START_Q)), 0]) for u in range(START_Q)])

        # The live bars: each bar's own color up to the smaller total; the gap above is profit (on TR) or loss (on TC).
        def set_rect(m, x, low, high, opacity):
            top = max(high, low + 1e-4)
            m.set_points_as_corners([[x - BAR_WIDTH / 2, low, 0], [x + BAR_WIDTH / 2, low, 0],
                                     [x + BAR_WIDTH / 2, top, 0], [x - BAR_WIDTH / 2, top, 0], [x - BAR_WIDTH / 2, low, 0]])
            m.set_fill(opacity=opacity if high - low > 1e-4 else 0)
            return m

        revenue_base, revenue_gain = (Polygon(ORIGIN, RIGHT, UP, stroke_width=0, fill_color=DEMAND, fill_opacity=BAR_FILL)
                                      for _ in range(2))
        cost_base = Polygon(ORIGIN, RIGHT, UP, stroke_width=0, fill_color=ATC_COLOR, fill_opacity=BAR_FILL)
        cost_loss = Polygon(ORIGIN, RIGHT, UP, stroke_width=0, fill_color=LOSS_COLOR, fill_opacity=BAR_FILL)
        revenue_gain.shown = True
        revenue_base.add_updater(lambda m: set_rect(m, bar_x(0), bar_y(0), bar_y(min(revenue(), total_cost())), BAR_FILL))
        revenue_gain.add_updater(lambda m: set_rect(m, bar_x(0), bar_y(total_cost()), bar_y(revenue()),
                                                    BAR_FILL if m.shown else 0))
        cost_base.add_updater(lambda m: set_rect(m, bar_x(1), bar_y(0), bar_y(min(revenue(), total_cost())), BAR_FILL))
        cost_loss.add_updater(lambda m: set_rect(m, bar_x(1), bar_y(revenue()), bar_y(total_cost()), BAR_FILL))
        revenue_edge = Line(LEFT * BAR_WIDTH / 2, RIGHT * BAR_WIDTH / 2, color=DEMAND, stroke_width=CURVE_WIDTH)
        revenue_edge.add_updater(lambda m: m.move_to([bar_x(0), bar_y(revenue()), 0]))
        cost_edge = Line(LEFT * BAR_WIDTH / 2, RIGHT * BAR_WIDTH / 2, color=ATC_COLOR, stroke_width=CURVE_WIDTH)
        cost_edge.add_updater(lambda m: m.move_to([bar_x(1), bar_y(total_cost()), 0]))
        revenue_value = DecimalNumber(FIRM_P * START_Q, num_decimal_places=0, color=DEMAND).scale(BAR_NUMBER_SCALE)
        revenue_value.add_updater(lambda m: m.set_value(round(revenue(), 4))
                                  .move_to([bar_x(0), bar_floor.get_y() - QUANTITY_NUMBER_OFFSET, 0]))
        cost_value = DecimalNumber(total_cost(), num_decimal_places=0, color=ATC_COLOR).scale(BAR_NUMBER_SCALE)
        cost_value.add_updater(lambda m: m.set_value(round(total_cost(), 4))
                               .move_to([bar_x(1), bar_floor.get_y() - QUANTITY_NUMBER_OFFSET, 0]))
        revenue_name = Tex('TR', color=INK).scale(BAR_NAME_SCALE)
        revenue_name.add_updater(lambda m: m.move_to([bar_x(0), bar_floor.get_y() - QUANTITY_LABEL_OFFSET, 0]))
        cost_name = Tex('TC', color=INK).scale(BAR_NAME_SCALE)
        cost_name.add_updater(lambda m: m.move_to([bar_x(1), bar_floor.get_y() - QUANTITY_LABEL_OFFSET, 0]))
        bars = [revenue_base, revenue_gain, cost_base, cost_loss]
        bar_marks = [revenue_edge, cost_edge, revenue_value, cost_value]
        for m in bars + bar_marks + [revenue_name, cost_name]:
            m.update()
        self.play(FadeIn(bar_floor), Transform(revenue_strips, revenue_slices), Transform(cost_strips, cost_slices),
                  ReplacementTransform(revenue_word, revenue_name), ReplacementTransform(cost_word, cost_name),
                  run_time=1.8)
        self.remove(revenue_strips, cost_strips)
        self.add(*bars)
        self.play(FadeIn(revenue_edge), FadeIn(cost_edge), FadeIn(revenue_value), FadeIn(cost_value))
        self.pause('2.b')

        # ---- 2.c.area · The difference on the graph: profit strips between ATC and P, one per unit.
        def update_profit_strips(strips):
            q, p = quantity.get_value(), price.get_value()
            low, high = min(p, atc(q)), max(p, atc(q))
            for u, strip in enumerate(strips):
                left, right = u + BAR_GAP / 2, min(u + 1 - BAR_GAP / 2, q)
                if right <= left or high - low < 1e-6:
                    strip.set_fill(opacity=0)
                    continue
                strip.set_points_as_corners([firm_ax.c2p(left, low), firm_ax.c2p(right, low), firm_ax.c2p(right, high),
                                             firm_ax.c2p(left, high), firm_ax.c2p(left, low)])
                strip.set_fill(PROFIT_COLOR if p >= atc(q) else LOSS_COLOR, opacity=AREA_FILL)

        profit_strips = VGroup(*[Polygon(ORIGIN, RIGHT, UP, stroke_width=0, fill_color=PROFIT_COLOR, fill_opacity=0)
                                 .set_z_index(FILL_LAYER) for u in range(FIRM_Q_MAX)]).set_z_index(FILL_LAYER)
        update_profit_strips(profit_strips)

        # π and Loss name the box when it is tall enough, clear of the curves; each fades in only on its own
        # side of ATC (π above it, Loss below it). The word Profit could not fit the q = 40 box clear of ATC.
        def place_area_word(m):
            q, p = quantity.get_value(), price.get_value()
            low, high = min(p, atc(q)), max(p, atc(q))
            m.move_to(area_word_spot(m, q, low, high, (q / 2, (low + high) / 2)))
            m.set_opacity(np.clip(((high - low) * Y_UNIT - 0.28) / 0.14, 0, 1) if (p >= atc(q)) == m.for_profit else 0)

        profit_area_word = MathTex(r'\pi', color=INK).scale(PI_NAME_SCALE).set_z_index(WORD_LAYER)
        loss_area_word = Tex('Loss', color=INK).scale(AREA_WORD_SCALE).set_z_index(WORD_LAYER)
        profit_area_word.for_profit, loss_area_word.for_profit = True, False
        for m in (profit_area_word, loss_area_word):
            m.half_size, m.above_atc = (m.width / 2, m.height / 2), m.for_profit
        place_area_word(profit_area_word)
        self.remove(note)
        note = teaching('So we usually just look at the difference on the graph.')
        self.play(LaggedStart(*[FadeIn(strip) for strip in profit_strips[:START_Q]], lag_ratio=0.1), FadeIn(note), run_time=2)
        self.remove(*profit_strips)
        self.add(profit_strips)
        self.play(FadeIn(profit_area_word))
        self.pause('2.c.area')

        # ---- 2.c.side · The difference area moves to the side: it is the part of the TR bar above the TC bar.
        profit_strips.add_updater(update_profit_strips)
        profit_area_word.add_updater(place_area_word)
        loss_area_word.add_updater(place_area_word)
        loss_area_word.update()
        self.add(loss_area_word)
        profit_copy = VGroup(*[strip.copy() for strip in profit_strips[:START_Q]])
        profit_copy.clear_updaters()
        profit_slices = VGroup(*[Rectangle(width=BAR_WIDTH, height=(FIRM_P - atc(START_Q)) * BAR_SCALE, stroke_width=0,
                                           fill_color=PROFIT_COLOR, fill_opacity=AREA_FILL)
                                 .move_to([bar_x(0), bar_y(total_cost() + (u + 0.5) * (FIRM_P - atc(START_Q))), 0])
                                 for u in range(START_Q)])
        revenue_gain.shown = False
        revenue_gain.set_fill(PROFIT_COLOR)
        profit_readout = VGroup(Tex(r'$\pi=$', color=PROFIT_COLOR),
                                DecimalNumber(0, num_decimal_places=0, color=PROFIT_COLOR)).scale(PRICE_SCALE)
        profit_readout.add_updater(lambda m: (
            m[1].set_value(round(revenue() - total_cost(), 4)),
            m.set_color(PROFIT_COLOR if revenue() >= total_cost() - 1e-6 else LOSS_COLOR),
            m.arrange(RIGHT, buff=0.12),
            m.move_to([bar_floor.get_left()[0] + SLOT, PROFIT_READOUT_Y, 0])))
        profit_readout.update()
        self.add(profit_copy)
        self.play(Transform(profit_copy, profit_slices), run_time=1.6)
        revenue_gain.shown = True
        self.remove(profit_copy)
        self.play(FadeIn(profit_readout))
        self.pause('2.c.side')

        # ---- 2.c · The same profit, read off the box: q(P - ATC).
        self.remove(note)
        self.play(FadeIn(equation_second))
        self.pause('2.c')

        # ---- 2.d.question · Start small: the 40th unit's marginal cost on MC, below the price.
        mc_dot = Dot(firm_ax.c2p(START_Q, mc(START_Q)), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        mc_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), mc(quantity.get_value()))))
        q_drop.with_mc = True
        note = teaching('Should we increase our quantity by 10?')
        self.play(FadeIn(mc_dot), FadeIn(note))
        self.pause('2.d.question')

        # ---- 2.d.ten · Ten more units: the box, the bars and every number roll together.
        self.play(quantity.animate.set_value(50), run_time=1.6, rate_func=smooth)
        self.pause('2.d.ten')

        # ---- 2.d.past · Keep going: profit rises until MR = MC at 80, then falls by 100.
        self.remove(note)
        note = teaching('Profit will continue to rise until MR = MC, then it will fall.')
        self.play(FadeIn(note))
        self.play(quantity.animate.set_value(100), run_time=3.2, rate_func=smooth)
        self.pause('2.d.past')

        # ---- 2.d · Back down to 80.
        self.play(quantity.animate.set_value(80), run_time=2, rate_func=smooth)
        self.pause('2.d')

        # ---- 2.e · MC = MR: the chosen quantity becomes q*.
        q_star = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        q_star.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        q_star.update()
        self.remove(note, q_symbol)
        note = teaching('How much should the firm choose to produce? At MC = MR!')
        self.play(FadeIn(q_star), Indicate(mc_dot, color=FOCUS, scale_factor=1.6), FadeIn(note))
        self.pause('2.e')

        # ---- 2.f.low · Move the price: q* rides MC, and the box, bars and numbers follow.
        self.remove(note)
        note = teaching('This is an example of marginal thinking.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(60), quantity.animate.set_value(60), run_time=2.4, rate_func=smooth)
        self.pause('2.f.low')

        # ---- 2.f.high · A higher price.
        self.play(price.animate.set_value(90), quantity.animate.set_value(90), run_time=3, rate_func=smooth)
        self.pause('2.f.high')

        # ---- 2.f · Back to the market's 80.
        self.play(price.animate.set_value(FIRM_P), quantity.animate.set_value(FIRM_P), run_time=1.8, rate_func=smooth)
        self.pause('2.f')

        # ---- 3.a · The market: the firm and its bars move right, and its flat demand becomes the market's on the left.
        for m in (atc_guide, atc_number):
            m.update()
            m.clear_updaters()
        self.remove(head, note)
        head = title('The Market')
        note = teaching('So we need to zoom back out to see the whole market.')
        self.play(FadeOut(equation_pi), FadeOut(equation_first), FadeOut(equation_second), FadeOut(atc_guide),
                  FadeOut(atc_number), run_time=0.5)
        self.play(firm.animate.shift(RIGHT * (FIRM_BESIDE_X - FIRM_ALONE_X)),
                  bar_floor.animate.shift(RIGHT * (FLOOR_BESIDE_X - FLOOR_ALONE_X)),
                  divider.animate.set_x(DIVIDER_BESIDE_X), FadeIn(head), FadeIn(market_ax), FadeIn(market_words),
                  run_time=1.6)
        flat_copy = price_line.copy().clear_updaters()
        self.play(ReplacementTransform(flat_copy, market_demand), FadeIn(demand_word), run_time=1.4)
        self.play(FadeIn(market_supply), FadeIn(supply_word), FadeIn(note))
        self.pause('3.a')

        # ---- 3.b.demand · Wiggle demand: many buyers' willingness to pay.
        self.remove(note)
        note = teaching('Demand: the willingness to pay of many people, all added together.')
        self.play(FadeIn(note))
        self.play(Indicate(market_demand, color=FOCUS), run_time=0.5)
        self.pause('3.b.demand')

        # ---- 3.b.supply · Wiggle supply: many sellers' willingness to sell.
        self.remove(note)
        note = teaching('Supply: the willingness to sell of many sellers, all added together.')
        self.play(FadeIn(note))
        self.play(Indicate(market_supply, color=FOCUS), run_time=0.5)
        self.pause('3.b.supply')

        # ---- 3.b.equilibrium · Where they cross: P* = 80 and Q* = 20 (thousand), on the market's axes.
        market_dot = Dot(market_ax.c2p(market_q(FIRM_P), FIRM_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        market_dot.add_updater(lambda m: m.move_to(market_ax.c2p(market_q(price.get_value()), price.get_value())))
        market_across = DashedLine(market_ax.c2p(0, FIRM_P), market_ax.c2p(market_q(FIRM_P), FIRM_P), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER)
        market_across.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(0, price.get_value()), market_ax.c2p(market_q(price.get_value()), price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER).set_style(**m.get_style())))
        market_drop = DashedLine(market_ax.c2p(market_q(FIRM_P), 0), market_ax.c2p(market_q(FIRM_P), FIRM_P), color=GUIDE,
                                 stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER)
        market_drop.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(market_q(price.get_value()), 0), market_ax.c2p(market_q(price.get_value()), price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER).set_style(**m.get_style())))
        market_price = VGroup(Tex('$P^*=$', color=GUIDE), DecimalNumber(FIRM_P, num_decimal_places=2, color=GUIDE))
        market_price.scale(PRICE_SCALE).arrange(RIGHT, buff=0.06)
        market_price.add_updater(lambda m: (m[1].set_value(price.get_value()), m.arrange(RIGHT, buff=0.06),
                                            m.next_to(market_ax.c2p(0, price.get_value()), LEFT, buff=0.2)))
        market_quantity = VGroup(DecimalNumber(market_q(FIRM_P), num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE),
                                 Tex('$Q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        market_quantity.add_updater(lambda m: (
            m[0].set_value(float(np.round(market_q(price.get_value()))))
                .move_to(market_ax.c2p(market_q(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            m[1].move_to(market_ax.c2p(market_q(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        market_marks = [market_dot, market_across, market_drop, market_price, market_quantity]
        for m in market_marks:
            m.update()
        self.remove(note)
        note = teaching('We find equilibrium by intersecting the supply and demand curves.')
        self.play(FadeIn(market_dot), FadeIn(note))
        self.play(Create(market_across), Create(market_drop), FadeIn(market_price), FadeIn(market_quantity))
        self.pause('3.b.equilibrium')

        # ---- 3.b · The price carries across to the firm: the red line runs on to the firm's price axis.
        price_bridge = DashedLine(market_ax.c2p(market_q(FIRM_P), FIRM_P), firm_ax.c2p(0, FIRM_P), color=GUIDE,
                                  stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER)
        price_bridge.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(market_q(price.get_value()), price.get_value()), firm_ax.c2p(0, price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH, z_index=GUIDE_LAYER).set_style(**m.get_style())))
        price_number.update()
        price_number.clear_updaters()
        self.remove(note)
        note = teaching('This is where the price for the firm comes from.')
        self.play(Create(price_bridge), FadeOut(price_number), FadeIn(note), run_time=1.4)
        self.pause('3.b')

        # ---- 3.c · At this price the firm makes a profit: the box pulses.
        self.remove(note)
        note = teaching('At this price, the firm is making a profit, which is nice for them.')
        self.play(FadeIn(note))
        self.play(Indicate(profit_strips, color=FOCUS, scale_factor=1), Indicate(revenue_gain, color=FOCUS), run_time=0.8)
        self.pause('3.c')

        # ---- 3.d.entry · Entry: supply shifts down, the price falls to 60, and the firm's line, box and bars follow.
        market_supply.add_updater(lambda m: m.put_start_and_end_on(market_ax.c2p(0, 0),
                                                                   market_ax.c2p(*supply_end(price.get_value()))))
        supply_word.add_updater(lambda m: m.next_to(market_ax.c2p(*supply_end(price.get_value())), RIGHT, buff=0.12))
        self.remove(head, note)
        head = title('Entry And Exit')
        note = teaching('New firms open up, so the supply curve shifts down.')
        self.play(FadeIn(head), FadeIn(note))
        self.play(price.animate.set_value(60), quantity.animate.set_value(60), run_time=2.4, rate_func=smooth)
        self.pause('3.d.entry')

        # ---- 3.d.zero · Entry continues toward zero profit: 50.
        self.remove(note)
        note = teaching('Firms will continue to enter until there is no profit left.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(50), quantity.animate.set_value(50), run_time=2, rate_func=smooth)
        self.pause('3.d.zero')

        # ---- 3.d · Too far: at 30 the price is below ATC, and the box turns red.
        LOSS_P = 30
        self.remove(note)
        note = teaching('A negative profit is what we sometimes call a loss.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(LOSS_P), quantity.animate.set_value(LOSS_P), run_time=2.4, rate_func=smooth)
        self.pause('3.d')

        # ---- 3.e.avc · Average variable cost joins the firm's graph; at q* = 30 the price is above it.
        avc_line = Line(firm_ax.c2p(0, 0), firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), color=AVC_COLOR, stroke_width=CURVE_WIDTH)
        avc_word = Tex('AVC', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), RIGHT, buff=0.15)
        avc_dot = Dot(firm_ax.c2p(LOSS_P, avc(LOSS_P)), radius=DOT_RADIUS, color=AVC_COLOR).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('Firms earning a loss will exit the market if price is below their AVC.')
        self.play(FadeIn(avc_line), FadeIn(avc_word), FadeIn(avc_dot), FadeIn(note))
        self.pause('3.e.avc')

        # ---- 3.e.fc · A third bar: the fixed cost, which the firm pays even if it shuts down.
        fixed_bar = Rectangle(width=BAR_WIDTH, height=FC * BAR_SCALE, stroke_width=0, fill_color=FC_COLOR, fill_opacity=0.6)
        fixed_bar.move_to([FLOOR_BESIDE_X + SLOT * 2.5, ORIGIN_Y + FC * BAR_SCALE / 2, 0])
        fixed_edge = Line(LEFT * BAR_WIDTH / 2, RIGHT * BAR_WIDTH / 2, color=CAPTION, stroke_width=CURVE_WIDTH)
        fixed_edge.move_to([FLOOR_BESIDE_X + SLOT * 2.5, ORIGIN_Y + FC * BAR_SCALE, 0])
        fixed_value = Tex('1,000', color=CAPTION).scale(BAR_NUMBER_SCALE)
        fixed_value.move_to([FLOOR_BESIDE_X + SLOT * 2.5, ORIGIN_Y - QUANTITY_NUMBER_OFFSET, 0])
        fixed_name = Tex('FC', color=INK).scale(BAR_NAME_SCALE)
        fixed_name.move_to([FLOOR_BESIDE_X + SLOT * 2.5, ORIGIN_Y - QUANTITY_LABEL_OFFSET, 0])
        self.remove(note)
        note = teaching('Is operating with a loss better than exiting and paying the fixed cost?')
        self.play(bar_floor.animate.put_start_and_end_on(np.array([FLOOR_BESIDE_X, ORIGIN_Y, 0]), np.array([FLOOR_BESIDE_X + 3 * SLOT, ORIGIN_Y, 0])),
                  run_time=0.6)
        self.play(GrowFromEdge(fixed_bar, DOWN), FadeIn(fixed_edge), FadeIn(fixed_value), FadeIn(fixed_name), FadeIn(note))
        self.pause('3.e.fc')

        # ---- 3.e · The loss slides into the fixed-cost bar: it is the smaller of the two, so the firm keeps operating.
        loss_copy = cost_loss.copy().clear_updaters()
        loss_target = Rectangle(width=BAR_WIDTH, height=(total_cost() - revenue()) * BAR_SCALE, stroke_width=0,
                                fill_color=LOSS_COLOR, fill_opacity=0.8)
        loss_target.move_to([FLOOR_BESIDE_X + SLOT * 2.5, ORIGIN_Y + (total_cost() - revenue()) * BAR_SCALE / 2, 0])
        self.remove(note)
        note = teaching('Price is above AVC, so the loss is smaller than the fixed cost.')
        self.play(Transform(loss_copy, loss_target), FadeIn(note), run_time=1.4)
        self.pause('3.e')

        # ---- 3.f.exit · The long run: below ATC firms exit, supply shifts up, and the price rises from 30 to 48.
        self.remove(head, note)
        head = title('The Long Run')
        note = teaching('A loss in the long run: firms exit, supply shifts up, the price rises.')
        self.play(FadeOut(avc_line), FadeOut(avc_word), FadeOut(avc_dot), FadeOut(fixed_bar), FadeOut(fixed_edge),
                  FadeOut(fixed_value), FadeOut(fixed_name), FadeOut(loss_copy), run_time=0.6)
        self.play(bar_floor.animate.put_start_and_end_on(np.array([FLOOR_BESIDE_X, ORIGIN_Y, 0]), np.array([FLOOR_BESIDE_X + 2 * SLOT, ORIGIN_Y, 0])),
                  FadeIn(head), FadeIn(note), run_time=0.6)
        self.play(price.animate.set_value(48), quantity.animate.set_value(48), run_time=2.2, rate_func=smooth)
        self.pause('3.f.exit')

        # ---- 3.f.cycle · In and out: entry, a small overshoot, exit, settling where P = MC = ATC.
        # One eased motion that overshoots below 44.72 and comes back (r(0) = 0, r(1) = 1).
        settle = lambda t: 1 - (1 - smooth(t)) * np.cos(2.5 * np.pi * smooth(t)) * np.exp(-2 * smooth(t))
        self.remove(note)
        note = teaching('A profit: new firms enter, supply shifts down, the price falls.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(LONG_RUN_P), quantity.animate.set_value(LONG_RUN_P), run_time=4.5,
                  rate_func=settle)
        self.pause('3.f.cycle')

        # ---- 3.f · The long run: P = MC = ATC at its minimum, and profit is zero.
        self.remove(note)
        note = teaching('Zero profit condition: in the long run, firms earn zero profit.')
        self.play(FadeIn(note), Indicate(lowest_atc, color=FOCUS, scale_factor=1.6))
        self.pause('3.f')

        # ---- 4.a · Next time: the firm's demand tilts down.
        leaving = [price_word, q_drop, q_number, q_star, mc_dot, profit_strips, profit_area_word, loss_area_word,
                   *bars, *bar_marks, revenue_name, cost_name, profit_readout, price_bridge, *market_marks]
        for m in leaving + [price_line, market_supply, supply_word]:
            m.update()
            m.clear_updaters()
        self.remove(head, note)
        head = title('Next Time')
        note = teaching('What happens to marginal revenue when demand slopes down?')
        firm.remove(lowest_atc)
        self.play(*[FadeOut(m) for m in leaving], FadeOut(market_picture), FadeOut(bar_floor), FadeOut(divider),
                  FadeOut(lowest_atc), run_time=0.8)
        self.play(firm.animate.shift(RIGHT * (FIRM_CENTER_X - FIRM_BESIDE_X)),
                  price_line.animate.shift(RIGHT * (FIRM_CENTER_X - FIRM_BESIDE_X)), FadeIn(head), run_time=1.2)
        sloped = Line(firm_ax.c2p(0, 100), firm_ax.c2p(100, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        sloped_word = Tex('D', color=INK).scale(WORD_SCALE).next_to(firm_ax.c2p(100, 0), UR, buff=0.12)
        self.play(Transform(price_line, sloped), FadeIn(sloped_word), FadeIn(note), run_time=1.6)
        self.pause('4.a')
