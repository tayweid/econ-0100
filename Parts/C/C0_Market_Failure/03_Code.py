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

class animation_0(MovingCameraScene):

    """Animation 0 | Show the PPF with gains and market"""

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
        
        ppf_axes = PPF_axis.to_edge(RIGHT).scale(0.8)
        
        y_label = ppf_axes.get_y_axis_label("A").shift(LEFT*2/3)
        x_label = ppf_axes.get_x_axis_label("B").shift(DOWN/2)
        
        alpha = ValueTracker(1)

        def Linear_PPF(x):
            return 100 - x
        
        def Bowed_PPF(x):
            return (100**alpha.get_value() - (x)**alpha.get_value())**(1/alpha.get_value())
        
        def PPF_Group():
            linear_ppf = ppf_axes.plot(Linear_PPF, color=GREY, x_range=(0, 100))
            linear_ppf.z_index = -1

            bowed_ppf = ppf_axes.plot(Bowed_PPF, color=PINK, x_range=(0, 100, .1))
            bowed_ppf.z_index = -1
            
            return VGroup(linear_ppf, bowed_ppf)
        
        ppf_group = always_redraw(PPF_Group)

        self.add(part_label, ppf_axes, y_label, x_label, ppf_group)
                
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
        p1 = ppf_axes.coords_to_point(x1,y1)
        dot1 = Dot(p1).set_color(WHITE)
        
        dot1_l = Tex('Option 1').next_to(dot1,RIGHT).set_color(YELLOW)
        
        x2 = 80
        y2 = Bowed_PPF(x2)
        p2 = ppf_axes.coords_to_point(x2,y2)
        dot2 = Dot(p2).set_color(WHITE)
        
        dot2_l = Tex('Option 2').next_to(dot2,UP+RIGHT).set_color(YELLOW)
        
        self.play(FadeIn(dot1), FadeIn(dot1_l), FadeIn(questions[1]))
        self.play(FadeIn(dot2), FadeIn(dot2_l))
        self.wait()
        
        self.play(FadeIn(questions[2]))
        self.wait()
        
        
    """ Definitions """
        
        PQ_axis = Axes(            
            x_range=[0, 1000, 500],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 1000, 500),
                "decimal_number_config": {
                    "num_decimal_places":0,
                },
            },
            y_range=[0, 100, 50],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": [100,50,0],
                "decimal_number_config": {
                    "num_decimal_places":0,
                }
            },
            tips=False,
        )
        
    """ Starting Objects """
        
        axes = PQ_axis.copy().next_to(ppf_axes, RIGHT*6)

        y_label = axes.get_y_axis_label("P")
        x_label = axes.get_x_axis_label("Q")
        grid_labels = VGroup(x_label, y_label)
        
        all_things = VGroup(ppf_group, axes, part_label)
        
        self.play(
            self.camera.frame.animate.move_to(all_things).set(width=all_things.width*1.1),
            FadeIn(axes), FadeIn(grid_labels))
        
    """ Starting Equilibrium """
        
        demand_intercept = ValueTracker(100)
        def Demand(q):
            return demand_intercept.get_value() - q/10
        def Inv_Demand(p):
            return (demand_intercept.get_value() - p) * 10
        def Demand_Line():
            return axes.plot(Demand, x_range=[0, Inv_Demand(0)]).set_color(BLUE)        
        demand = always_redraw(Demand_Line)
        
        demand_base = Demand_Line().set_color(GREY)
        demand_base.z_index = -1
        
        supply_intercept = ValueTracker(10)
        def Supply(q):
            return supply_intercept.get_value() + q/10
        def Inv_Supply(p):
            return (supply_intercept.get_value() + p) * 10
        def Supply_Line():
            return axes.plot(Supply, x_range=[0, Inv_Supply(80)]).set_color(YELLOW)        
        supply = always_redraw(Supply_Line)
        
        supply_base = Supply_Line().set_color(GREY)
        supply_base.z_index = -1
        
        def Equilibrium_Price():
            return supply_intercept.get_value() + (demand_intercept.get_value() - supply_intercept.get_value())/2
        
        price_value = ValueTracker(Equilibrium_Price())
        def Price_Line():
            price_value.set_value(Equilibrium_Price())
            return axes.plot(lambda x:price_value.get_value(), x_range=[0,1000]).set_color(RED) 
        price = always_redraw(Price_Line)
        
        price_base = Price_Line().set_color(GREY)
        price_base.z_index = -1
        
        def Quantity_Demanded():
            p = price_value.get_value()
            q = Inv_Demand(p)
            point = axes.c2p(q, p)
            dot = Dot(point).set_color(RED)
            dot.z_index = 3
            line = axes.get_vertical_line(axes.input_to_graph_point(q, demand), color=RED)
            return VGroup(dot, line)
        quantity_demanded = always_redraw(Quantity_Demanded)
        
        def Quantity_Exchanged(p):
            qs = Inv_Supply(p)
            qd = Inv_Demand(p)
            return min(qs, qd)
                
        self.play(FadeIn(demand), FadeIn(demand_base), 
                  FadeIn(supply), FadeIn(supply_base),
                  FadeIn(price), FadeIn(quantity_demanded))
        self.wait()

        def Total_Surplus():
            area = axes.get_area(Supply_Line(), [0, Quantity_Exchanged(Equilibrium_Price())], bounded_graph=Demand_Line(), color=PURPLE, opacity=0.5)
            area.z_index = -3
            return area
        TS = always_redraw(Total_Surplus)
        
        TS_base = Total_Surplus().set_color(PURPLE)

        self.play(FadeIn(TS), FadeIn(TS_base))
        self.wait()


class animation_1(Scene):

    """Animation 1 | Intro Sequence"""

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
            
        part_label = Tex('{{Part C}} $|$ Externalities Simulation').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part B": BLUE,}
        ).scale(1.5).next_to(Squares, DOWN)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.move_to(0))
        
        self.wait()
        
        rule_label = Tex('{{Rules}}').set_color(RED).scale(1.5).to_edge(UP+LEFT, buff=1).shift(DOWN*3)
        
        rules = [
            Tex('- Your card is your points if you exchange').set_color(RED).to_edge(UP+LEFT, buff=1).shift(DOWN*4),
            Tex('- It costs 4 points to exchange').set_color(RED).to_edge(UP+LEFT, buff=1).shift(DOWN*4.5),
            Tex('- One random person gets two pennies each exchange').set_color(RED).to_edge(UP+LEFT, buff=1).shift(DOWN*5)
        ]
        
        self.play(group.animate.to_edge(UP, buff=1))
        self.play(FadeIn(rule_label))
        for rule in rules:
            self.play(FadeIn(rule))
