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


class animation_1(Scene):

    """Animation 1 | Marginal Cost

Show opportunity cost in terms of carrots, but then multiply by dollars to get marginal cost. Define marginal cost."""

    def construct(self):
        
        a = Tex('OpportunityCost(','SPINACH',')')
        a[1].set_color(GREEN)
        a_t = Tex('OpportunityCost(','S',')')
        a_t[1].set_color(GREEN)
        
        b = Text(r'=')
        b_t = Text(r'=')
        
        
        c = Tex(r'CARROTS')
        c[0].set_color(ORANGE)
        c_t = Tex(r'C')
        c_t[0].set_color(ORANGE)

        d = Tex(r'$\times$')
        d_t = Tex(r'$\times$')

        e = Tex(r'PRICE of CARROTS')
        e[0].set_color(BLUE)
        e_t = Tex(r'P')
        e_t[0].set_color(BLUE)
        
        text_list = [
            a, b, c, d, e
        ]
        text_list_t = [
            a_t, b_t, c_t, d_t, e_t
        ]
        
        text,text_t = VGroup(),VGroup()
        
        for t,t_t in zip(text_list,text_list_t):
            
            text.add(t.next_to(text))
            self.play(FadeIn(t),text.animate.move_to(0))

            text_t.add(t_t.next_to(text_t)).move_to(0)
            self.play(Transform(text,text_t))
        
    """ Marginal Cost """
        
        paragraph = Paragraph(
            'Marginal Cost \n',
            ' is the value of what I give up',
            ' by adding one more unit of output.',
        font_size=32)
        paragraph[0][:12].set_color(DEFINITION)
        self.play(FadeIn(paragraph), text.animate.to_edge(UP, buff=1))
        self.wait()


