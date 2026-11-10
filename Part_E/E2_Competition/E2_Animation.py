# maniml E2_Animation.py EpisodeE2
# Teaching notes and current hold references: E2_Notes.md. Earlier storyboards are archived. All choreography stays in construct().
# Competitive firms: E1's firm takes the market price, profit built from one unit (TR, TC, the box, q(P - ATC)),
# the next unit decides the quantity (MC = MR), then the market beside the firm: entry and exit until profit is zero.
# One firm throughout, E1's: TC = 1000 + q^2 (a $100 wage, a $1,000 fixed cost), MC = 2q, AVC = q, ATC = q + 1000/q,
# lowest at q = sqrt(1000) = 31.6 where ATC = MC = 63.25. Market (Q in thousands): D: P = 120 - 2Q/3, S: P = kQ,
# k = P*/Q* falls with entry and rises with exit. The firm's price is 100: q* = 50, ATC 70, TR 5,000, TC 3,500, profit 1,500.
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
        EXERCISE_SCALE, EXERCISE_HEADING_Y, EXERCISE_LEFT = 0.95, 2.95, 1.5
        EXERCISE_CONTEXT_SCALE, EXERCISE_CONTEXT_TOP = 0.84, 2.25
        EXERCISE_SETUP_GAP, EXERCISE_ITEM_INDENT = 0.65, 0.8
        EXERCISE_LINE_STEP, EXERCISE_MARKER_GAP = 0.6, 0.18
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Firm theory palette (shared_E.md). Profit is green, a loss red.
        MC_COLOR, ATC_COLOR, AVC_COLOR, FC_COLOR, FC_WORD = SUPPLY, TOTAL, PINK, MUTED, CAPTION
        REVENUE_COLOR, PROFIT_COLOR, LOSS_COLOR = DEMAND, GREEN, GUIDE    # profit green: orange is MC's (Taylor); the price line is GUIDE red
        # One baseline and price scale throughout. Section 2 pairs the firm with calculations, then the Next Unit panel.
        ORIGIN_Y = BODY_MID - 2.15
        GRAPH_HEIGHT, PRICE_MAX, CURVE_TOP = 4.0, 130, 120   # square 4.0 graphs; S and MC stop at 120 so their names clear the panel labels
        MARKET_WIDTH, MARKET_Q_MAX, MARKET_X_PAIR = 4.0, 120, -5.6
        FIRM_WIDTH, FIRM_Q_MAX, FIRM_X_PAIR, FIRM_X_ALONE, FIRM_X_PANEL = 4.0, 70, 1.0, -2.0, -3.4   # beside the market; alone; with the Next Unit panel
        CALC_SCALE, CALC_ROW_GAP, CALC_LINE_GAP = 0.68, 1.65, 0.5
        CALC_REVENUE_Y = BODY_MID + 2.0
        CALC_COST_Y, CALC_PROFIT_Y = CALC_REVENUE_Y - CALC_ROW_GAP, CALC_REVENUE_Y - 2 * CALC_ROW_GAP
        CHECKLIST_LEFT, CHECKLIST_DIVIDER_X = 1.1, 0.3   # the list centred right of a divider that clears the market's captions


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
        supply_slope = lambda p: p / market_q(p)                  # identical firms' MC sums horizontally: entry flattens S through the origin
        START_Q = 20

        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)

        # ---- 0.warmup · Retrieve E1's average and marginal costs before asking about revenue.
        warmup_label = Tex(r'Exercise E1 \textbar{} Warmup', color=DEFINITION).scale(EXERCISE_SCALE)
        warmup_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        warmup_context = Tex(
            r'\begin{minipage}{27em}\sffamily\raggedright '
            r'Producing 40 units costs \$2,600.\\'
            r'Producing 41 units costs \$2,681.\end{minipage}', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        warmup_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        # Single-spaced questions form an indented block, separated from the setup.
        warmup_question = VGroup(
            Tex('What is average total cost at 40 units?', color=INK),
            Tex('How much does the 41st unit add to cost?', color=INK),
            Tex(r'\begin{minipage}{27em}\raggedright What else do we need to know to tell whether\\'
                r'producing the 41st unit increases profit?\end{minipage}', color=INK),
        ).scale(EXERCISE_SCALE)
        for row, question in enumerate(warmup_question):
            question.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
                warmup_context.get_bottom()[1] - EXERCISE_SETUP_GAP - row * EXERCISE_LINE_STEP, direction=UP)
        warmup_markers = VGroup(*[Tex(letter, color=INK).scale(EXERCISE_SCALE) for letter in ('a)', 'b)', 'c)')])
        for marker, question in zip(warmup_markers, warmup_question):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP, aligned_edge=UP)
        warmup_text = VGroup(warmup_label, warmup_context, warmup_question, warmup_markers)
        self.play(FadeIn(warmup_text), run_time=0.4)
        self.pause('0.warmup')
        self.play(FadeOut(warmup_text), run_time=0.4)

        # ---- 0.opener · Hold the article headline for the spoken spinach story, then invite predictions.
        # Actual USDA Amber Waves article, June 1, 2007; see Assets/spinach-outbreak-article.source.json.
        opener_head = title('The Spinach Market')
        opener_setup = Tex(
            r'\begin{minipage}{40em}\sffamily\raggedright '
            r'In 2006, an E. coli outbreak was linked to spinach.\\'
            r'California introduced a food-safety program in 2007; growers reported higher costs.'
            r'\end{minipage}', color=CAPTION,
        ).scale(0.6)
        opener_setup.next_to(opener_head, DOWN, buff=0.4).align_to(opener_head, LEFT)
        opener_article = ImageMobject(os.path.join(os.path.dirname(__file__), 'Assets', 'spinach-outbreak-article.jpg'))
        opener_article.set_width(10.9).next_to(opener_setup, DOWN, buff=0.4).set_x(0)
        opener_credit = Tex(r'USDA Economic Research Service, \textit{Amber Waves}, June 1, 2007', color=CAPTION).scale(0.32)
        opener_credit.next_to(opener_article, DOWN, buff=0.12)
        self.play(FadeIn(opener_head), FadeIn(opener_setup), FadeIn(opener_article), FadeIn(opener_credit))
        self.pause('0.opener')
        opener_question = Tex(
            r'If every unit becomes more expensive to produce,\\'
            r'what happens to price, output, and the number of growers?', color=DEFINITION,
        ).scale(DEFINITION_SCALE)
        opener_question.next_to(opener_credit, DOWN, buff=0.65).set_x(0)
        self.play(FadeIn(opener_question), run_time=0.5)
        self.pause('0.opener.question')
        self.play(FadeOut(opener_head), FadeOut(opener_setup), FadeOut(opener_article), FadeOut(opener_credit), FadeOut(opener_question))

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

        # ---- 1.b.buyers · Build the user's sentence as each condition appears.
        head = title('Competitive Markets')
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
        # Supply pivots at the origin and passes through the market equilibrium; clip its far end to the graph bounds.
        supply_top_q = lambda p: min(MARKET_Q_MAX, CURVE_TOP / supply_slope(p))
        supply_ends = lambda p: (market_ax.c2p(0, 0), market_ax.c2p(supply_top_q(p), supply_slope(p) * supply_top_q(p)))
        market_supply = Line(*supply_ends(FIRM_P), color=SUPPLY, stroke_width=CURVE_WIDTH)
        supply_word = Tex('S', color=SUPPLY).scale(CURVE_WORD_SCALE).next_to(supply_ends(FIRM_P)[1], RIGHT, buff=0.12)
        checklist = VGroup()
        for i, item in enumerate(['Many buyers', 'Many sellers', 'Low barriers to entry', 'A homogeneous good', 'No externalities']):
            row = Tex(rf'{i + 1}.\enspace {item}', color=INK).scale(LIST_SCALE).align_to(ORIGIN, LEFT)
            row.shift(UP * (-i * LIST_STEP - row.family_members_with_points()[0].get_bottom()[1]))
            checklist.add(row)
        checklist.move_to([0, BODY_MID, 0]).align_to(np.array([CHECKLIST_LEFT, 0, 0]), LEFT)
        # The graph-beside-text divider (B2's), between the market and the list; it leaves with the list.
        checklist_divider = Line([CHECKLIST_DIVIDER_X, -3.0, 0], [CHECKLIST_DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        # Typeset the whole sentence once; reveal only the appended phrase at each step.
        market_phrases = ['Many buyers', ', many sellers', ', low barriers', ', selling a homogeneous good', ', with no externalities.']
        market_context = Tex(r'\mbox{' + narration(''.join(market_phrases)) + '}',
                             isolate=market_phrases, color=CAPTION).scale(SCALE_SUBTITLE)
        market_context.next_to(head, DOWN, buff=0.10).align_to(head, LEFT)
        buyer_context, seller_context, entry_context, good_context, externality_context = [
            market_context.get_part_by_tex(phrase) for phrase in market_phrases]
        self.play(FadeIn(head), FadeIn(market_ax), FadeIn(VGroup(*market_words[1:])), FadeIn(checklist_divider))
        self.play(FadeIn(checklist[0]), FadeIn(buyer_context), FadeIn(market_demand), FadeIn(demand_word))
        self.pause('1.b.buyers')

        # ---- 1.b.sellers · Many sellers, with supply.
        self.play(FadeIn(seller_context), FadeIn(checklist[1]), FadeIn(market_supply), FadeIn(supply_word))
        self.pause('1.b.sellers')

        # ---- 1.b · Low barriers follows many sellers.
        self.play(FadeIn(entry_context), FadeIn(checklist[2]))
        self.pause('1.b')

        # ---- 1.b.good · A homogeneous good.
        self.play(FadeIn(good_context), FadeIn(checklist[3]))
        self.pause('1.b.good')

        # ---- 1.b.externalities · No externalities.
        self.play(FadeIn(externality_context), FadeIn(checklist[4]))
        self.pause('1.b.externalities')

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
        # ATC is named where it enters at the upper left; its right end shares heights with MR and AVC.
        atc_word = Tex('ATC', color=ATC_COLOR).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(ATC_START, ATC_TOP), RIGHT, buff=0.15)
        lowest_atc = Dot(firm_ax.c2p(np.sqrt(FIXED), LONG_RUN_P), radius=0.085, color=MUTED).set_z_index(DOT_LAYER + 1)   # grey, not yellow (Taylor)
        firm = VGroup(firm_ax, firm_words, mc_line, mc_word, atc_curve, atc_word)      # the grey dot joins only at zero profit (3.d.zero)
        self.play(FadeOut(checklist), FadeOut(checklist_divider), run_time=0.5)
        self.play(FadeIn(firm), FadeIn(market_label))
        self.pause('1.c')

        # ---- 1.d.equilibrium · Mark the market equilibrium and pause before connecting it to the firm.
        # One tracker for the price, one for the firm's quantity.
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
        market_price = VGroup(Tex('$P^*=$', color=GUIDE), DecimalNumber(FIRM_P, num_decimal_places=0, color=GUIDE)).scale(0.65)
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
        # The connector is a red guide; the firm's demand is solid and shares market demand's color.
        # Its label waits until the marginal-revenue explanation at 1.e.mr.
        price_line = Line(firm_ax.c2p(0, FIRM_P), firm_ax.c2p(FIRM_Q_MAX, FIRM_P), color=DEMAND, stroke_width=CURVE_WIDTH)
        price_line.add_updater(lambda m: m.put_start_and_end_on(
            firm_ax.c2p(0, price.get_value()), firm_ax.c2p(FIRM_Q_MAX, price.get_value())))
        mr_word = Tex('MR', color=DEMAND).scale(CURVE_WORD_SCALE)
        mr_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        mr_only_word = Tex('MR', color=DEMAND).scale(CURVE_WORD_SCALE)       # section 2, where P reads on the firm's own axis
        mr_only_word.add_updater(lambda m: m.next_to(firm_ax.c2p(FIRM_Q_MAX, price.get_value()), RIGHT, buff=0.15))
        market_supply.add_updater(lambda m: m.put_start_and_end_on(*supply_ends(price.get_value())))
        supply_word.add_updater(lambda m: m.next_to(supply_ends(price.get_value())[1], RIGHT, buff=0.12))
        for m in market_marks + [price_line, mr_word, mr_only_word]:
            m.update()
        note = teaching('Competitive firms are what we call price takers.')
        self.play(FadeIn(market_dot))
        self.play(Create(market_across), Create(market_drop), FadeIn(market_price), FadeIn(market_quantity))
        self.pause('1.d.equilibrium')

        # ---- 1.d · Carry the market price across, then draw the firm's unlabeled demand line.
        self.play(Create(price_bridge), run_time=1.2)
        self.play(Create(price_line), FadeIn(note))
        self.pause('1.d')

        # ---- 1.e · Wiggle the firm's quantity: the price it gets does not move.
        # One persistent MR marker follows q and price; its blue rim stays visible around ATC when the points coincide.
        firm_dot = Dot(firm_ax.c2p(60, FIRM_P), radius=DOT_RADIUS * 1.3, color=REVENUE_COLOR).set_z_index(DOT_LAYER + 2)
        firm_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), price.get_value())))
        price_guide = DashedLine(firm_ax.c2p(0, FIRM_P), firm_ax.c2p(quantity.get_value(), FIRM_P), color=GUIDE,
                                 stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        price_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(0, price.get_value()), firm_ax.c2p(quantity.get_value(), price.get_value()),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        # Revenue reads at the price; include ATC only once the cost area is introduced.
        show_average_cost = [False]
        show_unit_mc = [False]                                   # True while the next unit's MC dot is on the graph (2.d)
        guide_top = lambda: max(price.get_value(), atc(max(quantity.get_value(), 1)) if show_average_cost[0] else 0,
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
        for m in (firm_dot, price_guide, q_drop, q_number, q_symbol):
            m.update()
        self.remove(note)
        note = teaching('This firm changing quantity ($q$) has no real effect on the price.')
        self.play(FadeIn(firm_dot), FadeIn(price_guide), FadeIn(q_drop), FadeIn(q_number), FadeIn(q_symbol), FadeIn(note))
        # One eased wiggle: 60 up to 68, down to 30, back to 60 (the axis ends at 70).
        wiggle = lambda a: 60 + np.sin(2 * np.pi * smooth(a)) * (8 if np.sin(2 * np.pi * smooth(a)) >= 0 else 30)
        self.play(UpdateFromAlphaFunc(quantity, lambda m, a: m.set_value(wiggle(a))), run_time=3.2)
        quantity.set_value(60)
        self.pause('1.e')

        # ---- 1.e.mr · Why the price is marginal revenue: the units sold are bars of revenue, each exactly P tall. The bars
        # fade in at q = 60; the quantity falls to 40 and rises back to 60, a bar leaving or arriving with each unit, each one
        # worth the price. Name the line MR.
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
        note = teaching('One more unit sells for the price: Marginal Revenue is the price.')
        self.play(FadeIn(mr_bars), FadeIn(note))
        self.play(quantity.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.play(quantity.animate.set_value(60), run_time=ROLL_TIME, rate_func=smooth)
        self.play(FadeIn(mr_word), run_time=0.5)
        price_word = mr_word
        self.pause('1.e.mr')

        # ---- 1.f.exercise · Q1a stays on screen while students work on the board.
        # An open prompt on the same graphite ground; cover the graph and its answer.
        # Keep the lecture objects in place so advancing resumes the existing sequence.
        exercise_ground = Rectangle(width=config.frame_width, height=config.frame_height,
                                    stroke_width=0, fill_color=BG, fill_opacity=1).set_z_index(100)
        exercise_label = Tex(r'Exercise E2 \textbar{} Q1a', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_context = Tex(r'\sffamily If the market price is 80, find:', color=CAPTION).scale(EXERCISE_CONTEXT_SCALE)
        exercise_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        # Q1a wording from Exercise/Exercise_E2.md; consistent left alignment and wrapping.
        exercise_question = VGroup(
            Tex(r'Total revenue from selling 20 units: $TR_{20}$', color=INK),
            Tex(r'Total revenue from selling 21 units: $TR_{21}$', color=INK),
            Tex('What is marginal revenue?', color=INK),
        ).scale(EXERCISE_SCALE)
        for row, question in enumerate(exercise_question):
            question.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
                exercise_context.get_bottom()[1] - EXERCISE_SETUP_GAP - row * EXERCISE_LINE_STEP, direction=UP)
        exercise_markers = VGroup(*[Tex(r'$\bullet$', color=INK).scale(EXERCISE_SCALE) for _ in exercise_question])
        for marker, question in zip(exercise_markers, exercise_question):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP)
        exercise_text = VGroup(exercise_label, exercise_context, exercise_question, exercise_markers).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_text), run_time=0.4)
        self.pause('1.f.exercise')
        self.play(FadeOut(exercise_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 2.a · The market leaves; the firm moves left to leave room for the revenue, cost, and profit calculations.
        for m in market_marks:
            m.update()
        self.remove(note)
        context = subtitle(head, 'Profit is Total Revenue (TR) minus Total Costs (TC).')
        price_number = VGroup(MathTex('P=', color=GUIDE), DecimalNumber(FIRM_P, num_decimal_places=0, color=GUIDE)).scale(READOUT_SCALE)
        price_number.arrange(RIGHT, buff=0.08).next_to(
            firm_ax.c2p(0, FIRM_P) + RIGHT * (FIRM_X_PANEL - FIRM_X_PAIR), LEFT, buff=0.2)
        market_price.save_state()
        market_picture = VGroup(market_ax, market_words, market_demand, demand_word, market_supply, supply_word)
        for bar in mr_bars:
            bar.clear_updaters()
        self.play(*[FadeOut(m) for m in market_marks if m is not market_price], FadeOut(mr_bars), run_time=0.5)
        # The Firm label goes dark while the firm is alone (it stays in the group, so it pans with it).
        self.play(FadeOut(market_picture), firm.animate.shift(RIGHT * (FIRM_X_PANEL - FIRM_X_PAIR)), firm_label.animate.set_opacity(0),
                  ReplacementTransform(market_price, price_number), run_time=1.6, rate_func=smooth)
        market_price.restore()                              # keep its original P* label ready for the market's return
        price_number.add_updater(lambda m: (m[1].set_value(price.get_value()), m.arrange(RIGHT, buff=0.08),
                                            m.next_to(firm_ax.c2p(0, price.get_value()), LEFT, buff=0.2)))
        price_number.update()
        note = teaching('Profit is everything left over after we’ve paid our costs.')
        mr_only_word.update()
        self.remove(price_word)
        price_word = mr_only_word
        self.add(price_word)
        self.play(FadeOut(market_context), FadeIn(context), FadeIn(note))
        self.pause('2.a')

        # ---- 2.b.revenue.unit · Move the selected quantity down to 1, then hold on its $100 revenue bar.
        self.play(quantity.animate.set_value(1), run_time=1.6, rate_func=smooth)
        # One aligned calculation column, separated from the graph and its full horizontal-axis label.
        CALC_DIVIDER_X = firm_words[4].get_right()[0] + 0.35
        CALC_CENTER_X = (CALC_DIVIDER_X + config.frame_width / 2 - 0.6) / 2
        CALC_LEFT = CALC_CENTER_X - 2.1
        CALC_EQUALS_X = CALC_LEFT + 0.9
        calculation_divider = Line([CALC_DIVIDER_X, -3.0, 0], [CALC_DIVIDER_X, 2.3, 0], color=MUTED, stroke_width=1.5)
        revenue_formula = VGroup(MathTex(r'\mathrm{TR}', color=REVENUE_COLOR), MathTex('=', color=INK),
                                 MathTex('P', color=GUIDE), MathTex(r'\times', color=INK), MathTex('q', color=GUIDE)
                                 ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_REVENUE_Y)
        revenue_formula.shift(RIGHT * (CALC_EQUALS_X - revenue_formula[1].get_x()))
        revenue_work = VGroup(MathTex('=', color=INK), DecimalNumber(FIRM_P, num_decimal_places=0, color=GUIDE),
                              MathTex(r'\times', color=INK), DecimalNumber(1, num_decimal_places=0, color=GUIDE)
                              ).scale(CALC_SCALE)
        revenue_work.add_updater(lambda m: (
            m[1].set_value(price.get_value()), m[3].set_value(float(np.round(quantity.get_value()))),
            m.arrange(RIGHT, buff=0.12).set_y(CALC_REVENUE_Y - CALC_LINE_GAP),
            m.shift(RIGHT * (CALC_EQUALS_X - m[0].get_x()))))
        revenue_result = VGroup(MathTex('=', color=INK), DecimalNumber(FIRM_P, num_decimal_places=0, color=REVENUE_COLOR)).scale(CALC_SCALE)
        revenue_result.add_updater(lambda m: (
            m[1].set_value(price.get_value() * float(np.round(quantity.get_value()))),
            m.arrange(RIGHT, buff=0.12).set_y(CALC_REVENUE_Y - 2 * CALC_LINE_GAP),
            m.shift(RIGHT * (CALC_EQUALS_X - m[0].get_x()))))
        revenue_work.update()
        revenue_result.update()
        revenue_q_symbol = revenue_formula[4].copy().move_to(revenue_work[3])
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
        self.play(*dim_curves(0.25))
        self.play(FadeIn(revenue_strips[0]), FadeIn(calculation_divider), FadeIn(revenue_formula), FadeIn(note), run_time=0.6)
        self.pause('2.b.revenue.unit')

        # ---- 2.b.revenue.price · Copy the price into the substitution line, leaving q symbolic.
        self.play(TransformFromCopy(revenue_formula[1], revenue_work[0]), TransformFromCopy(revenue_formula[2], revenue_work[1]),
                  TransformFromCopy(revenue_formula[3], revenue_work[2]), TransformFromCopy(revenue_formula[4], revenue_q_symbol))
        self.pause('2.b.revenue.price')

        # ---- 2.b.revenue.quantity · Substitute the first unit's quantity only after the price has settled.
        self.play(FadeOut(revenue_q_symbol), TransformFromCopy(revenue_formula[4], revenue_work[3]))
        self.add(revenue_work)
        self.pause('2.b.revenue.quantity')

        # ---- 2.b.revenue.result · Evaluate on its own third line; retain the formula and inputs.
        self.play(TransformFromCopy(revenue_work[0], revenue_result[0]), TransformFromCopy(VGroup(*revenue_work[1:]), revenue_result[1]))
        self.add(revenue_result)
        self.pause('2.b.revenue.result')

        # ---- 2.b.revenue · Add the remaining units as quantity grows to 20, then name their total revenue.
        self.remove(note)
        note = teaching('Total Revenue is the revenue for all units added together.')
        for u, strip in enumerate(revenue_strips):
            strip.add_updater(lambda m, u=u: m
                .set_stroke(opacity=float(np.clip(quantity.get_value() - u, 0, 1)))
                .set_fill(opacity=AREA_OPACITY * float(np.clip(quantity.get_value() - u, 0, 1))))
            strip.update()
        self.add(revenue_strips)
        self.play(quantity.animate.set_value(START_Q), FadeIn(note), run_time=2, rate_func=smooth)
        revenue_work.clear_updaters()
        revenue_result.clear_updaters()
        for strip in revenue_strips:
            strip.clear_updaters()
        self.play(FadeIn(revenue_word), run_time=0.4)
        self.pause('2.b.revenue')

        # ---- 2.b.cost.formula · Total cost is the average cost per unit multiplied by the number of units.
        cost_formula = VGroup(MathTex(r'\mathrm{TC}', color=ATC_COLOR), MathTex('=', color=INK),
                              MathTex(r'\mathrm{ATC}_q', color=ATC_COLOR), MathTex(r'\times', color=INK),
                              MathTex('q', color=GUIDE)).scale(CALC_SCALE).arrange(RIGHT, buff=0.12)
        cost_formula.shift(RIGHT * (CALC_EQUALS_X - cost_formula[1].get_x())).set_y(CALC_COST_Y)
        self.remove(note)
        note = teaching('Total Cost is Average Total Cost times quantity ($q$).')
        self.play(revenue_strips.animate.set_fill(opacity=0.08).set_stroke(opacity=0.25), FadeOut(revenue_word), *dim_atc(1),
                  FadeIn(cost_formula), FadeIn(note))
        self.pause('2.b.cost.formula')

        # ---- 2.b.atc.point · Plug q = 20 into ATC and locate the corresponding point on the curve.
        # Drawn from the point toward the axis (its start is the point, so Create runs leftward).
        show_average_cost[0] = True
        atc_guide = DashedLine(firm_ax.c2p(START_Q, atc(START_Q)), firm_ax.c2p(0, atc(START_Q)), color=GUIDE,
                               stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        atc_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), atc(quantity.get_value())), firm_ax.c2p(0, atc(quantity.get_value())),
            color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)))
        atc_dot = Dot(firm_ax.c2p(START_Q, atc(START_Q)), radius=DOT_RADIUS, color=ATC_COLOR).set_z_index(DOT_LAYER + 3)
        atc_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), atc(quantity.get_value()))))
        atc_number = VGroup(MathTex(r'\mathrm{ATC}_q=', color=ATC_COLOR),
                            DecimalNumber(atc(START_Q), num_decimal_places=0, color=ATC_COLOR)).scale(READOUT_SCALE)
        atc_number.add_updater(lambda m: (m[1].set_value(atc(quantity.get_value())), m.arrange(RIGHT, buff=0.08),
                                          m.next_to(firm_ax.c2p(0, atc(quantity.get_value())), LEFT, buff=0.2)))
        atc_number.update()
        cost_word = Tex('TC', color=INK).scale(AREA_WORD_SCALE).move_to(firm_ax.c2p(START_Q / 2, atc(START_Q) / 2))   # white over its shaded region
        cost_work = VGroup(MathTex('=', color=INK), MathTex(r'\mathrm{ATC}_{20}', color=ATC_COLOR),
                           MathTex(r'\times', color=INK), MathTex('20', color=GUIDE)
                           ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_COST_Y - CALC_LINE_GAP)
        cost_work.shift(RIGHT * (CALC_EQUALS_X - cost_work[0].get_x()))
        self.remove(note)
        note = teaching('Plug the quantity ($q$) into Average Total Cost.')
        self.play(Indicate(q_number, color=GUIDE), FadeIn(atc_dot), FadeIn(note),
                  *[TransformFromCopy(cost_formula[i + 1], cost_work[i]) for i in range(4)])
        self.add(cost_work)
        self.pause('2.b.atc.point')

        # ---- 2.b.atc.read · Read ATC_q = 70 on the axis before substituting it into the formula.
        cost_product = VGroup(MathTex('=', color=INK), MathTex('70', color=ATC_COLOR), MathTex(r'\times', color=INK),
                              MathTex('20', color=GUIDE)).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).move_to(cost_work, aligned_edge=LEFT)
        self.remove(note)
        note = teaching('On average, each unit costs \\$70.')
        self.play(Create(atc_guide), run_time=1.0)
        self.play(FadeIn(atc_number), FadeIn(note), run_time=0.5)
        self.pause('2.b.atc.read')

        # ---- 2.b.atc · Substitute the cost per unit after the graph readout has been discussed.
        self.play(Transform(cost_work, cost_product), run_time=0.6)
        self.pause('2.b.atc')

        # ---- 2.b.cost · Multiply the $70 height by the 20-unit width to fill the $1,400 total-cost area.
        cost_result = VGroup(MathTex('=', color=INK), MathTex('1{,}400', color=ATC_COLOR)
                             ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_COST_Y - 2 * CALC_LINE_GAP)
        cost_result.shift(RIGHT * (CALC_EQUALS_X - cost_result[0].get_x()))
        self.remove(note)
        note = teaching('Multiply the cost per unit by the number of units.')
        self.play(LaggedStart(*[FadeIn(strip) for strip in cost_strips], lag_ratio=0.1), FadeIn(note), run_time=2)
        self.play(FadeIn(cost_word), TransformFromCopy(cost_work[0], cost_result[0]),
                  TransformFromCopy(VGroup(*cost_work[1:]), cost_result[1]), run_time=0.8)
        self.add(cost_result)
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
        profit_formula = VGroup(Tex('Profit', color=PROFIT_COLOR), MathTex('=', color=INK),
                                MathTex(r'\mathrm{TR}', color=REVENUE_COLOR), MathTex('-', color=INK), MathTex(r'\mathrm{TC}', color=ATC_COLOR)
                                ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_PROFIT_Y)
        profit_formula.shift(RIGHT * (CALC_EQUALS_X - profit_formula[1].get_x()))
        profit_work = VGroup(MathTex('=', color=INK), MathTex('2{,}000', color=REVENUE_COLOR), MathTex('-', color=INK),
                             MathTex('1{,}400', color=ATC_COLOR)
                             ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_PROFIT_Y - CALC_LINE_GAP)
        profit_work.shift(RIGHT * (CALC_EQUALS_X - profit_work[0].get_x()))
        profit_result = VGroup(MathTex('=', color=INK), MathTex('600', color=PROFIT_COLOR)
                               ).scale(CALC_SCALE).arrange(RIGHT, buff=0.12).set_y(CALC_PROFIT_Y - 2 * CALC_LINE_GAP)
        profit_result.shift(RIGHT * (CALC_EQUALS_X - profit_result[0].get_x()))
        self.remove(note)
        note = teaching('Usually we find profit as the difference between TR and TC on the graph.')
        self.play(FadeOut(revenue_strips), FadeOut(cost_strips), FadeOut(cost_word), *dim_curves(0.25), FadeIn(profit_box), FadeIn(note),
                  run_time=1.2)
        self.play(FadeIn(profit_name), FadeIn(profit_formula))
        self.add(loss_name)
        self.pause('2.c.area')

        # ---- 2.c.revenue · Substitute both already-known totals together.
        self.play(*[TransformFromCopy(profit_formula[i + 1], profit_work[i]) for i in range(4)])
        self.add(profit_work)
        self.pause('2.c.revenue')

        # ---- 2.c.profit · The subtraction becomes the result on a new line.
        self.play(TransformFromCopy(profit_work[0], profit_result[0]), TransformFromCopy(VGroup(*profit_work[1:]), profit_result[1]))
        self.add(profit_result)
        self.pause('2.c.profit')

        # ---- 2.c.formula · B2's measurement, laid just outside the axes as E1 lays its interval marks: a yellow line left of the price
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
        profit_area_formula = VGroup(MathTex('=', color=INK),
                                     MathTex('q', color=GUIDE), MathTex('(', color=INK), MathTex('P', color=GUIDE),
                                     MathTex('-', color=INK), MathTex(r'\mathrm{ATC}_q', color=ATC_COLOR), MathTex(')', color=INK)
                                     ).scale(CALC_SCALE).arrange(RIGHT, buff=0.06).set_y(CALC_PROFIT_Y - CALC_LINE_GAP)
        profit_area_formula.shift(RIGHT * (CALC_EQUALS_X - profit_area_formula[0].get_x()))
        profit_area_work = VGroup(MathTex('=', color=INK), MathTex('20', color=GUIDE), MathTex('(', color=INK),
                                  MathTex('100', color=GUIDE), MathTex('-', color=INK), MathTex('70', color=ATC_COLOR),
                                  MathTex(')', color=INK)
                                  ).scale(CALC_SCALE).arrange(RIGHT, buff=0.06).set_y(CALC_PROFIT_Y - 2 * CALC_LINE_GAP)
        profit_area_work.shift(RIGHT * (CALC_EQUALS_X - profit_area_work[0].get_x()))
        profit_area_result = profit_result.copy().shift(DOWN * CALC_LINE_GAP)
        self.remove(note)
        note = teaching(r'Profit is mathematically equivalent to $q(P - \mathrm{ATC})$.')
        self.play(Create(height_mark), FadeOut(profit_work), FadeOut(profit_result))
        self.play(Create(base_mark), TransformFromCopy(VGroup(*profit_formula[1:]), profit_area_formula), FadeIn(note))
        self.pause('2.c.formula')

        # ---- 2.c.quantity · Substitute all three already-known inputs together.
        self.play(*[TransformFromCopy(profit_area_formula[i], profit_area_work[i]) for i in range(7)])
        self.add(profit_area_work)
        self.pause('2.c.quantity')

        # ---- 2.c · Evaluate the product on its own result line.
        self.play(TransformFromCopy(profit_area_work[0], profit_area_result[0]),
                  TransformFromCopy(VGroup(*profit_area_work[1:]), profit_area_result[1]))
        self.add(profit_area_result)
        calculations = VGroup(revenue_formula, revenue_work, revenue_result, cost_formula, cost_work, cost_result,
                              profit_formula, profit_area_formula, profit_area_work, profit_area_result)
        self.pause('2.c')

        # ---- 2.d.question · Clear the calculations and center the graph for the output decision.
        self.remove(note)
        note = teaching('Is there a quantity that gives the firm a higher profit?')
        self.play(FadeOut(calculations), FadeOut(calculation_divider), FadeIn(note),
                  firm.animate.shift(RIGHT * (FIRM_X_ALONE - FIRM_X_PANEL)), run_time=1.2, rate_func=smooth)
        self.pause('2.d.question')

        # ---- 2.d.margin · Turn the larger decision into a one-unit comparison.
        self.remove(note)
        note = teaching('Should the firm increase or decrease quantity by 1?')
        self.play(FadeIn(note))
        self.pause('2.d.margin')

        # ---- 2.d.mr · Name the value of another unit before turning to its cost.
        mr_value_note = Tex(r'\sffamily Value of one more unit', color=CAPTION).scale(0.55)
        mr_value_note.next_to(mr_only_word, RIGHT, buff=1.1).shift(UP * 0.55)
        mr_value_arrow = Arrow(mr_value_note.get_left() + LEFT * 0.12, mr_only_word.get_right() + RIGHT * 0.12,
                               buff=0, color=CAPTION, thickness=2)
        self.play(FadeIn(mr_value_note), GrowArrow(mr_value_arrow))
        self.pause('2.d.mr')

        # ---- 2.d.cost.question · Find the marginal cost at the current quantity before comparing it with revenue. Beside the
        # graph, E1 4.d's close-up: two columns at the same price scale, MR and MC, so the gap between them is what the
        # unit adds to profit. The MC column climbs as q rolls and meets MR at 50.
        unit_mc = lambda: mc(quantity.get_value())            # the next unit's cost, read as MC at q (so MC = MR reads 100 = 100)
        unit_cost_dot = Dot(radius=0.065, color=MC_COLOR).set_z_index(DOT_LAYER + 3)
        unit_cost_dot.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), unit_mc())))
        # The close-up columns: faint fill, a solid value edge, the value beside the edge, the name under the base (E1 4.d).
        MR_X, MC_X, UNIT_COLUMN_W, UNIT_COLUMN_FILL = 3.5, 4.3, 0.5, 0.4
        price_y = lambda p: firm_ax.c2p(0, p)[1]
        column_corners = lambda x, top: [[x - UNIT_COLUMN_W / 2, ORIGIN_Y, 0], [x + UNIT_COLUMN_W / 2, ORIGIN_Y, 0],
                                         [x + UNIT_COLUMN_W / 2, top, 0], [x - UNIT_COLUMN_W / 2, top, 0], [x - UNIT_COLUMN_W / 2, ORIGIN_Y, 0]]
        unit_base = Line([MR_X - 0.45, ORIGIN_Y, 0], [MC_X + 0.45, ORIGIN_Y, 0], color=MUTED)
        unit_divider = calculation_divider
        unit_title = Tex('Next Unit', color=INK).scale(0.8).move_to([(MR_X + MC_X) / 2, ORIGIN_Y + GRAPH_HEIGHT + 0.6, 0])
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
        unit_marks = [unit_cost_dot, mr_column, mc_column, mr_edge, mc_edge, mr_value, mc_value, mr_guide, mc_guide,
                      gain_cap, gain_value]
        for m in unit_marks:
            m.update()
        # First the next unit's marginal cost read off the curve: a red dashed guide from the dot to the axis, MC_q = 40 there.
        mc_axis_guide = DashedLine(firm_ax.c2p(START_Q, mc(START_Q)), firm_ax.c2p(0, mc(START_Q)), color=GUIDE,
                                   stroke_width=GUIDE_WIDTH).set_z_index(GUIDE_LAYER)
        # Keep MC's guide and readout visible; fade the price readout as they approach it, gone within $4.
        near_price = lambda: float(np.clip((abs(unit_mc() - price.get_value()) - 4) / 6, 0, 1))
        price_visibility = lambda m: m.set_opacity(near_price())
        price_number.add_updater(price_visibility)
        mc_axis_guide.add_updater(lambda m: m.become(DashedLine(
            firm_ax.c2p(quantity.get_value(), unit_mc()), firm_ax.c2p(0, unit_mc()), color=GUIDE, stroke_width=GUIDE_WIDTH)
            .set_z_index(GUIDE_LAYER)))
        mc_number = VGroup(MathTex(r'\mathrm{MC}_q=', color=MC_COLOR), DecimalNumber(unit_mc(), num_decimal_places=0, color=MC_COLOR)).scale(READOUT_SCALE)
        mc_number.add_updater(lambda m: (m[1].set_value(round(unit_mc(), 4)), m.arrange(RIGHT, buff=0.08),
                                         m.next_to(firm_ax.c2p(0, unit_mc()), LEFT, buff=0.2)))
        mc_number.update()
        unit_marks += [mc_axis_guide, mc_number]
        self.remove(note)
        note = teaching('What does the next unit cost to make?')
        # Only the next unit's two heights matter here: ATC's guide and readout leave and its curve recedes (its point stays
        # on the curve); MC returns.
        self.play(*[m.animate.set_opacity(0.5) for m in measure_marks], *dim_mc(1), *dim_atc(0.25), FadeOut(atc_guide),
                  FadeOut(atc_number), FadeIn(note))
        self.pause('2.d.cost.question')

        # ---- 2.d.mc.point · Locate the point on MC first, without an axis guide or value yet.
        show_unit_mc[0] = True
        self.play(FadeIn(unit_cost_dot), run_time=0.6)
        self.pause('2.d.mc.point')

        # ---- 2.d.mc · Read leftward from the point to the axis, then show its marginal-cost value.
        self.play(Create(mc_axis_guide), run_time=1.0, rate_func=linear)
        self.play(FadeIn(mc_number), run_time=0.5)
        mc_cost_note = Tex(r'\sffamily Cost of one more unit', color=CAPTION).scale(0.55)
        mc_cost_note.next_to(mc_number, LEFT, buff=0.9).shift(DOWN * 0.55)
        mc_cost_arrow = Arrow(mc_cost_note.get_right() + RIGHT * 0.12, mc_number.get_left() + LEFT * 0.12,
                              buff=0, color=CAPTION, thickness=2)
        self.play(FadeIn(mc_cost_note), GrowArrow(mc_cost_arrow))
        self.pause('2.d.mc')

        # ---- 2.d.unit · Carry both callouts to the matching column heights as the Next Unit comparison appears.
        self.remove(note)
        note = teaching('Should the firm increase or decrease quantity by 1?')
        mr_note_target = Tex(r'\sffamily \shortstack[l]{Value of one\\more unit}', color=CAPTION).scale(0.55)
        mr_note_target.move_to([2.0, price_y(CURVE_TOP) + 0.4, 0], aligned_edge=LEFT)
        mc_note_target = mc_cost_note.copy().move_to([5.05, price_y(unit_mc()) + 0.55, 0], aligned_edge=LEFT)
        mr_arrow_target = Arrow(mr_note_target.get_bottom() + DOWN * 0.12,
                                [MR_X - UNIT_COLUMN_W / 2 - 0.12, price_y(price.get_value()), 0],
                                buff=0, color=CAPTION, thickness=2)
        mc_arrow_target = Arrow(mc_note_target.get_left() + LEFT * 0.12,
                                [MC_X + UNIT_COLUMN_W / 2 + 0.12, price_y(unit_mc()), 0],
                                buff=0, color=CAPTION, thickness=2)
        self.play(firm.animate.shift(RIGHT * (FIRM_X_PANEL - FIRM_X_ALONE)), FadeIn(unit_divider),
                  FadeIn(unit_title), FadeIn(unit_base), FadeIn(unit_names),
                  FadeIn(mr_column), FadeIn(mc_column), FadeIn(mr_edge), FadeIn(mc_edge), FadeIn(mr_value), FadeIn(mc_value),
                  Transform(mr_value_note, mr_note_target), Transform(mc_cost_note, mc_note_target),
                  Transform(mr_value_arrow, mr_arrow_target), Transform(mc_cost_arrow, mc_arrow_target),
                  FadeIn(note), run_time=1.2, rate_func=smooth)
        mc_cost_note.add_updater(lambda m: m.move_to([5.05, price_y(unit_mc()) + 0.55, 0], aligned_edge=LEFT))
        mr_value_arrow.add_updater(lambda m: m.become(Arrow(mr_value_note.get_bottom() + DOWN * 0.12,
            [MR_X - UNIT_COLUMN_W / 2 - 0.12, price_y(price.get_value()), 0], buff=0, color=CAPTION, thickness=2)))
        mc_cost_arrow.add_updater(lambda m: m.become(Arrow(mc_cost_note.get_left() + LEFT * 0.12,
            [MC_X + UNIT_COLUMN_W / 2 + 0.12, price_y(unit_mc()), 0], buff=0, color=CAPTION, thickness=2)))
        for m in (mr_guide, mc_guide):
            m.update()
        self.play(Create(mr_guide), Create(mc_guide), run_time=0.8)
        self.play(FadeIn(gain_cap), FadeIn(gain_value), run_time=0.6)
        unit_marks += [unit_base, unit_names, unit_divider, unit_title, mr_value_note, mr_value_arrow, mc_cost_note, mc_cost_arrow]
        self.pause('2.d.unit')

        # ---- 2.d.ten · More units: the unit rides up MC, the MC column climbs toward MR, and the bars and numbers roll. The stop
        # is 35, just past 30, where the MC and ATC points would sit on top of each other.
        self.play(quantity.animate.set_value(START_Q + 15), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.ten')

        # ---- 2.d.equal · Keep going to 50: MC's readout replaces P, and its orange dot sits over the larger blue MR dot.
        self.remove(note)
        note = teaching('Profit will go up by adding another unit until MR = MC.')
        self.play(FadeIn(note))
        self.play(quantity.animate.set_value(FIRM_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.equal')

        # ---- 2.d.past · Past 50 the next unit costs more than it brings in, and profit falls.
        self.remove(note)
        note = teaching('Beyond MC = MR, adding another unit lowers profit.')
        self.play(FadeIn(note))
        self.play(quantity.animate.set_value(60), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d.past')

        # ---- 2.d · Back down to 50, with the answer.
        self.remove(note)
        note = teaching('How much should the firm choose to produce? At MC = MR!')
        self.play(FadeIn(note), quantity.animate.set_value(FIRM_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('2.d')

        # ---- 2.e · MC = MR: the unit marks leave, the MR-colored intersection dot pulses, and q becomes q*.
        q_star = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        q_star.add_updater(lambda m: m.move_to(firm_ax.c2p(quantity.get_value(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        q_star.update()
        for m in unit_marks:
            m.clear_updaters()
        price_number.remove_updater(price_visibility)
        self.remove(q_symbol)
        self.play(*[FadeOut(m) for m in unit_marks], price_number.animate.set_opacity(1), run_time=0.5)
        show_unit_mc[0] = False
        self.play(firm.animate.shift(RIGHT * (FIRM_X_ALONE - FIRM_X_PANEL)), run_time=1.2, rate_func=smooth)
        for m in (atc_guide, atc_number):
            m.update()
        self.play(FadeIn(q_star), *dim_atc(1), FadeIn(atc_guide), FadeIn(atc_number))
        self.play(Indicate(firm_dot, color=REVENUE_COLOR, scale_factor=1.6))
        self.pause('2.e')

        # ---- 2.f.exercise.b · Retrieve the output decision after MC = MR, with work on the board.
        # The graph stays covered through both questions; no solution is revealed on screen.
        exercise_b_label = Tex(r'Exercise E2 \textbar{} Q1b', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_b_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_b_context = Tex(r'\sffamily Use $MC = 2q$ and $P = 80$.', color=CAPTION).scale(EXERCISE_CONTEXT_SCALE)
        exercise_b_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        exercise_b_question = VGroup(
            Tex(r'What quantity maximizes the firm\textquotesingle s profit?', color=INK),
            Tex('Why not 30 or 50 units?', color=INK),
        ).scale(EXERCISE_SCALE)
        for row, question in enumerate(exercise_b_question):
            question.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
                exercise_b_context.get_bottom()[1] - EXERCISE_SETUP_GAP - row * EXERCISE_LINE_STEP, direction=UP)
        exercise_b_markers = VGroup(*[Tex(r'$\bullet$', color=INK).scale(EXERCISE_SCALE) for _ in exercise_b_question])
        for marker, question in zip(exercise_b_markers, exercise_b_question):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP)
        exercise_b_text = VGroup(exercise_b_label, exercise_b_context, exercise_b_question, exercise_b_markers).set_z_index(101)
        self.play(FadeIn(exercise_ground), run_time=0.4)
        self.play(FadeIn(exercise_b_text), run_time=0.4)
        self.pause('2.f.exercise.b')

        # ---- 2.f.exercise.c · Keep the chosen quantity on the board; supply ATC for profit.
        exercise_c_label = Tex(r'Exercise E2 \textbar{} Q1c', color=DEFINITION).scale(EXERCISE_SCALE)
        exercise_c_label.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_HEADING_Y)
        exercise_c_context = Tex(
            r'\sffamily Hint: $ATC$ at the profit-maximizing quantity is 65.', color=CAPTION,
        ).scale(EXERCISE_CONTEXT_SCALE)
        exercise_c_context.to_edge(LEFT, buff=EXERCISE_LEFT).set_y(EXERCISE_CONTEXT_TOP, direction=UP)
        exercise_c_question = VGroup(
            Tex(r'At $P = 80$, calculate the firm\textquotesingle s maximal profit.', color=INK),
        ).scale(EXERCISE_SCALE)
        for row, question in enumerate(exercise_c_question):
            question.to_edge(LEFT, buff=EXERCISE_LEFT + EXERCISE_ITEM_INDENT).set_y(
                exercise_c_context.get_bottom()[1] - EXERCISE_SETUP_GAP - row * EXERCISE_LINE_STEP, direction=UP)
        exercise_c_markers = VGroup(*[Tex(r'$\bullet$', color=INK).scale(EXERCISE_SCALE) for _ in exercise_c_question])
        for marker, question in zip(exercise_c_markers, exercise_c_question):
            marker.next_to(question, LEFT, buff=EXERCISE_MARKER_GAP)
        exercise_c_text = VGroup(exercise_c_label, exercise_c_context, exercise_c_question, exercise_c_markers).set_z_index(101)
        self.play(FadeOut(exercise_b_text), run_time=0.3)
        self.play(FadeIn(exercise_c_text), run_time=0.4)
        self.pause('2.f.exercise.c')
        self.play(FadeOut(exercise_c_text), run_time=0.3)
        self.play(FadeOut(exercise_ground), run_time=0.4)

        # ---- 3.a · Entry and exit: the subtitle changes; the firm pans back beside the market, which returns where it was,
        # then its marks and the price guide to the firm; the ATC dot keeps tracking quantity as the axis readouts leave.
        for m in (atc_guide, atc_number, price_number):
            m.update()
            m.clear_updaters()
        self.remove(context, note)
        context = subtitle(head, 'Entry and exit: long run dynamics.')
        note = teaching('The price comes from the market.')
        self.play(FadeOut(atc_guide), FadeOut(atc_number), FadeOut(price_number), run_time=0.5)
        self.remove(price_word)
        price_word = mr_word                                   # MR stays the label when the market returns.
        self.play(FadeIn(context), firm.animate.shift(RIGHT * (FIRM_X_PAIR - FIRM_X_ALONE)), FadeIn(market_picture), FadeIn(price_word),
                  firm_label.animate.set_opacity(1), run_time=1.6, rate_func=smooth)
        for m in market_marks:
            m.update()
        self.play(*[FadeIn(m) for m in market_marks], FadeIn(note))
        self.pause('3.a')

        # ---- 3.d.entry · Entry: supply pivots outward around the origin, the price falls to 80, and the firm's line and box follow.
        self.remove(note)
        note = teaching('With profit, more firms enter, pivoting the supply curve outward.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(80), quantity.animate.set_value(40), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d.entry')

        # ---- 3.d.zero · Entry continues until the box closes onto the minimum of ATC: 63.25, zero profit.
        self.remove(note)
        note = teaching("Firms continue to enter until price is low enough that there's no more profit.")
        self.play(FadeIn(note), FadeIn(lowest_atc))           # the grey dot at ATC's minimum, where the bars will close
        self.play(price.animate.set_value(LONG_RUN_P), quantity.animate.set_value(LONG_RUN_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d.zero')

        # ---- 3.d · Too far: at 50 the price is below ATC, the box flips above the price and turns red.
        LOSS_P = 50
        self.remove(note)
        note = teaching('When price is low firms make a negative profit, called a loss.')
        self.play(FadeIn(note))
        self.play(price.animate.set_value(LOSS_P), quantity.animate.set_value(LOSS_P / 2), run_time=ROLL_TIME, rate_func=smooth)
        self.pause('3.d')

        # ---- 3.e.avc · Average variable cost joins the firm's graph; at q* = 25 the price is above it.
        avc_line = Line(firm_ax.c2p(0, 0), firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), color=AVC_COLOR, stroke_width=CURVE_WIDTH)
        avc_word = Tex('AVC', color=AVC_COLOR).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(FIRM_Q_MAX, avc(FIRM_Q_MAX)), RIGHT, buff=0.15)
        avc_dot = Dot(firm_ax.c2p(LOSS_P / 2, avc(LOSS_P / 2)), radius=DOT_RADIUS, color=AVC_COLOR).set_z_index(DOT_LAYER)
        self.remove(note)
        note = teaching('Shut down this period if price is below AVC at the best positive output.')
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
        note = teaching('Is operating with a loss better than shutting down and paying the fixed cost?')
        self.play(FadeIn(fixed_box), FadeIn(fixed_name), FadeIn(note))
        self.pause('3.e.fc')

        # ---- 3.e · The loss is the top of the fixed-cost box: smaller than the fixed cost, so the firm keeps operating.
        self.remove(note)
        note = teaching('Price is above AVC, so the loss is smaller than the fixed cost.')
        self.play(FadeIn(note), Indicate(profit_box, color=FOCUS, scale_factor=1), run_time=0.8)
        self.pause('3.e')

        # ---- 3.f.exit · The long run: below ATC firms exit, supply pivots inward around the origin, and the price rises to 63.25.
        self.remove(note)
        note = teaching('With a loss, firms exit, pivoting the supply curve inward.')
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
        leaving = [price_word, q_drop, q_number, q_star, profit_box, profit_name, loss_name, *measure_marks, *market_marks,
                   market_supply, supply_word]
        for m in leaving + [price_line, price_guide, firm_dot]:
            m.update()
            m.clear_updaters()
        self.remove(head, context, note)
        head = title('Next Time')
        note = teaching('What happens to Marginal Revenue when demand slopes down?')
        self.play(*[FadeOut(m) for m in leaving], FadeOut(market_ax), FadeOut(market_words), FadeOut(market_demand),
                  FadeOut(demand_word), FadeOut(lowest_atc), run_time=0.8)
        sloped = Line(firm_ax.c2p(0, 120), firm_ax.c2p(60, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        sloped_word = Tex('D', color=DEMAND).scale(CURVE_WORD_SCALE).next_to(firm_ax.c2p(60, 0), UR, buff=0.12)
        self.play(FadeIn(head), FadeOut(price_line), FadeOut(price_guide), FadeOut(firm_dot), FadeIn(sloped), FadeIn(sloped_word), FadeOut(firm_label),
                  FadeIn(note), run_time=1.6)
        self.pause('4.a')
