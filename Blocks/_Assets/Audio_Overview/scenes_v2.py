# scenes.py
## https://docs.manim.community/en/v0.10.0/reference.html

import os
import sys

from manim import *
import random
import seaborn as sns

# Raster_Font is shared with the block animations; the canonical copy
# lives in F26/Assets. Not named 'scenes' because this directory has a
# scenes.py of its own, which would shadow it.
sys.path.append(os.path.join(os.path.dirname(__file__), '../Assets'))
from scene_helpers import Raster_Font

""" Settings """

sns.color_palette("YlGn", 10).as_hex()

""" Scenes """

class Overview(Scene):

    def construct(self, part='Part B', chapter='Chapter 1'):
        self.colors = sns.color_palette("Blues", 50).as_hex()
        self.squares = Raster_Font('MICROECONOMISC')
        self.Square_Group = VGroup(*self.squares)
        self.add(self.Square_Group)

        self.part_label = Tex(r'{{' + f'{part}' + '}} $|$ ' + f'{chapter}').scale(3).next_to(self.Square_Group, DOWN*4)
        self.part_label = self.part_label.set_color(GREY).set_color_by_tex_to_color_map(
            {f'{part}': BLUE,}
        )

    def Intro(self, steps=8):
        colors = sns.color_palette("Blues", 50).as_hex()
        
        for i in range(steps):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in self.squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        self.group = VGroup(self.Square_Group, self.part_label)
        self.play(FadeIn(self.part_label), self.group.animate.move_to(0))

    def Loop(self, steps=8):
        colors = sns.color_palette("Blues", 50).as_hex()
        
        self.group = VGroup(self.Square_Group, self.part_label).move_to(0)
        update_squares = [s.set_fill(random.sample(self.colors,1),opacity=1) for s in self.squares]
        self.add(*update_squares, self.part_label)

        for i in range(steps):
            update_squares = [s.animate.set_fill(random.sample(self.colors,1),opacity=1) for s in self.squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        