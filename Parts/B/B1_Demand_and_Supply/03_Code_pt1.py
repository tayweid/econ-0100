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
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
            
        part_label = Tex('{{Part B}} $|$ Episode 1').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part B": BLUE,}
        ).scale(3).next_to(Squares, DOWN*4)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.move_to(0))
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        
        self.wait()


class animation_1(MovingCameraScene):

    """Animation 1 | Quantity Demand Data

This animation plots the data from class on the P,Q graph."""

    def construct(self):
        
    """ Definitions """
        
        PQ_axis = Axes(            
            x_range=[0, 30, 5],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 30, 5) + [1],
                "decimal_number_config": {
                    "num_decimal_places":0,
                },
            },
            y_range=[0, 2, 2],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": [2, 1, 0.5, 0.25, 0.10],
                "numbers_with_elongated_ticks": [2, 1, 0.5, 0.25, 0.10],
                "decimal_number_config": {
                    "num_decimal_places":2,
                }
            },
            tips=False,
        )
        PQ_axis_large = Axes(            
            x_range=[0, 300, 50],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 300, 50),
                "decimal_number_config": {
                    "num_decimal_places":0,
                },
            },
            y_range=[0, 2, 2],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": [2, 1, 0.5, 0.25, 0.10],
                "numbers_with_elongated_ticks": [2, 1, 0.5, 0.25, 0.10],
                "decimal_number_config": {
                    "num_decimal_places":2,
                }
            },
            tips=False,
        )
        PQ_axis_small = Axes(            
            x_range=[0, 2, 1],
            x_length = 1,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": [1],
                "decimal_number_config": {
                    "num_decimal_places":0,
                },
            },
            y_range=[0, 2, 2],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0,2,1),
                "numbers_with_elongated_ticks": [1],
                "decimal_number_config": {
                    "num_decimal_places":2,
                }
            },
            tips=False,
        )
        
    """ Starting Objects """
        
        title = Tex("{{Quantity Demanded}} ($Q_d$) is a point on the (Q,P) plane.").set_color_by_tex_to_color_map(
            {"Quantity Demanded": YELLOW,}
        ).to_edge(UP)
        
        axes = PQ_axis.copy().scale(0.8).to_edge(DOWN).shift(UP/2)

        y_label = axes.get_y_axis_label("P")
        x_label = axes.get_x_axis_label("Q")
        grid_labels = VGroup(x_label, y_label)
        
        self.play(FadeIn(title), FadeIn(axes), FadeIn(grid_labels))
        
    """ Plot Quantity Demanded """
        
        data = [ # (q,p)
            (0,2), (1,1), (4,0.5), (10, 0.25), (25, 0.1)
        ]
        points = []
        lines = []
        for i, d in enumerate(data):
            d = axes.c2p(*data[i])
            d_last = axes.c2p(*data[i-1])
            point = Dot(d).set_color(YELLOW)
            point.z_index = 2
            points.append(point)
            self.play(FadeIn(point))
            if i > 0:
                line = Line(d_last, d)
                lines.append(line)
                self.play(FadeIn(line))
        self.wait()
        
        new_title = Tex("{{Law of Demand}} price and quantity are inversely related.").set_color_by_tex_to_color_map(
            {"Law of Demand": YELLOW,}
        ).to_edge(UP)
        self.play(Transform(title, new_title))
        self.wait()
        
    """ Show Consumer Surplus """
        
        new_title = Tex("{{Consumer Surplus}} is the buyer's extra value from an exchange.").set_color_by_tex_to_color_map(
            {"Consumer Surplus": YELLOW,}
        ).to_edge(UP)
        
        axes_small = PQ_axis_small.copy().scale(0.8).to_edge(DOWN).shift(UP/2).shift(LEFT*2)
        
        y_label_small = axes_small.get_y_axis_label("P")
        x_label_small = axes_small.get_x_axis_label("Q")
        grid_labels_small = VGroup(x_label_small, y_label_small)
        
        cs_point = Dot(axes_small.c2p(*data[1])).set_color(YELLOW)
        pre_point = points[1].copy()
        self.add(pre_point)
        self.play(FadeOut(axes), FadeIn(axes_small), 
                  Transform(grid_labels, grid_labels_small), 
                  FadeOut(*points), FadeIn(points[1]), 
                  Transform(pre_point, cs_point), FadeOut(*lines),
                 Transform(title, new_title))
        self.wait()
        
        # show the willingness to pay on the number line
        price = ValueTracker(1/2)
        def PriceLine(x):
            return price.get_value()
        def PricePlot():
            line = axes_small.plot(PriceLine, x_range=[-1,0.5]).set_color(RED)
            number = DecimalNumber(num_decimal_places=2).set_color(RED).scale(0.8).next_to(line,LEFT).set_value(price.get_value())
            label = Tex("Price").set_color(RED).next_to(number, LEFT, buff=1/2)

            return VGroup(line, label, number)
        price_line = always_redraw(PricePlot)
        self.play(FadeIn(price_line))
        self.wait()
        
        # show some price and label expenditure and consumer surplus on the number line
        def ConsumerSurplus():
            point = axes.c2p(3, price.get_value())
            cs_label = Tex("Consumer Surplus").next_to(point, RIGHT, buff=3).set_color(GREEN).shift(UP/2)
            spend_label = Tex("Expenditure").next_to(point, RIGHT, buff=3).set_color(PURPLE).shift(DOWN/2)

            if float(price.get_value()) < 1:
                cs = Line(axes_small.c2p(1,price.get_value()), axes_small.c2p(*data[1])).set_color(GREEN)
                cs_number = DecimalNumber(num_decimal_places=2).set_color(GREEN).scale(0.8).next_to(cs_label,RIGHT,buff=1/2).set_value(1 - price.get_value())
                
                spend = Line(axes_small.c2p(1,price.get_value()), axes_small.c2p(1,0)).set_color(PURPLE)                
                spend_number = DecimalNumber(num_decimal_places=2).set_color(PURPLE).scale(0.8).next_to(spend_label,RIGHT, buff=1/2).set_value(price.get_value())
                
            if float(price.get_value()) >= 1:                
                cs = Line(axes_small.c2p(*data[1]), axes_small.c2p(*data[1])).set_color(GREEN)
                cs_number = DecimalNumber(num_decimal_places=2).set_color(GREEN).scale(0.8).next_to(cs_label,RIGHT,buff=1/2).set_value(0)
                
                spend = Line(axes_small.c2p(1,0), axes_small.c2p(1,0)).set_color(PURPLE)
                spend_number = DecimalNumber(num_decimal_places=2).set_color(PURPLE).scale(0.8).next_to(spend_label,RIGHT, buff=1/2).set_value(0)
            
            return VGroup(cs, cs_number, spend, spend_number, cs_label, spend_label)
        consumer_surplus = always_redraw(ConsumerSurplus)
        
        self.play(FadeIn(consumer_surplus))
        self.wait()
        
        # then move the price around
        self.play(price.animate.set_value(1.5))
        self.wait()
        self.play(price.animate.set_value(1))
        self.wait()
        self.play(price.animate.set_value(0.25))
        self.wait()
        
        y_label = axes.get_y_axis_label("P")
        x_label = axes.get_x_axis_label("Q")
        grid_labels_large = VGroup(x_label, y_label)
        self.play(
            FadeIn(axes), FadeOut(axes_small), Transform(grid_labels, grid_labels_large), 
            FadeIn(*points), FadeOut(pre_point),
            FadeOut(consumer_surplus), FadeOut(price_line),
        )
        self.wait()
        
        # maybe show cs for all quantities
        
    """ Plot Demand """
        
        new_title = Tex("{{Individual Demand}} is every possible $Q_d$ for an individual.").set_color_by_tex_to_color_map(
            {"Individual Demand": YELLOW,}
        ).to_edge(UP)
        self.play(Transform(title, new_title), *[l.animate.set_color(YELLOW) for l in lines])
        self.wait()
        
    """ Demand as a Line """
        
        new_title = Tex("{{Individual Demand}} is every possible $Q_d$ for an individual.").set_color_by_tex_to_color_map(
            {"Individual Demand": YELLOW,}
        ).to_edge(UP)
        
        def Demand(q):
            return 1 - q/25
        
        demand = lines[2].copy()
        new_demand = axes.plot(Demand, x_range=[0,25]).set_color(BLUE)
        self.play(Transform(demand, new_demand), FadeOut(*points), FadeOut(*lines))
        self.wait()
        
    """ Quantity Demanded """
        
        new_title = Tex("{{Quantity Demanded}} ($Q_d$) is a point on the (Q,P) plane.").set_color_by_tex_to_color_map(
            {"Quantity Demanded": YELLOW,}
        ).to_edge(UP)
        
        def Inv_Demand(p):
            return (1 - p) * 25
        def Quantity_Demanded():
            p = price.get_value()
            q = Inv_Demand(p)
            point = axes.c2p(q, p)
            dot = Dot(point).set_color(YELLOW)
            dot.z_index = 3
            
            p_line = axes.plot(PriceLine, x_range=[-1,]).set_color(RED)
            p_line.z_index = 2
            p_number = DecimalNumber(num_decimal_places=2).set_color(RED).scale(0.8).next_to(p_line,LEFT, buff=3/4).set_value(p)
            p_label = Tex("Price").set_color(RED).next_to(p_number, LEFT, buff=1/4)

            q_line = Line(axes.c2p(q,0), axes.c2p(q,p)).set_color(RED)
            q_line.z_index = 2
            q_number = DecimalNumber(num_decimal_places=2).set_color(RED).scale(0.8).next_to(q_line,DOWN, buff=1/2).set_value(q)
            q_label = Tex("$q_d$").set_color(RED).next_to(q_number, LEFT, buff=1/4)

            return VGroup(dot, p_label, p_line, p_number, q_label, q_line, q_number)
        
        quantity_demanded = always_redraw(Quantity_Demanded)
        self.play(FadeIn(quantity_demanded), Transform(title, new_title))
        self.wait()
        self.play(price.animate.set_value(0.3))
        self.wait()
        self.play(price.animate.set_value(0.75))
        self.wait()
        self.play(price.animate.set_value(0.25))
        self.wait()
        
    """ Consumer Surplus """
        
        new_title = Tex(
            "{{Consumer Surplus}} is the buyer's extra value from an exchange.",
            #"{{Expenditure}} is the price times the quantity demanded.",
        ).set_color_by_tex_to_color_map(
            {"Consumer Surplus": GREEN,}
        ).to_edge(UP)
        
        def CSPlot():
    """ This function plots a line at all integers up to Q_d. """
            p = price.get_value()
            q = Inv_Demand(p)
            lines = []
            for i in np.arange(0,q,0.25):
                i_p = Demand(i)
                cs_line = Line(axes.c2p(i,p), axes.c2p(i,i_p)).set_color(GREEN)
                lines.append(cs_line)
                spend_line = Line(axes.c2p(i,0), axes.c2p(i,p)).set_color(PURPLE)
                lines.append(spend_line)
                
            return VGroup(*lines)
        
        cs_plot = always_redraw(CSPlot)
        self.play(Transform(title, new_title), Create(cs_plot))
        self.wait()
        
        self.play(price.animate.set_value(3/4))
        self.wait()
        
        self.play(price.animate.set_value(1/2))
        self.wait()

    """ Elasticity """
        
        #new_title = Tex("{{Elasticity}} of Demand: how $Q_d$ changes with a change in $P$.").set_color_by_tex_to_color_map(
        #    {"Elasticity": YELLOW,}
        #).to_edge(UP)
        
        #elasticity_equation = Tex("$\\frac{Q_1 - Q_2}{\\bar{Q}} \\Big/ \\frac{P_1 - P_2}{\\bar{P}}$")
        
        #self.play(FadeIn(elasticity_equation), Transform(title, new_title))
        #self.wait()
        
        # show another graph with elasticity
        
    """ Add Individual Demands Together """
        
        axes_large = PQ_axis_large.copy().scale(0.8).to_edge(DOWN).shift(UP/2)

        def AgDemand(q):
            return 1 - q/250
        ag_demand = axes_large.plot(AgDemand, x_range=[0,250]).set_color(BLUE)
        
        new_title = Tex("{{Demand}} is all possible quantity demanded.").set_color_by_tex_to_color_map(
            {"Demand": YELLOW,}
        ).to_edge(UP)
        self.play(FadeOut(cs_plot), Transform(title, new_title), Transform(axes, axes_large), Transform(demand, ag_demand))
        self.wait()
        
    """ Shifters """
        
        new_title = Tex("A {{Demand Shifter}} changes the demand curve.").set_color_by_tex_to_color_map(
            {"Demand Shifter": YELLOW,}
        ).to_edge(UP)
        self.play(Transform(title, new_title), axes.animate.shift(RIGHT*3), demand.animate.shift(RIGHT*3), grid_labels.animate.shift(RIGHT*3))
        
        shifter_list = [
            "- Preferences", 
            "- Prices of related goods", 
            "- Income", 
            "- Buyer expectations",
        ]
        for i, shifter in enumerate(shifter_list):
            self.play(FadeIn(Tex(shifter).set_color(BLUE).to_edge(UP + LEFT).shift(DOWN*(1 + i*2/3))))
            self.wait()