class animation_2(MovingCameraScene):

    """Animation 2 | Individual Supply Curve

Add in molly's farm. Show different prices and the resulting supply curve. Show the definition of the law of supply and marginal cost. Then show a shifter."""

    def construct(self):
        
    """ Definitions """
        
        PQ_axis = Axes(            
            x_range=[0, 2000, 500],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 2500, 500),
                "numbers_with_elongated_ticks": np.arange(0, 2000, 500),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":GREEN,
                },
            },
            y_range=[0, 8, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 9, 2),
                "numbers_with_elongated_ticks": np.arange(0, 9, 2),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":BLUE,
                }
            },
            tips=False,
        )
               
    """ Starting Objects """
        
        axes = PQ_axis.shift(RIGHT*3+DOWN/2).scale(0.8)

        y_label = axes.get_y_axis_label("P").set_color(BLUE)
        x_label = axes.get_x_axis_label("Q").set_color(GREEN)
        grid_labels = VGroup(x_label, y_label)
        
        farm = Rectangle(height=5, width=2, fill_opacity=0).move_to(LEFT*5+DOWN/2)
        farm.z_index = 2
        farm_name = Tex("Molly's Farm").scale(1).next_to(farm,UP)#.shift(RIGHT)
        
        farm_group = VGroup(farm,farm_name)
        
        grow = Rectangle(height=5, width=2, color=GREEN, fill_opacity=1).next_to(farm_name,DOWN)
        
    """ Setup Scene """
        
        self.play(FadeIn(axes), FadeIn(grid_labels), FadeIn(grow),FadeIn(farm_group))
        self.wait()
        
    """ Some Quantities """
        
        pq_list = [[4, 1000], [6,1500], [2,500]]
        dots = VGroup()
        math = VGroup()
        
        for p,q in pq_list:
            a = Tex('$q_s($',r'\$',p,') =',q).move_to(LEFT*2+UP*(p/3))
            a[1].set_color(BLUE)
            a[2].set_color(BLUE)
            a[-1].set_color(GREEN)
            math.add(a)
            
            new_grow = Rectangle(height=5*p/6, width=2, color=GREEN, fill_opacity=1).move_to(LEFT*5+DOWN/2)
            new_farm = Rectangle(height=5*p/6, width=2, fill_opacity=0).move_to(LEFT*5+DOWN/2)

            self.play(FadeIn(a),Transform(grow,new_grow),Transform(farm,new_farm))
            self.wait()
            
            point = axes.coords_to_point(q, p)
            dot = Dot(point)
            dots.add(dot)
            
            self.play(FadeIn(dot))
            self.wait()
            
        self.play(farm.animate.shift(UP*3/2),grow.animate.shift(UP*3/2))

    """ Law of Supply """
        
        law_of_supply = Paragraph(
            'Law of Supply \n',
            ' The quantity supplied',
            ' of a good rises with',
            ' its price.',
        font_size=32).to_edge(DOWN+LEFT, buff=1)
        law_of_supply[0][:11].set_color(DEFINITION)
        self.play(FadeIn(law_of_supply))
        
    """ Supply Curve """
        
        supply_graph = axes.plot(Supply_Curve, color=SUPPLY, x_range=(0, 2000))
        self.play(FadeIn(supply_graph))
        
        title = Tex("{{Supply}} = The cost of one additional unit.").set_color_by_tex_to_color_map(
            {"Supply": YELLOW,}
        ).to_edge(UP)        
        self.play(
            FadeIn(title),
            FadeOut(dots)
        )
        
        self.wait(1/2)
        new_title = Tex("{{Supply}} is all possible quantity supplied.").set_color_by_tex_to_color_map(
            {"Supply": YELLOW,}
        ).to_edge(UP)
        self.play(
            #dots.animate.shift(DOWN).scale(0.5), 
            #supply_graph.animate.shift(DOWN).scale(0.5),
            #grid_labels.animate.shift(DOWN).scale(0.5), 
            #axes.animate.shift(DOWN).scale(0.5), 
            Transform(title,new_title),
        )

        self.wait()
        
    """ Clear Screen """
        
        #supply_curve_label = Text(
        #    'Individual Supply Curve',
        #font_size=32).to_edge(UP, buff=1).set_color(SUPPLY)
        
        self.play(
            FadeOut(law_of_supply),
            FadeOut(farm_group),
            FadeOut(grow),
            FadeOut(math),
            #FadeOut(dots),
            #Transform(supply_curve_def, supply_curve_label),
            #supply_graph.animate.shift(LEFT*2 + UP).scale(2),
            #grid_labels.animate.shift(LEFT*2 + UP).scale(2), 
            #axes.animate.shift(LEFT*1 + UP).scale(2)
        )        
        

    """ Shifters """
        
        new_title = Tex("A {{Supply Shifter}} changes the supply curve.").set_color_by_tex_to_color_map(
            {"Supply Shifter": YELLOW,}
        ).to_edge(UP)
        self.play(Transform(title, new_title))#, axes.animate.shift(RIGHT*3), grid_labels.animate.shift(RIGHT*3))
        
        shifter_list = [
            "- Input Prices", 
            "- Technology", 
            "- Number of sellers", 
        ]
        for i, shifter in enumerate(shifter_list):
            new_old_supply_graph = DashedVMobject(axes.plot(Supply_Curve, color=SUPPLY, x_range=(0, 2000)))

            self.play(
                FadeIn(Tex(shifter).set_color(BLUE).to_edge(UP + LEFT).shift(DOWN*(1 + i*2/3))),
                Transform(supply_graph,new_old_supply_graph)
            )
            
            old_supply_graph = axes.plot(Supply_Curve, color=SUPPLY, x_range=(0, 2000))
            self.add(old_supply_graph)
            new_supply_graph = axes.plot(New_Supply_Curve, color=SUPPLY, x_range=(0, 2000))
            self.wait(1/2)
            self.play(
                Transform(old_supply_graph,new_supply_graph)
            )
            self.wait()
            
            self.play(FadeOut(old_supply_graph),)


