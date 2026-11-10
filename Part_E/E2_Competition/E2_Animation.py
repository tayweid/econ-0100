# maniml E2_Animation.py EpisodeE2
# Teaching notes and current hold references: E2_Notes.md. Earlier storyboards are archived. All choreography stays in construct().
# Competitive firms: E1's firm takes the market price, profit built from one unit (TR, TC, the box, q(P - ATC)),
# the next unit decides the quantity (MC = MR), then the market beside the firm: entry and exit until profit is zero.
# One firm throughout, E1's: TC = 1000 + q^2 (a $100 wage, a $1,000 fixed cost), MC = 2q, AVC = q, ATC = q + 1000/q,
# lowest at q = sqrt(1000) = 31.6 where ATC = MC = 63.25. Market (Q in thousands): D: P = 120 - 2Q/3, S: P = (10/3)(Q - s),
# s the entry shift (0 at the start, 180 - 1.8 P* after). The firm's price is 100: q* = 50, ATC 70, TR 5,000, TC 3,500, profit 1,500.
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
        READOUT_SCALE, CURVE_WORD_SCALE, AREA_WORD_SCALE = 0.7, 0.7, 0.72
        CURVE_WIDTH, GUIDE_WIDTH, BAR_OUTLINE, DOT_RADIUS = 3, 2, 1.0, 0.07
        GUIDE_LAYER, DOT_LAYER = 5, 10
        LIST_SCALE, LIST_STEP = 0.9, 0.78
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Firm theory palette (shared_E.md). Profit is green, a loss red.
        MC_COLOR, ATC_COLOR, AVC_COLOR, FC_COLOR, FC_WORD = SUPPLY, TOTAL, PINK, MUTED, CAPTION
        REVENUE_COLOR, PROFIT_COLOR, LOSS_COLOR = DEMAND, GREEN, GUIDE    # profit green: orange is MC's (Taylor); the price line is GUIDE red
        # Layout: one baseline and one price scale ($0 to $130 per unit) throughout, and each section's composition
        # centred on the frame: market and firm side by side (sections 1 and 3); the firm alone (section 2). Everything
        # happens on the graph: no side panel (Taylor, November 9). The firm pans between its two positions, as E1 pans.
        ORIGIN_Y = BODY_MID - 2.15
        GRAPH_HEIGHT, PRICE_MAX, CURVE_TOP = 4.0, 130, 120   # square 4.0 graphs; S and MC stop at 120 so their names clear the panel labels
        MARKET_WIDTH, MARKET_Q_MAX, MARKET_X_PAIR = 4.0, 120, -5.6
        FIRM_WIDTH, FIRM_Q_MAX, FIRM_X_PAIR, FIRM_X_ALONE, FIRM_X_PANEL = 4.0, 70, 1.0, -2.0, -3.4   # beside the market; alone; with the Next Unit panel
        CHECKLIST_LEFT, CHECKLIST_DIVIDER_X = 1.1, 0.3   # the list centred right of a divider that clears the market's captions
        # Taxonomy grid, E4's object: a label column and two cell columns; a header row and three seller rows.
        LABEL_W, CELL_W, HEADER_H, CELL_H, TAXONOMY_X = 2.9, 3.3, 0.8, 1.25, 0.4
        BOX_BUFF = 0.12

        # The model, as one-line functions (q one firm's output in units, Q market output in thousands).
        FIXED = 1000
        total = lambda q: FIXED + q ** 2
        mc = lambda q: 2 * q
        avc = lambda q: q
        atc = lambda q: q + FIXED / q
        FIRM_P, LONG_RUN_P = 100, 2 * np.sqrt(FIXED)              # 100, and 63.25 where MC = ATC
        ATC_TOP = 118                                              # ATC is drawn from where it comes down to 118
        ATC_START = (ATC_TOP - np.sqrt(ATC_TOP ** 2 - 4 * FIXED)) / 2
        market_q = lambda p: 1.5 * (120 - p)                       # D: P = 120 - 2Q/3, from the axis at 120
        SUPPLY_SLOPE = 10 / 3                                      # S: P = (10/3)(Q - s), through (30, 100) at s = 0
        supply_shift = lambda p: 180 - 1.8 * p                     # the s at which S meets D at price p
        START_Q = 20

        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)

        # ---- 0.a · The shared bumper with E2's subtitle.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 2)
        thesis = Tex(r'\textit{Competitive Firms}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a · The market-structures taxonomy (E4's object), the many-sellers homogeneous cell boxed, as E1 leaves it.
        head = title('Competitive Markets')
        grid_left = TAXONOMY_X - (LABEL_W + 2 * CELL_W) / 2
        grid_right = grid_left + LABEL_W + 2 * CELL_W
        grid_top = BODY_MID + (HEADER_H + 3 * CELL_H) / 2
        column_x = [grid_left + LABEL_W + CELL_W * (i + 0.5) for i in range(2)]
        row_y = [grid_top - HEADER_H - CELL_H * (i + 0.5) for i in range(3)]
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
        box = SurroundingRectangle(perfect, buff=BOX_BUFF, color=NASH)
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a')

        # ---- 1.b.buyers · The market's axes on the left and a divider; the five conditions fade in one per hold, in white,
        # many buyers with demand.
        market_ax = style_axes([0, MARKET_Q_MAX, 10], [0, PRICE_MAX, 10], x_length=MARKET_WIDTH, y_length=GRAPH_HEIGHT)
        market_ax.shift(np.array([MARKET_X_PAIR, ORIGIN_Y, 0]) - market_ax.c2p(0, 0))
        market_label = Tex('Market', color=INK).scale(0.8).next_to(market_ax.c2p(MARKET_Q_MAX / 2, PRICE_MAX), UP, buff=0.12)
        market_words = VGroup(
            market_label,
            Tex('P', color=INK).scale(0.8).next_to(market_ax.c2p(0, PRICE_MAX), LEFT, buff=0.25),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55),
            Tex('Q', color=INK).scale(0.8).next_to(market_ax.c2p(MARKET_Q_MAX, 0), DOWN, buff=0.35),
            Tex(r'\textsf{1,000 units}', color=CAPTION).scale(0.55))
        market_words[2].next_to(market_words[1], RIGHT, buff=0.35)
        market_words[4].next_to(market_words[3], RIGHT, buff=0.3)
        DEMAND_END = 110                                           # D stops short of the axis end so its name clears the firm's P
        market_demand = Line(market_ax.c2p(0, 120), market_ax.c2p(DEMAND_END, 120 - 2 * DEMAND_END / 3), color=DEMAND, stroke_width=CURVE_WIDTH)
        demand_word = Tex('D', color=DEMAND).scale(CURVE_WORD_SCALE).next_to(market_ax.c2p(DEMAND_END, 120 - 2 * DEMAND_END / 3), RIGHT, buff=0.12)
        # Supply runs from its intercept up to the top of the price scale, or to the end of the quantity axis if sooner.
        supply_top_q = lambda p: min(MARKET_Q_MAX, supply_shift(p) + CURVE_TOP / SUPPLY_SLOPE)
        supply_ends = lambda p: (market_ax.c2p(supply_shift(p), 0),
                                 market_ax.c2p(supply_top_q(p), SUPPLY_SLOPE * (supply_top_q(p) - supply_shift(p))))
        market_supply = Line(*supply_ends(FIRM_P), color=SUPPLY, stroke_width=CURVE_WIDTH)
        supply_word = Tex('S', color=SUPPLY).scale(CURVE_WORD_SCALE).next_to(supply_ends(FIRM_P)[1], RIGHT, buff=0.12)
        checklist = VGroup()
        for i, item in enumerate(['Many buyers', 'Many identical sellers', 'A homogeneous good', 'No externalities',
                                  'Low barriers to entry']):
            row = Tex(rf'{i + 1}.\enspace {item}', color=INK).scale(LIST_SCALE).align_to(ORIGIN, LEFT)
            row.shift(UP * (-i * LIST_STEP - row.family_members_with_points()[0].get_bottom()[1]))
            checklist.add(row)
        checklist.move_to([0, BODY_MID, 0]).align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        # The graph-beside-text divider (B2's), between the market and the list; it leaves with the list.
        checklist_divider = Line([CHECKLIST_DIVIDER_X, -3.0, 0], [CHECKLIST_DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        self.play(FadeOut(taxonomy), FadeOut(box), run_time=0.6)
        self.play(FadeIn(market_ax), FadeIn(VGroup(*market_words[1:])), FadeIn(checklist_divider))   # the Market label waits for the firm
        self.play(FadeIn(checklist[0]), FadeIn(market_demand), FadeIn(demand_word))
        self.pause('1.b.buyers')

        # ---- 1.b.sellers · Many identical sellers lights with supply.
        self.play(FadeIn(checklist[1]), FadeIn(market_supply), FadeIn(supply_word))
        self.pause('1.b.sellers')

        # ---- 1.b.good · A homogeneous good.
        self.play(FadeIn(checklist[2]))
        self.pause('1.b.good')

        # ---- 1.b.externalities · No externalities.
        self.play(FadeIn(checklist[3]))
        self.pause('1.b.externalities')

        # ---- 1.b · Low barriers to entry.
        self.play(FadeIn(checklist[4]))
        self.pause('1.b')

        # ---- 1.c · The list leaves; the market stays. E1's firm beside it: MC, ATC, a grey dot at ATC's minimum.
        firm_ax = style_axes([0, FIRM_Q_MAX, 10], [0, PRICE_MAX, 10], x_length=FIRM_WIDTH, y_length=GRAPH_HEIGHT)
        firm_ax.shift(np.array([FIRM_X_PAIR, ORIGIN_Y, 0]) - firm_ax.c2p(0, 0))
        firm_label = Tex('Firm', color=INK).scale(0.8).next_to(firm_ax.c2p(FIRM_Q_MAX / 2, PRICE_MAX), UP, buff=0.12)
        firm_words = VGroup(
            firm_label,
            Tex('P', color=INK).scale(0.8).next_to(firm_ax.c2p(0, PRICE_MAX), LEFT, buff=0.25),
            Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55),
            Tex('q', color=INK).scale(0.8).next_to(firm_ax.c2p(FIRM_Q_MAX, 0), DOWN, buff=0.35),
            Tex(r'\textsf{units}', color=CAPTION).scale(0.55))
        firm_words[2].next_to(firm_words[1], RIGHT, buff=0.35)
        firm_words[4].next_to(firm_words[3], RIGHT, buff=0.3)
        mc_line = Line(firm_ax.c2p(0, 0), firm_ax.c2p(CURVE_TOP / 2, CURVE_TOP), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        mc_word = Tex('MC', color=MC_COLOR).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(CURVE_TOP / 2, CURVE_TOP), RIGHT, buff=0.15)
        atc_curve = polyline([firm_ax.c2p(q, atc(q)) for q in np.geomspace(ATC_START, FIRM_Q_MAX, 240)], ATC_COLOR, CURVE_WIDTH)
        # ATC is named where it enters at the upper left; its right end shares heights with P = MR and AVC.
        atc_word = Tex('ATC', color=ATC_COLOR).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(ATC_START, ATC_TOP), RIGHT, buff=0.15)
        lowest_atc = Dot(firm_ax.c2p(np.sqrt(FIXED), LONG_RUN_P), radius=0.085, color=MUTED).set_z_index(DOT_LAYER + 1)   # grey, not yellow (Taylor)
        firm = VGroup(firm_ax, firm_words, mc_line, mc_word, atc_curve, atc_word)      # the grey dot joins only at zero profit (3.d.zero)
        self.play(FadeOut(checklist), FadeOut(checklist_divider), run_time=0.5)
        self.play(FadeIn(firm), FadeIn(market_label))
        self.pause('1.c')

        # ---- 1.d · Where S meets D: P* and Q* on the market, and the red price guide runs on across the gap to the firm's
        # axis, where it is the firm's flat demand, P = MR. One tracker for the price, one for the firm's quantity.
        price = ValueTracker(FIRM_P)
        quantity = ValueTracker(60)
        market_dot = Dot(market_ax.c2p(market_q(FIRM_P), FIRM_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        market_dot.add_updater(lambda m: m.move_to(market_ax.c2p(market_q(price.get_value()), price.get_value())))
        market_across = DashedLine(market_ax.c2p(0, FIRM_P), market_ax.c2p(market_q(FIRM_P), FIRM_P), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        market_across.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(0, price.get_value()), market_ax.c2p(market_q(price.get_value()), price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        market_drop = DashedLine(market_ax.c2p(market_q(FIRM_P), 0), market_ax.c2p(market_q(FIRM_P), FIRM_P), color=GUIDE,
                                 stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        market_drop.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(market_q(price.get_value()), 0), market_ax.c2p(market_q(price.get_value()), price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        market_price = VGroup(Tex('$P^*=$', color=GUIDE), DecimalNumber(FIRM_P, num_decimal_places=2, color=GUIDE)).scale(0.65)
        market_price.add_updater(lambda m: (m[1].set_value(price.get_value()), m.arrange(RIGHT, buff=0.06),
                                            m.next_to(market_ax.c2p(0, price.get_value()), LEFT, buff=0.2)))
        market_quantity = VGroup(DecimalNumber(market_q(FIRM_P), num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE),
                                 Tex('$Q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE))
        market_quantity.add_updater(lambda m: (
            m[0].set_value(float(np.round(market_q(price.get_value()))))
                .move_to(market_ax.c2p(market_q(price.get_value()), 0) + DOWN * QUANTITY_NUMBER_OFFSET),
            m[1].move_to(market_ax.c2p(market_q(price.get_value()), 0) + DOWN * QUANTITY_LABEL_OFFSET)))
        price_bridge = DashedLine(market_ax.c2p(market_q(FIRM_P), FIRM_P), firm_ax.c2p(0, FIRM_P), color=GUIDE,
                                  stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        price_bridge.add_updater(lambda m: m.become(DashedLine(
            market_ax.c2p(market_q(price.get_value()), price.get_value()), firm_ax.c2p(0, price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        market_marks = [market_dot, market_across, market_drop, market_price, market_quantity, price_bridge]
        # The firm's flat demand is the price itself: the same dashed red as the guide, running on from the bridge.
        price_line = DashedLine(firm_ax.c2p(0, FIRM_P), firm_ax.c2p(FIRM_Q_MAX, FIRM_P), color=GUIDE, stroke_width=CURVE_WIDTH)
        price_line.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(0, price.get_value()), firm_ax.c2p(FIRM_Q_MAX, price.get_value()), color=GUIDE, stroke_width=CURVE_WIDTH)))
        price_word = Tex('P', color=DEMAND)          # curve names take their curve's color (Taylor); MR the course blue.scale(CURVE_WORD_SCALE)
        price_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        mr_word = Tex('P = MR', color=DEMAND).scale(CURVE_WORD_SCALE)
        mr_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        mr_only_word = Tex('MR', color=DEMAND).scale(CURVE_WORD_SCALE)       # section 2, where P reads on the firm's own axis
        mr_only_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        market_supply.add_updater(lambda m: m.put_start_and_end_on(*supply_ends(price.get_value())))
        supply_word.add_updater(lambda m: m.next_to(supply_ends(price.get_value())[1], RIGHT, buff=0.12))
        for m in market_marks + [price_line, price_word, mr_word, mr_only_word]:
            m.update()
        note = teaching('Competitive firms are what we call price takers.')
        self.play(FadeIn(market_dot))
        self.play(Create(market_across), Create(market_drop), FadeIn(market_price), FadeIn(market_quantity))
        self.play(Create(price_bridge), run_time=1.2)
        self.play(FadeIn(price_line), FadeIn(price_word), FadeIn(note))
        self.pause('1.d')

        # ---- 1.e · Wiggle the firm's quantity: the price it gets does not move.
        firm_dot = Dot(firm_ax.c2p(60, FIRM_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        firm_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), price.get_value())))
        # The quantity guide reaches the price line, or the top of the profit box when ATC is above the price.
        show_unit_mc = [False]                                   # True while the next unit's MC dot is on the graph (2.d)
        guide_top = lambda: max(price.get_value(), atc(max(quantity.get_value(), 1)),
                                mc(quantity.get_value()) if show_unit_mc[0] else 0)
        q_drop = DashedLine(firm_ax.c2p(60, 0), firm_ax.c2p(60, FIRM_P), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        q_drop.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), 0), firm_ax.c2p(quantity.get_value(), guide_top()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
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
        # One eased wiggle: 60 up to 68, down to 30, back to 60 (the axis ends at 70).
        wiggle = lambda a: 60 + np.sin(2 * np.pi * smooth(a)) * (8 if np.sin(2 * np.pi * smooth(a)) >= 0 else 30)
        self.play(UpdateFromAlphaFunc(quantity, lambda m, a: m.set_value(wiggle(a))), run_time=3.2)
        quantity.set_value(60)
        self.pause('1.e')

        # ---- 1.e.mr · Why the price is marginal revenue: the units sold are bars of revenue, each exactly P tall. The bars
        # fade in at q = 60; the quantity falls to 40 and rises back to 60, a bar leaving or arriving with each unit, each one
        # worth the price. The line is renamed P = MR.
        mr_bars = VGroup(*[Polygon(firm_ax.c2p(u, 0), firm_ax.c2p(u + 1, 0), firm_ax.c2p(u + 1, FIRM_P), firm_ax.c2p(u, FIRM_P),
                                   color=REVENUE_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY) for u in range(FIRM_Q_MAX)])
        for u, bar in enumerate(mr_bars):                      # bar u is there while the quantity covers unit u + 1
            bar.add_updater(lambda m, u=u: m.set_points_as_corners([
                firm_ax.c2p(u, 0), firm_ax.c2p(u + 1, 0), firm_ax.c2p(u + 1, price.get_value()), firm_ax.c2p(u, price.get_value()),
                firm_ax.c2p(u, 0)]).set_stroke(REVENUE_COLOR, BAR_OUTLINE, opacity=float(u + 1 <= quantity.get_value() + 1e-6))
                .set_fill(REVENUE_COLOR, AREA_OPACITY * float(u + 1 <= quantity.get_value() + 1e-6)))
        for bar in mr_bars:
            bar.update()
        self.remove(note)
        note = teaching('One more unit sells for the price: marginal revenue is the price.')
        self.play(FadeIn(mr_bars), FadeIn(note))
        self.play(quantity.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.play(quantity.animate.set_value(60), run_time=ROLL_TIME, rate_func=smooth)
        self.remove(price_word)
        self.play(FadeIn(mr_word), run_time=0.5)
        price_word = mr_word
        self.pause('1.e.mr')

        # ---- 1.f.exercise · Q1a stays on screen while students work on the board.
        # An open prompt on the same graphite ground; cover the graph and its answer.
        # Keep the lecture objects in place so advancing resumes the existing sequence.
        exercise_ground = Rectangle(width=config.frame_width, height=config.frame_height,
                                    stroke_width=0, fill_color=BG, fill_opacity=1).set_z_index(100)
        exercise_label = Tex(r'Exercise E2 \textbar{} Q1a', color=CAPTION).scale(0.64)
        # Q1a wording from Exercise/Exercise_E2.md; TeX handles paragraph justification and wrapping.
        exercise_question = Tex(
            r'\begin{minipage}{27em}'
            r'\setlength{\parindent}{0pt}'
            r'If the market price is 90, find:'
            r'\begin{itemize}\setlength{\itemsep}{0.35em}'
            r'\item Total revenue from selling 20 units: $TR_{20}$'
            r'\item Total revenue selling 21 units: $TR_{21}$'
            r'\end{itemize}'
            r'What is marginal revenue?'
            r'\end{minipage}', color=INK,
        ).scale(0.95)
        exercise_text = VGroup(exercise_label, exercise_question)
        exercise_text.arrange(DOWN, aligned_edge=LEFT, buff=0.6)
        exercise_text.set_y(BODY_MID).to_edge(LEFT, buff=1.5).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_text), run_time=0.4)
        self.pause('1.f.exercise')
        self.play(FadeOut(exercise_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 2.a · Profit: zoomed in on the firm. The market leaves and the firm pans to the centre; the subtitle says what
        # profit is, and the firm's price reads on its own axis while the market is away.
        for m in market_marks:
            m.update()
        self.remove(note)
        context = subtitle(head, 'Profit is the difference between total revenue and total costs.')
        price_number = VGroup(MathTex('P=', color=GUIDE), DecimalNumber(FIRM_P, num_decimal_places=2, color=GUIDE)).scale(READOUT_SCALE)
        price_number.add_updater(lambda m: (m[1].set_value(price.get_value()), m.arrange(RIGHT, buff=0.08),
                                            m.next_to(firm_ax.c2p(0, price.get_value()), LEFT, buff=0.2)))
        price_number.update()
        market_picture = VGroup(market_ax, market_words, market_demand, demand_word, market_supply, supply_word)
        for bar in mr_bars:
            bar.clear_updaters()
        self.play(*[FadeOut(m) for m in market_marks], FadeOut(mr_bars), FadeOut(firm_dot), FadeOut(q_drop), FadeOut(q_number),
                  FadeOut(q_symbol), run_time=0.5)
        # The Firm label goes dark while the firm is alone (it stays in the group, so it pans with it).
        self.play(FadeOut(market_picture), firm.animate.shift(RIGHT * (FIRM_X_ALONE - FIRM_X_PAIR)), firm_label.animate.set_opacity(0),
                  run_time=1.6, rate_func=smooth)
        note = teaching('Profit is everything left over after we’ve paid our costs.')
        mr_only_word.update()
        self.remove(price_word)
        price_word = mr_only_word
        self.play(FadeIn(context), FadeIn(price_number), FadeIn(price_word), FadeIn(note))
        self.pause('2.a')

        # ---- 2.b.revenue · Start small: q = 20. Twenty one-unit strips from the axis up to the price, one after another: each
        # sells for $100. Total revenue, named in teal.
        quantity.set_value(START_Q)
        for m in (q_drop, q_number, q_symbol):
            m.update()
        revenue_strips = VGroup(*[Polygon(firm_ax.c2p(u, 0), firm_ax.c2p(u + 1, 0), firm_ax.c2p(u + 1, FIRM_P), firm_ax.c2p(u, FIRM_P),
                                          color=REVENUE_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
                                  for u in range(START_Q)])
        cost_strips = VGroup(*[Polygon(firm_ax.c2p(u, 0), firm_ax.c2p(u + 1, 0), firm_ax.c2p(u + 1, atc(START_Q)), firm_ax.c2p(u, atc(START_Q)),
                                       color=ATC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=AREA_OPACITY)
                               for u in range(START_Q)])
        revenue_word = Tex('TR', color=INK).scale(AREA_WORD_SCALE).move_to(firm_ax.c2p(START_Q / 2, FIRM_P / 2))   # on its region
        # Curves recede while they are not the subject. Stroke opacity for the curves: set_opacity would also give the open
        # ATC path a fill.
        dim_mc = lambda a: [mc_line.animate.set_stroke(opacity=a), mc_word.animate.set_opacity(a)]
        dim_atc = lambda a: [atc_curve.animate.set_stroke(opacity=a), atc_word.animate.set_opacity(a)]
        dim_curves = lambda a: dim_mc(a) + dim_atc(a)
        self.remove(note)
        note = teaching('Each unit sells for the market price.')
        self.play(FadeIn(q_drop), FadeIn(q_number), FadeIn(q_symbol), *dim_curves(0.25))
        self.play(LaggedStart(*[FadeIn(strip) for strip in revenue_strips], lag_ratio=0.1), FadeIn(note), run_time=2)
        self.play(FadeIn(revenue_word), run_time=0.4)
        self.pause('2.b.revenue')

        # ---- 2.b.atc.point · Reading ATC off the curve: plug q = 20 into ATC, a purple point where the quantity line meets it.
        # The TR bars recede to a ghost as the subject turns to cost.
        # Drawn from the point toward the axis (its start is the point, so Create runs leftward).
        atc_guide = DashedLine(firm_ax.c2p(START_Q, atc(START_Q)), firm_ax.c2p(0, atc(START_Q)), color=ATC_COLOR,
                               stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        atc_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), atc(quantity.get_value())), firm_ax.c2p(0, atc(quantity.get_value())),
            color=ATC_COLOR, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        atc_dot = Dot(firm_ax.c2p(START_Q, atc(START_Q)), radius=DOT_RADIUS, color=ATC_COLOR).set_z_index(DOT_LAYER)
        atc_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), atc(quantity.get_value()))))
        atc_number = VGroup(MathTex(r'\mathrm{ATC}_q=', color=ATC_COLOR),
                            DecimalNumber(atc(START_Q), num_decimal_places=2, color=ATC_COLOR)).scale(READOUT_SCALE)
        atc_number.add_updater(lambda m: (m[1].set_value(atc(quantity.get_value())), m.arrange(RIGHT, buff=0.08),
                                          m.next_to(firm_ax.c2p(0, atc(quantity.get_value())), LEFT, buff=0.2)))
        atc_number.update()
        cost_word = Tex('TC', color=INK).scale(AREA_WORD_SCALE).move_to(firm_ax.c2p(START_Q / 2, atc(START_Q) / 2))   # on its region
        self.remove(note)
        note = teaching('Plug the quantity into average total cost.')
        # The TR bars recede to a ghost (not out); ATC comes back as the subject.
        self.play(revenue_strips.animate.set_fill(opacity=0.08).set_stroke(opacity=0.25), FadeOut(revenue_word), *dim_atc(1),
                  FadeIn(atc_dot), FadeIn(note))
        self.pause('2.b.atc.point')

        # ---- 2.b.atc · The dashed guide runs from the point to the axis, where ATC at q reads 70.00.
        self.remove(note)
        note = teaching('On average, each unit costs \\$70.')
        self.play(Create(atc_guide), run_time=1.0)
        self.play(FadeIn(atc_number), FadeIn(note), run_time=0.5)
        self.pause('2.b.atc')

        # ---- 2.b.cost · Twenty bars up to ATC fade in, one after another: total cost, named on its region.
        self.remove(note)
        note = teaching('Profit is the difference between these two areas.')
        self.play(LaggedStart(*[FadeIn(strip) for strip in cost_strips], lag_ratio=0.1), run_time=2)
        self.play(FadeIn(cost_word), FadeIn(note), run_time=0.5)
        self.pause('2.b.cost')

        # ---- 2.c.area · The difference: one-unit bars from ATC to P over 0 to q, orange for a profit, red for a loss, the name
        # centred over them (it fades when the bars are thinner than 0.3 units). The curves recede while profit is the subject.
        box_low = lambda: min(price.get_value(), atc(max(quantity.get_value(), 1)))
        box_high = lambda: max(price.get_value(), atc(max(quantity.get_value(), 1)))
        in_profit = lambda: price.get_value() >= atc(max(quantity.get_value(), 1))
        box_color = lambda: PROFIT_COLOR if in_profit() else LOSS_COLOR
        # One bar per unit from ATC to P; bar u shows while u < q, and the last one is cut at q as q rolls.
        bar_right = lambda u: max(u, min(u + 1, quantity.get_value()))
        bar_shape = lambda u: [firm_ax.c2p(u, box_low()), firm_ax.c2p(bar_right(u), box_low()), firm_ax.c2p(bar_right(u), box_high()),
                               firm_ax.c2p(u, box_high()), firm_ax.c2p(u, box_low())]
        profit_box = VGroup(*[Polygon(ORIGIN, RIGHT, UP, stroke_width=BAR_OUTLINE, fill_opacity=0) for u in range(FIRM_Q_MAX)])
        for u, bar in enumerate(profit_box):
            bar.add_updater(lambda m, u=u: m.set_points_as_corners(bar_shape(u))
                            .set_stroke(box_color(), BAR_OUTLINE, opacity=float(u < quantity.get_value()))
                            .set_fill(box_color(), AREA_OPACITY * float(u < quantity.get_value())))
        box_height = lambda: (box_high() - box_low()) * GRAPH_HEIGHT / PRICE_MAX
        box_name_opacity = lambda: float(np.clip((box_height() - 0.3) / 0.15, 0, 1))
        name_spot = lambda: firm_ax.c2p(quantity.get_value() / 2, (box_low() + box_high()) / 2)
        profit_name = Tex('Profit', color=INK).scale(AREA_WORD_SCALE).set_z_index(DOT_LAYER)
        profit_name.add_updater(lambda m: m.move_to(name_spot()).set_opacity(box_name_opacity() if in_profit() else 0))
        loss_name = Tex('Loss', color=INK).scale(AREA_WORD_SCALE).set_z_index(DOT_LAYER)
        loss_name.add_updater(lambda m: m.move_to(name_spot()).set_opacity(0 if in_profit() else box_name_opacity()))
        for m in (*profit_box, profit_name, loss_name):
            m.update()
        self.remove(note)
        note = teaching('So we usually just look at the difference on the graph.')
        self.play(FadeOut(revenue_strips), FadeOut(cost_strips), FadeOut(cost_word), *dim_curves(0.25), FadeIn(profit_box), FadeIn(note),
                  run_time=1.2)
        self.play(FadeIn(profit_name))
        self.add(loss_name)
        self.pause('2.c.area')

        # ---- 2.c · B2's measurement, laid just outside the axes as E1 lays its interval marks: a yellow line left of the price
        # axis from ATC to P and one under the quantity axis from 0 to q, no labels (the bottom line names them). They ride the trackers and
        # stay, at half strength, while things move on the graph.
        MARK_GAP = 0.14
        height_mark = Line(ORIGIN, UP, color=FOCUS, stroke_width=4)
        height_mark.add_updater(lambda m: m.put_start_and_end_on(firm_ax.c2p(0, box_low()) + LEFT * MARK_GAP,
                                                                 firm_ax.c2p(0, box_high()) + LEFT * MARK_GAP))
        base_mark = Line(ORIGIN, RIGHT, color=FOCUS, stroke_width=4)
        base_mark.add_updater(lambda m: m.put_start_and_end_on(firm_ax.c2p(0, 0) + DOWN * MARK_GAP,
                                                               firm_ax.c2p(max(quantity.get_value(), 0.5), 0) + DOWN * MARK_GAP))
        measure_marks = [height_mark, base_mark]
        for m in measure_marks:
            m.update()
        self.remove(note)
        note = teaching(r'Which is mathematically equivalent to $q(P - \mathrm{ATC})$.')
        self.play(Create(height_mark))
        self.play(Create(base_mark), FadeIn(note))
        self.pause('2.c')

        # ---- 2.d.mc · The next unit, the 21st, at the red dashed quantity line: a teal dot where it meets the price
        # (its marginal revenue) and an orange dot where it meets MC (its marginal cost, TC(21) - TC(20) = $41). Beside the
        # graph, E1 4.d's close-up: two columns at the same price scale, MR and MC, so the gap between them is what the
        # unit adds to profit. The MC column climbs as q rolls and meets MR at 50.
        unit_mc = lambda: mc(quantity.get_value())            # the next unit's cost, read as MC at q (so MC = MR reads 100 = 100)
        unit_revenue_dot = Dot(radius=0.065, color=REVENUE_COLOR).set_z_index(DOT_LAYER)
        unit_revenue_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), price.get_value())))
        unit_cost_dot = Dot(radius=0.065, color=MC_COLOR).set_z_index(DOT_LAYER)
        unit_cost_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), unit_mc())))
        # The close-up columns: faint fill, a solid value edge, the value beside the edge, the name under the base (E1 4.d).
        MR_X, MC_X, UNIT_COLUMN_W, UNIT_COLUMN_FILL, UNIT_DIVIDER_X = 3.5, 4.3, 0.5, 0.4, 2.3
        price_y = lambda p: firm_ax.c2p(0, p)[1]
        column_corners = lambda x, top: [[x - UNIT_COLUMN_W / 2, ORIGIN_Y, 0], [x + UNIT_COLUMN_W / 2, ORIGIN_Y, 0],
                                         [x + UNIT_COLUMN_W / 2, top, 0], [x - UNIT_COLUMN_W / 2, top, 0], [x - UNIT_COLUMN_W / 2, ORIGIN_Y, 0]]
        unit_base = Line([MR_X - 0.45, ORIGIN_Y, 0], [MC_X + 0.45, ORIGIN_Y, 0], color=MUTED)
        unit_divider = Line([UNIT_DIVIDER_X, -3.0, 0], [UNIT_DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        unit_title = Tex('Next Unit', color=INK).scale(0.8).move_to([(MR_X + MC_X) / 2, ORIGIN_Y + GRAPH_HEIGHT + 0.3, 0])
        mr_column = Polygon(*column_corners(MR_X, price_y(FIRM_P)), stroke_width=0, fill_color=REVENUE_COLOR, fill_opacity=UNIT_COLUMN_FILL)
        mr_column.add_updater(lambda m: m.set_points_as_corners(column_corners(MR_X, price_y(price.get_value()))))
        mc_column = Polygon(*column_corners(MC_X, price_y(unit_mc())), stroke_width=0, fill_color=MC_COLOR, fill_opacity=UNIT_COLUMN_FILL)
        mc_column.add_updater(lambda m: m.set_points_as_corners(column_corners(MC_X, price_y(unit_mc()))))
        mr_edge = Line(LEFT * UNIT_COLUMN_W / 2, RIGHT * UNIT_COLUMN_W / 2, color=REVENUE_COLOR, stroke_width=CURVE_WIDTH)
        mr_edge.add_updater(lambda m: m.move_to([MR_X, price_y(price.get_value()), 0]))
        mc_edge = Line(LEFT * UNIT_COLUMN_W / 2, RIGHT * UNIT_COLUMN_W / 2, color=MC_COLOR, stroke_width=CURVE_WIDTH)
        mc_edge.add_updater(lambda m: m.move_to([MC_X, price_y(unit_mc()), 0]))
        mr_value = DecimalNumber(FIRM_P, num_decimal_places=0, color=REVENUE_COLOR).scale(0.6)
        mr_value.add_updater(lambda m: m.set_value(round(price.get_value(), 4)).next_to([MR_X, price_y(price.get_value()), 0], UP, buff=0.12))
        mc_value = DecimalNumber(unit_mc(), num_decimal_places=0, color=MC_COLOR).scale(0.6)
        mc_value.add_updater(lambda m: m.set_value(round(unit_mc(), 4)).next_to([MC_X, price_y(unit_mc()), 0], UP, buff=0.12))
        # What the next unit does to profit: the part of the taller column above the shorter one, green on MR_q while the unit
        # brings in more than it costs, red on MC_q once it costs more, with the signed difference beside it.
        unit_gain = lambda: price.get_value() - unit_mc()
        gain_cap = Polygon(*column_corners(MR_X, price_y(FIRM_P)), stroke_width=0, fill_color=PROFIT_COLOR, fill_opacity=0.75)
        gain_cap.add_updater(lambda m: m.set_points_as_corners(
            [[x, max(y, price_y(min(price.get_value(), unit_mc()))), 0] for x, y, _ in
             column_corners(MR_X if unit_gain() >= 0 else MC_X, price_y(max(price.get_value(), unit_mc())))])
            .set_fill(PROFIT_COLOR if unit_gain() >= 0 else LOSS_COLOR, 0.75 if abs(unit_gain()) > 0.5 else 0))
        gain_value = DecimalNumber(FIRM_P - mc(START_Q), num_decimal_places=0, include_sign=True, color=PROFIT_COLOR).scale(0.6)
        gain_value.add_updater(lambda m: m.set_value(round(unit_gain(), 4)).set_color(PROFIT_COLOR if unit_gain() >= 0 else LOSS_COLOR)
                               .set_opacity(1 if abs(unit_gain()) > 0.5 else 0)
                               .next_to([MR_X - UNIT_COLUMN_W / 2 if unit_gain() >= 0 else MC_X + UNIT_COLUMN_W / 2,
                                         price_y((price.get_value() + unit_mc()) / 2), 0], LEFT if unit_gain() >= 0 else RIGHT, buff=0.15))
        unit_names = VGroup(MathTex(r'\mathrm{MR}_q', color=REVENUE_COLOR).scale(0.6).move_to([MR_X, ORIGIN_Y - 0.3, 0]),
                            MathTex(r'\mathrm{MC}_q', color=MC_COLOR).scale(0.6).move_to([MC_X, ORIGIN_Y - 0.3, 0]))
        # Dashed guides carry the two heights to the column tops, both starting just right of the line's name: MR's in teal,
        # MC's in orange.
        mr_guide = DashedLine(ORIGIN, RIGHT, color=REVENUE_COLOR, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        mr_guide.add_updater(lambda m: m.become(DashedLine(
            [mr_only_word.get_right()[0] + 0.15, price_y(price.get_value()), 0], [MR_X - UNIT_COLUMN_W / 2, price_y(price.get_value()), 0],
            color=REVENUE_COLOR, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        mc_guide = DashedLine(ORIGIN, RIGHT, color=MC_COLOR, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        mc_guide.add_updater(lambda m: m.become(DashedLine(
            [mr_only_word.get_right()[0] + 0.15, price_y(unit_mc()), 0], [MC_X - UNIT_COLUMN_W / 2, price_y(unit_mc()), 0],
            color=MC_COLOR, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        unit_marks = [unit_revenue_dot, unit_cost_dot, mr_column, mc_column, mr_edge, mc_edge, mr_value, mc_value, mr_guide, mc_guide,
                      gain_cap, gain_value]
        for m in unit_marks:
            m.update()
        # First the next unit's marginal cost read off the curve: a red dashed guide from the dot to the axis, MC_q = 40 there.
        mc_axis_guide = DashedLine(firm_ax.c2p(START_Q, mc(START_Q)), firm_ax.c2p(0, mc(START_Q)), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        # The axis guide and readout fade as MC_q comes within $10 of the price, gone within $4 (they would sit on P's).
        near_price = lambda: float(np.clip((abs(unit_mc() - price.get_value()) - 4) / 6, 0, 1))
        mc_axis_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), unit_mc()), firm_ax.c2p(0, unit_mc()), color=GUIDE, stroke_width=GUIDE_WIDTH)
            .set_z_index(GUIDE_LAYER)).set_stroke(opacity=near_price()))
        mc_number = VGroup(MathTex(r'\mathrm{MC}_q=', color=MC_COLOR), DecimalNumber(unit_mc(), num_decimal_places=0, color=MC_COLOR)).scale(READOUT_SCALE)
        mc_number.add_updater(lambda m: (m[1].set_value(round(unit_mc(), 4)), m.arrange(RIGHT, buff=0.08),
                                         m.next_to(firm_ax.c2p(0, unit_mc()), LEFT, buff=0.2), m.set_opacity(near_price())))
        mc_number.update()
        unit_marks += [mc_axis_guide, mc_number]
        self.remove(note)
        note = teaching('What does the next unit cost to make?')
        # Only the next unit's two heights matter here: ATC's guide and readout leave and its curve recedes (its point stays
        # on the curve); MC returns.
        self.play(*[m.animate.set_opacity(0.5) for m in measure_marks], *dim_mc(1), *dim_atc(0.25), FadeOut(atc_guide),
                  FadeOut(atc_number), FadeIn(unit_revenue_dot), FadeIn(unit_cost_dot), FadeIn(note))
        show_unit_mc[0] = True
        self.play(Create(mc_axis_guide), run_time=1.0)
        self.play(FadeIn(mc_number), run_time=0.5)
        self.pause('2.d.mc')

        # ---- 2.d.unit · The firm pans left and the Next Unit panel joins beside it, the pair centred; the axis guide and
        # MC_q readout stay.
        self.remove(note)
        note = teaching('Should we increase our quantity by 1?')
        self.play(firm.animate.shift(RIGHT * (FIRM_X_PANEL - FIRM_X_ALONE)), run_time=1.2, rate_func=smooth)
        self.play(Create(mr_guide), Create(mc_guide), run_time=0.8)
        self.play(FadeIn(unit_divider), FadeIn(unit_title), FadeIn(unit_base), FadeIn(unit_names), FadeIn(mr_column), FadeIn(mc_column),
                  FadeIn(mr_edge), FadeIn(mc_edge), FadeIn(mr_value), FadeIn(mc_value), FadeIn(note))
        self.play(FadeIn(gain_cap), FadeIn(gain_value), run_time=0.6)
        unit_marks += [unit_base, unit_names, unit_divider, unit_title]
        self.pause('2.d.unit')

        # ---- 2.d.ten · More units: the unit rides up MC, the MC column climbs toward MR, and the bars and numbers roll. The stop
        # is 35, just past 30, where the MC and ATC points would sit on top of each other.
        self.play(quantity.animate.set_value(START_Q + 15), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.ten')

        # ---- 2.d.equal · Keep going to 50: the next unit costs what it brings in, MC meets MR.
        self.remove(note)
        note = teaching('Profit will continue to rise until MR = MC.')
        self.play(FadeIn(note))
        self.play(quantity.animate.set_value(FIRM_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.equal')

        # ---- 2.d.past · Past 50 the next unit costs more than it brings in, and profit falls.
        self.remove(note)
        note = teaching('Then it will fall.')
        self.play(FadeIn(note))
        self.play(quantity.animate.set_value(60), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.past')

        # ---- 2.d · Back down to 50, with the answer.
        self.remove(note)
        note = teaching('How much should the firm choose to produce? At MC = MR!')
        self.play(FadeIn(note), quantity.animate.set_value(FIRM_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d')

        # ---- 2.e · MC = MR: the unit marks leave, a red dot where MC meets the price pulses, and q becomes q*.
        mc_dot = Dot(firm_ax.c2p(FIRM_P / 2, FIRM_P), radius=DOT_RADIUS, color=GUIDE).set_z_index(DOT_LAYER)
        mc_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), mc(quantity.get_value()))))
        q_star = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        q_star.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        for m in (mc_dot, q_star):
            m.update()
        for m in unit_marks:
            m.clear_updaters()
        self.remove(q_symbol)
        self.play(*[FadeOut(m) for m in unit_marks], run_time=0.5)
        show_unit_mc[0] = False
        self.play(firm.animate.shift(RIGHT * (FIRM_X_ALONE - FIRM_X_PANEL)), run_time=1.2, rate_func=smooth)
        for m in (atc_guide, atc_number):
            m.update()
        self.play(FadeIn(mc_dot), FadeIn(q_star), *dim_atc(1), FadeIn(atc_guide), FadeIn(atc_number))
        self.play(Indicate(mc_dot, color=FOCUS, scale_factor=1.6))
        self.pause('2.e')

        # ---- 3.a · Entry and exit: the subtitle changes; the firm pans back beside the market, which returns where it was,
        # then its marks and the price guide to the firm; the ATC guide and the firm's own price number leave.
        for m in (atc_guide, atc_number, atc_dot, price_number):
            m.update()
            m.clear_updaters()
        self.remove(context, note)
        context = subtitle(head, 'Entry and exit: long run dynamics.')
        note = teaching('The price comes from the market.')
        self.play(FadeOut(atc_guide), FadeOut(atc_number), FadeOut(atc_dot), FadeOut(price_number), run_time=0.5)
        self.remove(price_word)
        price_word = mr_word                                   # P = MR again, with the price back on the market's axis
        self.play(FadeIn(context), firm.animate.shift(RIGHT * (FIRM_X_PAIR - FIRM_X_ALONE)), FadeIn(market_picture), FadeIn(price_word),
                  firm_label.animate.set_opacity(1), run_time=1.6, rate_func=smooth)
        for m in market_marks:
            m.update()
        self.play(*[FadeIn(m) for m in market_marks], FadeIn(note))
        self.pause('3.a')

        # ---- 3.d.entry · Entry: supply shifts out in parallel, the price falls to 80, and the firm's line and box follow.
        self.remove(note)
        note = teaching('With profit, more firms enter, shifting the supply curve.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(80), quantity.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d.entry')

        # ---- 3.d.zero · Entry continues until the box closes onto the minimum of ATC: 63.25, zero profit.
        self.play(FadeIn(lowest_atc))                        # the grey dot at ATC's minimum, where the bars will close
        self.play(price.animate.set_value(LONG_RUN_P), quantity.animate.set_value(LONG_RUN_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d.zero')

        # ---- 3.d · Too far: at 50 the price is below ATC, the box flips above the price and turns red.
        LOSS_P = 50
        self.remove(note)
        note = teaching('A negative profit is a loss.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(LOSS_P), quantity.animate.set_value(LOSS_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d')

        # ---- 3.e.avc · Average variable cost joins the firm's graph; at q* = 25 the price is above it.
        avc_line = Line(firm_ax.c2p(0, 0), firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), color=AVC_COLOR, stroke_width=CURVE_WIDTH)
        avc_word = Tex('AVC', color=AVC_COLOR).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), RIGHT, buff=0.15)
        avc_dot = Dot(firm_ax.c2p(LOSS_P / 2, avc(LOSS_P / 2)), radius=DOT_RADIUS, color=AVC_COLOR).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('Firms earning a loss will exit the market if price is below their AVC.')
        self.play(FadeIn(avc_line), FadeIn(avc_word), FadeIn(avc_dot), FadeIn(note))
        self.pause('3.e.avc')

        # ---- 3.e.fc · The fixed cost on the graph: grey bars between AVC and ATC over 0 to q* make q(ATC - AVC) = FC, and
        # the red loss bars are their upper part.
        q_loss = LOSS_P / 2
        fixed_box = VGroup(*[Polygon(firm_ax.c2p(u, avc(q_loss)), firm_ax.c2p(u + 1, avc(q_loss)), firm_ax.c2p(u + 1, atc(q_loss)),
                                     firm_ax.c2p(u, atc(q_loss)), color=FC_COLOR, stroke_width=BAR_OUTLINE, fill_opacity=0.15)
                             for u in range(int(q_loss))]).set_z_index(-1)
        fixed_name = Tex('FC', color=FC_WORD).scale(AREA_WORD_SCALE).move_to(firm_ax.c2p(q_loss / 2, (avc(q_loss) + LOSS_P) / 2))
        self.remove(note)
        note = teaching('Is operating with a loss better than exiting and paying the fixed cost?')
        self.play(FadeIn(fixed_box), FadeIn(fixed_name), FadeIn(note))
        self.pause('3.e.fc')

        # ---- 3.e · The loss is the top of the fixed-cost box: smaller than the fixed cost, so the firm keeps operating.
        self.remove(note)
        note = teaching('Price is above AVC, so the loss is smaller than the fixed cost.')
        self.play(FadeIn(note), Indicate(profit_box, color=FOCUS, scale_factor=1), run_time=0.8)
        self.pause('3.e')

        # ---- 3.f.exit · The long run: below ATC firms exit, supply shifts back in, and the price rises to 63.25.
        self.remove(note)
        note = teaching('With a loss, firms exit, shifting the supply curve.')
        self.play(FadeOut(avc_line), FadeOut(avc_word), FadeOut(avc_dot), FadeOut(fixed_box), FadeOut(fixed_name), run_time=0.6)
        self.play(FadeIn(note))
        self.play(price.animate.set_value(LONG_RUN_P), quantity.animate.set_value(LONG_RUN_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.f.exit')

        # ---- 3.f · The long run: P = MC = ATC at its minimum, and profit is zero.
        self.remove(note)
        note = teaching('The only place with no change is where there is no profit.')
        self.play(FadeIn(note), Indicate(lowest_atc, color=FOCUS, scale_factor=1.6))
        self.pause('3.f')

        # ---- 4.a · Next time: the market and the readouts leave; the firm stays, and its flat line gives way to a sloped D.
        leaving = [price_word, q_drop, q_number, q_star, mc_dot, profit_box, profit_name, loss_name, *measure_marks, *market_marks,
                   market_supply, supply_word]
        for m in leaving + [price_line]:
            m.update()
            m.clear_updaters()
        self.remove(head, context, note)
        head = title('Next Time')
        note = teaching('What happens to marginal revenue when demand slopes down?')
        self.play(*[FadeOut(m) for m in leaving], FadeOut(market_ax), FadeOut(market_words), FadeOut(market_demand),
                  FadeOut(demand_word), FadeOut(lowest_atc), run_time=0.8)
        sloped = Line(firm_ax.c2p(0, 120), firm_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        sloped_word = Tex('D', color=DEMAND).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(60, 0), UR, buff=0.12)
        self.play(FadeIn(head), FadeOut(price_line), FadeIn(sloped), FadeIn(sloped_word), FadeOut(firm_label), FadeIn(note), run_time=1.6)
        self.pause('4.a')
