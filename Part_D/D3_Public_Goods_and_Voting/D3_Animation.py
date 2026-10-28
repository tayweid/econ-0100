# maniml D3_Animation.py EpisodeD3
# Public goods and voting: the bumper and a warmup from Exercise D3, the NPR game,
# three contributors, a memorial to Dobby, the Exercise D3 card, and a brief look at the
# limits of voting.
# Layout and rhythm mirror D2_Animation.py: the arithmetic on the left, a graph on the
# right that keeps every outcome, a thin divider, then the graph shrinks left while the
# matrix fades in right and the numbers move into their cells. Narration: D3_Notes.md.
# /// script
# requires-python = ">=3.11"
# dependencies = ["seaborn==0.13.2"]
# ///

from manim import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *

config.frame_rate = 15


class EpisodeD3(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.5, -2.8
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        TEACHING_SCALE, TEACHING_BOTTOM = 0.7443, 0.05
        RULE_POS = np.array([-3.7, 1.35, 0])            # the rule and its braces, top of the left panel
        ROWS_LEFT, ROW_Y = -6.7, (-0.35, -0.95, -1.55)  # worked lines under the rule, one per player
        EQ_LEFT = ROWS_LEFT + 2.05                      # the expression starts here, after the "Player i (S):" label
        CHART_CENTER = np.array([4.2, -0.3, 0])         # two players: Player 2's contribution 0..15 on a 0..20 axis
        CHART_CENTER_3 = np.array([4.3, -0.3, 0])       # three players: the others' contributions 0..30 on a 0..35 axis
        PLAYER_COLORS = (ROW_PLAYER, COL_PLAYER, PURPLE)
        # Right panel: D2's diamond matrix.
        CELL_SIDE = 1.5
        DIAMOND_ANGLE = -PI / 4
        GAME_CENTER = np.array([3.9, -0.2, 0])
        TABLE_RIGHT = (RIGHT + DOWN) / 2**0.5
        TABLE_UP = (RIGHT + UP) / 2**0.5
        # A memorial to Dobby, from the October 30 notes.
        residents = ('Harry', 'Ron', 'Hermione', 'Ginny', 'Neville')
        benefits = (34, 29, 24, 19, 14)
        COST = 100

        def teach(text):
            return Tex(text, color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)

        # ---- 0.a · The bumper, as Part A opens: the wordmark flickers, then "Part D | Episode 3" joins beneath it.
        squares = bumper_raster(self)
        flicker(self, squares, rounds=5)
        bumper_title(self, squares, 'D', 3)
        self.pause('0.a')

        # ---- 0.b · Warmup, before any model: the title, then Exercise D3 Q1 on an exercise card in D1's style, with
        # the handout's table as three bars. The handout's a) and b) only, so the letters match the card after Dobby,
        # which carries c)–e): who visits (all three) and whether 30 coins a year from each would get it funded once the
        # endowment runs out (no: only Aurelius, at 75, would pay). No teaching line; whether it is worth it to the three
        # together (105 > 90) is for the discussion. The free-rider problem found before the lecture names it.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Warmup')
        context = subtitle(head, 'Exercise D3, Q1, in groups, five minutes.')
        warm_panel = RoundedRectangle(width=13.6, height=5.4, corner_radius=0.25, color=MUTED,
                                      stroke_width=2, fill_color=BG, fill_opacity=1).move_to([0, -0.2, 0])
        warm_head = Tex('Exercise D3 $|$ Q1: The Dumbledore Memorial', color=DEFINITION).scale(1.05)
        warm_head.move_to(warm_panel.get_corner(UL) + RIGHT * 0.65 + DOWN * 0.7, aligned_edge=LEFT)
        warm_setup = VGroup(
            Tex('Three Dumbledores are considering a memorial to their', color=INK),
            Tex('brother Albus, just outside their town. Anyone can enjoy it,', color=INK),
            Tex('whether or not they helped pay. It costs 90 coins a year.', color=INK),
        ).scale(0.62).arrange(DOWN, buff=0.18, aligned_edge=LEFT).next_to(warm_head, DOWN, buff=0.35, aligned_edge=LEFT)
        warm_parts = VGroup(
            Tex('a) If it were built, how many of the three would visit?', color=INK),
            Tex('b) An endowment covers the first year. After that, each', color=INK),
            Tex('must put in 30 coins a year. Would it get funded?', color=INK),
        ).scale(0.66).arrange(DOWN, buff=0.26, aligned_edge=LEFT).next_to(warm_setup, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.3)
        warm_parts[2].shift(RIGHT * 0.38)       # the continuation line hangs under the text of b)
        # The handout's table as the three bars the later exercise card uses too.
        warm_chart = axes([0, 4, 1], [0, 90, 30], x_length=3.8, y_length=2.4).move_to([4.8, -0.2, 0])
        warm_heading = Tex('Annual benefit', color=CAPTION).scale(0.6).next_to(warm_chart, UP, buff=0.22)
        warm_benefits = (75, 10, 20)
        warm_bars = VGroup(*[Rectangle(width=0.6, height=2.4 * v / 90, color=DEMAND, fill_color=DEMAND, fill_opacity=0.3, stroke_width=2)
                             .move_to(warm_chart.c2p(i + 1, v / 2)) for i, v in enumerate(warm_benefits)])
        warm_values = VGroup(*[Tex(str(v), color=DEMAND).scale(0.6).next_to(bar, UP, buff=0.1) for v, bar in zip(warm_benefits, warm_bars)])
        warm_names = VGroup(*[Tex(name, color=CAPTION).scale(0.42).next_to(warm_chart.c2p(i + 1, 0), DOWN, buff=0.18)
                              for i, name in enumerate(('Aurelius', 'Aberforth', 'Ariana'))])
        warm_cost = VGroup(Tex('Annual cost:', color=SUPPLY), Tex('90', color=SUPPLY)).arrange(RIGHT, buff=0.12).scale(0.65).next_to(warm_names, DOWN, buff=0.35)
        warm_card = VGroup(warm_head, warm_setup, warm_parts, warm_chart, warm_heading, warm_bars, warm_values, warm_names, warm_cost)
        self.play(FadeIn(head), FadeIn(context), FadeIn(warm_panel), FadeIn(warm_card))
        self.pause('0.b')

        # ---- 1.a · D1's taxonomy again: a hold on common resources, last time's topic, then the box and the words
        # move to public goods.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Common Resources')
        context = subtitle(head, 'Goods that are rival and non-excludable.')
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.7).move_to([0.4, BODY_MID, 0])
        box = SurroundingRectangle(taxonomy.get_entries_without_labels((2, 1)), buff=0.22, color=NASH)
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxonomy), FadeIn(box))
        self.pause('1.a.commons')
        new_head = title('Public Goods')
        self.play(box.animate.move_to(taxonomy.get_entries_without_labels((2, 2))), Transform(head, new_head),
                  Transform(context, subtitle(new_head, 'Goods that are non-rival and non-excludable.')), run_time=0.8)
        self.pause('1.a')

        # ---- 1.b · The NPR game opens on the rule alone, centered, its two braces arriving on separate holds. Then
        # everything moves into place: the rule at the top of the left panel, the two strategies beneath it until the
        # first worked lines replace them, and the empty graph on the right. The worked lines carry each profile's
        # arithmetic and the graph keeps every outcome, as D2's harvest graph did.
        self.play(FadeOut(taxonomy), FadeOut(box), FadeOut(context), Transform(head, title('The NPR Game')))
        context = subtitle(head, 'Everyone can listen, whether or not they contribute.')

        def rule_block(terms):
            """The board's rule with its two underbraces. Double braces isolate the terms (the course's idiom);
            the trailing thin space keeps the closing braces apart."""
            fund_tex = '(' + terms + r')\cdot\tfrac{2}{3}\,'
            rule = MathTex(r'\text{Payoff}_i = {{(15 - c_i)}} + {{' + fund_tex + '}}', color=INK).scale(0.75)
            kept_brace = Brace(rule.get_part_by_tex('(15 - c_i)'), DOWN, buff=0.1, color=CAPTION)
            fund_brace = Brace(rule.get_part_by_tex(fund_tex), DOWN, buff=0.1, color=CAPTION)
            kept_note = Tex('the money I keep', color=CAPTION).scale(0.5).next_to(kept_brace, DOWN, buff=0.08)
            fund_note = Tex('funding NPR', color=CAPTION).scale(0.5).next_to(fund_brace, DOWN, buff=0.08)
            return VGroup(rule, kept_brace, fund_brace, kept_note, fund_note)

        def payoff_row(i, values, strategy=None, result=None):
            """Player i's line: "Player i (S):" with the strategy in grey, then the rule's right-hand side in white with
            the choices as isolated slots in the players' colors, then the result. `values` holds each player's c as
            text ('c_1', '15' or '0'). The result is its own mobject so a copy of it can fly to the graph."""
            color = PLAYER_COLORS[i - 1]
            tag = r' {{\textsf{(' + strategy + ')}}}:' if strategy else ':'
            label = Tex(r'{{Player ' + str(i) + '}}' + tag, color=CAPTION).set_color_by_tex(f'Player {i}', color).scale(0.58)
            label.move_to([ROWS_LEFT, ROW_Y[i - 1], 0], aligned_edge=LEFT)
            own = values[i - 1]
            total = ' + '.join('{{' + v + '}}' for v in values)
            eq = MathTex(rf'(15 - {{{{{own}}}}}) + ({total})\cdot\tfrac{{2}}{{3}}', color=INK).scale(0.58)
            slots = []
            for key in dict.fromkeys(values):
                slots.extend(eq.get_parts_by_tex(key))
            slots.sort(key=lambda part: part.get_center()[0])
            for slot, slot_color in zip(slots, (color,) + PLAYER_COLORS[:len(values)]):
                slot.set_color(slot_color)
            eq.move_to([EQ_LEFT, ROW_Y[i - 1], 0], aligned_edge=LEFT)
            row = VGroup(label, eq)
            if result is not None:
                row.add(MathTex(f'= {result}', color=color).scale(0.58).next_to(eq, RIGHT, buff=0.15))
            return row

        def worked_rows(profile):
            """Every player's line with the profile's strategies, choices and results filled in."""
            values = tuple(str(c) for c in profile)
            return VGroup(*[payoff_row(i + 1, values, 'C' if c_i else 'DC', 15 - c_i + 2 * sum(profile) // 3)
                            for i, c_i in enumerate(profile)])

        def reprofile(rows, new_rows):
            """Move from one profile's rows to the next: matching pieces slide, the changed slots and results swap."""
            return ([ReplacementTransform(r[0], n[0]) for r, n in zip(rows, new_rows)]
                    + [TransformMatchingTex(r[1], n[1]) for r, n in zip(rows, new_rows)]
                    + [ReplacementTransform(r[2], n[2]) for r, n in zip(rows, new_rows)])

        def payoff_chart(x_max, y_max, x_caption, x_length, center, marks):
            """Player 1's payoff against what the others contribute: the rule's two cases are lines on it.
            Only the contributions that occur are marked under the axis; payoffs are read beside the points."""
            chart = axes([0, x_max, 5], [0, y_max, 5], x_length=x_length, y_length=3.4).move_to(center)
            captions = VGroup(Tex(x_caption, color=CAPTION).scale(0.55).next_to(chart.c2p(x_max / 2, 0), DOWN, buff=0.5),
                              Tex("Player 1's payoff", color=CAPTION).scale(0.55).next_to(chart.c2p(0, y_max), UP, buff=0.12)
                              .align_to(chart.c2p(0, 0), LEFT),
                              *[Tex(str(v), color=CAPTION).scale(0.5).next_to(chart.c2p(v, 0), DOWN, buff=0.12) for v in marks])
            return chart, captions

        def plot_point(chart, x, p1, pair, others=()):
            """A pink dot for Player 1's payoff with the strategy pair beside it and the payoffs as a row,
            left of the point at x = 0 and right of it otherwise. The numbers later move into the matrix."""
            dot = Dot(chart.c2p(x, p1), radius=0.07, color=ROW_PLAYER)
            numbers = VGroup(Tex(str(p1), color=ROW_PLAYER))
            for value, color in zip(others, PLAYER_COLORS[1:]):
                numbers.add(Tex(r'$\mid$', color=MUTED), Tex(str(value), color=color))
            numbers.arrange(RIGHT, buff=0.1).scale(0.6)
            pair_label = Tex(r'\textsf{' + pair + '}', color=CAPTION).scale(0.55)
            VGroup(pair_label, numbers).arrange(RIGHT, buff=0.2).next_to(dot, LEFT if x == 0 else RIGHT, buff=0.2)
            return dot, pair_label, numbers

        rule_group = rule_block('c_1 + c_2')
        rule, kept_brace, fund_brace, kept_note, fund_note = rule_group
        RULE_ZOOM = 1.35
        rule_group.scale(RULE_ZOOM).move_to([0, BODY_MID + 0.2, 0])
        self.play(FadeIn(context), FadeIn(rule))
        self.pause('1.b.rule')
        self.play(FadeIn(kept_brace), FadeIn(kept_note))
        self.pause('1.b.kept')
        self.play(FadeIn(fund_brace), FadeIn(fund_note))
        self.pause('1.b.fund')
        strategies_heading = Tex('Two Strategies:', color=INK).scale(0.85)
        c_rule = VGroup(Tex('- Contribute (C):', color=INK), Tex('15', color=CAPTION)).arrange(RIGHT, buff=0.18).scale(0.75)
        dc_rule = VGroup(Tex('- Do not contribute (DC):', color=INK), Tex('0', color=CAPTION)).arrange(RIGHT, buff=0.18).scale(0.75)
        strategies = VGroup(strategies_heading, c_rule, dc_rule).arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        divider = Line([0, 2.5, 0], [0, -2.55, 0], color=MUTED, stroke_width=1)
        chart, chart_captions = payoff_chart(20, 30, "Player 2's contribution", 3.4, CHART_CENTER, (0, 15))
        strategies.move_to([-3.7, -0.95, 0])          # where the worked lines will sit
        teaching = teach('Do I contribute, or keep my money?')
        self.play(rule_group.animate.scale(1 / RULE_ZOOM).move_to(RULE_POS), FadeIn(strategies), Create(divider), FadeIn(chart),
                  FadeIn(chart_captions), FadeIn(teaching), run_time=1.0)
        self.pause('1.b')

        # ---- 1.d · The first profile, one player at a time. Each player's equation is a copy of the rule; the choices
        # drop into their slots in the players' colors, Player 1's first, then Player 2's; then the result.
        self.play(FadeOut(teaching), FadeOut(strategies))
        row1 = payoff_row(1, ('c_1', 'c_2'))
        teaching = teach("Player 1's payoff: the rule, with $i = 1$.")
        self.play(FadeIn(row1[0]), TransformFromCopy(rule, row1[1]), FadeIn(teaching))
        self.pause('1.d.rule')
        self.play(FadeOut(teaching))
        new_row = payoff_row(1, ('15', 'c_2'), 'C')
        teaching = teach('Player 1 contributes: $c_1 = 15$.')
        self.play(ReplacementTransform(row1[0], new_row[0]), TransformMatchingTex(row1[1], new_row[1]), FadeIn(teaching))
        row1 = new_row
        self.pause('1.d.c1')
        self.play(FadeOut(teaching))
        new_row = payoff_row(1, ('15', '0'), 'C')
        teaching = teach('Player 2 does not: $c_2 = 0$.')
        self.play(ReplacementTransform(row1[0], new_row[0]), TransformMatchingTex(row1[1], new_row[1]), FadeIn(teaching))
        row1 = new_row
        self.pause('1.d.c2')
        self.play(FadeOut(teaching))
        result_1 = MathTex('= 10', color=ROW_PLAYER).scale(0.58).next_to(row1[1], RIGHT, buff=0.15)
        teaching = teach('Player 1 keeps nothing and gets two thirds of 15.')
        self.play(FadeIn(result_1), FadeIn(teaching))
        row1.add(result_1)
        self.pause('1.d.p1')
        self.play(FadeOut(teaching))
        row2 = payoff_row(2, ('c_1', 'c_2'))
        teaching = teach("Player 2's payoff: the same rule, with $i = 2$.")
        self.play(FadeIn(row2[0]), TransformFromCopy(rule, row2[1]), FadeIn(teaching))
        self.pause('1.d.rule2')
        self.play(FadeOut(teaching))
        teaching = teach('Player 2 keeps 15: $c_2 = 0$. Player 1 put in $c_1 = 15$.')
        new_row = payoff_row(2, ('c_1', '0'), 'DC')
        self.play(ReplacementTransform(row2[0], new_row[0]), TransformMatchingTex(row2[1], new_row[1]), FadeIn(teaching), run_time=0.7)
        row2 = new_row
        new_row = payoff_row(2, ('15', '0'), 'DC')
        self.play(ReplacementTransform(row2[0], new_row[0]), TransformMatchingTex(row2[1], new_row[1]), run_time=0.7)
        row2 = new_row
        self.pause('1.d.choices2')
        self.play(FadeOut(teaching))
        result_2 = MathTex('= 25', color=COL_PLAYER).scale(0.58).next_to(row2[1], RIGHT, buff=0.15)
        teaching = teach('A contribution costs me 15 and benefits each of us by 10.')
        self.play(FadeIn(result_2), FadeIn(teaching))
        row2.add(result_2)
        rows = VGroup(row1, row2)
        self.pause('1.d.payoffs')

        # ---- 1.e · The results fly to the graph: the first point.
        self.play(FadeOut(teaching))
        dot, pair_label, numbers = plot_point(chart, 0, 10, 'C,DC', (25,))
        teaching = teach("Each run is a point: Player 1's payoff against Player 2's contribution.")
        self.play(FadeIn(dot), FadeIn(pair_label), FadeIn(numbers[1]), TransformFromCopy(rows[0][-1], numbers[0]),
                  TransformFromCopy(rows[1][-1], numbers[2]), FadeIn(teaching), run_time=0.8)
        self.pause('1.e.graph')
        graph_points = VGroup(dot, pair_label, numbers)   # shrinks with the graph later; copies of the numbers fill the matrix
        graph_numbers = {(0, 1): numbers}             # matrix cell (Player 1's row, Player 2's column) -> its pair of numbers

        # ---- 1.f · Nobody contributes: each keeps 15.
        self.play(FadeOut(teaching))
        new_rows = worked_rows((0, 0))
        teaching = teach('Nobody contributes: each keeps 15.')
        self.play(*reprofile(rows, new_rows), FadeIn(teaching), run_time=0.6)
        rows = new_rows
        self.pause('1.f.payoffs')
        dot, pair_label, numbers = plot_point(chart, 0, 15, 'DC,DC', (15,))
        self.play(FadeIn(dot), FadeIn(pair_label), FadeIn(numbers[1]), TransformFromCopy(rows[0][-1], numbers[0]),
                  TransformFromCopy(rows[1][-1], numbers[2]), run_time=0.8)
        graph_points.add(dot, pair_label, numbers)
        graph_numbers[(1, 1)] = numbers
        self.pause('1.f.graph')

        # ---- 1.g · Both contribute: 20 each. The second contributing point completes the C line.
        self.play(FadeOut(teaching))
        new_rows = worked_rows((15, 15))
        teaching = teach('Both contribute: each receives 20.')
        self.play(*reprofile(rows, new_rows), FadeIn(teaching), run_time=0.6)
        rows = new_rows
        self.pause('1.g.payoffs')
        dot, pair_label, numbers = plot_point(chart, 15, 20, 'C,C', (20,))
        c_line = Line(chart.c2p(0, 10), chart.c2p(15, 20), color=INK, stroke_width=2)
        c_label = Tex(r'\textsf{C}', color=INK).scale(0.55).move_to(chart.c2p(7.5, 17))
        self.play(FadeIn(dot), FadeIn(pair_label), FadeIn(numbers[1]), TransformFromCopy(rows[0][-1], numbers[0]),
                  TransformFromCopy(rows[1][-1], numbers[2]), run_time=0.8)
        self.play(Create(c_line), FadeIn(c_label), run_time=0.6)
        graph_points.add(dot, pair_label, numbers, c_line, c_label)
        graph_numbers[(0, 0)] = numbers
        self.pause('1.g.graph')

        # ---- 1.h · Switch the contributor: Player 1 keeps 15 and still gets 10. The DC line completes above the C line.
        self.play(FadeOut(teaching))
        new_rows = worked_rows((0, 15))
        teaching = teach('Switch the contributor; switch the payoffs.')
        self.play(*reprofile(rows, new_rows), FadeIn(teaching), run_time=0.6)
        rows = new_rows
        self.pause('1.h.payoffs')
        self.play(FadeOut(teaching))
        dot, pair_label, numbers = plot_point(chart, 15, 25, 'DC,C', (10,))
        dc_line = Line(chart.c2p(0, 15), chart.c2p(15, 25), color=INK, stroke_width=2)
        dc_label = Tex(r'\textsf{DC}', color=INK).scale(0.55).move_to(chart.c2p(7.5, 22))
        teaching = teach('Whatever Player 2 does, not contributing pays 5 more.')
        self.play(FadeIn(dot), FadeIn(pair_label), FadeIn(numbers[1]), TransformFromCopy(rows[0][-1], numbers[0]),
                  TransformFromCopy(rows[1][-1], numbers[2]), run_time=0.8)
        self.play(Create(dc_line), FadeIn(dc_label), FadeIn(teaching), run_time=0.6)
        graph_points.add(dot, pair_label, numbers, dc_line, dc_label)
        graph_numbers[(1, 0)] = numbers
        self.pause('1.h.graph')

        # ---- 1.i · D2's turn: the rule panel fades, the graph shrinks into the left panel, the matrix fades in on the
        # right, and copies of the pairs fly from the points into their cells. The graph keeps its labels and numbers.
        self.play(FadeOut(teaching), FadeOut(rule_group), FadeOut(rows))
        npr = [[(20, 20), (10, 25)], [(25, 10), (15, 15)]]
        payoffs = [[VGroup(Tex(f'{a}', color=ROW_PLAYER), Tex(r'$\mid$', color=MUTED), Tex(f'{b}', color=COL_PLAYER))
                    .arrange(RIGHT, buff=0.12).scale(0.7) for a, b in row] for row in npr]
        entries = [cell for row in payoffs for cell in row]
        matrix = Table(payoffs, h_buff=CELL_SIDE - max(cell.width for cell in entries),
                       v_buff=CELL_SIDE - max(cell.height for cell in entries), include_outer_lines=True,
                       line_config={'color': MUTED, 'stroke_width': 2}).rotate(DIAMOND_ANGLE).move_to(GAME_CENTER)
        for cell in entries:
            cell.rotate(-DIAMOND_ANGLE, about_point=cell.get_center())
        row_labels = VGroup(*[Tex(r'\textsf{' + s + '}', color=CAPTION).scale(0.7) for s in ('C', 'DC')])
        col_labels = VGroup(*[Tex(r'\textsf{' + s + '}', color=CAPTION).scale(0.7) for s in ('C', 'DC')])
        for i in range(2):
            offset = (0.5 - i) * CELL_SIDE
            row_anchor = GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP
            col_anchor = GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP
            row_labels[i].move_to(row_anchor + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[i].move_to(col_anchor + RIGHT * 0.3, aligned_edge=LEFT)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).move_to([1.9, 2.15, 0])
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).move_to([5.9, 2.15, 0])
        graph = VGroup(chart, chart_captions, graph_points)
        teaching = teach("Player 1's payoff first; Player 2's payoff second.")
        self.play(graph.animate.scale(0.85).move_to([-3.7, -0.4, 0]),
                  FadeIn(matrix.get_horizontal_lines()), FadeIn(matrix.get_vertical_lines()),
                  FadeIn(row_labels), FadeIn(col_labels), FadeIn(player_1), FadeIn(player_2),
                  *[TransformFromCopy(graph_numbers[cell], payoffs[cell[0]][cell[1]]) for cell in graph_numbers],
                  FadeIn(teaching), run_time=1.2)
        self.add(*entries)
        self.pause('1.i.matrix')

        # ---- 1.j–1.m · Two comparisons for Player 1, as in D2: shade the fixed column, and the same x on the graph.
        def graph_band(x):
            top, bottom = chart.c2p(0, 30)[1], chart.c2p(0, 0)[1]
            return (Rectangle(width=0.4, height=top - bottom, stroke_width=0, fill_color=COL_PLAYER, fill_opacity=0.12)
                    .move_to(chart.c2p(x, 15)).set_z_index(-1))

        self.play(FadeOut(teaching))
        shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE, stroke_width=0, fill_color=COL_PLAYER, fill_opacity=0.12)
        shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - 0.5 * CELL_SIDE * TABLE_RIGHT).set_z_index(-1)
        underline = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        band = graph_band(15)
        teaching = teach("If Player 2 contributes, what is Player 1's best response?")
        self.play(FadeIn(shade), FadeIn(underline), FadeIn(band), FadeIn(teaching))
        self.pause('1.j.response-c')
        response_c = SurroundingRectangle(payoffs[1][0][0], buff=0.08, color=ROW_PLAYER)
        self.play(FadeOut(teaching), Create(response_c))
        teaching = teach(r'Do not contribute: $25 > 20$.')
        self.play(FadeIn(teaching))
        self.pause('1.k.answer-c')
        self.play(FadeOut(shade), FadeOut(underline), FadeOut(band), FadeOut(teaching))
        shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE, stroke_width=0, fill_color=COL_PLAYER, fill_opacity=0.12)
        shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + 0.5 * CELL_SIDE * TABLE_RIGHT).set_z_index(-1)
        underline = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        band = graph_band(0)
        teaching = teach("If Player 2 does not contribute, what is Player 1's best response?")
        self.play(FadeIn(shade), FadeIn(underline), FadeIn(band), FadeIn(teaching))
        self.pause('1.l.response-dc')
        response_dc = SurroundingRectangle(payoffs[1][1][0], buff=0.08, color=ROW_PLAYER)
        self.play(FadeOut(teaching), Create(response_dc))
        teaching = teach(r'Do not contribute: $15 > 10$.')
        self.play(FadeIn(teaching))
        self.pause('1.m.answer-dc')

        # ---- 1.n · Player 2 by symmetry, then the unilateral-deviation test.
        self.play(FadeOut(shade), FadeOut(underline), FadeOut(band), FadeOut(teaching))
        player_2_responses = VGroup(*[SurroundingRectangle(payoffs[r][1][2], buff=0.08, color=COL_PLAYER) for r in (0, 1)])
        teaching = teach('The same comparisons hold for Player 2. Neither contributes.')
        self.play(Create(player_2_responses), FadeIn(teaching))
        self.pause('1.n.symmetry')
        self.play(FadeOut(teaching))
        nash_box = Square(side_length=CELL_SIDE - 0.15, color=NASH, stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1])
        teaching = teach('Neither player gains by changing alone.')
        self.play(Create(nash_box), FadeIn(teaching))
        self.pause('1.n.nash')

        # ---- 1.o · End on the incentive conflict, as D2 ended on the tragedy of the commons.
        self.play(FadeOut(teaching))
        efficient_box = Square(side_length=CELL_SIDE - 0.15, color=EFFICIENT, stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[0][0])
        comparison = Tex(r'$20 > 15$ for each player.', color=INK).scale(0.65).move_to([3.9, 2.65, 0])
        teaching = VGroup(
            Tex('Free rider problem', color=DEFINITION).scale(TEACHING_SCALE),
            Tex('Individual incentives lead to the underprovision of a public good:', color=INK).scale(0.65),
            Tex('each contributor pays the full cost but receives only part of the total benefit.', color=INK).scale(0.65),
        ).arrange(DOWN, buff=0.12).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(efficient_box), FadeIn(comparison), FadeIn(teaching))
        self.pause('1.o.free-rider')

        # ---- 1.p · Back to the taxonomy: the commons is overused, the public good underprovided.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Common Resources And Public Goods')
        context = subtitle(head, 'Both are non-excludable. One is rival; the other is not.')
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.7).move_to([0.4, BODY_MID + 0.3, 0])
        commons_box = SurroundingRectangle(taxonomy.get_entries_without_labels((2, 1)), buff=0.22, color=NASH)
        public_box = SurroundingRectangle(taxonomy.get_entries_without_labels((2, 2)), buff=0.22, color=NASH)
        take = Tex('Take too much', color=INK).scale(0.7).next_to(commons_box, DOWN, buff=0.3)
        give = Tex('Contribute too little', color=INK).scale(0.7).next_to(public_box, DOWN, buff=0.3)
        teaching = teach('The commons is overused; the public good is underprovided.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxonomy), FadeIn(commons_box), FadeIn(public_box))
        self.play(FadeIn(take), FadeIn(give), FadeIn(teaching))
        self.pause('1.p.contrast')

        # ---- 2.a · Three contributors: the same rule with one more term, the same two lines drawn out to 30, one more
        # point. The graph is Player 1's payoff against what the other two contribute together.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Three Contributors')
        context = subtitle(head, 'The same rule, with one more contribution in the fund.')
        rule_group = rule_block('c_1 + c_2 + c_3').move_to(RULE_POS)
        divider = Line([0, 2.5, 0], [0, -2.55, 0], color=MUTED, stroke_width=1)
        chart, chart_captions = payoff_chart(35, 35, "The others' contributions", 3.2, CHART_CENTER_3, (0, 15, 30))
        c_line = Line(chart.c2p(0, 10), chart.c2p(30, 30), color=INK, stroke_width=2)
        dc_line = Line(chart.c2p(0, 15), chart.c2p(30, 35), color=INK, stroke_width=2)
        c_label = Tex(r'\textsf{C}', color=INK).scale(0.55).move_to(chart.c2p(15, 22))
        dc_label = Tex(r'\textsf{DC}', color=INK).scale(0.55).move_to(chart.c2p(15, 27))
        rows = worked_rows((15, 0, 0))
        teaching = teach('One contributor: 10 for them, 25 for each of the others.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(rule_group), Create(divider), FadeIn(chart), FadeIn(chart_captions),
                  Create(c_line), Create(dc_line), FadeIn(c_label), FadeIn(dc_label))
        self.play(FadeIn(rows), FadeIn(teaching), run_time=0.6)
        dot, pair_label, numbers = plot_point(chart, 0, 10, 'C,DC,DC')
        self.play(FadeIn(dot), FadeIn(pair_label), TransformFromCopy(rows[0][-1], numbers[0]), run_time=0.8)
        self.pause('2.a.one')

        # ---- 2.b · Nobody contributes: 15 each.
        self.play(FadeOut(teaching))
        new_rows = worked_rows((0, 0, 0))
        teaching = teach('Nobody contributes: 15 each.')
        self.play(*reprofile(rows, new_rows), FadeIn(teaching), run_time=0.6)
        rows = new_rows
        dot, pair_label, numbers = plot_point(chart, 0, 15, 'DC,DC,DC')
        self.play(FadeIn(dot), FadeIn(pair_label), TransformFromCopy(rows[0][-1], numbers[0]), run_time=0.8)
        self.pause('2.b.none')

        # ---- 2.c · Everybody contributes: 30 each, at the far end of the C line.
        self.play(FadeOut(teaching))
        new_rows = worked_rows((15, 15, 15))
        teaching = teach('Everybody contributes: 30 each. Could a group arrange that?')
        self.play(*reprofile(rows, new_rows), FadeIn(teaching), run_time=0.6)
        rows = new_rows
        dot, pair_label, numbers = plot_point(chart, 30, 30, 'C,C,C')
        self.play(FadeIn(dot), FadeIn(pair_label), TransformFromCopy(rows[0][-1], numbers[0]), run_time=0.8)
        self.pause('2.c.all')

        # ---- 3.a · Five people, five benefits, one memorial. Who visits?
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('A Memorial To Dobby')
        context = subtitle(head, 'Annual benefits and costs, in coins. Everyone can enjoy the memorial.')
        chart = axes([0, 6, 1], [0, 40, 10], x_length=6.2, y_length=3.3).move_to([-3.75, -0.1, 0])
        chart_heading = Tex('Marginal benefit', color=CAPTION).scale(0.65).move_to([-3.75, 2.2, 0])
        bars = VGroup(*[Rectangle(width=0.62, height=3.3 * v / 40, color=DEMAND, fill_color=DEMAND, fill_opacity=0.3, stroke_width=2)
                        .move_to(chart.c2p(i + 1, v / 2)) for i, v in enumerate(benefits)])
        bar_values = VGroup(*[Tex(str(v), color=DEMAND).scale(0.7).next_to(bar, UP, buff=0.12) for v, bar in zip(benefits, bars)])
        bar_names = VGroup(*[Tex(name, color=CAPTION).scale(0.55).next_to(chart.c2p(i + 1, 0), DOWN, buff=0.2)
                             for i, name in enumerate(residents)])
        divider = Line([0, 2.5, 0], [0, -2.7, 0], color=MUTED, stroke_width=1)
        cost_label = VGroup(Tex('Annual cost:', color=SUPPLY), Tex(str(COST), color=SUPPLY)).arrange(RIGHT, buff=0.15).scale(0.8).move_to([3.8, 1.9, 0])
        teaching = Tex('If it is built, how many people will visit?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(chart), FadeIn(chart_heading), FadeIn(bars), FadeIn(bar_values), FadeIn(bar_names),
                  Create(divider), FadeIn(cost_label), FadeIn(teaching))
        self.pause('3.a.visits')

        # ---- 3.b · All five.
        self.play(FadeOut(teaching))
        visitors = VGroup(Tex('Visitors:', color=INK), Tex('5', color=INK)).arrange(RIGHT, buff=0.15).scale(0.8).move_to([3.8, 0.9, 0])
        teaching = Tex('All five: each gets a benefit, and no one can be kept out.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(visitors), FadeIn(teaching))
        self.pause('3.b.all-five')

        # ---- 3.c · An equal tax of 20: one red line across the bars, read on the axis like a price.
        self.play(FadeOut(teaching), FadeOut(visitors))
        tax = ValueTracker(20)
        tax_line = DashedLine(chart.c2p(0, 20), chart.c2p(6, 20), color=GUIDE, stroke_width=2)
        tax_line.add_updater(lambda m: m.set_y(chart.c2p(0, tax.get_value())[1]))
        tax_readout = DecimalNumber(20, num_decimal_places=0, color=GUIDE).scale(0.65)
        tax_readout.add_updater(lambda m: m.set_value(round(tax.get_value(), 4)).next_to(chart.c2p(0, tax.get_value()), LEFT, buff=0.15))
        tax_readout.update()
        tax_word = Tex('tax', color=GUIDE).scale(0.5)
        tax_word.add_updater(lambda m: m.next_to(chart.c2p(6, tax.get_value()), UP, buff=0.08, aligned_edge=RIGHT))
        tax_word.update()
        teaching = Tex('Would a tax of 20 each pass a majority vote?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(tax_line), FadeIn(tax_readout), FadeIn(tax_word), FadeIn(teaching))
        self.pause('3.c.vote')

        # ---- 3.d · Each person compares their benefit with the tax: checks and crosses, as on the board.
        self.play(FadeOut(teaching))
        votes = VGroup()
        for v, name in zip(benefits, bar_names):
            spot = name.get_center() + DOWN * 0.42
            if v > 20:
                votes.add(polyline([spot + np.array([-0.16, 0.01, 0]), spot + np.array([-0.05, -0.12, 0]), spot + np.array([0.17, 0.15, 0])],
                                   color=EFFICIENT, width=4))
            else:
                votes.add(VGroup(Line(spot + np.array([-0.12, -0.12, 0]), spot + np.array([0.12, 0.12, 0]), color=NASH, stroke_width=4),
                                 Line(spot + np.array([-0.12, 0.12, 0]), spot + np.array([0.12, -0.12, 0]), color=NASH, stroke_width=4)))
        vote_result = Tex('3 Yes, 2 No', color=INK).scale(0.8).move_to([3.8, 0.5, 0])
        tax_total = Tex(r'$5 \times 20 = 100$', color=GOV).scale(0.75).move_to([3.8, -0.5, 0])
        teaching = Tex('It passes, and the tax pays for the memorial.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(LaggedStart(*[FadeIn(vote) for vote in votes], lag_ratio=0.25), run_time=0.8)
        self.play(FadeIn(vote_result), run_time=0.4)
        self.play(FadeIn(tax_total), FadeIn(teaching))
        self.pause('3.d.passes')
        self.play(FadeOut(teaching))
        teaching = Tex('Ginny and Neville pay 20 for benefits of 19 and 14.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.d.outvoted')

        # ---- 3.e · Is it efficient? Keep the bars and the tax line; clear the vote.
        self.play(FadeOut(teaching), FadeOut(votes), FadeOut(vote_result), FadeOut(tax_total))
        teaching = Tex('Is building the memorial socially efficient?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.e.efficiency')

        # ---- 3.f · Add the five benefits vertically: one memorial, enjoyed by all five.
        STACK_X, STACK_BOTTOM, STACK_UNIT = 3.3, -1.9, 0.025
        segments = VGroup()
        running = 0
        for v in benefits:
            segments.add(Rectangle(width=0.9, height=v * STACK_UNIT, color=DEMAND, fill_color=DEMAND, fill_opacity=0.3, stroke_width=2)
                         .move_to([STACK_X, STACK_BOTTOM + (running + v / 2) * STACK_UNIT, 0]))
            running += v
        msb_name = Tex('MSB', color=INK).scale(0.6).move_to([STACK_X, STACK_BOTTOM - 0.3, 0])
        msb_value = Tex(str(sum(benefits)), color=DEMAND).scale(0.7).next_to(segments, UP, buff=0.12)
        cost_line = DashedLine([STACK_X - 1.0, STACK_BOTTOM + COST * STACK_UNIT, 0], [STACK_X + 1.4, STACK_BOTTOM + COST * STACK_UNIT, 0],
                               color=SUPPLY, stroke_width=2)
        msc_label = VGroup(Tex('MSC', color=SUPPLY), Tex(str(COST), color=SUPPLY)).arrange(RIGHT, buff=0.15).scale(0.65).next_to(cost_line, RIGHT, buff=0.15)
        self.play(FadeOut(teaching))
        self.play(*[TransformFromCopy(bar, segment) for bar, segment in zip(bars, segments)], FadeIn(msb_name), run_time=1.0)
        self.play(FadeIn(msb_value), FadeIn(cost_line), FadeIn(msc_label[0]), TransformFromCopy(cost_label[1], msc_label[1]), run_time=0.8)
        teaching = Tex(r'$MSB = 120 > MSC = 100$: building it is efficient.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.f.efficient')

        # ---- 3.g · The vignette's higher tax: the same line rolls up to 25.
        self.play(FadeOut(teaching), FadeOut(segments), FadeOut(msb_name), FadeOut(msb_value), FadeOut(cost_line), FadeOut(msc_label))
        teaching = Tex('What if the proposed tax were 25 each?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(tax.animate.set_value(25), FadeIn(teaching), run_time=1.0)
        self.pause('3.g.tax25')

        # ---- 3.h · It fails, though nothing about the memorial's efficiency has changed.
        self.play(FadeOut(teaching))
        votes = VGroup()
        for v, name in zip(benefits, bar_names):
            spot = name.get_center() + DOWN * 0.42
            if v > 25:
                votes.add(polyline([spot + np.array([-0.16, 0.01, 0]), spot + np.array([-0.05, -0.12, 0]), spot + np.array([0.17, 0.15, 0])],
                                   color=EFFICIENT, width=4))
            else:
                votes.add(VGroup(Line(spot + np.array([-0.12, -0.12, 0]), spot + np.array([0.12, 0.12, 0]), color=NASH, stroke_width=4),
                                 Line(spot + np.array([-0.12, 0.12, 0]), spot + np.array([0.12, -0.12, 0]), color=NASH, stroke_width=4)))
        vote_result = Tex('2 Yes, 3 No', color=INK).scale(0.8).move_to([3.8, 0.5, 0])
        teaching = Tex('It fails, even though the memorial is still efficient.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(LaggedStart(*[FadeIn(vote) for vote in votes], lag_ratio=0.25), run_time=0.8)
        self.play(FadeIn(vote_result), run_time=0.4)
        self.play(FadeIn(teaching))
        self.pause('3.h.fails')

        # ---- 3.i · Change the assumption: now non-payers can be kept out. The tax line becomes a fee.
        tax_word.clear_updaters()
        self.play(FadeOut(teaching), FadeOut(votes), FadeOut(vote_result), FadeOut(context), FadeOut(tax_word))
        context = subtitle(head, 'Now suppose a private company can keep non-payers out, for a fee.')
        fee_word = Tex('fee', color=GUIDE).scale(0.5)
        fee_word.add_updater(lambda m: m.next_to(chart.c2p(6, tax.get_value()), UP, buff=0.08, aligned_edge=RIGHT))
        fee_word.update()
        revenue_heading = Tex('Admission revenue', color=CAPTION).scale(0.7).move_to([3.8, 0.9, 0])
        teaching = Tex('Can one fee cover the annual cost of 100?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(context), FadeIn(fee_word), FadeIn(revenue_heading), tax.animate.set_value(20), FadeIn(teaching), run_time=1.0)
        self.pause('3.i.admission')

        # ---- 3.j–3.l · Three fees from the board. Non-buyers go grey; earlier results are stored in grey.
        revenue_20 = Tex(r'$3 \times 20 = 60$', color=INK).scale(0.8).move_to([3.8, 0.0, 0])
        self.play(bars[3].animate.set_color(MUTED), bar_values[3].animate.set_color(CAPTION),
                  bars[4].animate.set_color(MUTED), bar_values[4].animate.set_color(CAPTION), FadeIn(revenue_20), run_time=0.6)
        self.pause('3.j.fee20')
        revenue_24 = Tex(r'$3 \times 24 = 72$', color=INK).scale(0.8).move_to([3.8, 0.0, 0])
        self.play(tax.animate.set_value(24), revenue_20.animate.scale(0.75).set_color(CAPTION).move_to([3.8, -0.9, 0]), run_time=0.8)
        self.play(FadeIn(revenue_24), run_time=0.4)
        self.pause('3.k.fee24')
        revenue_19 = Tex(r'$4 \times 19 = 76$', color=INK).scale(0.8).move_to([3.8, 0.0, 0])
        self.play(tax.animate.set_value(19), revenue_20.animate.move_to([3.8, -1.6, 0]), FadeOut(teaching),
                  revenue_24.animate.scale(0.75).set_color(CAPTION).move_to([3.8, -0.9, 0]),
                  bars[3].animate.set_color(DEMAND), bar_values[3].animate.set_color(DEMAND), run_time=0.8)
        self.play(FadeIn(revenue_19), run_time=0.4)
        teaching = Tex(r'Even the best single fee raises only $76 < 100$.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.l.fee19')

        # ---- 3.m · Different payments for different people: the idea behind Lindahl taxes.
        tax_line.clear_updaters()
        tax_readout.clear_updaters()
        fee_word.clear_updaters()
        self.play(FadeOut(teaching), FadeOut(revenue_19), FadeOut(revenue_24), FadeOut(revenue_20), FadeOut(revenue_heading),
                  FadeOut(tax_line), FadeOut(tax_readout), FadeOut(fee_word), FadeOut(context),
                  bars[4].animate.set_color(DEMAND), bar_values[4].animate.set_color(DEMAND))
        context = subtitle(head, 'What if each person paid a different amount?')
        teaching = Tex('Could different payments make everyone willing to fund it?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(context), FadeIn(teaching))
        self.pause('3.m.personalized-question')

        # ---- 3.n · Payments 4 below each benefit: everyone says yes, and the payments cover the cost.
        payments = (30, 25, 20, 15, 10)
        payment_marks = [Line(chart.c2p(i + 1, p) + LEFT * 0.42, chart.c2p(i + 1, p) + RIGHT * 0.42, color=GUIDE, stroke_width=3)
                         for i, p in enumerate(payments)]
        payment_values = [Tex(str(p), color=GUIDE).scale(0.6).next_to(name, DOWN, buff=0.22) for p, name in zip(payments, bar_names)]
        payment_total = Tex(r'$30 + 25 + 20 + 15 + 10 = 100$', color=GOV).scale(0.7).move_to([3.8, 0.4, 0])
        self.play(FadeOut(teaching))
        teaching = Tex('Each pays 4 less than their benefit: all five say yes.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(LaggedStart(*[FadeIn(VGroup(mark, value)) for mark, value in zip(payment_marks, payment_values)], lag_ratio=0.2), run_time=0.8)
        self.play(FadeIn(payment_total), FadeIn(teaching))
        self.pause('3.n.personalized')
        self.play(FadeOut(teaching))
        teaching = Tex('The difficulty: learning how much each person really values it.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.n.elicitation')

        # ---- 3.exercise · Exercise D3 Q1 card, D1 style: the warmup's memorial again, now with the tools; parts c)–e).
        card_head = Tex('Exercise D3 $|$ Q1, continued: The Dumbledore Memorial', color=DEFINITION).scale(1.05)
        card_parts = VGroup(
            Tex('c) Does a referendum for a tax of 30 each pass?'),
            Tex('d) What is the marginal social benefit?'),
            Tex('e) If it passed, would the outcome be efficient?'),
        ).scale(0.7).arrange(DOWN, buff=0.4, aligned_edge=LEFT)
        card_chart = axes([0, 4, 1], [0, 90, 30], x_length=4.2, y_length=2.4).move_to([4.5, -0.2, 0])
        card_benefits = (75, 10, 20)
        card_bars = VGroup(*[Rectangle(width=0.6, height=2.4 * v / 90, color=DEMAND, fill_color=DEMAND, fill_opacity=0.3, stroke_width=2)
                             .move_to(card_chart.c2p(i + 1, v / 2)) for i, v in enumerate(card_benefits)])
        card_values = VGroup(*[Tex(str(v), color=DEMAND).scale(0.6).next_to(bar, UP, buff=0.1) for v, bar in zip(card_benefits, card_bars)])
        card_names = VGroup(*[Tex(name, color=CAPTION).scale(0.45).next_to(card_chart.c2p(i + 1, 0), DOWN, buff=0.18)
                              for i, name in enumerate(('Aurelius', 'Aberforth', 'Ariana'))])
        card_cost = VGroup(Tex('Annual cost:', color=SUPPLY), Tex('90', color=SUPPLY)).arrange(RIGHT, buff=0.12).scale(0.65).move_to([4.5, -2.15, 0])
        card_panel = RoundedRectangle(width=13.6, height=5.4, corner_radius=0.25, color=MUTED,
                                      stroke_width=2, fill_color=BG, fill_opacity=1).move_to([0, -0.2, 0])
        card_head.move_to(card_panel.get_corner(UL) + RIGHT * 0.65 + DOWN * 0.7, aligned_edge=LEFT)
        card_note = subtitle(card_head, 'The memorial from the warmup, now with the tools.')
        card_parts.next_to(card_note, DOWN, buff=0.4, aligned_edge=LEFT).shift(RIGHT * 0.35)
        card = VGroup(card_head, card_note, card_parts, card_chart, card_bars, card_values, card_names, card_cost)
        card_panel.set_z_index(50)
        for glyph in card.get_family():
            glyph.set_z_index(51)
        self.play(*[mob.animate.set_opacity(0.05) for mob in list(self.mobjects)], FadeIn(card_panel), FadeIn(card))
        self.pause('3.exercise')

        # ---- 5.a · A brief look past majority votes on one proposal: three voters, three alternatives.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Three Voters, Three Alternatives')
        context = subtitle(head, 'Each voter ranks A, B, and C. Rankings read from least to most preferred.')
        rankings = (('C', 'B', 'A'), ('A', 'C', 'B'), ('B', 'A', 'C'))
        ranking_rows = VGroup(*[VGroup(Tex(f'Voter {i + 1}', color=CAPTION).scale(0.75), Tex('$' + r' \prec '.join(rank) + '$').scale(0.9)).arrange(RIGHT, buff=0.55)
                                for i, rank in enumerate(rankings)]).arrange(DOWN, buff=0.65, aligned_edge=LEFT).move_to([-3.9, BODY_MID, 0])
        divider = Line([0, 2.5, 0], [0, -2.7, 0], color=MUTED, stroke_width=1)
        teaching = Tex('Which alternative wins a majority against each of the others?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(ranking_rows), Create(divider), FadeIn(teaching))
        self.pause('5.a.rankings')
        pair_results = VGroup(*[Tex(s, color=INK).scale(0.85).move_to([3.8, y, 0])
                                for s, y in zip(('A beats B, 2 to 1', 'B beats C, 2 to 1', 'C beats A, 2 to 1'), (1.2, 0.3, -0.6))])
        self.play(FadeIn(pair_results[0]))
        self.pause('5.b.ab')
        self.play(FadeIn(pair_results[1]))
        self.pause('5.c.bc')
        self.play(FadeOut(teaching))
        teaching = Tex('A Condorcet cycle: no alternative beats every other one.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(pair_results[2]), FadeIn(teaching))
        self.pause('5.d.cycle')
        self.play(FadeOut(teaching))
        agenda = VGroup(Tex('A vs. B first, then the winner vs. C: C wins', color=CAPTION),
                        Tex('B vs. C first, then the winner vs. A: A wins', color=CAPTION)
                        ).arrange(DOWN, buff=0.2, aligned_edge=LEFT).scale(0.6).move_to([3.8, -1.9, 0])
        teaching = Tex('The order of the votes can change the winner.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(agenda), FadeIn(teaching))
        self.pause('5.e.agenda')

        # ---- 5.f · Arrow, as a statement only.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title("Arrow's Impossibility Theorem")
        context = subtitle(head, 'With three or more alternatives, no voting rule can do all of the following.')
        conditions = VGroup(
            Tex('Accept any individual rankings', color=INK),
            Tex('Respect unanimous preferences', color=INK),
            Tex('Compare two alternatives using only how people rank those two', color=INK),
            Tex('Let no single voter always decide', color=INK),
        ).arrange(DOWN, buff=0.4, aligned_edge=LEFT).scale(0.75).move_to([0, 0.5, 0])
        arrow_result = Tex('No rule does all four and always produces a consistent social ranking.', color=INK).scale(0.7).move_to([0, -1.8, 0])
        teaching = Tex('A limit on ranking rules, not a reason to abandon voting.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(conditions))
        self.play(FadeIn(arrow_result), FadeIn(teaching))
        self.pause('5.f.arrow')

        # ---- 6.a · Close: gold terms, white descriptions.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head = title('Public Goods And Voting')
        context = subtitle(head, 'Both common resources and public goods are non-excludable.')
        recap = VGroup(
            VGroup(Tex('Common resources', color=DEFINITION), Tex('Rival: individual incentives lead to overuse.', color=INK)),
            VGroup(Tex('Public goods', color=DEFINITION), Tex('Non-rival: individual incentives lead to underprovision.', color=INK)),
            VGroup(Tex('Voting', color=DEFINITION), Tex('Can fund a public good, but a majority need not choose efficiently.', color=INK)),
        ).scale(0.7)
        for i, row in enumerate(recap):
            row[0].move_to([-6.0, 0.9 - 0.9 * i, 0], aligned_edge=LEFT)
            row[1].move_to([-2.4, 0.9 - 0.9 * i, 0], aligned_edge=LEFT)
        self.play(FadeIn(head), FadeIn(context), FadeIn(recap))
        self.pause('6.a.recap')
