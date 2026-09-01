from manim import *
import pandas as pd
import seaborn as sns
import numpy as np
import os
import warnings
import random
import sys

# Add the shared F26/Assets directory to the path for scene helpers
sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from scene_helpers import Raster_Font

warnings.filterwarnings('ignore')

# Paths
tutorial_path = 'PartA_E0'
if not os.path.exists(tutorial_path):
    os.makedirs(tutorial_path)
config.media_dir = tutorial_path
config.verbosity = 'ERROR'

# Colors
CUSTOM_BLACK = '#1f1f1f'
CUSTOM_GREY = '#696969'
CUSTOM_BLUE = '#0096FF'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY

# Frames
PIXEL_HEIGHT = 1080
FPS = 60
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT * 2
config.frame_rate = FPS

class Animation0(Scene):
    """Animation 0 | Intro Sequence"""
    
    def construct(self):
        # Definitions
        colors = sns.color_palette("Blues", 50).as_hex()
        
        # Get the raster font squares
        squares = Raster_Font('MICROECONOMICS')
        Squares = VGroup(*squares)
        
        self.add(Squares)
        
        # Animate the squares
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors, 1)[0], opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        part_label = Tex('{{Part A}} $|$ Episode 0').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part A": BLUE}
        ).scale(3).move_to(DOWN)
        
        self.play(AddTextWordByWord(part_label), Squares.animate.to_edge(UP, buff=1))
        
        # Continue animating squares
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors, 1)[0], opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        
        self.wait()


class Animation1(Scene):
    """Animation 1 | Unemployment Graph
    Graph unemployment, moving right.
    """
    
    def construct(self):
        # Load data
        data = pd.read_csv(os.path.join(os.path.dirname(__file__), "00_Assets/unemployment.csv"))
        
        max_rate = max(data['rate'])
        min_date = data['date'].iloc[0].split('-')[0]
        
        axes = Axes(
            x_range=[0, 10],
            y_range=[0, max_rate],
            x_length=10,
            y_length=5,
            axis_config={"color": CUSTOM_GREY, "include_ticks": False},
            tips=False,
            x_axis_config={
                "numbers_with_elongated_ticks": [0, 10],
            },
        )

        axes_labels = axes.get_axis_labels(x_label="Date", y_label="Unemployment Rate")
        ts1 = axes.plot(
            lambda x: data.loc[x, "rate"], x_range=[0, 10, 1], color=BLUE
        )
        
        d_list = VGroup()
        for i in [0, 10]:
            date = data['date'].iloc[i].split('-')[0]
            d = Tex(date)
            d.next_to(axes.coords_to_point(i, 0), DOWN)
            d_list.add(d)
        
        rate = data['rate'].iloc[10]
        r = Tex(str(rate)).set_color(RED)
        r.next_to(axes.coords_to_point(0, rate), LEFT)
        
        point = axes.coords_to_point(10, rate)
        dot = Dot(point, color=RED, z_index=10)
        hline = axes.get_horizontal_line(point, color=RED, line_config={"dashed_ratio": 0.85}).set_opacity(0.3)

        self.add(axes, axes_labels, d, r, dot, hline)
        self.play(FadeIn(ts1), run_time=1/10)
        
        for xl in np.arange(400, 889, 4):
            x_min = 0
            if xl > 12*20:
                x_min = xl - 12*20
            
            axes_ = Axes(
                x_range=[x_min, xl],
                y_range=[0, max_rate],
                x_length=10,
                y_length=5,
                axis_config={"color": CUSTOM_GREY, "include_ticks": False},
                tips=False,
            )

            axes_labels_ = axes_.get_axis_labels(x_label="Date", y_label="Unemployment Rate")
            ts1_ = axes_.plot(
                lambda x: data.loc[x, "rate"], x_range=[x_min, xl, 1], color=BLUE
            )
            
            d_list_ = VGroup()
            for i in [xl, x_min]:
                date = data['date'].iloc[i].split('-')[0]
                d_ = Tex(date)
                d_.next_to(axes_.coords_to_point(i, 0), DOWN)
                d_list_.add(d_)
            
            rate = data['rate'].iloc[xl]
            r_ = Tex(str(rate)).set_color(RED)
            r_.next_to(axes_.coords_to_point(x_min, rate), LEFT)
            
            point_ = axes_.coords_to_point(xl, rate)
            dot_ = Dot(point_, color=RED, z_index=10)
            hline_ = axes_.get_horizontal_line(point_, color=RED, line_config={"dashed_ratio": 0.85}).set_opacity(0.3)
            
            self.play(
                Transform(d_list, d_list_),
                Transform(hline, hline_),
                Transform(dot, dot_),
                Transform(r, r_),
                Transform(axes, axes_),
                Transform(axes_labels, axes_labels_),
                Transform(ts1, ts1_),
                run_time=1/10
            )
            
        self.wait()


