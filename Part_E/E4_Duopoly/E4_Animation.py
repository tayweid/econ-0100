# maniml E4_Animation.py EpisodeE4
# Storyboard: E4_Notes.md. All lesson choreography stays in construct().
# Duopoly, following the steps of Taylor's handwritten sheet (E5_Wrap_Up/E5_Handwritten_Three_Markets.pdf) on E2 and E3's market: demand
# P = 120 - Q, every firm MC = 2q. Monopoly MR = 120 - 2q, q* = 30, P* = 90 (E3's answer); duopoly
# MR_A = 120 - 2q_A - q_B, BR_A: q_A = 30 - q_B/4, Nash q_A* = q_B* = 24, Q = 48, P* = 72.
# Section 1.b to 1.l opens with the same game as a two-by-two matrix in D1's diamond layout: each firm makes
# Low = 20 (its share of the 40 a cartel would make; the cartel holds that derived it were cut 2026-11-18) or High = 24 (the Nash quantity), and the profits use the
# firm's TC = 900 + q^2: 300 each at Low, 252 each at High, 348 and 220 when only one goes High.
# One cost curve for the whole episode (2026-11-18): a fixed cost of 900 puts the lowest ATC at 60, at 30 units, so
# the monopoly's ATC, the long-run competitive price and every profit are whole numbers. E1 and E2 use 1,000 and
# E3 uses 1,200 this semester (at 1,200 the duopolists here would lose money); all move to 900 next time.
# (Until 2026-11-11 this used the sheet's own market, P = 200 - Q/2 and MC = 20 + q: 90 and 155, then 72 each and
# 128. That build is _archive/2026-11-11_consolidation/E4_Animation_handwritten_sheet_market.py.)
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


