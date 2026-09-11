# maniml 03_Code.py __

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

class __(Scene):

    """Animation -1 | Last Time..."""

    def construct(self):
        text = Tex('Last Time...').scale(3)
        self.play(FadeIn(text), run_time=1/2)
        self.wait()
        self.play(FadeOut(text), run_time=1/2)
        self.wait()


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
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        part_label = Tex('{{Part B}} $|$ Episode 0').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part B": BLUE,}
        ).scale(3).next_to(Squares, DOWN)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.move_to(0))
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        
        self.wait()


class animation_1(Scene):

    """Animation 1 | Show the PPF with gains"""

    def construct(self):
        
    """ Definitions """
        
        PPF_axis = Axes(            
            x_range=[0, 100, 100],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "decimal_number_config": {
                    "num_decimal_places":0,
                }
            },
            y_range=[0, 100, 100],
            y_length = 7,
            y_axis_config={
                "decimal_number_config": {
                    "num_decimal_places":0,
                }
            },
            tips=False,
        )
        
        part_label = Tex('Part B').set_color(BLUE).scale(2).to_edge(UP+LEFT, buff=1)
        
    """ Starting Objects """
        
        axes = PPF_axis.to_edge(RIGHT).scale(0.8)
        
        y_label = axes.get_y_axis_label("A").shift(LEFT*2/3)
        x_label = axes.get_x_axis_label("B").shift(DOWN/2)
        
        alpha = ValueTracker(1)

        def Linear_PPF(x):
            return 100 - x
        
        def Bowed_PPF(x):
            return (100**alpha.get_value() - (x)**alpha.get_value())**(1/alpha.get_value())
        
        def PPF_Group():
            linear_ppf = axes.plot(Linear_PPF, color=GREY, x_range=(0, 100))
            linear_ppf.z_index = -1

            bowed_ppf = axes.plot(Bowed_PPF, color=PINK, x_range=(0, 100, .1))
            bowed_ppf.z_index = -1
            
            return VGroup(linear_ppf, bowed_ppf)
        
        ppf_group = always_redraw(PPF_Group)

        self.add(part_label, axes, y_label, x_label, ppf_group)
                
        questions = [
            Tex('- Coordinate large groups').set_color(YELLOW).to_edge(UP+LEFT, buff=1).shift(DOWN*2),
            Tex('- Which point on the PPF').set_color(YELLOW).to_edge(UP+LEFT, buff=1).shift(DOWN*3),
            Tex('- Who benefits').set_color(YELLOW).to_edge(UP+LEFT, buff=1).shift(DOWN*4)
        ]
        
        arrow = Arrow(start=RIGHT*3, end=RIGHT*3.8 + UP*0.8).set_color(YELLOW)
        self.play(FadeIn(arrow), alpha.animate.set_value(1.5), FadeIn(questions[0]))
        self.wait()
        
        x1 = 30
        y1 = Bowed_PPF(x1)
        p1 = axes.coords_to_point(x1,y1)
        dot1 = Dot(p1).set_color(WHITE)
        
        dot1_l = Tex('Option 1').next_to(dot1,RIGHT).set_color(YELLOW)
        
        x2 = 80
        y2 = Bowed_PPF(x2)
        p2 = axes.coords_to_point(x2,y2)
        dot2 = Dot(p2).set_color(WHITE)
        
        dot2_l = Tex('Option 2').next_to(dot2,UP+RIGHT).set_color(YELLOW)
        
        self.play(FadeIn(dot1), FadeIn(dot1_l), FadeIn(questions[1]))
        self.play(FadeIn(dot2), FadeIn(dot2_l))
        self.wait()
        
        self.play(FadeIn(questions[2]))
        self.wait()