class animation_3(MovingCameraScene):

    """Animation 3 | Market Supply Curve

Show how we horizontally add the quantities together to get a market supply curve."""

    def construct(self):
        
    """ Definitions """
        
        PQ_axis = Axes(            
            x_range=[0, 3000, 1000],
            x_length = 7,
            axis_config={"color": WHITE},
            x_axis_config={
                "numbers_to_include": np.arange(0, 3500, 1000),
                "numbers_with_elongated_ticks": np.arange(0, 3000, 1000),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":GREEN,
                },
            },
            y_range=[0, 8, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 9, 2),
                "numbers_with_elongated_ticks": np.arange(0, 9, 2),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":BLUE,
                }
            },
            tips=False,
        )
        
    """ Starting Objects """
        
        axes = PQ_axis.shift(RIGHT*3.5+DOWN/4).scale(0.8)
        
        molly = Rectangle(height=3, width=3, color=PURPLE).move_to(LEFT*4.5 + UP*7/4)
        molly.z_index = 2
        molly_name = Tex("Molly").scale(1.5).next_to(molly,LEFT,buff=-1/2).set_color(PURPLE).rotate(np.pi/2)
        molly_group = VGroup(molly,molly_name)
        
        m_spinach = Rectangle(height=3, width=3, color=GREEN, fill_opacity=1)
        molly_crops = VGroup(m_spinach.next_to(molly_name,RIGHT,buff=0)).move_to(molly)
        
        andrew = Rectangle(height=3, width=2, color=RED).move_to(LEFT*4.5 + DOWN*7/4)
        andrew.z_index = 2
        andrew_name = Tex("Andrew").scale(1.5).next_to(andrew,LEFT,buff=-0.8).set_color(RED).rotate(np.pi/2)
        andrew_group = VGroup(andrew,andrew_name)
        
        a_spinach = Rectangle(height=3, width=2, color=GREEN, fill_opacity=1)
        andrew_crops = VGroup(a_spinach.next_to(andrew_name,RIGHT,buff=0)).move_to(andrew)

        supply_curve_label = Text(
            'Individual Supply Curves',
        font_size=32).next_to(axes, UP).set_color(SUPPLY)
        
    """ Setup """
        
        self.add(axes,molly_group,molly_crops,andrew_group,andrew_crops, supply_curve_label)
        
        molly_supply_graph = axes.plot(Molly_Supply, color=PURPLE, x_range=(0, 2000))
        self.add(molly_supply_graph)
        
        self.wait()
        
    """ Andrew's Supply Curve """
        
        andrew_supply_graph = axes.plot(Andrew_Supply, color=RED, x_range=(0, 800))
        self.play(FadeIn(andrew_supply_graph))
        
        self.wait()
        
    """ Add Quantities """
        
        pq_list = [[4, 1000], [6,1500], [2,500]]
        dots = VGroup()
        m_dots = VGroup()
        a_dots = VGroup()
        m_math = VGroup()
        a_math = VGroup()
        m_lines = VGroup()
        a_lines = VGroup()
        
        for p,q in pq_list:
            m = Tex('$q_s($',r'\$',p,') = ',q).set_color(PURPLE).scale(0.9).move_to(LEFT*3/2+UP*(p/3+1/2))
            m[1].set_color(BLUE)
            m[2].set_color(BLUE)
            m[-1].set_color(GREEN)
            m_math.add(m)
            
            new_molly = Rectangle(height=3*p/6, width=3, color=PURPLE, fill_opacity=0).move_to(LEFT*4.5 + UP*7/4)
            new_m_spinach = Rectangle(height=3*p/6, width=3, color=GREEN, fill_opacity=1).move_to(LEFT*4.5 + UP*7/4)

            q_a = Andrew_Supply_Inv(p)
            a = Tex('$q_s($',r'\$',p,') = ',q_a).set_color(RED).scale(0.9).move_to(LEFT*3/2+DOWN*((8-p)/3+1/2))
            a[1].set_color(BLUE)
            a[2].set_color(BLUE)
            a[-1].set_color(GREEN)
            a_math.add(a)
            
            new_andrew = Rectangle(height=3*p/6, width=2, color=RED).move_to(LEFT*4.5 + DOWN*7/4)
            new_a_spinach = Rectangle(height=3*p/6, width=2, color=GREEN, fill_opacity=1).move_to(LEFT*4.5 + DOWN*7/4)
        
            self.play(FadeIn(m),
                      FadeIn(a),
                      Transform(m_spinach,new_m_spinach),
                      Transform(molly,new_molly),
                      Transform(a_spinach,new_a_spinach),
                      Transform(andrew,new_andrew),
                     )
            self.wait()
            
            m_point = axes.coords_to_point(q, p)
            m_dot = Dot(m_point).set_color(PURPLE)
            m_dot.z_index = 2
            m_dots.add(m_dot)
            m_line = DashedVMobject(axes.plot(lambda x : p, color=PURPLE, x_range=(0, q)))
            m_lines.add(m_line)
            
            a_point = axes.coords_to_point(q_a, p)
            a_dot = Dot(a_point).set_color(RED)
            a_dot.z_index = 2
            a_dots.add(a_dot)
            a_line = DashedVMobject(axes.plot(lambda x : p, color=RED, x_range=(0, q_a)))
            a_lines.add(a_line)
            
            self.play(FadeIn(m_dot),FadeIn(a_dot),FadeIn(m_line))
            self.add(a_line)
            self.play(a_line.animate.move_to(m_dot,LEFT))

            point = axes.coords_to_point(q_a + q, p)
            dot = Dot(point)
            dot.z_index = 2
            dots.add(dot)
            self.play(FadeIn(dot))
            self.wait()
            
    """ Add Market Supply """
        
        market_supply_curve_label = Text(
            'Market Supply Curve',
        font_size=32).next_to(axes, UP).set_color(SUPPLY)
        
        supply_graph = axes.plot(Supply, color=SUPPLY, x_range=(0, 3000))
        self.play(FadeIn(supply_graph),Transform(supply_curve_label,market_supply_curve_label))
        
        self.wait()
        
    """ Clear Screen """
        
        self.play(
            FadeOut(m_dots),
            FadeOut(a_dots),
            FadeOut(m_lines),
            FadeOut(a_lines),
            FadeOut(m_math),
            FadeOut(a_math),
            FadeOut(dots),
        )

        self.wait()
        
        supply_definition = Paragraph(
            'Market Supply Curve \n',
            ' The sum of all ',
            ' individual supply curves.',
        font_size=32).to_edge(LEFT).shift(UP*2)
        supply_definition[0][:17].set_color(DEFINITION)
        
        higher_costs = Paragraph(
            'Higher costs shifts the',
            'supply curves up.',
        font_size=32).to_edge(LEFT).shift(DOWN)
        
        self.play(
            FadeOut(molly_group),
            FadeOut(m_spinach),
            FadeOut(andrew_group),
            FadeOut(a_spinach),
            FadeIn(supply_definition)
        )
        self.wait()
        self.play(FadeIn(higher_costs))
        self.wait()
        
    """ Clear More """
        
        more_info = Paragraph(
            'More info in Chapter 4.',
        font_size=32).to_edge(LEFT).shift(DOWN)
        self.play(FadeOut(higher_costs),FadeIn(more_info))
        self.wait()