class EpisodeE4(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.4, -2.55
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE, DEFINITION_BOTTOM = 0.7443, 0.05
        QUANTITY_NUMBER_OFFSET, QUANTITY_LABEL_OFFSET = 0.32, 0.72
        QUANTITY_NUMBER_SCALE, QUANTITY_LABEL_SCALE = 0.64, 0.60
        PRICE_SCALE, CURVE_WORD_SCALE = 0.7, 0.7
        ROW_SCALE, ROW_GAP = 0.72, 0.26          # side-panel algebra rows, as C2's side solve
        EQUATION_SCALE = 0.6                     # standing equations in open graph space
        CURVE_WIDTH, GUIDE_WIDTH, DOT_RADIUS = 3, 2, 0.07
        # Firm theory palette (shared_E.md); firm A keeps Part D's row colour.
        MC_COLOR, MR_COLOR, ATC_COLOR = SUPPLY, PINK, TOTAL
        FIRM_A, FIRM_B = ROW_PLAYER, INK              # firm B in white: Part D's column teal is demand's colour here
        # Layout: the market graph on the left; right of it either the algebra panel (divider at 2.45, as C2)
        # or the best-response graph. Beside a definition the best-response graph moves left (D1's divider at 0.3).
        # The best-response graph's origin keeps its right-hand words (firm A, BR_B) inside the 0.6 safe margin.
        MARKET_ORIGIN = np.array([-5.4, BODY_MID - 2.15, 0])
        BR_ORIGIN = np.array([2.45, BODY_MID - 2.15, 0])
        BR_SHIFT = LEFT * 8.05
        PANEL_X, SOLVE_X = 5.2, 3.95
        ROLL_TIME, SWEEP_TIME = 2.4, 4.0
        # Taxonomy, as E3's: three seller rows with horizontal separators and no header.
        LABEL_W, CELL_W, CELL_H, TAXONOMY_X = 2.9, 3.3, 1.25, 0.4
        BOX_BUFF = 0.12                          # keep each selection clear of the row separators

        # The model (E2 and E3's market), as one-line functions.
        TOP_PRICE = 120                               # demand's start on the price axis, and its foot in units
        X_END, Y_TOP, BR_END = 120, 140, 140          # the market graph's axes; the best-response graph's axes
        demand = lambda Q: TOP_PRICE - Q
        mc = lambda q: 2 * q
        MC_END = 60                                   # MC is drawn to (60, 120)
        start_a = lambda q_b: TOP_PRICE - q_b         # where firm A's demand and MR_A meet the price axis
        best_a = lambda q_b: 30 - q_b / 4             # BR_A: MR_A = MC_A
        MONOPOLY_Q, NASH_Q = 30, 24                   # the boxed answers
        MARKET_Q = 2 * NASH_Q                         # 48
        LAST_Q_B = 120                                # the sweep's end: firm A's best response is 0
        MONOPOLY_P, MARKET_P = demand(MONOPOLY_Q), demand(MARKET_Q)   # 90 and 72, read from demand
        # The two-by-two game: Low is each firm's share of the cartel's 40 units, High is the Nash quantity.
        FIXED_COST = 900                              # lowest ATC 60, at 30 units
        LOW_Q, HIGH_Q = 20, NASH_Q
        profit = lambda q, other: int(demand(q + other) * q - (FIXED_COST + q ** 2))
        # D1's diamond matrix: square cells turned 45 degrees, text upright. Wider cells for three-digit profits.
        DIAMOND_ANGLE, CELL_SIDE, CHOICE_FILL_OPACITY = -PI / 4, 1.8, 0.12
        GAME_CENTER = DOWN * 0.55
        TABLE_RIGHT, TABLE_UP = (RIGHT + DOWN) / 2 ** 0.5, (RIGHT + UP) / 2 ** 0.5

        # The one object factory: the yellow bottom line.
        teaching = lambda text: Tex(text, color=DEFINITION).scale(DEFINITION_SCALE).set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)

        # ---- 0.a · The shared bumper with E4's thesis from the notes header.
        squares = bumper_raster(self)
        flicker(self, squares)
        episode = bumper_title(self, squares, 'E', 4)
        thesis = Tex(r'\textit{When sellers play games with each other}', color=CAPTION).scale(0.9)
        thesis.next_to(episode, DOWN, buff=0.55)
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))
        self.clear()

        # ---- 1.a.last · The three-row market-structures table, last episode's cell boxed.
        head = title('Monopoly')
        context = subtitle(head, 'One seller, many buyers.')
        grid_left = TAXONOMY_X - (LABEL_W + CELL_W) / 2
        grid_right = grid_left + LABEL_W + CELL_W
        grid_top = BODY_MID + 3 * CELL_H / 2
        column_x = grid_left + LABEL_W + CELL_W / 2
        row_y = [grid_top - CELL_H * (i + 0.5) for i in range(3)]
        # Only the two separators between seller rows; no top, bottom, or vertical rules. (Until 2026-11-18 this
        # was the two-column grid with Homogeneous and Differentiated headers and Monopolistic Competition.)
        taxonomy_rules = VGroup(
            *[Line([grid_left, grid_top - CELL_H * i, 0], [grid_right, grid_top - CELL_H * i, 0],
                   color=MUTED, stroke_width=2) for i in range(1, 3)])
        row_words = VGroup(Tex('Many Sellers', color=GUIDE), Tex('Few Sellers', color=GUIDE),
                           Tex('One Seller', color=GUIDE)).scale(0.75)
        for word, y in zip(row_words, row_y):
            word.move_to([grid_left + LABEL_W / 2, y, 0])
        perfect = Tex(r'Perfect\\Competition').scale(0.75).move_to([column_x, row_y[0], 0])
        oligopoly = Tex('Oligopoly').scale(0.75).move_to([column_x, row_y[1], 0])
        monopoly = Tex('Monopoly').scale(0.75).move_to([column_x, row_y[2], 0])
        taxonomy = VGroup(taxonomy_rules, row_words, perfect, oligopoly, monopoly)
        box = SurroundingRectangle(monopoly, buff=BOX_BUFF, color=NASH)
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a.last')

        # ---- 1.a · The box moves to the few-sellers cell: oligopoly, defined in Taylor's words.
        self.remove(head, context)
        head = title('Oligopoly')
        note = teaching('Oligopoly: a few sellers with some but not complete control of the price.')
        self.play(Transform(box, SurroundingRectangle(oligopoly, buff=BOX_BUFF, color=NASH)), FadeIn(head), run_time=0.8)
        self.play(FadeIn(note))
        self.pause('1.a')

        # ---- 1.b · The same market as a two-by-two game: two firms, each makes a low or a high quantity.
        self.play(FadeOut(taxonomy), FadeOut(box), FadeOut(head), FadeOut(note))
        # No demand or cost on screen yet: the profits are given here and derived from the market later.
        head = title('Duopoly')
        context = subtitle(head, 'Many buyers, two sellers, selling a homogeneous good, with no externalities.')
        choices = [LOW_Q, HIGH_Q]
        payoffs = [[VGroup(Tex(str(profit(a, b)), color=FIRM_A), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                           Tex(str(profit(b, a)), color=FIRM_B)).arrange(RIGHT, buff=0.3).scale(0.8)
                    for b in choices] for a in choices]
        entries = [cell for row in payoffs for cell in row]
        matrix = Table(
            payoffs,
            h_buff=CELL_SIDE - max(cell.width for cell in entries),
            v_buff=CELL_SIDE - max(cell.height for cell in entries),
            include_outer_lines=True,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).rotate(DIAMOND_ANGLE).move_to(GAME_CENTER)
        for cell in entries:
            cell.rotate(-DIAMOND_ANGLE, about_point=cell.get_center())
        choice_words = [rf'\textsf{{Low: {LOW_Q}}}', rf'\textsf{{High: {HIGH_Q}}}']
        row_labels = VGroup(*[Tex(word, color=CAPTION) for word in choice_words]).scale(0.7)
        col_labels = VGroup(*[Tex(word, color=CAPTION) for word in choice_words]).scale(0.7)
        for index in range(2):
            offset = (0.5 - index) * CELL_SIDE
            row_labels[index].move_to(GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[index].move_to(GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP + RIGHT * 0.3, aligned_edge=LEFT)
        firm_a_word = Tex('Firm A', color=FIRM_A).scale(0.8).move_to([-3.2, 1.75, 0])
        firm_b_word = Tex('Firm B', color=FIRM_B).scale(0.8).move_to([3.2, 1.75, 0])
        # Shades and best-response boxes, by the other firm's choice (0 = Low, 1 = High).
        col_shade = lambda k: Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE, stroke_width=0, fill_color=FIRM_B,
                                        fill_opacity=CHOICE_FILL_OPACITY).rotate(DIAMOND_ANGLE).move_to(
            GAME_CENTER + (k - 0.5) * CELL_SIDE * TABLE_RIGHT).set_z_index(-1)
        row_shade = lambda k: Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE, stroke_width=0, fill_color=FIRM_A,
                                        fill_opacity=CHOICE_FILL_OPACITY).rotate(DIAMOND_ANGLE).move_to(
            GAME_CENTER + (0.5 - k) * CELL_SIDE * TABLE_UP).set_z_index(-2)
        underline = lambda word, color: Underline(word, buff=0.1, stroke_color=color, stroke_width=3, stretch_factor=1)
        cell_box = lambda cell, color: Rectangle(width=CELL_SIDE - 0.15, height=CELL_SIDE - 0.15, color=color).rotate(
            DIAMOND_ANGLE).move_to(cell)
        note = teaching('How does a firm pick its quantity from these two options?')
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()), FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(firm_b_word), FadeIn(col_labels))
        self.play(FadeIn(firm_a_word), FadeIn(row_labels), FadeIn(note))
        self.pause('1.b')

        # ---- 1.c · One cell first: both Low. (The profits come from the market, 80 * 20 - (900 + 20^2) = 300,
        # which stays off screen until the firm's problem.)
        self.remove(note)
        note = teaching(rf'If both firms choose Low, each earns a profit of {profit(LOW_Q, LOW_Q)}.')
        self.play(FadeIn(note))
        self.play(FadeIn(payoffs[0][0]))
        self.pause('1.c')

        # ---- 1.d.a, 1.d.b, 1.d · The other three cells, one at a time, each with its own line.
        for hold, cell, text in [
                ('1.d.a', payoffs[1][0], rf'If only firm A chooses High, firm A earns {profit(HIGH_Q, LOW_Q)} and firm B earns {profit(LOW_Q, HIGH_Q)}.'),
                ('1.d.b', payoffs[0][1], rf'If only firm B chooses High, firm B earns {profit(HIGH_Q, LOW_Q)} and firm A earns {profit(LOW_Q, HIGH_Q)}.'),
                ('1.d', payoffs[1][1], rf'If both firms choose High, each earns a profit of {profit(HIGH_Q, HIGH_Q)}.')]:
            self.remove(note)
            note = teaching(text)
            self.play(FadeIn(cell), FadeIn(note))
            self.pause(hold)

        # ---- 1.e · Hold firm B at Low: the question.
        self.remove(note)
        note = teaching("If firm B chooses Low, what is firm A's best response?")
        b_choice, b_shade = underline(col_labels[0], FIRM_B), col_shade(0)
        self.play(FadeIn(b_choice), FadeIn(b_shade), FadeIn(note))
        self.pause('1.e')

        # ---- 1.f · The answer.
        responses = VGroup(SurroundingRectangle(payoffs[1][0][0], buff=0.08, color=FIRM_A))
        self.remove(note)
        note = teaching(rf"Firm A's best response to Low is High: ${profit(HIGH_Q, LOW_Q)} > {profit(LOW_Q, LOW_Q)}$.")
        self.play(FadeIn(responses[0]), FadeIn(note))
        self.pause('1.f')

        # ---- 1.g · Hold firm B at High: the question.
        self.remove(note)
        note = teaching("If firm B chooses High, what is firm A's best response?")
        self.play(Transform(b_choice, underline(col_labels[1], FIRM_B)), Transform(b_shade, col_shade(1)), FadeIn(note))
        self.pause('1.g')

        # ---- 1.h · The answer: High again.
        responses.add(SurroundingRectangle(payoffs[1][1][0], buff=0.08, color=FIRM_A))
        self.remove(note)
        note = teaching(rf"Firm A's best response to High is also High: ${profit(HIGH_Q, HIGH_Q)} > {profit(LOW_Q, HIGH_Q)}$.")
        self.play(FadeIn(responses[1]), FadeIn(note))
        self.pause('1.h')

        # ---- 1.i · Firm B, by symmetry: its best response is High in both of firm A's rows.
        responses.add(SurroundingRectangle(payoffs[0][1][2], buff=0.08, color=FIRM_B),
                      SurroundingRectangle(payoffs[1][1][2], buff=0.08, color=FIRM_B))
        self.remove(note)
        note = teaching('The firms are symmetric.')
        self.play(FadeOut(b_choice), FadeOut(b_shade), FadeIn(responses[2]), FadeIn(responses[3]), FadeIn(note))
        self.pause('1.i')

        # ---- 1.j · The Nash equilibrium: both High.
        nash_cell = cell_box(payoffs[1][1], NASH)
        self.remove(note)
        note = teaching(rf'Nash equilibrium: both choose High, and each earns {profit(HIGH_Q, HIGH_Q)}.')
        self.play(FadeIn(nash_cell), FadeIn(note))
        self.pause('1.j')

        # ---- 1.k · Both Low pays each firm more, and neither firm stays there.
        low_cell = cell_box(payoffs[0][0], EFFICIENT)
        self.remove(note)
        note = teaching(rf'Both Low pays each {profit(LOW_Q, LOW_Q)}, but each firm would rather switch to High.')
        self.play(FadeIn(low_cell), FadeIn(note))
        self.pause('1.k')

        # ---- 1.l · The bridge to the rest of the lesson: any quantity, not two.
        self.remove(note)
        note = teaching('What if each firm can choose any quantity?')
        self.play(FadeIn(note))
        self.pause('1.l')

        # ---- 2.a to 2.c · The firm's problem: the steps centred first, then beside two reviews on small graphs with
        # the episode's one cost curve. A competitive firm in the long run (30 units at a price of 60, ATC 60, profit
        # zero), then the monopoly (30 units at 90, ATC 60, profit 900): the same output and cost, a higher price.
        # E4's own palette for D, MR and MC so the hand-off to 3.a keeps its colours; ATC grey, profit green.
        REVIEW_MR, REVIEW_PROFIT, REVIEW_WORD, REVIEW_NUMBER = MR_COLOR, GREEN, 0.55, 0.55
        REVIEW_ATC = CAPTION                             # ATC in grey
        REVIEW_X_LENGTH, REVIEW_Y_LENGTH, REVIEW_Y = 4.0, 3.6, -2.0
        STEPS_LEFT, STEP_SCALE, RULE_SCALE, RULE_INDENT, DIM = 3.95, 0.62, 0.55, 0.3, 0.3

        def review_graph(origin_x, name, fixed_cost, atc_to):
            """One small firm graph on E3's axes (0 to 120 units, 0 to 140 dollars) with its label above."""
            g = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=REVIEW_X_LENGTH, y_length=REVIEW_Y_LENGTH)
            g.shift(np.array([origin_x, REVIEW_Y, 0]) - g.c2p(0, 0))
            cost = lambda q: q + fixed_cost / q
            atc_from = min(q for q in np.linspace(5, 40, 400) if cost(q) <= 118)
            return {
                'ax': g, 'atc': cost,
                'label': Tex(name, color=INK).scale(0.75).move_to([origin_x, 2.15, 0], aligned_edge=LEFT),
                'words': VGroup(Tex('P', color=INK).scale(0.65).next_to(g.c2p(0, Y_TOP), LEFT, buff=0.15),
                                Tex('q', color=INK).scale(0.65).next_to(g.c2p(X_END, 0), DOWN, buff=0.15)),
                'mc': Line(g.c2p(0, 0), g.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=CURVE_WIDTH),
                'mc_word': Tex('MC', color=MC_COLOR).scale(REVIEW_WORD).next_to(g.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.1),
                'atc_curve': polyline([g.c2p(q, cost(q)) for q in np.geomspace(atc_from, atc_to, 120)], REVIEW_ATC, CURVE_WIDTH),
                'atc_word': Tex('ATC', color=REVIEW_ATC).scale(REVIEW_WORD).next_to(g.c2p(atc_to, cost(atc_to)), RIGHT, buff=0.1),
            }

        def review_marks(graph, q, mr_at_q, price):
            """The answer marks for one firm: step 1's dot and drop, step 2's rise and price, step 3's ATC, step 4's area."""
            g, average = graph['ax'], graph['atc'](q)
            guide = lambda a, b, color=GUIDE: DashedLine(g.c2p(*a), g.c2p(*b), color=color, stroke_width=GUIDE_WIDTH).set_z_index(10)
            dot = lambda at, color=GUIDE: Dot(g.c2p(*at), radius=DOT_RADIUS, color=color).set_z_index(30)
            number = lambda text, color: Tex(text, color=color).scale(REVIEW_NUMBER)
            return {
                'quantity': VGroup(dot((q, mr_at_q)), guide((q, mr_at_q), (q, 0)),
                                   number(str(q), GUIDE).move_to(g.c2p(q, 0) + DOWN * 0.25)),
                'price': VGroup(guide((q, mr_at_q), (q, price)), dot((q, price)), guide((q, price), (0, price)),
                                number(str(price), GUIDE).next_to(g.c2p(0, price), LEFT, buff=0.12)),
                # Where ATC equals the price (the long-run competitive firm) the price's guide and number already
                # stand there, so the ATC mark is its dot alone.
                'average': VGroup(dot((q, average), REVIEW_ATC)) if abs(average - price) < 1e-6 else VGroup(
                    dot((q, average), REVIEW_ATC), guide((q, average), (0, average)),
                    number(f'{average:.0f}', REVIEW_ATC).next_to(g.c2p(0, average), LEFT, buff=0.12)),
                'profit': Polygon(g.c2p(0, average), g.c2p(q, average), g.c2p(q, price), g.c2p(0, price), stroke_width=0,
                                  fill_color=REVIEW_PROFIT, fill_opacity=AREA_OPACITY).set_z_index(-3),
                'profit_value': MathTex(rf'\pi^* = {int((price - average) * q):,}'.replace(',', '{,}'),
                                        color=REVIEW_PROFIT).scale(0.6).next_to(graph['label'], RIGHT, buff=0.2),
            }

        self.play(*[FadeOut(m) for m in [head, context, matrix.get_horizontal_lines(), matrix.get_vertical_lines(),
                                         *entries, row_labels, col_labels, firm_a_word, firm_b_word, responses,
                                         nash_cell, low_cell, note]])
        head = title("The Firm's Problem")
        context = subtitle(head, 'Every firm solves the same problem, in the same five steps.')
        steps_heading = Tex('Maximize Profit').scale(0.75).move_to([STEPS_LEFT, 2.15, 0], aligned_edge=LEFT)
        # A quiet list: the questions and the math in grey, with red for the firm's choices and green for profit only.
        objective = MathTex(r'\max_{q}\ \pi = \mathrm{TR} - \mathrm{TC}', color=CAPTION,
                            tex_to_color_map={'q': GUIDE, r'\pi': REVIEW_PROFIT}).scale(STEP_SCALE)
        objective.move_to([STEPS_LEFT, 1.55, 0], aligned_edge=LEFT)
        step_questions = ['1. How much to produce?', '2. What price sells it all?', '3. What is the average cost?',
                          '4. What is the profit?', '5. Stay or exit?']
        step_rules = [
            MathTex(r'\mathrm{MR} = \mathrm{MC} \rightarrow q^*', color=CAPTION, tex_to_color_map={'q^*': GUIDE}),
            MathTex(r'q^* \rightarrow \mathrm{D} \rightarrow P^*', color=CAPTION, tex_to_color_map={'q^*': GUIDE, 'P^*': GUIDE}),
            MathTex(r'q^* \rightarrow \mathrm{ATC} \rightarrow \mathrm{ATC}^*', color=CAPTION, tex_to_color_map={'q^*': GUIDE}),
            MathTex(r'\pi^* = (P^* - \mathrm{ATC}^*)\cdot q^*', color=CAPTION,
                    tex_to_color_map={r'\pi^*': REVIEW_PROFIT, 'P^*': GUIDE, 'q^*': GUIDE}),
            MathTex(r'\pi^* \geq 0\ \text{stay},\quad \pi^* < 0\ \text{exit}', color=CAPTION, tex_to_color_map={r'\pi^*': REVIEW_PROFIT})]
        steps = VGroup()
        for index, (question, rule) in enumerate(zip(step_questions, step_rules)):
            row = Tex(question, color=CAPTION).scale(STEP_SCALE).move_to([STEPS_LEFT, 0.9 - 0.8 * index, 0], aligned_edge=LEFT)
            rule.scale(RULE_SCALE).move_to([STEPS_LEFT + RULE_INDENT, 0.9 - 0.8 * index - 0.34, 0], aligned_edge=LEFT)
            steps.add(VGroup(row, rule))

        # The competitive firm takes the left slot and goes first; the monopoly takes the middle slot and goes second,
        # so the scene ends on the monopoly and hands it to the duopoly's market graph (3.a).
        TAKEN_PRICE, TAKER_Q = 60, 30                   # the long run: price at the lowest ATC, zero profit
        competitive_graph = review_graph(-6.9, 'Competitive Firm', FIXED_COST, 85)
        g = competitive_graph['ax']
        taken_line = Line(g.c2p(0, TAKEN_PRICE), g.c2p(X_END, TAKEN_PRICE), color=REVIEW_MR, stroke_width=CURVE_WIDTH)
        taken_word = Tex('MR', color=REVIEW_MR).scale(REVIEW_WORD).next_to(g.c2p(X_END - 8, TAKEN_PRICE), UP, buff=0.08)
        # The price taker's demand is the same flat line as its MR: teal dashes over the pink, named below the line.
        taken_demand = DashedLine(g.c2p(0, TAKEN_PRICE), g.c2p(X_END, TAKEN_PRICE), color=DEMAND, stroke_width=CURVE_WIDTH,
                                  dash_length=0.14, dashed_ratio=0.5).set_z_index(1)
        taken_demand_word = Tex('D', color=DEMAND).scale(REVIEW_WORD).next_to(g.c2p(X_END - 8, TAKEN_PRICE), DOWN, buff=0.1)
        competitive_marks = review_marks(competitive_graph, TAKER_Q, TAKEN_PRICE, TAKEN_PRICE)
        competitive_view = [g, competitive_graph['label'], competitive_graph['words'], taken_line, taken_word,
                            taken_demand, taken_demand_word,
                            competitive_graph['mc'], competitive_graph['mc_word']]
        competitive_parts = competitive_view + [competitive_graph['atc_curve'], competitive_graph['atc_word'],
                                                *competitive_marks.values()]

        monopoly_graph = review_graph(-1.6, 'Monopoly', FIXED_COST, 85)
        g = monopoly_graph['ax']
        monopoly_demand = Line(g.c2p(0, TOP_PRICE), g.c2p(X_END, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        monopoly_demand_word = Tex('D', color=DEMAND).scale(REVIEW_WORD).next_to(g.c2p(X_END, 0), UR, buff=0.08)
        monopoly_mr = Line(g.c2p(0, TOP_PRICE), g.c2p(TOP_PRICE / 2, 0), color=REVIEW_MR, stroke_width=CURVE_WIDTH)
        monopoly_mr_word = Tex('MR', color=REVIEW_MR).scale(REVIEW_WORD).next_to(g.c2p(TOP_PRICE / 2, 0), UR, buff=0.08)
        monopoly_marks = review_marks(monopoly_graph, MONOPOLY_Q, mc(MONOPOLY_Q), MONOPOLY_P)
        monopoly_view = [g, monopoly_graph['label'], monopoly_graph['words'], monopoly_demand, monopoly_demand_word,
                         monopoly_mr, monopoly_mr_word, monopoly_graph['mc'], monopoly_graph['mc_word']]

        # ---- 2.a.1 to 2.a · The steps alone first, centred and larger, one hold per step.
        STEPS_ZOOM = 1.1
        # Two layouts. Pair: the first graph and the steps centred, a divider between them. Full: the competitive
        # firm, the monopoly and the steps across the frame, a divider on each side of the middle graph.
        PAIR_GRAPH_SHIFT, PAIR_STEPS_SHIFT = RIGHT * 2.7, LEFT * 2.8
        PAIR_DIVIDER_X, GRAPH_DIVIDER_X, STEPS_DIVIDER_X = 0.65, -2.4, 3.45
        review_divider = lambda x: Line([x, 2.45, 0], [x, -2.75, 0], color=MUTED, stroke_width=1.5)
        steps_panel = VGroup(steps_heading, objective, steps)
        steps_home = np.array(steps_panel.get_center())      # a copy: the engine's centre is a live view
        steps_panel.scale(STEPS_ZOOM).move_to([0, BODY_MID - 0.4, 0])
        self.play(FadeIn(head), FadeIn(context), FadeIn(steps_heading), FadeIn(objective))
        for index, step in enumerate(steps):
            self.play(FadeIn(step), run_time=0.6)
            self.pause('2.a' if index == 4 else f'2.a.{index + 1}')

        # ---- 2.b.setup · The steps slide right of centre behind a divider; E2's competitive firm (a flat MR at the
        # market price, and MC) takes the left of the pair.
        for m in competitive_parts:
            m.shift(PAIR_GRAPH_SHIFT)
        steps_divider, graph_divider = review_divider(PAIR_DIVIDER_X), review_divider(GRAPH_DIVIDER_X)
        note = teaching('The competitive firm takes the market price.')
        self.play(steps_panel.animate.scale(1 / STEPS_ZOOM).move_to(steps_home + PAIR_STEPS_SHIFT), run_time=1.0)
        self.play(GrowFromEdge(steps_divider, UP), *[FadeIn(m) for m in competitive_view], FadeIn(note))
        self.pause('2.b.setup')

        # ---- 2.b.q, 2.b.p, 2.b.atc, 2.b.profit, 2.b · The competitive firm, one step per hold, the current step lit:
        # 30 units at a market price of 60, ATC 60, profit zero, and no entry.
        competitive_passes = [
            ('2.b.q', [competitive_marks['quantity']], rf'MR equals MC at {TAKER_Q} units.'),
            ('2.b.p', [competitive_marks['price']], rf'The price is the market price: {TAKEN_PRICE}.'),
            ('2.b.atc', [competitive_graph['atc_curve'], competitive_graph['atc_word'], competitive_marks['average']],
             rf'Average total cost at {TAKER_Q} units is {TAKEN_PRICE}.'),
            ('2.b.profit', [competitive_marks['profit'], competitive_marks['profit_value']],
             rf'Profit is $({TAKEN_PRICE} - {TAKEN_PRICE})\cdot {TAKER_Q} = 0$.'),
            ('2.b', [], 'With zero profit, the competitive firm stays and no firms enter.')]

        # ---- 2.c.setup, then 2.c.q, 2.c.p, 2.c.atc, 2.c.profit, 2.c · Back to the full width: the competitive firm
        # moves left, the steps and their divider right, and the monopoly arrives between them behind a second divider.
        # The same five steps from the top: 30 units, a price of 90, ATC 60, profit 900, and no entry.
        monopoly_passes = [
            ('2.c.q', [monopoly_marks['quantity']], rf'MR equals MC at {MONOPOLY_Q} units.'),
            ('2.c.p', [monopoly_marks['price']], rf'Demand gives the price at {MONOPOLY_Q} units: {MONOPOLY_P}.'),
            ('2.c.atc', [monopoly_graph['atc_curve'], monopoly_graph['atc_word'], monopoly_marks['average']],
             rf'Average total cost at {MONOPOLY_Q} units is 60.'),
            ('2.c.profit', [monopoly_marks['profit'], monopoly_marks['profit_value']],
             rf'Profit is $({MONOPOLY_P} - 60)\cdot {MONOPOLY_Q} = 900$.'),
            ('2.c', [], 'The monopoly stays, and no other firm can enter.')]

        for passes in (competitive_passes, monopoly_passes):
            if passes is monopoly_passes:
                self.remove(note)
                note = teaching('The monopoly faces the whole demand curve.')
                # Relight the steps first: an opacity animation on a row would override the panel's shift.
                self.play(*[step.animate.set_opacity(1) for step in steps], FadeIn(note), run_time=0.5)
                self.play(*[m.animate.shift(-PAIR_GRAPH_SHIFT) for m in competitive_parts],
                          steps_panel.animate.shift(-PAIR_STEPS_SHIFT),
                          steps_divider.animate.set_x(STEPS_DIVIDER_X), run_time=1.0)
                self.play(GrowFromEdge(graph_divider, UP), *[FadeIn(m) for m in monopoly_view])
                self.pause('2.c.setup')
            for index, (hold, marks, text) in enumerate(passes):
                self.remove(note)
                note = teaching(text)
                self.play(*[step.animate.set_opacity(1 if k == index else DIM) for k, step in enumerate(steps)], FadeIn(note))
                if marks:
                    self.play(*[FadeIn(m) for m in marks])
                self.pause(hold)

        card = VGroup(steps_heading, objective, steps, steps_divider, graph_divider, *competitive_parts, *monopoly_view,
                      monopoly_graph['atc_curve'], monopoly_graph['atc_word'], *monopoly_marks.values())
        self.remove(note)

        # ---- 3.a · The hand-off: the review's monopoly becomes the market graph with one thing marked, where MR
        # meets MC. (Until 2026-11-18 holds 3.a to 3.d built this step by step with algebra rows and the price.)
        ax = style_axes([0, X_END, 20], [0, Y_TOP, 20], x_length=5.6, y_length=4.6)
        ax.shift(MARKET_ORIGIN - ax.c2p(0, 0))
        price_word = Tex('P', color=INK).scale(0.8).next_to(ax.c2p(0, Y_TOP), LEFT, buff=0.23)
        price_unit = Tex(r'\textsf{\$/unit}', color=CAPTION).scale(0.55).next_to(ax.c2p(0, Y_TOP), RIGHT, buff=0.22)
        quantity_word = Tex('Q', color=INK).scale(0.8).next_to(ax.c2p(X_END, 0), DOWN, buff=0.23)
        quantity_unit = Tex(r'\textsf{units}', color=CAPTION).scale(0.55).next_to(ax.c2p(X_END, 0), DOWN, buff=0.73)
        START_BUFF = 0.26                             # intercept numbers stand clear of the red gap line (4.b)
        demand_start = Tex('$120$', color=DEMAND).scale(0.65).next_to(ax.c2p(0, TOP_PRICE), LEFT, buff=START_BUFF)
        demand_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(X_END, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        mc_line = Line(ax.c2p(0, 0), ax.c2p(MC_END, mc(MC_END)), color=MC_COLOR, stroke_width=CURVE_WIDTH)
        demand_word = Tex('D', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(X_END, 0), UR, buff=0.12)
        mc_word = Tex('MC', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(MC_END, mc(MC_END)), RIGHT, buff=0.15)
        # The side panel's row slots (5.a's algebra uses slots 2 to 5); the rows themselves are layout only.
        panel_rows = VGroup(*[MathTex(r'q_A = 30 - \tfrac{1}{4}q_B') for _ in range(7)])
        panel_rows.arrange(DOWN, buff=ROW_GAP).scale(ROW_SCALE)
        panel_rows[2:].shift(DOWN * 0.15)
        panel_rows.move_to([PANEL_X, BODY_MID, 0])
        slots = [row.get_center() for row in panel_rows]
        mr_line = Line(ax.c2p(0, TOP_PRICE), ax.c2p(TOP_PRICE / 2, 0), color=MR_COLOR, stroke_width=CURVE_WIDTH)
        mr_word = Tex('MR$_A$', color=INK).scale(CURVE_WORD_SCALE).next_to(ax.c2p(TOP_PRICE / 2, 0), UR, buff=0.12)
        mono_dot = Dot(ax.c2p(MONOPOLY_Q, mc(MONOPOLY_Q)), radius=DOT_RADIUS, color=GUIDE).set_z_index(30)
        mono_drop = DashedLine(ax.c2p(MONOPOLY_Q, mc(MONOPOLY_Q)), ax.c2p(MONOPOLY_Q, 0),
                               color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        mono_number = DecimalNumber(MONOPOLY_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        mono_number.move_to(ax.c2p(MONOPOLY_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET)
        mono_symbol = Tex('$q^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(ax.c2p(MONOPOLY_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
        note = teaching('The monopoly produces where MR meets MC: 30 units.')
        self.play(FadeOut(card), FadeOut(head), FadeOut(context))
        head = title('Monopoly')
        context = subtitle(head, 'All firms are similar.')
        self.play(*[FadeIn(m) for m in [
            head, context, ax, price_word, price_unit, quantity_word, quantity_unit, demand_start, demand_line, mc_line,
            demand_word, mc_word, mr_line, mr_word, mono_dot, mono_drop, mono_number, mono_symbol, note]])
        self.pause('3.a')

        # ---- 4.a · Duopoly, with the other firm selling zero. Right of a divider stands firm B's quantity axis,
        # which becomes the best-response graph's vertical axis at 5.b.trace; a red tick and "q_B = 0" mark its
        # quantity. Above, firm A's demand with Q bracketed over q_A + q_B, firm B's quantity as a live number.
        # One tracker, q_B, moves everything in sections 4 and 5.
        q_b = ValueTracker(0)
        firm_q = lambda: best_a(q_b.get_value())
        top = lambda: start_a(q_b.get_value())
        DIVIDER_X = 0.95
        divider = Line([DIVIDER_X, 1.55, 0], [DIVIDER_X, -3.0, 0], color=MUTED, stroke_width=1.5)   # the demand math sits above it
        br_ax = style_axes([0, BR_END, 20], [0, BR_END, 20], x_length=4.6, y_length=4.6)
        br_ax.shift(BR_ORIGIN - br_ax.c2p(0, 0))
        br_words = VGroup(
            Tex('$q_A$', color=INK).scale(0.8).next_to(br_ax.c2p(BR_END, 0), DOWN, buff=0.23),
            Tex(r'\textsf{firm A}', color=FIRM_A).scale(0.55).next_to(br_ax.c2p(BR_END, 0), DOWN, buff=0.73),
            Tex('$q_B$', color=INK).scale(0.8).next_to(br_ax.c2p(0, BR_END), LEFT, buff=0.23),
            Tex(r'\textsf{firm B}', color=FIRM_B).scale(0.55).next_to(br_ax.c2p(0, BR_END), RIGHT, buff=0.22))
        # Firm B's axis stands alone first: centred in the right half, drawn only to 100 units, named above, with a
        # grey 0 at its foot and no q_B at its top. axis_dx slides it right to make room for the algebra (5.a.rule), then
        # left to the best-response graph's axis (5.b.trace).
        AXIS_CENTER_X, AXIS_TOP_Q = 4.5, 100
        axis_dx = ValueTracker(AXIS_CENTER_X - BR_ORIGIN[0])
        axis_at = lambda q: br_ax.c2p(0, q) + RIGHT * axis_dx.get_value()
        q_b_axis = Line(UP, DOWN, color=MUTED, stroke_width=2)
        q_b_axis.add_updater(lambda m: m.put_start_and_end_on(axis_at(0), axis_at(AXIS_TOP_Q)))
        axis_label = Tex("Firm B's Quantity", color=FIRM_B).scale(0.6)
        axis_label.add_updater(lambda m: m.next_to(axis_at(AXIS_TOP_Q), UP, buff=0.22))
        axis_foot = Line(LEFT * 0.1, RIGHT * 0.1, color=MUTED, stroke_width=2)
        axis_foot.add_updater(lambda m: m.move_to(axis_at(0)))
        axis_zero = Tex('0', color=CAPTION).scale(PRICE_SCALE).set_z_index(-1)
        axis_zero.add_updater(lambda m: m.next_to(axis_at(0), LEFT, buff=0.24))   # under the red 0 until q_B rises
        axis_parts = [q_b_axis, axis_label, axis_foot, axis_zero]
        q_b_tick = Line(LEFT * 0.14, RIGHT * 0.14, color=GUIDE, stroke_width=4).set_z_index(12)
        q_b_tick.add_updater(lambda m: m.move_to(axis_at(q_b.get_value())))
        br_q_b_number = DecimalNumber(0, num_decimal_places=0, color=GUIDE).scale(PRICE_SCALE)
        br_q_b_number.add_updater(lambda m: m.set_value(round(q_b.get_value(), 4))
                                  .next_to(axis_at(q_b.get_value()), LEFT, buff=0.24))
        br_q_b_prefix = MathTex(r'q_B =', color=GUIDE).scale(PRICE_SCALE)
        br_q_b_prefix.add_updater(lambda m: m.next_to(br_q_b_number, LEFT, buff=0.12)
                                  .shift(UP * (br_q_b_number.get_y() - m[-1].get_y())))
        # Firm A's demand as one line of math: P = 120 - (q_A + n), n rolling with q_B, and Q bracketed above the sum.
        DEMAND_MATH_SCALE, DEMAND_MATH_Y = 0.85, 2.3
        math_left = MathTex(r'P = {{120}} - (', color=DEMAND).scale(DEMAND_MATH_SCALE)
        math_q_a = MathTex(r'q_A +', color=DEMAND).scale(DEMAND_MATH_SCALE)
        math_q_b = DecimalNumber(48, num_decimal_places=0, color=GUIDE).scale(DEMAND_MATH_SCALE)
        math_right = MathTex(')', color=DEMAND).scale(DEMAND_MATH_SCALE)
        VGroup(math_left, math_q_a, math_q_b, math_right).arrange(RIGHT, buff=0.1).move_to([DIVIDER_X, DEMAND_MATH_Y, 0])
        math_q_a.set_y(math_left.get_y())
        math_q_b.add_updater(lambda m: m.set_value(round(q_b.get_value(), 4)).next_to(math_q_a, RIGHT, buff=0.12)
                             .set_y(math_left.get_part_by_tex('120').get_y()))
        math_right.add_updater(lambda m: m.next_to(math_q_b, RIGHT, buff=0.06).set_y(math_left.get_y()))
        math_q_b_name = MathTex('q_B', color=GUIDE).scale(0.5)
        math_q_b_name.add_updater(lambda m: m.next_to(math_q_b, DOWN, buff=0.16))
        bracket_y = math_left.get_top()[1] + 0.16
        math_bracket = VMobject(color=CAPTION, stroke_width=2)
        math_bracket.add_updater(lambda m: m.set_points_as_corners([
            [math_q_a.get_left()[0], bracket_y - 0.1, 0], [math_q_a.get_left()[0], bracket_y, 0],
            [math_q_b.get_right()[0], bracket_y, 0], [math_q_b.get_right()[0], bracket_y - 0.1, 0]]))
        math_total = MathTex('Q', color=CAPTION).scale(0.7)
        math_total.add_updater(lambda m: m.move_to([(math_q_a.get_left()[0] + math_q_b.get_right()[0]) / 2, bracket_y + 0.26, 0]))
        demand_math = [math_left, math_q_a, math_q_b, math_right, math_q_b_name, math_bracket, math_total]
        # Labels near the origin collide at the end of the 5.b sweep: firm A's D and MR names fade there.
        name_fade = lambda: smooth(np.clip((96 - q_b.get_value()) / 12, 0, 1))
        ghost_fade = lambda: smooth(np.clip((q_b.get_value() - 5) / 10, 0, 1))
        ghost_demand = Line(ax.c2p(0, TOP_PRICE), ax.c2p(X_END, 0), color=MUTED, stroke_width=2).set_z_index(-1)
        ghost_word = Tex('D', color=CAPTION).scale(CURVE_WORD_SCALE).next_to(ax.c2p(X_END, 0), UR, buff=0.12)
        ghost_word.add_updater(lambda m: m.set_opacity(ghost_fade()))
        firm_demand = Line(ax.c2p(0, TOP_PRICE), ax.c2p(X_END, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        firm_demand.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, top()), ax.c2p(top() + 1e-4, 0)))
        firm_demand_word = Tex('D$_A$', color=INK).scale(CURVE_WORD_SCALE)
        firm_demand_word.add_updater(lambda m: m.next_to(ax.c2p(top(), 0), UR, buff=0.12).set_opacity(name_fade()))
        mr_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, top()), ax.c2p(top() / 2 + 1e-4, 0)))
        mr_word.add_updater(lambda m: m.next_to(ax.c2p(top() / 2, 0), UR, buff=0.12).set_opacity(name_fade()))
        mono_dot.add_updater(lambda m: m.move_to(ax.c2p(firm_q(), mc(firm_q()))))
        mono_drop.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(firm_q(), mc(firm_q())), ax.c2p(firm_q(), 0) + DOWN * 1e-4))
        mono_number.add_updater(lambda m: m.set_value(round(firm_q(), 4))
                                .move_to(ax.c2p(firm_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        firm_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        firm_symbol.add_updater(lambda m: m.move_to(ax.c2p(firm_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        firm_quantity_word = Tex('$q_A$', color=INK).scale(0.8).next_to(ax.c2p(X_END, 0), DOWN, buff=0.23)
        # Firm A's demand starts at 120 - q_B: its teal intercept rolls with q_B (and fades as it nears the origin
        # at the end of the 5.b sweep); the market's 120 turns grey with the ghost demand and shows once firm A's
        # intercept has moved off it. A red line just outside the price axis spans the gap between the two: q_B.
        firm_start = DecimalNumber(TOP_PRICE, num_decimal_places=0, color=DEMAND).scale(0.65)
        firm_start.add_updater(lambda m: m.set_value(round(top(), 4)).next_to(ax.c2p(0, top()), LEFT, buff=START_BUFF)
                               .set_opacity(name_fade()))
        gap_line = Line(UP, DOWN, color=GUIDE, stroke_width=4).set_z_index(12)
        gap_line.add_updater(lambda m: m.put_start_and_end_on(ax.c2p(0, TOP_PRICE) + LEFT * 0.1,
                                                              ax.c2p(0, min(top(), TOP_PRICE - 1e-3)) + LEFT * 0.1)
                             .set_opacity(1 if q_b.get_value() > 0.5 else 0))
        live = [ghost_word, firm_demand, firm_demand_word, mr_line, mr_word, mono_dot, mono_drop, mono_number,
                firm_symbol, firm_start, demand_start, gap_line, *axis_parts, q_b_tick, br_q_b_number, br_q_b_prefix,
                *demand_math]
        for m in live:
            m.update()
        demand_start.set_color(CAPTION)
        demand_start.add_updater(lambda m: m.set_opacity(ghost_fade()))
        demand_start.update()
        self.remove(head, note, demand_line, demand_word, quantity_word, mono_symbol)
        self.add(ghost_demand, firm_demand, firm_start, gap_line)
        head = title('Duopoly')
        note = teaching('Both of you are trying to sell into the same market.')
        self.play(FadeIn(head), FadeIn(firm_demand_word), FadeIn(firm_quantity_word), FadeIn(firm_symbol),
                  GrowFromEdge(divider, UP), *[FadeIn(m) for m in axis_parts])
        self.play(FadeIn(q_b_tick), FadeIn(br_q_b_number), FadeIn(br_q_b_prefix), *[FadeIn(m) for m in demand_math],
                  FadeIn(note))
        self.add(ghost_word)
        self.pause('4.a')

        # ---- 4.b.twenty_four · Firm B sells 24: the tick rises, the number in the math rolls, firm A's demand and MR
        # slide down, and the red gap line opens between 120 and 96. Its best quantity falls to 24.
        # (Named 4.b.seventy_two until 2026-11-12, for the sheet's market.)
        self.remove(note)
        self.play(q_b.animate.set_value(NASH_Q), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching('The demand for your good depends on how much the other firm sells.')
        self.play(FadeIn(note))
        self.pause('4.b.twenty_four')

        # ---- 4.b · Firm B sells 48: firm A's best quantity falls to 18.
        self.remove(note)
        self.play(q_b.animate.set_value(MARKET_Q), run_time=ROLL_TIME, rate_func=smooth)
        note = teaching("The more the other firm sells, the less buyers need what you're selling.")
        self.play(FadeIn(note))
        self.pause('4.b')

        # ---- 5.a.rule · Best responses: back to q_B = 0, then MR_A = MC_A for any q_B.
        self.remove(note)
        self.play(q_b.animate.set_value(0), run_time=1.6, rate_func=smooth)
        for m in live:
            m.update()                       # Digits must already match before a number fades.
        self.remove(head, context)
        head = title('Best Responses')
        context = subtitle(head, 'The strategies are quantities.')
        br_rows = VGroup(
            MathTex(r'{{\mathrm{MR}_A}} = {{\mathrm{MC}_A}}'),
            MathTex(r'{{120 - 2q_A - q_B}} = {{2q_A}}'),
            MathTex(r'120 - q_B = 4q_A', color=FIRM_A),
            MathTex(r'\mathrm{BR}_A:\ q_A = 30 - \tfrac{1}{4}q_B', color=FIRM_A))
        br_rows[0].get_part_by_tex(r'\mathrm{MR}_A').set_color(MR_COLOR)
        br_rows[0].get_part_by_tex(r'\mathrm{MC}_A').set_color(MC_COLOR)
        br_rows[1].get_part_by_tex('120 - 2q_A - q_B').set_color(MR_COLOR)
        br_rows[1].get_part_by_tex('2q_A').set_color(MC_COLOR)
        # Three columns for the algebra: the market graph, the math between two dividers, firm B's axis on the right.
        MATH_X, MATH_SCALE, MATH_DIVIDER_X, AXIS_RIGHT_X = 2.75, 0.62, 4.55, 6.3
        math_divider = Line([MATH_DIVIDER_X, 1.55, 0], [MATH_DIVIDER_X, -3.0, 0], color=MUTED, stroke_width=1.5)
        # The algebra is step 1 of the firm's problem, named as in the review's list.
        step_label = Tex(step_questions[0], color=CAPTION).scale(0.58).move_to([MATH_X, slots[1][1] + 0.1, 0])
        for row, slot in zip(br_rows, slots[2:6]):
            row.scale(MATH_SCALE).move_to([MATH_X, slot[1], 0])
        for m in demand_math:
            m.clear_updaters()
        gap_line.clear_updaters()            # invisible at q_B = 0, and it stays off through the 5.b sweep
        note = teaching('Decide our best response to every decision the other seller might make.')
        self.play(*[FadeOut(m) for m in demand_math], axis_dx.animate.set_value(AXIS_RIGHT_X - BR_ORIGIN[0]),
                  GrowFromEdge(math_divider, UP), FadeIn(head), FadeIn(context))
        # Each row is a run of glyphs, so a term is a slice of them: terms arrive from the graph's curves and then
        # move from one row to the next, the way the algebra is done by hand.
        term = lambda row, start, stop: VGroup(*br_rows[row].submobjects[start:stop])
        rule_mr, rule_equals, rule_mc = term(0, 0, 3), term(0, 3, 4), term(0, 4, 7)                    # MR_A = MC_A
        sub_120, sub_2q, sub_qb, sub_equals, sub_mc = (term(1, 0, 3), term(1, 3, 7), term(1, 7, 10),
                                                        term(1, 10, 11), term(1, 11, 14))                # 120 - 2q_A - q_B = 2q_A
        mid_120, mid_qb, mid_equals, mid_4q = term(2, 0, 3), term(2, 3, 6), term(2, 6, 7), term(2, 7, 10)   # 120 - q_B = 4q_A
        br_name, br_q, br_equals, br_30, br_quarter = (term(3, 0, 4), term(3, 4, 6), term(3, 6, 7),
                                                       term(3, 7, 9), term(3, 9, 15))                    # BR_A: q_A = 30 - (1/4)q_B

        def from_curve(part, curve):
            """A faint small copy of an expression on its curve, ready to travel to the expression's place in the row."""
            return part.copy().scale(0.6).move_to(curve.get_center()).set_opacity(0.15)

        def carry(*pairs):
            """Move copies of one row's terms into the next row's terms; two sources may share a target."""
            movers = [(source.copy(), target) for source, target in pairs]
            self.add(*[m for m, _ in movers])
            self.play(*[Transform(m, target) for m, target in movers], run_time=1.2)
            self.remove(*[m for m, _ in movers])
            self.add(*{id(target): target for _, target in movers}.values())

        # The two names come from the curves' own labels.
        self.play(FadeIn(step_label), FadeIn(note))
        self.play(TransformFromCopy(mr_word, rule_mr), TransformFromCopy(mc_word, rule_mc), FadeIn(rule_equals), run_time=1.2)
        self.pause('5.a.rule')

        # ---- 5.a.substitute · Each curve's equation travels from its line into the row.
        mr_source, mc_source = from_curve(VGroup(sub_120, sub_2q, sub_qb), mr_line), from_curve(sub_mc, mc_line)
        self.add(mr_source, mc_source)
        self.play(ReplacementTransform(mr_source, VGroup(sub_120, sub_2q, sub_qb)), ReplacementTransform(mc_source, sub_mc),
                  FadeIn(sub_equals), run_time=1.4)
        self.pause('5.a.substitute')

        # ---- 5.a.simplify · Move 2q_A across: it joins the 2q_A on the right as 4q_A; the rest comes straight down.
        carry((sub_120, mid_120), (sub_qb, mid_qb), (sub_equals, mid_equals), (sub_2q, mid_4q), (sub_mc, mid_4q))
        self.pause('5.a.simplify')

        # ---- 5.a.solved · Divide by 4 and swap sides: firm A's quantity, not yet named.
        carry((mid_4q, br_q), (mid_equals, br_equals), (mid_120, br_30), (mid_qb, br_quarter))
        self.pause('5.a.solved')

        # ---- 5.a.depends · A yellow box on q_B: the answer depends on the other firm's quantity.
        depends_box = SurroundingRectangle(term(3, 13, 15), buff=0.035, color=DEFINITION, stroke_width=2.5)   # clear of the fraction
        self.play(FadeIn(depends_box))
        self.pause('5.a.depends')

        # ---- 5.a · Only now the name: firm A's best response to any q_B.
        self.play(FadeIn(br_name), run_time=0.6)
        self.pause('5.a')

        # ---- 5.b.graph · The best-response graph replaces the algebra, empty at first.
        br_a_equation = MathTex(r'\mathrm{BR}_A:\ q_A = 30 - \tfrac{1}{4}q_B', color=FIRM_A).scale(EQUATION_SCALE)
        br_a_equation.move_to(br_ax.c2p(93, 129))
        br_point = Dot(br_ax.c2p(MONOPOLY_Q, 0), radius=0.08, color=FIRM_A).set_z_index(31)
        br_point.add_updater(lambda m: m.move_to(br_ax.c2p(firm_q(), q_b.get_value())))
        br_across = DashedLine(br_ax.c2p(0, 0), br_ax.c2p(MONOPOLY_Q, 0), color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        br_across.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(0, q_b.get_value()),
                                                               br_ax.c2p(firm_q(), q_b.get_value()) + RIGHT * 1e-4))
        br_down = DashedLine(br_ax.c2p(MONOPOLY_Q, 0), br_ax.c2p(MONOPOLY_Q, 0) + UP * 1e-4, color=GUIDE, stroke_width=GUIDE_WIDTH).set_z_index(10)
        br_down.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(firm_q(), 0),
                                                             br_ax.c2p(firm_q(), q_b.get_value()) + UP * 1e-4))
        br_trace = Line(br_ax.c2p(MONOPOLY_Q, 0), br_ax.c2p(MONOPOLY_Q, 0) + UP * 1e-4, color=FIRM_A, stroke_width=CURVE_WIDTH).set_z_index(5)
        br_trace.add_updater(lambda m: m.put_start_and_end_on(br_ax.c2p(MONOPOLY_Q, 0),
                                                              br_ax.c2p(firm_q(), q_b.get_value()) + UP * 1e-4))
        br_q_a_number = DecimalNumber(MONOPOLY_Q, num_decimal_places=0, color=GUIDE).scale(QUANTITY_NUMBER_SCALE)
        br_q_a_number.add_updater(lambda m: m.set_value(round(firm_q(), 4))
                                  .move_to(br_ax.c2p(firm_q(), 0) + DOWN * QUANTITY_NUMBER_OFFSET))
        br_q_a_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE)
        br_q_a_symbol.add_updater(lambda m: m.move_to(br_ax.c2p(firm_q(), 0) + DOWN * QUANTITY_LABEL_OFFSET))
        tracing = [br_point, br_across, br_down, br_trace, br_q_b_number, br_q_b_prefix, br_q_a_number, br_q_a_symbol]
        for m in tracing:
            m.update()
        self.remove(note)
        # Firm B's axis becomes the graph's vertical axis in place; its q_B readout is already on screen.
        # The math has done its job: it and both dividers leave, and firm B's axis slides into the space to become the
        # graph's vertical axis; its q_B readout rides along.
        self.play(FadeOut(br_rows[:3]), FadeOut(step_label), FadeOut(depends_box), FadeOut(divider), FadeOut(math_divider), axis_dx.animate.set_value(0),
                  ReplacementTransform(br_rows[3], br_a_equation), run_time=1.2)
        for m in [q_b_tick, *axis_parts]:
            m.clear_updaters()
        self.play(FadeOut(q_b_tick), *[FadeOut(m) for m in axis_parts], FadeIn(br_ax), FadeIn(br_words), run_time=0.8)
        self.pause('5.b.graph')

        # ---- 5.b.zero · The first point: firm B sells nothing, firm A's best response is the monopoly's 30.
        self.add(br_trace)
        self.play(FadeIn(br_point), FadeIn(br_across), FadeIn(br_down), FadeIn(br_q_a_number), FadeIn(br_q_a_symbol))
        self.pause('5.b.zero')

        # ---- 5.b.part · Part of the way: q_B rises to 48 and the point traces the line as far as (18, 48).
        self.play(q_b.animate.set_value(MARKET_Q), run_time=SWEEP_TIME * 0.5, rate_func=smooth)
        self.pause('5.b.part')

        # ---- 5.b.trace · The rest of the sweep, to q_B = 120, where firm A sells nothing.
        self.play(q_b.animate.set_value(LAST_Q_B), run_time=SWEEP_TIME * 0.7, rate_func=smooth)
        br_a_word = Tex('BR$_A$', color=INK).scale(CURVE_WORD_SCALE).next_to(br_ax.c2p(0, LAST_Q_B), RIGHT, buff=0.22)
        for m in tracing:
            m.update()
            m.clear_updaters()
        # The point and its readouts stay through the hold, so q_B = 120 explains the market graph's q_A* = 0.
        self.play(FadeIn(br_a_word))
        self.pause('5.b.trace')

        # ---- 5.b · The definition, in D1's words: the market graph and the tracing marks leave, the best-response
        # graph slides left.
        for m in live:
            m.update()
            m.clear_updaters()
        market_view = [ax, price_word, price_unit, firm_quantity_word, quantity_unit, demand_start, firm_start, gap_line,
                       ghost_demand, ghost_word, firm_demand, firm_demand_word, mc_line, mc_word, mr_line,
                       mr_word, mono_dot, mono_drop, mono_number, firm_symbol]
        br_graph = VGroup(br_ax, br_words, br_trace, br_a_word, br_a_equation)
        self.remove(*br_graph)
        self.add(br_graph)
        definition_divider = Line([0.3, 2.5, 0], [0.3, -3.0, 0], color=MUTED, stroke_width=1.5)
        best_response = VGroup(
            Tex('Best Response', color=DEFINITION),
            Tex('The strategy that gives a player', color=INK),
            Tex('the highest payoff, given the strategies', color=INK),
            Tex('chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        best_response.move_to([0.85, 1.65, 0], aligned_edge=UL)
        self.play(*[FadeOut(m) for m in market_view + tracing], run_time=0.6)
        self.play(br_graph.animate.shift(BR_SHIFT), GrowFromEdge(definition_divider, UP), run_time=1.0)
        self.play(FadeIn(best_response))
        self.pause('5.b')

        # ---- 5.c · Symmetry: firm B's best response is firm A's mirrored across the 45-degree line.
        diagonal = DashedLine(br_ax.c2p(0, 0), br_ax.c2p(87, 87), color=MUTED, stroke_width=1.5)
        symmetry_word = Tex(r'\textsf{symmetry}', color=CAPTION).scale(0.55).next_to(br_ax.c2p(87, 87), RIGHT, buff=0.1)
        br_b_line = Line(br_ax.c2p(0, MONOPOLY_Q), br_ax.c2p(LAST_Q_B, 0), color=CAPTION, stroke_width=CURVE_WIDTH).set_z_index(5)   # firm B's line and equation in grey
        br_b_word = Tex('BR$_B$', color=INK).scale(CURVE_WORD_SCALE).next_to(br_ax.c2p(LAST_Q_B, 0), UR, buff=0.12)
        br_b_equation = MathTex(r'\mathrm{BR}_B:\ q_B = 30 - \tfrac{1}{4}q_A', color=CAPTION).scale(EQUATION_SCALE)
        br_b_equation.next_to(br_a_equation, DOWN, buff=0.22, aligned_edge=LEFT)
        self.play(FadeIn(diagonal), FadeIn(symmetry_word))
        self.play(TransformFromCopy(br_trace, br_b_line), run_time=1.4)
        self.play(FadeIn(br_b_word), FadeIn(br_b_equation))
        self.pause('5.c')

        # ---- 6.a · Where the best responses cross: the Nash equilibrium, values withheld.
        self.remove(head)
        head = title('Nash Equilibrium')
        nash_definition = VGroup(
            Tex('Nash Equilibrium', color=DEFINITION),
            Tex('A set of strategies such that no player', color=INK),
            Tex('can improve their payoff by unilaterally', color=INK),
            Tex('changing strategy.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        nash_definition.next_to(best_response, DOWN, buff=0.6, aligned_edge=LEFT)   # under the best-response definition, as D1
        nash_dot = Dot(br_ax.c2p(NASH_Q, NASH_Q), radius=0.08, color=NASH).set_z_index(31)
        nash_guides = VGroup(
            DashedLine(br_ax.c2p(NASH_Q, NASH_Q), br_ax.c2p(NASH_Q, 0), color=GUIDE, stroke_width=GUIDE_WIDTH),
            DashedLine(br_ax.c2p(NASH_Q, NASH_Q), br_ax.c2p(0, NASH_Q), color=GUIDE, stroke_width=GUIDE_WIDTH)).set_z_index(10)
        nash_word = Tex('Nash Equilibrium', color=NASH).scale(0.6).next_to(nash_dot, UR, buff=0.12)
        # Values withheld: question marks hold the number slots until the algebra fills them.
        q_a_slot = br_ax.c2p(NASH_Q, 0) + DOWN * QUANTITY_NUMBER_OFFSET
        q_a_unknown = Tex('?', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(q_a_slot)
        q_a_symbol = Tex('$q_A^*$', color=GUIDE).scale(QUANTITY_LABEL_SCALE).move_to(br_ax.c2p(NASH_Q, 0) + DOWN * QUANTITY_LABEL_OFFSET)
        q_a_value = Tex('24', color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(q_a_slot)
        q_b_value_slot = Tex('24', color=GUIDE).scale(PRICE_SCALE).next_to(br_ax.c2p(0, NASH_Q), LEFT, buff=0.2)
        q_b_unknown = Tex('?', color=GUIDE).scale(PRICE_SCALE).move_to(q_b_value_slot)
        q_b_star = MathTex(r'q_B^* =', color=GUIDE).scale(PRICE_SCALE).next_to(q_b_value_slot, LEFT, buff=0.12)
        q_b_star.shift(UP * (q_b_value_slot.get_y() - q_b_star[-1].get_y()))
        self.play(FadeOut(diagonal), FadeOut(symmetry_word), FadeIn(head))
        self.play(FadeIn(nash_definition), GrowFromCenter(nash_dot), FadeIn(nash_word))
        self.play(Create(nash_guides[0]), Create(nash_guides[1]), FadeIn(q_a_unknown), FadeIn(q_a_symbol),
                  FadeIn(q_b_unknown), FadeIn(q_b_star))
        self.pause('6.a')

        # ---- 6.b.symmetric to 6.b · Solving for the crossing the way it is done by hand, right of the divider. The rows
        # line up on their equals signs; terms are slices of glyphs, and carry() moves copies from one row to the next.
        SOLVE_TOP, SOLVE_STEP = 1.8, 0.74
        part = lambda mob, start, stop: VGroup(*mob.submobjects[start:stop])

        def solve_row(tex, equals_at, index):
            """A row of the solve, its equals sign (glyph `equals_at`) on the column's centre line."""
            row = MathTex(tex).scale(ROW_SCALE)
            return row.shift(np.array([SOLVE_X, SOLVE_TOP - SOLVE_STEP * index, 0]) - row.submobjects[equals_at].get_center())

        symmetry_math = solve_row(r'q_A = q_B', 2, 0)                                  # q A = q B
        symmetry_word = Tex(r'\textsf{symmetric:}', color=CAPTION).scale(ROW_SCALE).next_to(symmetry_math, LEFT, buff=0.25)
        response = solve_row(r'q_A = 30 - \tfrac{1}{4}q_B', 2, 1)                      # q A = 3 0 - 1 bar 4 q B
        swapped = solve_row(r'q_A = 30 - \tfrac{1}{4}q_A', 2, 1)                       # the same row after the swap
        moved = solve_row(r'q_A + \tfrac{1}{4}q_A = 30', 8, 2)                         # q A + 1 bar 4 q A = 3 0
        collected = solve_row(r'\tfrac{5}{4}q_A = 30', 5, 3)                           # 5 bar 4 q A = 3 0
        solved = solve_row(r'q_A = 24', 2, 4)                                          # q A = 2 4
        other = solve_row(r'q_B = 24', 2, 5)                                           # q B = 2 4
        part(solved, 3, 5).set_color(GUIDE)
        part(other, 3, 5).set_color(GUIDE)
        solve_rows = VGroup(symmetry_word, symmetry_math, swapped, moved, collected, solved, other)

        # ---- 6.b.symmetric · The symmetry idea first: the firms are the same, so their quantities are.
        self.play(FadeOut(best_response), FadeOut(nash_definition))
        self.play(FadeIn(symmetry_word), FadeIn(symmetry_math))
        self.pause('6.b.symmetric')

        # ---- 6.b.equation · Firm A's best-response equation flies in from the graph.
        self.play(TransformFromCopy(part(br_a_equation, 4, len(br_a_equation.submobjects)), response), run_time=1.2)
        self.pause('6.b.equation')

        # ---- 6.b.swap · Symmetry in use: a q_A from the symmetry row takes q_B's place.
        self.play(FadeOut(part(response, 9, 11)), TransformFromCopy(part(symmetry_math, 0, 2), part(swapped, 9, 11)), run_time=1.2)
        self.remove(response)
        self.add(swapped)
        self.pause('6.b.swap')

        # ---- 6.b.collect · Move the quarter q_A to the left side, then add the two together.
        carry((part(swapped, 0, 2), part(moved, 0, 2)), (part(swapped, 5, 6), part(moved, 2, 3)),
              (part(swapped, 6, 9), part(moved, 3, 6)), (part(swapped, 9, 11), part(moved, 6, 8)),
              (part(swapped, 2, 3), part(moved, 8, 9)), (part(swapped, 3, 5), part(moved, 9, 11)))
        carry((part(moved, 0, 2), part(collected, 0, 3)), (part(moved, 2, 6), part(collected, 0, 3)),
              (part(moved, 6, 8), part(collected, 3, 5)), (part(moved, 8, 9), part(collected, 5, 6)),
              (part(moved, 9, 11), part(collected, 6, 8)))
        self.pause('6.b.collect')

        # ---- 6.b.solve · Divide by five quarters: firm A makes 24.
        carry((part(collected, 3, 5), part(solved, 0, 2)), (part(collected, 5, 6), part(solved, 2, 3)),
              (part(collected, 0, 3), part(solved, 3, 5)), (part(collected, 6, 8), part(solved, 3, 5)))
        self.pause('6.b.solve')

        # ---- 6.b.both · Symmetry again: firm B's quantity is the same 24.
        carry((part(symmetry_math, 3, 5), part(other, 0, 2)), (part(solved, 2, 3), part(other, 2, 3)),
              (part(solved, 3, 5), part(other, 3, 5)))
        self.pause('6.b.both')

        # ---- 6.b · The two 24s fly back onto the graph's axes, replacing the question marks.
        self.play(TransformFromCopy(part(solved, 3, 5), q_a_value), TransformFromCopy(part(other, 3, 5), q_b_value_slot),
                  FadeOut(q_a_unknown), FadeOut(q_b_unknown), run_time=1.4)
        self.pause('6.b')

        # ---- 6.c.monopoly, 6.c, 7.a · The closing comparison on the market graph: one seller, two, many. Three points
        # on demand, each with a plain name, its quantity on the quantity axis and its price on the price axis.
        # (Until 2026-11-18 this was a duopoly price hold, three cartel holds and a competition point with its
        # numbers written beside it.)
        self.remove(head, context)
        head = title('One, Two, Many Sellers')
        context = subtitle(head, 'All firms are similar.')
        # The two best-response equations leave first: the closing graph keeps only the lines and the crossing.
        self.play(FadeOut(br_a_equation), FadeOut(br_b_equation), FadeOut(solve_rows), FadeOut(definition_divider), run_time=0.6)
        br_graph.remove(br_a_equation)
        br_graph.add(br_b_line, br_b_word, nash_dot, nash_guides, nash_word, q_a_symbol, q_a_value,
                     q_b_value_slot, q_b_star)
        self.remove(*br_graph)
        self.add(br_graph)
        market_demand = Line(ax.c2p(0, TOP_PRICE), ax.c2p(X_END, 0), color=DEMAND, stroke_width=CURVE_WIDTH)
        demand_start.set_color(DEMAND)
        LOWEST_ATC = int(round(2 * FIXED_COST ** 0.5))    # 60, where MC = ATC at q = 30
        COMPETITIVE_Q = TOP_PRICE - LOWEST_ATC            # 60, read from demand

        def outcome(name, quantity, price):
            """One market outcome: its point on demand, guides to both axes, the two axis numbers, and its name."""
            return VGroup(
                DashedLine(ax.c2p(quantity, price), ax.c2p(quantity, 0), color=GUIDE, stroke_width=GUIDE_WIDTH),
                DashedLine(ax.c2p(quantity, price), ax.c2p(0, price), color=GUIDE, stroke_width=GUIDE_WIDTH),
                Dot(ax.c2p(quantity, price), radius=DOT_RADIUS, color=GUIDE),
                Tex(str(price), color=GUIDE).scale(PRICE_SCALE).next_to(ax.c2p(0, price), LEFT, buff=0.2),
                Tex(str(quantity), color=GUIDE).scale(QUANTITY_NUMBER_SCALE).move_to(ax.c2p(quantity, 0) + DOWN * QUANTITY_NUMBER_OFFSET),
                Tex(rf'\textsf{{{name}}}', color=INK).scale(0.6).next_to(ax.c2p(quantity, price), UR, buff=0.08)).set_z_index(3)

        outcomes = [
            ('6.c.monopoly', outcome('Monopoly', MONOPOLY_Q, MONOPOLY_P), 'One seller sells 30 units at a price of 90.'),
            ('6.c', outcome('Duopoly', MARKET_Q, MARKET_P), 'Two sellers sell 48 units at a price of 72.'),
            ('7.a', outcome('Competition', COMPETITIVE_Q, LOWEST_ATC), 'Many sellers sell 60 units at a price of 60.')]
        self.play(br_graph.animate.shift(-BR_SHIFT), FadeIn(head), FadeIn(context), run_time=1.2)
        self.play(FadeIn(ax), FadeIn(price_word), FadeIn(price_unit), FadeIn(quantity_word), FadeIn(quantity_unit),
                  FadeIn(demand_start), FadeIn(market_demand), FadeIn(demand_word))
        note = None
        for hold, marks, text in outcomes:
            if note is not None:
                self.remove(note)
            note = teaching(text)
            self.play(FadeIn(marks), FadeIn(note))
            self.pause(hold)
