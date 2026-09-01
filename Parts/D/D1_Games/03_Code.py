# maniml 03_Code.py animation_0

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

# Configuration
CUSTOM_BLACK = '#1f1f1f'
CUSTOM_GREY = '#696969'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY

PIXEL_HEIGHT = 1080
FPS = 10
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT*2
config.frame_rate = FPS

class animation_0(Scene):

    """Animation 0 | Intro Sequence"""

    def construct(self):
        
    """ Definitions """
        
        colors = sns.color_palette("Blues", 50).as_hex()

        size = 1/6
        n_width = 2
        n_height = 3

        n_rows = len(range(-n_height,n_height+1))
        n_cols = len(range(-n_width,n_width+1))
        w_list = list(range(-n_width,n_width+1))*n_rows
        h_list = [i for i in range(-n_height,n_height+1) for x in 'a'*n_cols]
        block = list(zip(w_list,h_list)) # height: 7, width: 5
        
        string = 'MICROECONOMICS'
        letters = [raster_font[l] for l in string]
        
    """ Run """
                
        shift = 0
        centering = -39
        squares = []
        for l in letters:
            s = [Square(side_length=size, color=config.background_color).move_to(RIGHT*(w + shift*6 + centering)*size + DOWN*h*size) for w,h in [block[i] for i in l]]
            squares = squares + s
            shift = shift + 1
        
        Squares = VGroup(*squares)
        
        self.add(Squares)
        
        for i in range(5):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        part_label = Tex('{{Part D}} $|$ Baby Game Theory :)').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part D": RED,}
        ).scale(1.5).next_to(Squares, DOWN)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.to_edge(UP, buff=3))
        self.wait()


class animation_1(Scene):
    """Animation 1 |"""

    def construct(self):
        best_response_1 = Tex("{{Best Response}}: the strategy that gives a player").set_color_by_tex_to_color_map(
            {"Best Response": YELLOW,}
        ).to_edge(UP+LEFT).shift(DOWN)
        best_response_2 = Tex("the highest payoff, given the strategies chosen").to_edge(UP+LEFT).shift(DOWN*3/2+RIGHT)
        best_response_3 = Tex("by the other players in the game.").to_edge(UP+LEFT).shift(DOWN*2 +RIGHT)
        best_response = VGroup(best_response_1, best_response_2, best_response_3)
        
        dominant_strategy_1 = Tex("{{Dominant Strategy}}: a strategy that yields the").set_color_by_tex_to_color_map(
            {"Dominant Strategy": YELLOW,}
        ).to_edge(UP+LEFT).shift(DOWN*3)
        dominant_strategy_2 = Tex("highest payoff for a player regardless of").to_edge(UP+LEFT).shift(DOWN*3.5 +RIGHT)
        dominant_strategy_3 = Tex("the strategies chosen by the other players in the game.").to_edge(UP+LEFT).shift(DOWN*4 +RIGHT)
        dominant_strategy = VGroup(dominant_strategy_1, dominant_strategy_2, dominant_strategy_3)
        
        nash_equilibrium_1 = Tex("{{Nash Equilibrium}}: a set of strategies such that no player can").set_color_by_tex_to_color_map(
            {"Nash Equilibrium": YELLOW,}
        ).to_edge(UP+LEFT).shift(DOWN*5)
        nash_equilibrium_2 = Tex("improve their payoff by unilaterally changing strategy.").to_edge(UP+LEFT).shift(DOWN*5.5 +RIGHT)
        nash_equilibrium = VGroup(nash_equilibrium_1, nash_equilibrium_2)

        self.play(FadeIn(best_response))
        self.wait()
        self.play(FadeIn(dominant_strategy))
        self.wait()
        self.play(FadeIn(nash_equilibrium))
        self.wait()
        self.play(FadeOut(dominant_strategy), FadeOut(best_response), FadeOut(nash_equilibrium))