marginal_cost = 3

PQ_line = Axes(            
    x_range=[0, 2, 1],
    x_length = 1,
    axis_config={"color": WHITE},
    x_axis_config={
        "numbers_to_include": [],
        "decimal_number_config": {
            "num_decimal_places":0,
        },
    },
    y_range=[0, 8, 8],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": [],
        "numbers_with_elongated_ticks": [],
        "decimal_number_config": {
            "num_decimal_places":2,
        }
    },
    tips=False,
)

class animation_4(MovingCameraScene):

    def construct(self):

    """ Starting Objects """

        title_string = "{{Producer Surplus}} is the sellers's extra value from an exchange."
        title_color_map = {"Producer Surplus": BLUE}
        title =Tex(title_string).set_color_by_tex_to_color_map(title_color_map).to_edge(UP)
        
        axes = PQ_line.copy().scale(0.8).to_edge(DOWN).shift(UP/2).shift(LEFT*2)

        y_label = axes.get_y_axis_label("P")
        x_label = axes.get_x_axis_label("Q")
        
        grid_labels = VGroup(x_label, y_label)
        mc_line = axes.plot(lambda x: marginal_cost, x_range=[-0.5,0.5]).set_color(WHITE)
        mc_number = DecimalNumber(num_decimal_places=2).set_color(WHITE).scale(0.8).next_to(mc_line,LEFT).set_value(marginal_cost)
        
        self.play(FadeIn(title, axes, grid_labels, mc_line, mc_number))
        
    """ Show Producer Surplus """
        
        price = ValueTracker(5)
            
        def Plot_Price():
            line = axes.plot(lambda x: price.get_value(), x_range=[-0.5,0.5]).set_color(RED)
            number = DecimalNumber(num_decimal_places=2).set_color(RED).scale(0.8).next_to(line,LEFT).set_value(price.get_value())
            label = Tex("Price =").set_color(RED).next_to(number, LEFT, buff=1/4)
            return VGroup(line, label, number)
        price_line = always_redraw(Plot_Price)
        
        self.play(FadeIn(price_line))
        self.wait()

        def Single_Producer_Surplus():
            point = axes.c2p(-1, price.get_value())
            ps_label = Tex("Producer Surplus =").next_to(point, RIGHT, buff=3).set_color(BLUE).shift(UP/2)
            cost_label = Tex("Marginal Cost =").next_to(point, RIGHT, buff=3).set_color(PURPLE).shift(DOWN/2)

            if float(price.get_value()) > marginal_cost:
                ps = Line(axes.c2p(1,price.get_value()), axes.c2p(1,marginal_cost)).set_color(BLUE)
                ps_number = DecimalNumber(num_decimal_places=2).set_color(BLUE).scale(0.8).next_to(ps_label,RIGHT,buff=1/4).set_value(price.get_value()-marginal_cost)
                
                spend = Line(axes.c2p(1,marginal_cost), axes.c2p(1,0)).set_color(PURPLE)                
                spend_number = DecimalNumber(num_decimal_places=2).set_color(PURPLE).scale(0.8).next_to(cost_label,RIGHT, buff=1/4).set_value(marginal_cost)
                
            if float(price.get_value()) <= marginal_cost:                
                ps = Line(axes.c2p(1,marginal_cost), axes.c2p(1,marginal_cost)).set_color(BLUE)
                ps_number = DecimalNumber(num_decimal_places=2).set_color(BLUE).scale(0.8).next_to(ps_label,RIGHT,buff=1/4).set_value(0)
                
                spend = Line(axes.c2p(1,0), axes.c2p(1,0)).set_color(PURPLE)
                spend_number = DecimalNumber(num_decimal_places=2).set_color(PURPLE).scale(0.8).next_to(cost_label,RIGHT, buff=1/4).set_value(0)
            
            return VGroup(ps, ps_number, spend, spend_number, ps_label, cost_label)
            
        producer_surplus = always_redraw(Single_Producer_Surplus)
        self.play(FadeIn(producer_surplus))
        self.wait()

    """ Move Price Around """

        for p in [6, 2, 3.5, 5]:
            self.play(price.animate.set_value(p))
            self.wait()


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

