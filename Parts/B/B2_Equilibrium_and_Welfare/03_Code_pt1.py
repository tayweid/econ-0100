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

    """Animation 0 | Last Time...

Last time we ... ppf ... but we're left the question where to live on the PPF. How do we choose between a and b? That's the question we turn to: how to pick where on the PPF to live?"""

    def construct(self):
        text = Tex('Last Time...').scale(3)
        self.play(FadeIn(text), run_time=1/2)
        self.wait()
        self.play(FadeOut(text), run_time=1/2)
        self.wait()


class animation_(Scene):

    """Animation _ | Intro Sequence"""

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
            
        part_label = Tex('{{Part B}} $|$ Episode 3').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part B": BLUE,}
        ).scale(3).next_to(Squares, DOWN*4)
        group = VGroup(Squares, part_label)
        self.play(FadeIn(part_label), group.animate.move_to(0))
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
            self.wait(4/10)
        
        self.wait()


""" Axis Pamameters """

x_int = 10
x_max = 50
y_int = 2
y_max = 14

PQ_large = Axes(            
    x_range=[0, x_max, x_int],
    x_length = 7,
    axis_config={"color": WHITE},
    x_axis_config={
        "numbers_to_include": np.arange(0, x_max+x_int, x_int),
        "decimal_number_config": {
            "num_decimal_places":0,
        },
    },
    y_range=[0, y_max, y_int],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": np.arange(0,y_max+y_int,y_int),
        "decimal_number_config": {
            "num_decimal_places":0,
        }
    },
    tips=False,
)

