# maniml D1_Animation.py EpisodeD1
# Part D | Strategic Interaction — first day
# Taxonomy from D0, followed by the original Baby Game Theory sequence.
# Beat descriptions live in D1_Notes.md. All choreography is flat and editable.
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


class EpisodeD1(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP = 2.5
        BODY_BOTTOM = -2.8
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        DEFINITION_SCALE = 0.7443
        DEFINITION_BOTTOM = 0.05
        CELL_BOX_WIDTH = 1.65
        CELL_BOX_HEIGHT = 0.75

        # ---- 0.a · The existing raster bumper, with the current Part D title.
        squares = bumper_raster(self)
        flicker(self, squares)
        part = Tex(r'{{Part D}} $|$ Strategic Interaction', color=CAPTION)
        part.set_color_by_tex('Part D', TITLE).scale(1.5).move_to(DOWN * 0.9)
        self.play(FadeIn(part), squares.animate.move_to(UP * 0.9))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(part))
        self.clear()

        # ---- 1.a · The same four cells and orientation as the original D0.
        head = title('The Taxonomy Of Goods')
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable'), Tex('Non-Excludable')],
            col_labels=[Tex('Rival'), Tex('Non-Rival')],
            element_to_mobject=Tex,
            h_buff=0.65, v_buff=0.6,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.8).move_to([1.7, BODY_MID, 0])
        self.play(FadeIn(head), FadeIn(taxonomy.get_horizontal_lines()),
                  FadeIn(taxonomy.get_vertical_lines()))
        self.play(FadeIn(taxonomy.get_col_labels()))
        self.play(FadeIn(taxonomy.get_row_labels()))
        self.play(FadeIn(taxonomy.get_entries_without_labels()))
        self.pause('1.a')

        # ---- 1.b–1.d · Preserve the earlier Parts' private-goods map.
        parts = VGroup(Tex('Part A', color=CAPTION), Tex('Part B', color=CAPTION),
                       Tex('Part C', color=CAPTION))
        parts.arrange(DOWN, buff=0.5, aligned_edge=LEFT).move_to([-5.6, BODY_MID, 0])
        box = SurroundingRectangle(taxonomy.get_entries_without_labels((1, 1)),
                                   buff=0.2, color=FOCUS)
        self.play(FadeIn(box), FadeIn(parts[0]))
        self.pause('1.b')
        self.play(FadeIn(parts[1]))
        self.pause('1.c')
        self.play(FadeIn(parts[2]))
        self.pause('1.d')

        # ---- 1.e · The old map's move to common resources, then game theory.
        next_box = SurroundingRectangle(taxonomy.get_entries_without_labels((2, 1)),
                                        buff=0.2, color=FOCUS)
        part_d = Tex(r'Part D\\Strategic Interaction', color=DEFINITION).scale(0.7)
        part_d.next_to(parts, DOWN, buff=0.45)
        self.play(Transform(box, next_box), FadeIn(part_d))
        self.pause('1.e')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 2.a–2.c · Original definitions, with this semester's serif roles.
        head = title('Baby Game Theory')
        best_response = VGroup(
            Tex('Best Response', color=DEFINITION),
            Tex('The strategy that gives a player the highest payoff,', color=INK),
            Tex('given the strategies chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.8)
        dominant = VGroup(
            Tex('Dominant Strategy', color=DEFINITION),
            Tex('A strategy that yields the highest payoff for a player', color=INK),
            Tex('regardless of the strategies chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.8)
        nash_definition = VGroup(
            Tex('Nash Equilibrium', color=DEFINITION),
            Tex('A set of strategies such that no player can improve their payoff', color=INK),
            Tex('by unilaterally changing strategy.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.8)
        definitions = VGroup(best_response, dominant, nash_definition)
        definitions.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        definitions.move_to([0, BODY_MID, 0]).align_to(head, LEFT)
        self.play(FadeIn(head), FadeIn(best_response))
        self.pause('2.a')
        self.play(FadeIn(dominant))
        self.pause('2.b')
        self.play(FadeIn(nash_definition))
        self.pause('2.c')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 3.a · Original matrix 1; row payoff first.
        head = title("Prisoner's Dilemma")
        payoffs = [
            [
                VGroup(Tex('3', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('3', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('0', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('5', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
            [
                VGroup(Tex('5', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
        ]
        matrix = Table(
            payoffs,
            row_labels=[Tex('Cooperate', color=ROW_PLAYER), Tex('Defect', color=ROW_PLAYER)],
            col_labels=[Tex('Cooperate', color=COL_PLAYER), Tex('Defect', color=COL_PLAYER)],
            h_buff=1.1, v_buff=0.65,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.85)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).rotate(PI / 2)
        player_1.next_to(matrix, LEFT, buff=0.45)
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).next_to(matrix, UP, buff=0.3)
        game = VGroup(matrix, player_1, player_2).move_to([0, BODY_MID, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(matrix.get_col_labels()))
        self.play(FadeIn(player_1), FadeIn(matrix.get_row_labels()))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('3.a')

        # ---- 3.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Cooperate, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[1], buff=0.15, color=FOCUS)
        isolation = next_isolation
        self.play(FadeIn(isolation), FadeIn(teaching))
        self.pause('3.b')

        # ---- 3.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('3.c')

        # ---- 3.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Defect, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('3.d')

        # ---- 3.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('3.e')

        # ---- 3.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Cooperate, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('3.f')

        # ---- 3.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('3.g')

        # ---- 3.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Defect, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('3.h')

        # ---- 3.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('3.i')

        # ---- 3.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(isolation))
        self.remove(teaching)
        teaching = Tex('Both players have a dominant strategy: Defect.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[1][1]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('3.j')

        # ---- 3.k · Distinguish equilibrium from the efficient outcome.
        self.remove(teaching)
        teaching = Tex('Both players prefer (3, 3) to (1, 1).', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        efficient = Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=EFFICIENT)
        efficient.move_to(payoffs[0][0])
        self.play(FadeIn(efficient), FadeIn(teaching))
        self.pause('3.k')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 4.a · Original matrix 2; row payoff first.
        head = title('Play Or Movie')
        context = subtitle(head, 'Example 2')
        payoffs = [
            [
                VGroup(Tex('2', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('0', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
            [
                VGroup(Tex('0', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('2', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
        ]
        matrix = Table(
            payoffs,
            row_labels=[Tex('Play', color=ROW_PLAYER), Tex('Movie', color=ROW_PLAYER)],
            col_labels=[Tex('Play', color=COL_PLAYER), Tex('Movie', color=COL_PLAYER)],
            h_buff=1.1, v_buff=0.65,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.85)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).rotate(PI / 2)
        player_1.next_to(matrix, LEFT, buff=0.45)
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).next_to(matrix, UP, buff=0.3)
        game = VGroup(matrix, player_1, player_2).move_to([0, BODY_MID, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(matrix.get_col_labels()))
        self.play(FadeIn(player_1), FadeIn(matrix.get_row_labels()))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('4.a')

        # ---- 4.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[1], buff=0.15, color=FOCUS)
        isolation = next_isolation
        self.play(FadeIn(isolation), FadeIn(teaching))
        self.pause('4.b')

        # ---- 4.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('4.c')

        # ---- 4.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('4.d')

        # ---- 4.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('4.e')

        # ---- 4.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('4.f')

        # ---- 4.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('4.g')

        # ---- 4.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('4.h')

        # ---- 4.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('4.i')

        # ---- 4.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(isolation))
        self.remove(teaching)
        teaching = Tex('Two pure-strategy Nash equilibria: both Play or both Movie.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[0][0]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[1][1]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('4.j')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 5.a · Original matrix 3; row payoff first.
        head = title('Play Or Movie')
        context = subtitle(head, 'Example 3')
        payoffs = [
            [
                VGroup(Tex('2', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('2', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
            [
                VGroup(Tex('0', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
        ]
        matrix = Table(
            payoffs,
            row_labels=[Tex('Play', color=ROW_PLAYER), Tex('Movie', color=ROW_PLAYER)],
            col_labels=[Tex('Play', color=COL_PLAYER), Tex('Movie', color=COL_PLAYER)],
            h_buff=1.1, v_buff=0.65,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.85)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).rotate(PI / 2)
        player_1.next_to(matrix, LEFT, buff=0.45)
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).next_to(matrix, UP, buff=0.3)
        game = VGroup(matrix, player_1, player_2).move_to([0, BODY_MID, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(matrix.get_col_labels()))
        self.play(FadeIn(player_1), FadeIn(matrix.get_row_labels()))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('5.a')

        # ---- 5.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[1], buff=0.15, color=FOCUS)
        isolation = next_isolation
        self.play(FadeIn(isolation), FadeIn(teaching))
        self.pause('5.b')

        # ---- 5.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('5.c')

        # ---- 5.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('5.d')

        # ---- 5.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][0], buff=0.1, color=ROW_PLAYER),
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('5.e')

        # ---- 5.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('5.f')

        # ---- 5.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('5.g')

        # ---- 5.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('5.h')

        # ---- 5.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][2], buff=0.1, color=COL_PLAYER),
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('5.i')

        # ---- 5.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(isolation))
        self.remove(teaching)
        teaching = Tex('A tie means that both strategies are best responses.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[0][0]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[1][1]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('5.j')

        # ---- 5.k · Distinguish equilibrium from the efficient outcome.
        self.remove(teaching)
        teaching = Tex('Both Play is Pareto efficient; both Movie is not.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        efficient = Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=EFFICIENT)
        efficient.move_to(payoffs[0][0])
        efficient = DashedVMobject(efficient, num_dashes=36)
        self.play(FadeIn(efficient), FadeIn(teaching))
        self.pause('5.k')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 6.a · Original matrix 4; row payoff first.
        head = title('Play Or Movie')
        context = subtitle(head, 'Example 4')
        payoffs = [
            [
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('2', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
            [
                VGroup(Tex('2', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(',', color=INK),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.18),
            ],
        ]
        matrix = Table(
            payoffs,
            row_labels=[Tex('Play', color=ROW_PLAYER), Tex('Movie', color=ROW_PLAYER)],
            col_labels=[Tex('Play', color=COL_PLAYER), Tex('Movie', color=COL_PLAYER)],
            h_buff=1.1, v_buff=0.65,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.85)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).rotate(PI / 2)
        player_1.next_to(matrix, LEFT, buff=0.45)
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).next_to(matrix, UP, buff=0.3)
        game = VGroup(matrix, player_1, player_2).move_to([0, BODY_MID, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(matrix.get_col_labels()))
        self.play(FadeIn(player_1), FadeIn(matrix.get_row_labels()))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('6.a')

        # ---- 6.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[1], buff=0.15, color=FOCUS)
        isolation = next_isolation
        self.play(FadeIn(isolation), FadeIn(teaching))
        self.pause('6.b')

        # ---- 6.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('6.c')

        # ---- 6.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('6.d')

        # ---- 6.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('6.e')

        # ---- 6.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Play, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('6.f')

        # ---- 6.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('6.g')

        # ---- 6.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 1 chooses Movie, what is your best response?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=0.15, color=FOCUS)
        self.play(Transform(isolation, next_isolation), FadeIn(teaching))
        self.pause('6.h')

        # ---- 6.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][2], buff=0.1, color=COL_PLAYER),
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.play(FadeIn(responses))
        self.pause('6.i')

        # ---- 6.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(isolation))
        self.remove(teaching)
        teaching = Tex('Two pure-strategy Nash equilibria: different activities.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[0][1]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).move_to(payoffs[1][0]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('6.j')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 7.a · Original closing question; no invented payoff data.
        panel = RoundedRectangle(width=14.2, height=5.5, corner_radius=0.15,
                                 color=MUTED, stroke_width=2).move_to([0, BODY_MID, 0])
        question_head = Tex('Question', color=DEFINITION)
        question_head.move_to(panel.get_corner(UL) + RIGHT * 0.65 + DOWN * 0.65, aligned_edge=LEFT)
        question = VGroup(
            Tex('Ron and Harry share a room in the Gryffindor tower'),
            Tex('during the school year. Neither student is partial'),
            Tex('to chores, and would prefer not to tidy up their'),
            Tex(r'shared space.\ But both enjoy when the room is clean,'),
            Tex('and are more than willing to tidy the room if it'),
            Tex('means the space is neat.'),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).scale(0.8)
        question.next_to(question_head, DOWN, buff=0.45, aligned_edge=LEFT).shift(RIGHT * 0.35)
        head = title('Baby Game Theory')
        self.play(FadeIn(head), FadeIn(panel), FadeIn(question_head), FadeIn(question))
        self.pause('7.a')