class animation_5(MovingCameraScene):

    def construct(self):

    """ Starting Objects """

        title_string = "{{Producer Surplus}} is the sellers's extra value from an exchange."
        title_color_map = {"Producer Surplus": BLUE}
        title =Tex(title_string).set_color_by_tex_to_color_map(title_color_map).to_edge(UP)
        
        axes = PQ_large.copy().scale(0.8).to_edge(DOWN+LEFT).shift(UP/2+RIGHT*2)

        y_label = axes.get_y_axis_label("P")
        x_label = axes.get_x_axis_label("Q")
        grid_labels = VGroup(x_label, y_label)
        
        self.play(FadeIn(title, axes, grid_labels))

    """ Functions """

        slope = 5
        intercept = 2
        def Supply(q):
            return intercept + q / slope
        def Inv_Supply(p):
            return (p-intercept) * slope

    """ Supply as a Line """

        price = ValueTracker(5)
        
        Supply_Line = axes.plot(Supply, x_range=[0,x_max]).set_color(YELLOW)
        Supply_Line.z_index = 3
        self.play(FadeIn(Supply_Line))
        self.wait()
        
        def Quantity_Supplied():
            p = price.get_value()
            q = Inv_Supply(p)
            point = axes.c2p(q, p)
            dot = Dot(point).set_color(RED)
            dot.z_index = 4
            
            p_line = DashedVMobject(axes.plot(lambda x: price.get_value(), x_range=[-1,q])).set_color(RED)
            p_line.z_index = 2
            p_number = DecimalNumber(num_decimal_places=0).set_color(RED).scale(0.8).next_to(p_line,LEFT, buff=3/4).set_value(p)
            p_label = Tex("Price =").set_color(RED).next_to(p_number, LEFT, buff=1/4)

            q_line = DashedVMobject(Line(axes.c2p(q,0), axes.c2p(q,p))).set_color(RED)
            q_line.z_index = 2
            q_number = DecimalNumber(num_decimal_places=0).set_color(RED).scale(0.8).next_to(q_line,DOWN, buff=1/2+0.1).set_value(q)
            q_label = Tex("$Q_s =$").set_color(RED).next_to(q_number, LEFT, buff=1/4)

            return VGroup(dot, p_label, p_line, p_number, q_label, q_line, q_number)
            
        quantity_supplied = always_redraw(Quantity_Supplied)
        self.play(FadeIn(quantity_supplied))

    """ Supply Equation """

        supply_label = Tex("Supply:").set_color(YELLOW)
        supply_equation = always_redraw(
            lambda: MathTex(
                r"P = 2 + \frac{Q_s}{5} = " + f"{price.get_value():.0f}"
            ).next_to(supply_label,RIGHT).set_color(YELLOW)
        )
        supply_title = VGroup(supply_label,supply_equation).next_to(title,DOWN).to_edge(RIGHT)

        self.add(supply_title)

        self.play(price.animate.set_value(9))
        self.wait()

    """ Producer Surplus """
        
        def PS_Plot():
            p = price.get_value()
            q = Inv_Supply(p)
            lines = []
            
            for i in np.arange(1/2, q, 1/2):
                i_p = Supply(i)
                
                ps_line = Line(axes.c2p(i,p), axes.c2p(i,i_p)).set_color(BLUE)
                ps_line.z_index = -1
                lines.append(ps_line)
                
            return VGroup(*lines)

        ps_plot = always_redraw(PS_Plot)
        self.play(Create(ps_plot))
        self.wait()

    """ Producer Surplus Equation """

        ps_label = Tex("PS").set_color(BLUE)
        ps_equation = always_redraw(
            lambda: MathTex(
                f" = ({price.get_value():.0f} - {intercept:.0f}) \\cdot {Inv_Supply(price.get_value()):.0f} \\cdot" + r"\frac{1}{2}" + f" = {(price.get_value() - intercept)*Inv_Supply(price.get_value())/2:.1f}"
            ).next_to(ps_label,RIGHT).set_color(BLUE)
        )

        ps_title = VGroup(ps_label,ps_equation).next_to(supply_title,DOWN*5).to_edge(RIGHT)

        self.play(FadeIn(ps_title))
        self.wait()

    """ Comprehension Checks """

        for p in [4, 8]:
            self.play(FadeOut(supply_title, ps_title))
            self.play(price.animate.set_value(p))
            self.wait()
            self.play(FadeIn(supply_title))
            self.wait()
            self.play(FadeIn(ps_title))
            self.wait()
