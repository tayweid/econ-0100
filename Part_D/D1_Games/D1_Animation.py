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
        DIAMOND_ANGLE = -PI / 4
        CELL_SIDE = 1.5
        CHOICE_FILL_OPACITY = 0.12
        CELL_BOX_WIDTH = CELL_SIDE - 0.15
        CELL_BOX_HEIGHT = CELL_BOX_WIDTH
        GAME_CENTER = DOWN * 0.5
        # Unit vectors for the original table's right/up directions after rotation.
        TABLE_RIGHT = (RIGHT + DOWN) / 2**0.5
        TABLE_UP = (RIGHT + UP) / 2**0.5

        # ---- 0.a · Original D0 opening: the wordmark stays over the taxonomy.
        squares = bumper_raster(self)
        flicker(self, squares, rounds=5)
        part = Tex(r'{{Part D}} $|$ Strategic Interaction', color=CAPTION)
        part.set_color_by_tex('Part D', TITLE).scale(1.5).next_to(squares, DOWN)
        opening = VGroup(squares, part)
        self.play(FadeIn(part), opening.animate.to_edge(UP, buff=1))
        self.pause('0.a')

        # ---- 1.a · Copy D0's full-table reveal beneath the retained opening.
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.7).next_to(opening, DOWN).shift(RIGHT)
        self.play(FadeIn(taxonomy))
        self.pause('1.a')

        # ---- 1.b · Part A: the original generous box around private goods.
        part_a = Tex(r'Part~A', color=FOCUS).scale(1.6).to_corner(UL).shift(DOWN * 3)
        part_b = Tex(r'Part~B', color=GREEN).scale(1.6).to_corner(UL).shift(DOWN * 4)
        part_c = Tex(r'Part~C', color=BLUE).scale(1.6).to_corner(UL).shift(DOWN * 5)
        box = SurroundingRectangle(taxonomy.get_entries_without_labels((1, 1)),
                                   buff=0.5, color=FOCUS)
        self.play(FadeIn(box), FadeIn(part_a))
        self.pause('1.b')

        # ---- 1.c · Part B recolors the SAME box green; it does not move.
        self.play(box.animate.set_color(GREEN), FadeIn(part_b))
        self.pause('1.c')

        # ---- 1.d · Preserve D0's half-unit downward shift for Part C.
        self.play(box.animate.shift(DOWN * 0.5).set_color(BLUE), FadeIn(part_c))
        self.pause('1.d')

        # ---- 1.e · Same box, same size: move to common resources and turn red.
        self.play(box.animate.move_to(taxonomy.get_entries_without_labels((2, 1))).set_color(RED))
        self.pause('1.e')
        self.play(FadeOut(box), FadeOut(taxonomy), FadeOut(part_a), FadeOut(part_b), FadeOut(part_c))
        # The requested next topic replaces D0's fishing-simulation rules.
        self.play(FadeOut(opening))
        self.clear()

        # ---- 3.a · Original matrix 1; row payoff first.
        head = title("Prisoner's Dilemma")
        payoffs = [
            [
                VGroup(Tex('3', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('3', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('0', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('5', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
            [
                VGroup(Tex('5', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
        ]
        # Square data cells turn clockwise; text counter-rotates in place.
        for row in payoffs:
            for cell in row:
                cell.scale(0.85)
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
        row_labels = VGroup(Tex(r'\textsf{Cooperate}', color=CAPTION), Tex(r'\textsf{Defect}', color=CAPTION))
        col_labels = VGroup(Tex(r'\textsf{Cooperate}', color=CAPTION), Tex(r'\textsf{Defect}', color=CAPTION))
        row_labels.scale(0.7)
        col_labels.scale(0.7)
        for index in range(2):
            offset = (0.5 - index) * CELL_SIDE
            row_anchor = GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP
            col_anchor = GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP
            row_labels[index].move_to(row_anchor + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[index].move_to(col_anchor + RIGHT * 0.3, aligned_edge=LEFT)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).move_to([-2.8, 2.0, 0])
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).move_to([2.8, 2.0, 0])
        teaching = Tex('Player 1 can choose Cooperate or Defect.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_1), FadeIn(row_labels), FadeIn(teaching))
        self.pause('3.a1')
        self.remove(teaching)
        teaching = Tex('Player 2 has the same two choices.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(player_2), FadeIn(col_labels), FadeIn(teaching))
        self.pause('3.a2')

        # ---- 3.a2r · Player 2 chooses Cooperate.
        self.remove(teaching)
        teaching = Tex('What if Player 2 cooperates?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        col_choice = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        col_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        col_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeIn(col_choice), FadeIn(col_shade), FadeIn(teaching), run_time=0.4)
        self.pause('3.a2r')

        # ---- 3.a3q · Player 1 chooses Cooperate. What is their payoff?
        self.remove(teaching)
        teaching = Tex('If Player 1 also cooperates, what payoff do they receive?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        self.play(FadeIn(row_choice), FadeIn(teaching), run_time=0.4)
        self.pause('3.a3q')

        # ---- 3.a3 · If both cooperate, Player 1 receives 3.
        self.remove(teaching)
        teaching = Tex('If both cooperate, Player 1 receives 3.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[0][0][0]), FadeIn(payoffs[0][0][1]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a3')

        # ---- 3.a4 · If both cooperate, Player 2 receives 3.
        self.remove(teaching)
        teaching = Tex('If both cooperate, Player 2 receives 3.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[0][0][2]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a4')

        # ---- 3.a5q · Player 1 chooses Defect. What is their payoff?
        self.remove(teaching)
        teaching = Tex('If Player 2 cooperates, what if Player 1 defects?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[1], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        self.play(Transform(row_choice, next_choice), FadeIn(teaching), run_time=0.4)
        self.pause('3.a5q')

        # ---- 3.a5 · If only Player 1 defects, Player 1 receives 5.
        self.remove(teaching)
        teaching = Tex('If only Player 1 defects, Player 1 receives 5.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[1][0][0]), FadeIn(payoffs[1][0][1]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a5')

        # ---- 3.a6 · Player 2's payoff from continuing to cooperate.
        self.remove(teaching)
        teaching = Tex('If only Player 1 defects, Player 2 receives 0.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[1][0][2]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a6')

        # ---- 3.a6q · Switch to Player 2: Player 1's Defect is now fixed.
        self.remove(teaching)
        teaching = Tex("Now consider Player 2 switching to Defect.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                              stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        row_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(FadeOut(col_shade), FadeIn(row_shade), FadeIn(teaching), run_time=0.4)
        self.pause('3.a6q')

        # ---- 3.a6r · Player 2 considers Defect while Player 1 stays fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 also defects, what payoff do they receive?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        self.play(Transform(col_choice, next_choice), FadeIn(teaching), run_time=0.4)
        self.pause('3.a6r')

        # ---- 3.a8 · Reveal Player 2's gain before switching perspective back.
        self.remove(teaching)
        teaching = Tex('If both defect, Player 2 receives 1.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[1][1][2]), FadeIn(payoffs[1][1][1]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a8')

        # ---- 3.a7 · If both defect, Player 1 receives 1.
        self.remove(teaching)
        teaching = Tex('If both defect, Player 1 receives 1.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[1][1][0]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a7')

        # ---- 3.a7q · Return to Player 1: Player 2's Defect is now fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 defects, consider Player 1's choice.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        col_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                              stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        col_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeOut(row_shade), FadeIn(col_shade), FadeIn(teaching), run_time=0.4)
        self.pause('3.a7q')

        # ---- 3.a9q · Player 1 chooses Cooperate. What is their payoff?
        self.remove(teaching)
        teaching = Tex('If Player 2 defects, what if Player 1 cooperates?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        self.play(Transform(row_choice, next_choice), FadeIn(teaching), run_time=0.4)
        self.pause('3.a9q')

        # ---- 3.a9 · If only Player 2 defects, Player 1 receives 0.
        self.remove(teaching)
        teaching = Tex('If only Player 2 defects, Player 1 receives 0.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[0][1][0]), FadeIn(payoffs[0][1][1]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a9')

        # ---- 3.a · If only Player 2 defects, Player 2 receives 5.
        self.remove(teaching)
        teaching = Tex('If only Player 2 defects, Player 2 receives 5.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(payoffs[0][1][2]), FadeIn(teaching), run_time=0.4)
        self.pause('3.a')

        # ---- 3.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 cooperates, which choice gives Player 1 more?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeOut(row_choice), Transform(col_choice, next_choice), Transform(col_shade, next_shade),
                  FadeIn(teaching))
        self.pause('3.b')

        # ---- 3.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Defect: $5 > 3$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('3.c')

        # ---- 3.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex('If Player 2 defects, which choice gives Player 1 more?', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(Transform(col_choice, next_choice), Transform(col_shade, next_shade),
                  FadeIn(teaching))
        self.pause('3.d')

        # ---- 3.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Defect: $1 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('3.e')

        # ---- 3.e1 · Both comparisons establish Player 1's dominant strategy.
        self.remove(teaching)
        teaching = Tex('Defect is best for Player 1 against either choice.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeOut(col_choice), FadeOut(col_shade), FadeIn(teaching))
        self.pause('3.e1')

        # ---- 3.e2 · Slide the worked example left and drop the shared grey divider.
        game_objects = [mob for mob in self.mobjects if mob is not head and mob is not teaching]
        definition_divider = Line([0.3, 2.5, 0], [0.3, -3.0, 0],
                                  color=MUTED, stroke_width=1, stroke_opacity=0.5)
        best_response = VGroup(
            Tex('Best Response', color=DEFINITION),
            Tex('The strategy that gives a player', color=INK),
            Tex('the highest payoff, given the strategies', color=INK),
            Tex('chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        best_response.move_to([0.85, 1.65, 0], aligned_edge=UL)
        dominant = VGroup(
            Tex('Dominant Strategy', color=DEFINITION),
            Tex('A strategy that yields the highest payoff', color=INK),
            Tex('for a player regardless of the strategies', color=INK),
            Tex('chosen by the other players in the game.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        dominant.next_to(best_response, DOWN, buff=0.65, aligned_edge=LEFT)
        self.play(*[mob.animate.shift(LEFT * 3.7) for mob in game_objects],
                  GrowFromEdge(definition_divider, UP), FadeOut(teaching), run_time=1.0)
        self.play(FadeIn(best_response))
        self.pause('3.e2')

        # ---- 3.e3 · Add the second definition only on the next click.
        self.play(FadeIn(dominant))
        self.pause('3.e3')
        self.play(FadeOut(best_response), FadeOut(dominant), FadeOut(definition_divider))
        self.play(*[mob.animate.shift(RIGHT * 3.7) for mob in game_objects], run_time=1.0)

        # ---- 3.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 cooperates, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        row_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        row_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(FadeIn(row_choice), FadeIn(row_shade),
                  FadeIn(teaching))
        self.pause('3.f')

        # ---- 3.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Defect: $5 > 3$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('3.g')

        # ---- 3.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 defects, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[1], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(Transform(row_choice, next_choice), Transform(row_shade, next_shade),
                  FadeIn(teaching))
        self.pause('3.h')

        # ---- 3.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Defect: $1 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('3.i')

        # ---- 3.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(row_choice), FadeOut(row_shade))
        self.remove(teaching)
        teaching = Tex('At (Defect, Defect), neither player gains by switching alone.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('3.j')

        # ---- 3.j1 · Define Nash equilibrium beside the highlighted outcome.
        game_objects = [mob for mob in self.mobjects if mob is not head and mob is not teaching]
        definition_divider = Line([0.3, 2.5, 0], [0.3, -3.0, 0],
                                  color=MUTED, stroke_width=1, stroke_opacity=0.5)
        nash_definition = VGroup(
            Tex('Nash Equilibrium', color=DEFINITION),
            Tex('A set of strategies such that no player', color=INK),
            Tex('can improve their payoff by unilaterally', color=INK),
            Tex('changing strategy.', color=INK),
        ).arrange(DOWN, buff=0.12, aligned_edge=LEFT).scale(0.7)
        nash_definition.move_to([0.85, 1.65, 0], aligned_edge=UL)
        self.play(*[mob.animate.shift(LEFT * 3.7) for mob in game_objects],
                  GrowFromEdge(definition_divider, UP), FadeOut(teaching), run_time=1.0)
        self.play(FadeIn(nash_definition))
        self.pause('3.j1')
        self.play(FadeOut(nash_definition), FadeOut(definition_divider))
        self.play(*[mob.animate.shift(RIGHT * 3.7) for mob in game_objects], run_time=1.0)

        # ---- 3.k · Distinguish equilibrium from the efficient outcome.
        self.remove(teaching)
        teaching = Tex('Both players prefer (3, 3) to (1, 1).', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        efficient = Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=EFFICIENT).rotate(DIAMOND_ANGLE)
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
                VGroup(Tex('2', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('0', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
            [
                VGroup(Tex('0', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('2', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
        ]
        # Square data cells turn clockwise; text counter-rotates in place.
        for row in payoffs:
            for cell in row:
                cell.scale(0.85)
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
        row_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        col_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        row_labels.scale(0.7)
        col_labels.scale(0.7)
        for index in range(2):
            offset = (0.5 - index) * CELL_SIDE
            row_anchor = GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP
            col_anchor = GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP
            row_labels[index].move_to(row_anchor + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[index].move_to(col_anchor + RIGHT * 0.3, aligned_edge=LEFT)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).move_to([-2.8, 2.0, 0])
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).move_to([2.8, 2.0, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(col_labels))
        self.play(FadeIn(player_1), FadeIn(row_labels))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('4.a')

        # ---- 4.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Play, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        col_choice = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        col_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        col_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeIn(col_choice), FadeIn(col_shade), FadeIn(teaching))
        self.pause('4.b')

        # ---- 4.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Play: $2 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('4.c')

        # ---- 4.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Movie, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(Transform(col_choice, next_choice), Transform(col_shade, next_shade),
                  FadeIn(teaching))
        self.pause('4.d')

        # ---- 4.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Movie: $1 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('4.e')

        # ---- 4.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Play, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        row_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        row_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(FadeOut(col_choice), FadeOut(col_shade), FadeIn(row_choice), FadeIn(row_shade),
                  FadeIn(teaching))
        self.pause('4.f')

        # ---- 4.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Play: $1 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('4.g')

        # ---- 4.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Movie, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[1], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(Transform(row_choice, next_choice), Transform(row_shade, next_shade),
                  FadeIn(teaching))
        self.pause('4.h')

        # ---- 4.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Movie: $2 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('4.i')

        # ---- 4.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(row_choice), FadeOut(row_shade))
        self.remove(teaching)
        teaching = Tex('Two pure-strategy Nash equilibria: both Play or both Movie.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[0][0]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1]),
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
                VGroup(Tex('2', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('2', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
            [
                VGroup(Tex('0', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
        ]
        # Square data cells turn clockwise; text counter-rotates in place.
        for row in payoffs:
            for cell in row:
                cell.scale(0.85)
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
        row_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        col_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        row_labels.scale(0.7)
        col_labels.scale(0.7)
        for index in range(2):
            offset = (0.5 - index) * CELL_SIDE
            row_anchor = GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP
            col_anchor = GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP
            row_labels[index].move_to(row_anchor + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[index].move_to(col_anchor + RIGHT * 0.3, aligned_edge=LEFT)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).move_to([-2.8, 2.0, 0])
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).move_to([2.8, 2.0, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(col_labels))
        self.play(FadeIn(player_1), FadeIn(row_labels))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('5.a')

        # ---- 5.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Play, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        col_choice = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        col_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        col_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeIn(col_choice), FadeIn(col_shade), FadeIn(teaching))
        self.pause('5.b')

        # ---- 5.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Play: $2 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('5.c')

        # ---- 5.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Movie, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(Transform(col_choice, next_choice), Transform(col_shade, next_shade),
                  FadeIn(teaching))
        self.pause('5.d')

        # ---- 5.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][0], buff=0.1, color=ROW_PLAYER),
            SurroundingRectangle(payoffs[1][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex('Player 1 receives 1 either way: both choices are best responses.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('5.e')

        # ---- 5.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Play, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        row_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        row_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(FadeOut(col_choice), FadeOut(col_shade), FadeIn(row_choice), FadeIn(row_shade),
                  FadeIn(teaching))
        self.pause('5.f')

        # ---- 5.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][0][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Play: $2 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('5.g')

        # ---- 5.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Movie, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[1], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(Transform(row_choice, next_choice), Transform(row_shade, next_shade),
                  FadeIn(teaching))
        self.pause('5.h')

        # ---- 5.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][2], buff=0.1, color=COL_PLAYER),
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex('Player 2 receives 1 either way: both choices are best responses.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('5.i')

        # ---- 5.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(row_choice), FadeOut(row_shade))
        self.remove(teaching)
        teaching = Tex('Both Play and both Movie are Nash equilibria.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[0][0]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1]),
        )
        self.play(FadeIn(equilibria), FadeIn(teaching))
        self.pause('5.j')

        # ---- 5.k · Distinguish equilibrium from the efficient outcome.
        self.remove(teaching)
        teaching = Tex('Both Play is Pareto efficient; both Movie is not.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        efficient = Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=EFFICIENT).rotate(DIAMOND_ANGLE)
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
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('0', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('2', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
            [
                VGroup(Tex('2', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
                VGroup(Tex('1', color=ROW_PLAYER), Tex(r'$|$', color=MUTED).stretch(1.3, 1),
                       Tex('1', color=COL_PLAYER)).arrange(RIGHT, buff=0.3),
            ],
        ]
        # Square data cells turn clockwise; text counter-rotates in place.
        for row in payoffs:
            for cell in row:
                cell.scale(0.85)
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
        row_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        col_labels = VGroup(Tex(r'\textsf{Play}', color=CAPTION), Tex(r'\textsf{Movie}', color=CAPTION))
        row_labels.scale(0.7)
        col_labels.scale(0.7)
        for index in range(2):
            offset = (0.5 - index) * CELL_SIDE
            row_anchor = GAME_CENTER - CELL_SIDE * TABLE_RIGHT + offset * TABLE_UP
            col_anchor = GAME_CENTER - offset * TABLE_RIGHT + CELL_SIDE * TABLE_UP
            row_labels[index].move_to(row_anchor + LEFT * 0.3, aligned_edge=RIGHT)
            col_labels[index].move_to(col_anchor + RIGHT * 0.3, aligned_edge=LEFT)
        player_1 = Tex('Player 1', color=ROW_PLAYER).scale(0.8).move_to([-2.8, 2.0, 0])
        player_2 = Tex('Player 2', color=COL_PLAYER).scale(0.8).move_to([2.8, 2.0, 0])
        teaching = Tex('Payoffs: Player 1 first, Player 2 second.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(context), FadeIn(matrix.get_horizontal_lines()),
                  FadeIn(matrix.get_vertical_lines()))
        self.play(FadeIn(player_2), FadeIn(col_labels))
        self.play(FadeIn(player_1), FadeIn(row_labels))
        self.play(FadeIn(teaching))
        for row in payoffs:
            for cell in row:
                self.play(FadeIn(cell), run_time=0.4)
        self.pause('6.a')

        # ---- 6.b · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Play, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        col_choice = Underline(col_labels[0], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        col_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        col_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(FadeIn(col_choice), FadeIn(col_shade), FadeIn(teaching))
        self.pause('6.b')

        # ---- 6.c · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Movie: $2 > 1$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('6.c')

        # ---- 6.d · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 2 chooses Movie, what is Player 1's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(col_labels[1], buff=0.1, stroke_color=COL_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=CELL_SIDE, height=2 * CELL_SIDE,
                               stroke_width=0, fill_color=COL_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_RIGHT).set_z_index(-1)
        self.play(Transform(col_choice, next_choice), Transform(col_shade, next_shade),
                  FadeIn(teaching))
        self.pause('6.d')

        # ---- 6.e · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][0], buff=0.1, color=ROW_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 1's best response is Play: $2 > 1$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('6.e')

        # ---- 6.f · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Play, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        row_choice = Underline(row_labels[0], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        row_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        row_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER + CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(FadeOut(col_choice), FadeOut(col_shade), FadeIn(row_choice), FadeIn(row_shade),
                  FadeIn(teaching))
        self.pause('6.f')

        # ---- 6.g · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[0][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex("Player 2's best response is Movie: $1 > 0$.", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('6.g')

        # ---- 6.h · Hold the other player's choice fixed.
        self.remove(teaching)
        teaching = Tex("If Player 1 chooses Movie, what is Player 2's best response?", color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        next_choice = Underline(row_labels[1], buff=0.1, stroke_color=ROW_PLAYER, stroke_width=3, stretch_factor=1)
        next_shade = Rectangle(width=2 * CELL_SIDE, height=CELL_SIDE,
                               stroke_width=0, fill_color=ROW_PLAYER, fill_opacity=CHOICE_FILL_OPACITY)
        next_shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER - CELL_SIDE / 2 * TABLE_UP).set_z_index(-2)
        self.play(Transform(row_choice, next_choice), Transform(row_shade, next_shade),
                  FadeIn(teaching))
        self.pause('6.h')

        # ---- 6.i · Preserve every best response, including ties.
        responses = VGroup(
            SurroundingRectangle(payoffs[1][0][2], buff=0.1, color=COL_PLAYER),
            SurroundingRectangle(payoffs[1][1][2], buff=0.1, color=COL_PLAYER),
        )
        self.remove(teaching)
        teaching = Tex('Player 2 receives 1 either way: both choices are best responses.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        self.play(FadeIn(responses), FadeIn(teaching))
        self.pause('6.i')

        # ---- 6.j · A Nash cell contains a best response for both players.
        self.play(FadeOut(row_choice), FadeOut(row_shade))
        self.remove(teaching)
        teaching = Tex('Two pure-strategy Nash equilibria: different activities.', color=DEFINITION)
        teaching.scale(DEFINITION_SCALE).to_edge(DOWN, buff=DEFINITION_BOTTOM).set_x(0)
        equilibria = VGroup(
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[0][1]),
            Rectangle(width=CELL_BOX_WIDTH, height=CELL_BOX_HEIGHT, color=NASH).rotate(DIAMOND_ANGLE).move_to(payoffs[1][0]),
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