class Animation2(Scene):
    """Animation 2 | Preferences
    I prefer carrot cake to chocolate cake.
    I prefer dark roast coffee to medium roast coffee.
    And I prefer medium roast coffee to light roast coffee.
    """
    
    def construct(self):
        title_text = Tex('This class is about behavior.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.play(FadeIn(title_text))
        
        text_list = ['', 'Carrot Cake', '$\\prec$', 'Chocolate Cake']
        tex = Tex(text_list[0])
        
        text = VGroup(Tex(''))
        for t in text_list:
            t = Tex(t).next_to(text, LEFT)
            text.add(t)
            self.play(FadeIn(t), text.animate.move_to(0))
        self.wait()
        
        self.play(FadeOut(text))
        
        text_list = ['', 'Dark Roast', '$\\prec$', 'Medium Roast', '$\\prec$', 'Light Roast']
        
        text = VGroup()
        for t in text_list:
            t = Tex(t).next_to(text, LEFT)
            text.add(t)
            self.play(FadeIn(t), text.animate.move_to(0))
        self.wait()
        
        preference_line = NumberLine(
            x_range=[-10, 10, 2],
            length=10,
            color=BLUE,
            include_numbers=True,
            label_direction=UP,
        ).to_edge(DOWN, buff=1)
                
        value_text = VGroup()
        dots = VGroup()
        for t, p in zip(['Dark Roast', 'Medium Roast', 'Light Roast'], [9, 0, -9]):
            d = Dot(z_index=10, color=RED).move_to(preference_line.number_to_point(p))
            t = Tex(t).next_to(d, UP, buff=1)
            dots.add(d)
            value_text.add(t)
        
        self.play(FadeIn(preference_line))
        self.play(FadeIn(dots), Transform(text, value_text))
        
        quote1 = Tex('{{Preferences}} are rankings!').set_color_by_tex_to_color_map({
            "Preferences": DEFINITION
        })
        self.play(AddTextWordByWord(quote1))
        self.wait()


class Animation3(Scene):
    """Animation 3 | Scarcity
    With preferences in the face of scarcity, we must make choices requiring tradeoffs.
    """
    
    def construct(self):
        title_text = Tex('This class is about behavior.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.add(title_text)
        
        quote1 = Tex("We can't always have what we want most.")
        self.play(AddTextWordByWord(quote1.move_to(0)))
        quote2 = Tex('{{Scarcity}} is more basic than money.').next_to(quote1, DOWN*3).set_color_by_tex_to_color_map({
            "Scarcity": DEFINITION
        })
        self.play(Write(quote2))
        self.wait()
        
        self.play(FadeOut(quote1), FadeOut(quote2))


class Animation4(Scene):
    """Animation 4 | Choices Equation"""
    
    def construct(self):
        title_text = Tex('This class is about behavior.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.add(title_text)
        
        quote1 = Tex('With preferences in the face of scarcity,')
        self.play(AddTextWordByWord(quote1))
        quote2 = Tex('choices involve tradeoffs.').next_to(quote1, DOWN)
        self.play(AddTextWordByWord(quote2))
        
        self.wait()
        
        self.play(FadeOut(quote1), FadeOut(quote2))
        
        text_list = ['', 'Preferences', '+', 'Scarcity', '$\\Rightarrow$', 'Choices']
        tex = Tex(text_list[0])
        
        text = VGroup(Tex(''))
        for t in text_list:
            t = Tex(t).set_color(DEFINITION).next_to(text, RIGHT)
            text.add(t)
            self.play(FadeIn(t), text.animate.move_to(0))
        self.wait()
        
        self.play(FadeOut(text))


class Animation5(Scene):
    """Animation 5 | Opportunity Cost
    Opportunity cost is the value of the next best alternative: what you give up to make a choice.
    """
    
    def construct(self):
        title_text = Tex('This class is about behavior.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.add(title_text)
        
        OR = Tex(' or ').scale(1.5)
        
        A = Tex('A').scale(1.5).next_to(OR, LEFT, buff=2)
        self.play(FadeIn(A))
        
        self.wait()
        
        self.play(FadeIn(OR))
        
        self.wait()
        
        B = Tex('B').scale(1.5).next_to(OR, RIGHT, buff=2)
        self.play(FadeIn(B))
        
        self.wait()
        
        framebox1 = SurroundingRectangle(A, buff=0.3).set_color(GREEN)
        self.play(Create(framebox1))
        
        self.wait()
        
        framebox2 = SurroundingRectangle(B, buff=0.3).set_color(RED)
        self.play(Create(framebox2))
        
        self.wait()
        
        cost = Tex("Opportunity Cost({{A}}) = {{B}}").scale(1.5).next_to(OR, DOWN, buff=2).set_color_by_tex_to_color_map({
            "A": GREEN,
            "B": RED,
        })
        self.play(Create(cost))
        
        self.wait()
        
        cost2 = Tex("Opportunity Cost({{B}}) = {{A}}").scale(1.5).next_to(OR, DOWN, buff=2).set_color_by_tex_to_color_map({
            "A": RED,
            "B": GREEN,
        })
        self.play(
            framebox1.animate.move_to(B),
            framebox2.animate.move_to(A),
            Transform(cost, cost2)
        )
        
        self.wait()
        
        self.play(FadeOut(A), FadeOut(OR), FadeOut(B), FadeOut(framebox1), FadeOut(framebox2), FadeOut(cost))
        
        definition = Tex("{{Opportunity Cost}} is the value of the next best alternative.").set_color_by_tex_to_color_map({
            "Opportunity Cost": DEFINITION
        })
        self.play(AddTextWordByWord(definition))
        
        self.wait()
        
        self.play(FadeOut(definition))
        self.play(FadeOut(title_text))


class Animation6(Scene):
    """This class is about social environments.
    - Autarky def
    - Simple game
    - Generic two player equilibrium idea
    """
    
    def construct(self):
        title_text = Tex('This class is about social environments.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.play(FadeIn(title_text))
        
        definition = Tex("{{Autarky}} is a state of economic self-sufficiency.").set_color_by_tex_to_color_map({
            "Autarky": DEFINITION
        })
        self.play(AddTextWordByWord(definition))
        self.wait()
        
        self.play(FadeOut(definition))
        
        table = Table(
            [["10", "-1"],
             ["-1", "8"]],
            row_labels=[Text("T"), Text("M")],
            col_labels=[Text("T").set_color(PINK), Text("M").set_color(PINK)]
        )
        self.play(FadeIn(table))
        self.wait()
        
        box = SurroundingRectangle(table.get_columns()[1], buff=1/2)
        self.play(FadeIn(box))
        self.wait()
        
        new_box = SurroundingRectangle(table.get_columns()[2], buff=1/2)
        self.play(Transform(box, new_box))
        self.wait()
        
        self.play(FadeOut(box), FadeOut(table))


class Animation7(Scene):
    """Six Parts"""
    
    def construct(self):
        title_text = Tex('This class contains six parts.').scale(1.5).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.play(FadeIn(title_text))
        
        part_list = [
            '{{Part A}}. A history changing question',
            '{{Part B}}. Markets can coordinate our choices.',
            '{{Part C}}. Externalities break markets; governments can help.',
            '{{Part D}}. Some markets are not easily fixable.',
            "{{Part E}}. Sellers' decisions shape how markets behave.",
            "{{Part F}}. Buyers' decisions shape the demand curve.",
        ]
        
        part_color_map = {
            "Part A": RED,
            "Part B": RED,
            "Part C": RED,
            "Part D": RED,
            "Part E": RED,
            "Part F": RED,
        }
        
        for i, p in enumerate(part_list):
            self.play(FadeIn(
                Tex(p).to_edge(LEFT).shift(UP + DOWN*i*2/3).set_color_by_tex_to_color_map(part_color_map)
            ))
            self.wait()


class Animation8(Scene):
    """This class grounds a number of economic principles."""
    
    def construct(self):
        title_text = Tex('This class grounds a number of economic principles.').scale(1.2).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.play(FadeIn(title_text))
        
        principle_list = [
            '{{P1}}. People face tradeoffs.',
            '{{P2}}. The cost of something is what you give up to get it.',
            '{{P3}}. Trade can make everyone better off.',
            '{{P4}}. People respond to incentives.',
            '{{P5}}. Markets are often a good way to organize economies.',
            '{{P6}}. Governments can sometimes improve markets.',
            '{{P7}}. Rational people think on the margin.',
        ]
        principle_color_map = {
            "P1": RED,
            "P2": RED,
            "P3": RED,
            "P4": RED,
            "P5": RED,
            "P6": RED,
            "P7": RED,
        }
        
        for i, p in enumerate(principle_list):
            self.play(FadeIn(
                Tex(p).scale(0.8).to_edge(LEFT).shift(UP + DOWN*i*2/3).set_color_by_tex_to_color_map(principle_color_map)
            ))
            self.wait()


class Animation9(Scene):
    """Next class we'll begin with the motivating sequence which requires a trip back to 1800s British philosophy."""
    
    def construct(self):
        title_text = Tex('Next class...').scale(1.5).to_edge(UP, buff=1).set_color(CUSTOM_BLUE)
        self.add(title_text)
        
        next_topic = Tex('A trip back to 1800s British philosophy.').scale(1.2)
        self.add(next_topic)
        
        box = SurroundingRectangle(next_topic, buff=1/2)
        self.play(Create(box), run_time=2)
        self.play(Uncreate(box.flip(RIGHT)), run_time=2)
        self.wait()