class animation_1(MovingCameraScene):

    def construct(self):

    """ Starting Objects """

        title_string = "Where do prices come from?"
        title =Tex(title_string).to_edge(UP)
        
        supply_axes = PQ_large.copy().scale(0.6).to_edge(DOWN+LEFT).shift(2.5*UP/3+5*RIGHT/4)
        supply_y_label = supply_axes.get_y_axis_label("P")
        supply_x_label = supply_axes.get_x_axis_label("Q")
        supply_grid_labels = VGroup(supply_x_label, supply_y_label)

        demand_axes = PQ_large.copy().scale(0.6).to_edge(DOWN+RIGHT).shift(2.5*UP/3+5*LEFT/4)
        demand_y_label = demand_axes.get_y_axis_label("P")
        demand_x_label = demand_axes.get_x_axis_label("Q")
        demand_grid_labels = VGroup(demand_x_label, demand_y_label)
        
        self.play(FadeIn(title, supply_axes, supply_grid_labels, demand_axes, demand_grid_labels))

    """ Functions """

        supply_slope = 5
        supply_intercept = 2
        def Supply(q):
            return supply_intercept + q / supply_slope
        def Inv_Supply(p):
            return (p-supply_intercept) * supply_slope

        demand_slope = 5
        demand_intercept = 12
        def Demand(q):
            return demand_intercept - q / demand_slope
        def Inv_Demand(p):
            return (demand_intercept-p) * demand_slope

    """ Price """
        
        price = ValueTracker(5)

    """ Supply Curve """
        
        Supply_Line = supply_axes.plot(Supply, x_range=[0,x_max]).set_color(YELLOW)
        Supply_Line.z_index = 3
        self.play(FadeIn(Supply_Line))
        self.wait()

    """ Supply Equation """

        supply_label = Tex("S:").set_color(YELLOW)
        supply_equation = always_redraw(
            lambda: MathTex(
                r"P = 2 + \frac{Q_s}{5} = " + f"{price.get_value():.0f}"
            ).next_to(supply_label,RIGHT).set_color(YELLOW)
        )
        supply_title = VGroup(supply_label,supply_equation).next_to(supply_axes,UP*2)

        self.add(supply_title)

    """ Quantity Supplied """
        
        def Quantity_Supplied():
            p = price.get_value()
            q = Inv_Supply(p)
            point = supply_axes.c2p(q, p)
            dot = Dot(point).set_color(RED)
            dot.z_index = 4
            
            p_line = DashedVMobject(supply_axes.plot(lambda x: price.get_value(), x_range=[-1,x_max])).set_color(RED)
            p_line.z_index = 2
            p_number = DecimalNumber(num_decimal_places=0).set_value(p).set_color(RED).scale(0.8).next_to(p_line,LEFT, buff=1/3)
            p_label = Tex("P =").set_color(RED).next_to(p_number, LEFT, buff=1/4)

            p_dot = Line(supply_axes.c2p(-1.5,p), supply_axes.c2p(1.5,p)).set_color(RED)
            p_dot.z_index = 2

            q_line = DashedVMobject(Line(supply_axes.c2p(q,2), supply_axes.c2p(q,p))).set_color(RED)
            q_line.z_index = 2
            q_intercept = supply_axes.c2p(q, 0)
            q_number = DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept,DOWN, buff=1/3)
            q_label = Tex("$Q_s$").set_color(RED).next_to(q_intercept, UP, buff=0)

            q_dot = Line(supply_axes.c2p(q,-0.5), supply_axes.c2p(q,0.5)).set_color(RED)
            q_dot.z_index = 2

            return VGroup(dot, p_label, p_line, p_number, q_label, q_line, q_number, p_dot, q_dot)
            
        quantity_supplied = always_redraw(Quantity_Supplied)
        self.play(FadeIn(quantity_supplied))
        self.wait()

        self.play(price.animate.set_value(10))
        self.wait()

    """ Demand Line """
        
        Demand_Line = demand_axes.plot(Demand, x_range=[0,x_max]).set_color(BLUE)
        Demand_Line.z_index = 3
        self.play(FadeIn(Demand_Line))
        self.wait()

    """ Demand Equation """

        demand_label = Tex("D:").set_color(BLUE)
        demand_equation = always_redraw(
            lambda: MathTex(
                r"P = 12 - \frac{Q_b}{5} = " + f"{price.get_value():.0f}"
            ).next_to(demand_label,RIGHT).set_color(BLUE)
        )
        demand_title = VGroup(demand_label,demand_equation).next_to(demand_axes,UP*2)

        self.add(demand_title)

    """ Quantity Demanded """
        
        def Quantity_Demanded():
            p = price.get_value()
            q = Inv_Demand(p)
            point = demand_axes.c2p(q, p)
            dot = Dot(point).set_color(RED)
            dot.z_index = 4
            
            p_line = DashedVMobject(demand_axes.plot(lambda x: price.get_value(), x_range=[-1,x_max])).set_color(RED)
            p_line.z_index = 2
            p_number = DecimalNumber(num_decimal_places=0).set_value(p).set_color(RED).scale(0.8).next_to(p_line,LEFT, buff=1/3)
            p_label = Tex("P =").set_color(RED).next_to(p_number, LEFT, buff=1/4)

            p_dot = Line(demand_axes.c2p(-1.5,p), demand_axes.c2p(1.5,p)).set_color(RED)
            p_dot.z_index = 2

            q_intercept = demand_axes.c2p(q, 0)
            q_line = DashedVMobject(Line(demand_axes.c2p(q,2), demand_axes.c2p(q,p))).set_color(RED)
            q_line.z_index = 2
            q_number = DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept,DOWN, buff=1/3)
            q_label = Tex("$Q_b$").set_color(RED).next_to(q_intercept, UP, buff=0)

            q_dot = Line(demand_axes.c2p(q,-0.5), demand_axes.c2p(q,0.5)).set_color(RED)
            q_dot.z_index = 2

            return VGroup(dot, q_label, p_line, q_line, q_number, p_number, p_label, p_dot, q_dot)
            
        quantity_demanded = always_redraw(Quantity_Demanded)
        self.play(FadeIn(quantity_demanded))
        self.wait()

    """ Exchange """

        def Quantity_Exchanged():
            p = price.get_value()
            qb = Inv_Demand(p)
            qs = Inv_Supply(p)

            if qb > qs:
                shortage_text = 'Shortage'
                shortage_line = Line(demand_axes.c2p(qb,0), demand_axes.c2p(qs,0)).set_color(PINK)
                shortage_label = Tex(shortage_text).scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
                qx = qs

            if qb < qs:
                shortage_text = 'Surplus'
                shortage_line = Line(supply_axes.c2p(qb,0), supply_axes.c2p(qs,0)).set_color(PINK)
                shortage_label = Tex(shortage_text).scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
                qx = qb
            if qb == qs:
                qx = qs
                shortage_text = ''
                shortage_line = Line(demand_axes.c2p(qb,0), demand_axes.c2p(qs,0)).set_color(PINK)
                shortage_label = Tex(shortage_text).scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
            
            supply_qx = supply_axes.c2p(qx, 0)
            supply_qx_label = Tex("$Q_x$").set_color(RED).next_to(supply_qx, DOWN, buff=3/4)
            supply_qx_dot = Line(supply_axes.c2p(qx,-0.5), supply_axes.c2p(qx,0.5)).set_color(PINK)
            #supply_qx_dot = Dot(supply_qx).set_color(RED)
            supply_qx_dot.z_index = 1

            demand_qx = demand_axes.c2p(qx, 0)
            demand_qx_label = Tex("$Q_x$").set_color(RED).next_to(demand_qx, DOWN, buff=3/4)
            demand_qx_dot = Line(demand_axes.c2p(qx,-0.5), demand_axes.c2p(qx,0.5)).set_color(PINK)
            #demand_qx_dot = Dot(demand_qx).set_color(RED)
            demand_qx_dot.z_index = 1
            
            return VGroup(supply_qx_dot, supply_qx_label, demand_qx_dot, demand_qx_label, shortage_line, shortage_label)#, p_number, p_label

        quantity_exchanged = always_redraw(Quantity_Exchanged)
        self.play(FadeIn(quantity_exchanged))
        self.wait()

    """ Comprehension Checks """
        
        for p in [9, 4, 5, 7]:
            self.play(price.animate.set_value(p))
            self.wait()

    """ Supply and Demand Graph """

        new_supply_axes = supply_axes.copy().move_to(ORIGIN)
        new_demand_axes = demand_axes.copy().move_to(ORIGIN)

        self.play(
            supply_axes.animate.move_to(ORIGIN),
            supply_grid_labels.animate.move_to(ORIGIN),
            Transform(supply_grid_labels, VGroup(new_supply_axes.get_y_axis_label("P"), new_supply_axes.get_x_axis_label("Q"))),
            Transform(Supply_Line, new_supply_axes.plot(Supply, x_range=[0,x_max]).set_color(YELLOW)),
            
            demand_axes.animate.move_to(ORIGIN),
            Transform(demand_grid_labels, VGroup(new_demand_axes.get_y_axis_label("P"), new_demand_axes.get_x_axis_label("Q"))),
            Transform(Demand_Line, demand_axes.copy().move_to(ORIGIN).plot(Demand, x_range=[0,x_max]).set_color(BLUE)),
        )
        self.wait()
