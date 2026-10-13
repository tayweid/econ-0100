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

    """Animation 0 | Show the taxonomy"""

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
            
        part_label = Tex('{{Part D}} $|$ Common Resources').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part D": RED,}
        ).scale(1.5).next_to(Squares, DOWN)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.to_edge(UP, buff=1))
        
        self.wait()
        
    """ Starting Objects """
        
        taxonomy = Table(
            [["Private \n Goods", "Club \n Goods"],
            ["Common \n Resources", "Public \n Goods"]],
            row_labels=[Text("Excludable").set_color(RED), Text("Non-Excludable").set_color(RED)],
            col_labels=[Text("Rival").set_color(RED), Text("Non-Rival").set_color(RED)]
        ).scale(0.7).next_to(group, DOWN).shift(RIGHT)
        #for e in [3,4,6,7]:
        #    taxonomy.get_elements()[e].set_color(CUSTOM_BLACK)
        
        self.play(FadeIn(taxonomy))
        
        part_list = [
            Tex('Part A').scale(1.6).set_color(YELLOW).to_edge(LEFT+UP).shift(DOWN*3),
            Tex('Part B').scale(1.6).set_color(GREEN).to_edge(LEFT+UP).shift(DOWN*4),
            Tex('Part C').scale(1.6).set_color(BLUE).to_edge(LEFT+UP).shift(DOWN*5),
        ]
        
        box = SurroundingRectangle(taxonomy.get_elements()[3], buff=1/2).set_color(YELLOW)
        self.play(FadeIn(box), FadeIn(part_list[0]))
        self.wait()
        
        self.play(box.animate.set_color(GREEN), FadeIn(part_list[1]))
        self.wait()
        
        self.play(box.animate.shift(DOWN*1/2).set_color(BLUE), FadeIn(part_list[2]))
        self.wait()
        
        self.play(box.animate.move_to(taxonomy.get_elements()[6]).set_color(RED))
        self.wait()
        
        self.play(FadeOut(*[box, taxonomy]), FadeOut(*part_list))
        self.wait()
        
        
        new_part_label = Tex('{{Part D}} $|$ Common Resources Simulation').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part D": RED,}
        ).scale(1.5).next_to(Squares, DOWN)
        self.play(Transform(part_label, new_part_label))
        
        rule_label = Tex('{{Rules}}').set_color(YELLOW).scale(1.5).to_edge(UP+LEFT, buff=1).shift(DOWN*3 + RIGHT*2)
        
        rules = [
            Tex('- One lake, five firms').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*4 + RIGHT*2),
            Tex('- Each round, choose your harvest').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*4.5 + RIGHT*2),
            Tex('- Fish population doubles each round').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*5 + RIGHT*2),
            Tex('- Carrying capacity is 20,000 fish').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*5.5 + RIGHT*2),
            Tex('- Maximize harvest after 4 rounds').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*6 + RIGHT*2),
        ]
        
        self.play(FadeIn(rule_label))
        for rule in rules:
            self.play(FadeIn(rule))
            self.wait()