class animation_2(Scene):
    def construct(self):
        # Prisoner's Dilemma payoff matrix
        
        matrix = Table(
            [["3, 3", "0, 5"],
            ["5, 0", "1, 1"]],
            row_labels=[Text("Cooperate").set_color(RED), Text("Defect").set_color(RED)],
            col_labels=[Text("Cooperate").set_color(RED), Text("Defect").set_color(RED)]
        )        
        player_1 = Tex("Player 1").set_color(PINK).rotate(np.pi/2).scale(2).next_to(matrix, LEFT*2)
        player_2 = Tex("Player 2").set_color(BLUE).scale(2).next_to(matrix, UP*2)
        
        game_group = VGroup(matrix, player_1, player_2).move_to(ORIGIN)

        # Highlight best response
        
        self.play(FadeIn(matrix), FadeIn(player_1), FadeIn(player_2))
        self.wait()
        
        isolation = SurroundingRectangle(matrix.get_columns()[1], buff=1/2).set_color(YELLOW)
        self.play(Create(isolation))
        self.wait()
        
        br_p1_1 = SurroundingRectangle(matrix.get_rows()[2][1][0][0]).set_color(PINK)#.shift(LEFT/4)
        self.play(Create(br_p1_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p1_2 = SurroundingRectangle(matrix.get_rows()[2][2][0][0]).set_color(PINK)#.shift(LEFT/4)
        self.play(Create(br_p1_2))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_1 = SurroundingRectangle(matrix.get_columns()[2][1][0][2]).set_color(BLUE)
        self.play(Create(br_p2_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_2 = SurroundingRectangle(matrix.get_columns()[2][2][0][2]).set_color(BLUE)
        self.play(Create(br_p2_2))
        self.play(FadeOut(isolation))
        self.wait()
        
        equilibrium = VGroup(
            SurroundingRectangle(matrix.get_rows()[2][2], buff=1/2).set_color(RED),
            SurroundingRectangle(matrix.get_rows()[1][1], buff=1/2).set_color(GREEN),
        )
        self.play(Create(equilibrium))
        self.wait()


class animation_3(Scene):
    def construct(self):
        # Prisoner's Dilemma payoff matrix
        
        matrix = Table(
            [["2, 1", "0, 0"],
            ["0, 0", "1, 2"]],
            row_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)],
            col_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)]
        )        
        player_1 = Tex("Player 1").set_color(PINK).rotate(np.pi/2).scale(2).next_to(matrix, LEFT*2)
        player_2 = Tex("Player 2").set_color(BLUE).scale(2).next_to(matrix, UP*2)
        
        game_group = VGroup(matrix, player_1, player_2).move_to(ORIGIN)

        # Highlight best response
        
        self.play(FadeIn(matrix), FadeIn(player_1), FadeIn(player_2))
        self.wait()
        
        isolation = SurroundingRectangle(matrix.get_columns()[1], buff=1/2).set_color(YELLOW)
        self.play(Create(isolation))
        self.wait()
        
        br_p1_1 = SurroundingRectangle(matrix.get_rows()[1][1][0][0]).set_color(PINK)
        self.play(Create(br_p1_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p1_2 = SurroundingRectangle(matrix.get_rows()[2][2][0][0]).set_color(PINK)
        self.play(Create(br_p1_2))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_1 = SurroundingRectangle(matrix.get_columns()[1][1][0][2]).set_color(BLUE)
        self.play(Create(br_p2_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_2 = SurroundingRectangle(matrix.get_columns()[2][2][0][2]).set_color(BLUE)
        self.play(Create(br_p2_2))
        self.play(FadeOut(isolation))
        self.wait()
        
        equilibrium = VGroup(
            SurroundingRectangle(matrix.get_rows()[2][2], buff=1/2).set_color(RED),
            SurroundingRectangle(matrix.get_rows()[1][1], buff=1/2).set_color(RED),
        )
        self.play(Create(equilibrium))
        self.wait()


class animation_4(Scene):
    def construct(self):
        # Prisoner's Dilemma payoff matrix
        
        matrix = Table(
            [["2, 2", "1, 0"],
            ["0, 1", "1, 1"]],
            row_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)],
            col_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)]
        )        
        player_1 = Tex("Player 1").set_color(PINK).rotate(np.pi/2).scale(2).next_to(matrix, LEFT*2)
        player_2 = Tex("Player 2").set_color(BLUE).scale(2).next_to(matrix, UP*2)
        
        game_group = VGroup(matrix, player_1, player_2).move_to(ORIGIN)

        # Highlight best response
        
        self.play(FadeIn(matrix), FadeIn(player_1), FadeIn(player_2))
        self.wait()
        
        isolation = SurroundingRectangle(matrix.get_columns()[1], buff=1/2).set_color(YELLOW)
        self.play(Create(isolation))
        self.wait()
        
        br_p1_1 = VGroup(
            SurroundingRectangle(matrix.get_rows()[1][1][0][0]).set_color(PINK),
        )
        self.play(Create(br_p1_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p1_2 = VGroup(
            SurroundingRectangle(matrix.get_rows()[2][2][0][0]).set_color(PINK),
            SurroundingRectangle(matrix.get_rows()[1][2][0][0]).set_color(PINK),
        )
        self.play(Create(br_p1_2))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_1 = VGroup(
            SurroundingRectangle(matrix.get_columns()[1][1][0][2]).set_color(BLUE),
        )
        self.play(Create(br_p2_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_2 = VGroup(
            SurroundingRectangle(matrix.get_columns()[2][2][0][2]).set_color(BLUE),
            SurroundingRectangle(matrix.get_columns()[1][2][0][2]).set_color(BLUE),
        )
        
        self.play(Create(br_p2_2))
        self.play(FadeOut(isolation))
        self.wait()
        
        equilibrium = VGroup(
            SurroundingRectangle(matrix.get_rows()[2][2], buff=1/2).set_color(RED),
            SurroundingRectangle(matrix.get_rows()[1][1], buff=1/2).set_color(RED),
            SurroundingRectangle(matrix.get_rows()[1][1], buff=1/2).set_color(GREEN),
        )
        self.play(Create(equilibrium))
        self.wait()


class animation_5(Scene):
    def construct(self):
        
        matrix = Table(
            [["1, 0", "2, 1"],
            ["2, 1", "1, 1"]],
            row_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)],
            col_labels=[Text("Play").set_color(RED), Text("Movie").set_color(RED)]
        )        
        player_1 = Tex("Player 1").set_color(PINK).rotate(np.pi/2).scale(2).next_to(matrix, LEFT*2)
        player_2 = Tex("Player 2").set_color(BLUE).scale(2).next_to(matrix, UP*2)
        
        game_group = VGroup(matrix, player_1, player_2).move_to(ORIGIN)

        # Highlight best response
        
        self.play(FadeIn(matrix), FadeIn(player_1), FadeIn(player_2))
        self.wait()
        
        isolation = SurroundingRectangle(matrix.get_columns()[1], buff=1/2).set_color(YELLOW)
        self.play(Create(isolation))
        self.wait()
        
        br_p1_1 = VGroup(
            SurroundingRectangle(matrix.get_rows()[2][1][0][0]).set_color(PINK),
        )
        self.play(Create(br_p1_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_columns()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p1_2 = VGroup(
            SurroundingRectangle(matrix.get_rows()[1][2][0][0]).set_color(PINK),
        )
        self.play(Create(br_p1_2))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[1], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_1 = VGroup(
            SurroundingRectangle(matrix.get_columns()[2][1][0][2]).set_color(BLUE),
        )
        self.play(Create(br_p2_1))
        self.wait()
        
        new_isolation = SurroundingRectangle(matrix.get_rows()[2], buff=1/2).set_color(YELLOW)
        self.play(Transform(isolation, new_isolation))
        self.wait()
        
        br_p2_2 = VGroup(
            SurroundingRectangle(matrix.get_columns()[2][2][0][2]).set_color(BLUE),
            SurroundingRectangle(matrix.get_columns()[1][2][0][2]).set_color(BLUE),
        )
        
        self.play(Create(br_p2_2))
        self.play(FadeOut(isolation))
        self.wait()
        
        equilirium = VGroup(
            SurroundingRectangle(matrix.get_rows()[1][2], buff=1/2).set_color(RED),
            SurroundingRectangle(matrix.get_rows()[2][1], buff=1/2).set_color(RED)
        )
        self.play(Create(equilirium))
        self.wait()


class animation_6(Scene):
    def construct(self):
        
        question_title = Text("Question").scale(1.5).to_edge(UP, buff=1).set_color(PURPLE)
        question = Paragraph(
            "Ron and Harry share a room in the Gryffindor tower",
            "  during the school year. Neither student is partial",
            "  to chores, and would prefer not to tidy up their",
            "  shared space. But both enjoy when the room is clean,",
            "  and are more than willing to tidy the room if it",
            "  means the space is neat.", 
            width=12
        ).next_to(question_title, DOWN*2)
        
        self.play(FadeIn(question_title), FadeIn(question))
        self.wait()
