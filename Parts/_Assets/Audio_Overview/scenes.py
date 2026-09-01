# scenes.py
from manim import *
import random
import seaborn as sns

## https://docs.manim.community/en/v0.10.0/reference.html

import os
import seaborn as sns
import pandas as pd
from datetime import date
from IPython.display import Image
import nbformat
import warnings
from manim import *
import random

""" Intro Sequence """

# https://render.fontstruct.com/renderer/render?id=261025&v=5afd1b5b&w=800&h=400&sz=100&wr=1&pds=all
# Blues, Reds, Greys, Purples, Greens, Oranges
# https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f
# Paired, Spectral, Pastel1,  
# PuBu, PuBuGn, CMRmap, GnBu, OrRd, PRGn, PiYG, PuOr, PuRd, RdBu, RdGy, RdPu, RdYlBu, RdYlGn, YlGn, YlGnBu, YlOrBr

raster_font = {
    ' ': [],
    'A': [],
    'B': [],
    'C': [1,2,3,5,9,10,15,20,25,29,31,32,33],
    'D': [],
    'E': [0,1,2,3,4,5,10,15,16,17,18,20,25,30,31,32,33,34],
    'F': [],
    'G': [],
    'H': [],
    'I': [1,2,3,7,12,17,22,27,31,32,33],
    'J': [],
    'K': [],
    'L': [],
    'M': [0,4,5,6,8,9,10,12,14,15,19,20,24,25,29,30,34],
    'N': [0,4,5,6,9,10,12,14,15,18,19,20,24,25,29,30,34],
    'O': [1,2,3,5,9,10,14,15,19,20,24,25,29,31,32,33],
    'P': [],
    'Q': [],
    'R': [0,1,2,3,5,9,10,14,15,16,17,18,20,23,25,29,30,34],
    'S': [1,2,3,5,9,10,16,17,18,24,25,29,31,32,33],
    'T': [],
    'U': [],
    'V': [],
    'W': [],
    'X': [],
    'Y': [],
    'Z': [],
}
sns.color_palette("YlGn", 10).as_hex()

class Overview(Scene):

    def construct(self):
        
        """ Definitions """
        
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
        self.squares = []
        for l in letters:
            s = [Square(side_length=size, color=config.background_color).move_to(RIGHT*(w + shift*6 + centering)*size + DOWN*h*size) for w,h in [block[i] for i in l]]
            self.squares = self.squares + s
            shift = shift + 1
        
        self.Squares = VGroup(*self.squares)
        self.add(self.Squares)

    def play_intro(self, part='Part A', chapter='Chapter 1'):
        
        colors = sns.color_palette("Blues", 50).as_hex()
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in self.squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        part_label = Tex('{{part}} $|$ {{chapter}}').set_color(GREY).set_color_by_tex_to_color_map(
            {part: BLUE,}
        ).scale(3).next_to(self.Squares, DOWN*4)
        group = VGroup(self.Squares, part_label)
        self.play(FadeIn(part_label), group.animate.move_to(0))
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in self.squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        