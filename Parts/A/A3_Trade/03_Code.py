# maniml 03_Code.py animation_0

from manim import *
import numpy as np
import os, sys, warnings, random

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *          # palette tokens, frame config, beat(), title(), bumper(), ...
from style import axes as style_axes
from Video import *          # PPF_Molly / PPF_Andrew / PPF_Guild -- the numbers of record

warnings.filterwarnings('ignore')


class animation_0(Scene):

    """Animation 0 | Intro Sequence"""

    def construct(self):
        bumper(self, 'A', 3)


class animation_1(Scene):

    """Animation 1 | Last Time..."""

    def construct(self):
        last_time(self)
        self.wait()


class animation_2(Scene):

    """Animation 2 | The Specialized Guild"""

    def construct(self):
        
        # ---- Definitions
        
        PPF_axis = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 65, 15),
                "numbers_with_elongated_ticks": np.arange(0, 65, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 10, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 11, 2),
                "numbers_with_elongated_ticks": np.arange(0, 11, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )
        
        # ---- Starting Objects
        
        axes = PPF_axis.shift(RIGHT*2).scale(0.8)
        
        ppf_molly_graph = axes.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        molly = Rectangle(height=3, width=3, color=MOLLY).move_to(LEFT*4.5 + UP*2)
        molly.z_index = 2
        molly_name = Tex("Molly").scale(1.5).next_to(molly,LEFT,buff=-1/2).set_color(MOLLY).rotate(np.pi/2)
        molly_cost = Tex("$1C=9S$").next_to(molly,RIGHT,buff=-0.6).set_color(MOLLY).rotate(np.pi/2)
        molly_group = VGroup(molly,molly_name,molly_cost)
        
        m_carrots = Rectangle(height=3/2, width=3, color=CARROTS, fill_opacity=1)
        m_spinach = Rectangle(height=3/2, width=3, color=SPINACH, fill_opacity=1)
        molly_crops = VGroup(m_carrots,m_spinach.next_to(m_carrots,DOWN,buff=0)).move_to(molly)
        
        ppf_andrew_graph = axes.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))
        andrew = Rectangle(height=3, width=3, color=ANDREW).move_to(LEFT*4.5 + DOWN*2)
        andrew.z_index = 2
        andrew_name = Tex("Andrew").scale(1.5).next_to(andrew,LEFT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_cost = Tex("$1C=4.5S$").next_to(andrew,RIGHT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_group = VGroup(andrew,andrew_name,andrew_cost)
        
        a_carrots = Rectangle(height=3/2, width=3, color=CARROTS, fill_opacity=1)
        a_spinach = Rectangle(height=3/2, width=3, color=SPINACH, fill_opacity=1)
        andrew_crops = VGroup(a_carrots,a_spinach.next_to(a_carrots,DOWN,buff=0)).move_to(andrew)
        
        ppf_guild_graph = axes.plot(PPF_Guild, color=GUILD, x_range=(0, 63))
    
        p1m = axes.coords_to_point(22.5, 2.5)
        p1a = axes.coords_to_point(9, 2)
        p1g = axes.coords_to_point(31.5, 4.5)
        dotm = Dot(p1m)
        dotm.z_index = 2
        dota = Dot(p1a)
        dota.z_index = 2
        dotg = Dot(p1g)
        dotg.z_index = 2
        
        guild_name = Tex("Guild PPF").scale(1.2).next_to(axes, UP).set_color(GUILD)

        spinach_advantage = Tex("Spinach").rotate(np.pi/2).set_color(SPINACH).next_to(molly_group,RIGHT)
        carrot_advantage = Tex("Carrots").rotate(np.pi/2).set_color(CARROTS).next_to(andrew_group,RIGHT)
        
        # ---- Setup
        self.add(dotm,dota,dotg,spinach_advantage,carrot_advantage)
        self.add(axes,molly_group,molly_crops,andrew_group,andrew_crops,ppf_molly_graph,ppf_andrew_graph,guild_name,ppf_guild_graph)
        self.wait()
        
        # ---- Show Comparative Advantages
        
        molly_ad = axes.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        andrew_ad = axes.coords_to_point(0,4)
        andrew_ad = Dot(andrew_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        andrew_ad.z_index = 0
        
        self.play(FadeIn(molly_ad),FadeIn(andrew_ad))
        self.wait()
        
        # ---- Specialize
        
        alpha_pairs = [[1,0],[0,1]]
        for pair in alpha_pairs:
            alpha_m = pair[0]
            alpha_a = pair[1]

            m_carrots_new = Rectangle(height=alpha_m*3, width=3, color=CARROTS, fill_opacity=1)
            m_spinach_new = Rectangle(height=(1-alpha_m)*3, width=3, color=SPINACH, fill_opacity=1)
            molly_crops_new = VGroup(m_carrots_new,m_spinach_new.next_to(m_carrots_new,DOWN,buff=0)).move_to(molly)

            a_carrots_new = Rectangle(height=alpha_a*3, width=3, color=CARROTS, fill_opacity=1)
            a_spinach_new = Rectangle(height=(1-alpha_a)*3, width=3, color=SPINACH, fill_opacity=1)
            andrew_crops_new = VGroup(a_carrots_new,a_spinach_new.next_to(a_carrots_new,DOWN,buff=0)).move_to(andrew)

            p2m = axes.coords_to_point(45*(1-alpha_m), 5*alpha_m)
            p2a = axes.coords_to_point(18*(1-alpha_a), 4*alpha_a)
            p2g = axes.coords_to_point(45*(1-alpha_m)+18*(1-alpha_a), 5*alpha_m+4*alpha_a)

            self.play(dotm.animate.move_to(p2m),dota.animate.move_to(p2a),dotg.animate.move_to(p2g),
                      Transform(molly_crops,molly_crops_new),Transform(andrew_crops,andrew_crops_new))
            self.wait()
            
        # ---- Trace The Specialized Guild
            
        path = VMobject(color=TRADE)
        path.set_points_as_corners([dotg.get_center(), dotg.get_center()])
        def update_path(path):
            previous_path = path.copy()
            previous_path.add_points_as_corners([dotg.get_center()])
            path.become(previous_path)
        path.add_updater(update_path)
        self.add(path, dotg)
        
        self.play(ppf_guild_graph.animate.set_opacity(0.1))
        
        alpha_pairs = [[1,1],[0,1],[0,0]]
        for pair in alpha_pairs:
            alpha_m = pair[0]
            alpha_a = pair[1]

            m_carrots_new = Rectangle(height=alpha_m*3, width=3, color=CARROTS, fill_opacity=1)
            m_spinach_new = Rectangle(height=(1-alpha_m)*3, width=3, color=SPINACH, fill_opacity=1)
            molly_crops_new = VGroup(m_carrots_new,m_spinach_new.next_to(m_carrots_new,DOWN,buff=0)).move_to(molly)

            a_carrots_new = Rectangle(height=alpha_a*3, width=3, color=CARROTS, fill_opacity=1)
            a_spinach_new = Rectangle(height=(1-alpha_a)*3, width=3, color=SPINACH, fill_opacity=1)
            andrew_crops_new = VGroup(a_carrots_new,a_spinach_new.next_to(a_carrots_new,DOWN,buff=0)).move_to(andrew)

            p2m = axes.coords_to_point(45*(1-alpha_m), 5*alpha_m)
            p2a = axes.coords_to_point(18*(1-alpha_a), 4*alpha_a)
            p2g = axes.coords_to_point(45*(1-alpha_m)+18*(1-alpha_a), 5*alpha_m+4*alpha_a)

            self.play(dotm.animate.move_to(p2m),dota.animate.move_to(p2a),dotg.animate.move_to(p2g),
                      Transform(molly_crops,molly_crops_new),Transform(andrew_crops,andrew_crops_new))
            self.wait(1/10)
            
        # ---- Show Gains From Specialization
        
        a = axes.coords_to_point(63, 0)
        b = axes.coords_to_point(45, 4)
        c = axes.coords_to_point(0, 9)
        
        gains = Polygon(a,b,c, color=TRADE, fill_opacity=1)
        gains.z_index = 0
        gains_text = Tex('Gains From Specialization').scale(1.2).set_color(TRADE).next_to(gains, UP*3).shift(RIGHT/2)
        
        self.play(FadeOut(guild_name),FadeIn(gains),FadeIn(gains_text))
        self.wait()
        
        # ---- Do More Pairs
        
        alpha_pairs = [[0,1],[0.1,1],[0.2,1],[0.3,1],[0.4,1],[0.5,1],[0.6,1],[0.7,1],[0.8,1],[0.9,1],[1,1]] + [[0,0.9],[0,0.8],[0,0.7],[0,0.6],[0,0.5],[0,0.4],[0,0.3],[0,0.2],[0,0.1],[0,0], [0,1]]
        random.shuffle(alpha_pairs)
        for pair in alpha_pairs:
            alpha_m = pair[0]
            alpha_a = pair[1]

            m_carrots_new = Rectangle(height=alpha_m*3, width=3, color=CARROTS, fill_opacity=1)
            m_spinach_new = Rectangle(height=(1-alpha_m)*3, width=3, color=SPINACH, fill_opacity=1)
            molly_crops_new = VGroup(m_carrots_new,m_spinach_new.next_to(m_carrots_new,DOWN,buff=0)).move_to(molly)

            a_carrots_new = Rectangle(height=alpha_a*3, width=3, color=CARROTS, fill_opacity=1)
            a_spinach_new = Rectangle(height=(1-alpha_a)*3, width=3, color=SPINACH, fill_opacity=1)
            andrew_crops_new = VGroup(a_carrots_new,a_spinach_new.next_to(a_carrots_new,DOWN,buff=0)).move_to(andrew)

            p2m = axes.coords_to_point(45*(1-alpha_m), 5*alpha_m)
            p2a = axes.coords_to_point(18*(1-alpha_a), 4*alpha_a)
            p2g = axes.coords_to_point(45*(1-alpha_m)+18*(1-alpha_a), 5*alpha_m+4*alpha_a)

            self.play(dotm.animate.move_to(p2m),dota.animate.move_to(p2a),dotg.animate.move_to(p2g),
                      Transform(molly_crops,molly_crops_new),Transform(andrew_crops,andrew_crops_new))
            self.wait(1/10)

        self.wait()


class animation_3(MovingCameraScene):

    """Animation 3 | Setup The Questions"""

    def construct(self):
        
        # ---- Definitions
        
        PPF_axis = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 65, 15),
                "numbers_with_elongated_ticks": np.arange(0, 65, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 10, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 11, 2),
                "numbers_with_elongated_ticks": np.arange(0, 11, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )
        
        # ---- Starting Objects
        
        axes = PPF_axis.shift(RIGHT*2).scale(0.8)
        
        ppf_molly_graph = axes.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        molly = Rectangle(height=3, width=3, color=MOLLY).move_to(LEFT*4.5 + UP*2)
        molly.z_index = 2
        molly_name = Tex("Molly").scale(1.5).next_to(molly,LEFT,buff=-1/2).set_color(MOLLY).rotate(np.pi/2)
        molly_cost = Tex("$1C=9S$").next_to(molly,RIGHT,buff=-0.6).set_color(MOLLY).rotate(np.pi/2)
        molly_group = VGroup(molly,molly_name,molly_cost)
        
        m_carrots = Rectangle(height=3/2, width=3, color=CARROTS, fill_opacity=1)
        m_spinach = Rectangle(height=3/2, width=3, color=SPINACH, fill_opacity=1)
        molly_crops = VGroup(m_carrots,m_spinach.next_to(m_carrots,DOWN,buff=0)).move_to(molly)
        
        ppf_andrew_graph = axes.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))
        andrew = Rectangle(height=3, width=3, color=ANDREW).move_to(LEFT*4.5 + DOWN*2)
        andrew.z_index = 2
        andrew_name = Tex("Andrew").scale(1.5).next_to(andrew,LEFT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_cost = Tex("$1C=4.5S$").next_to(andrew,RIGHT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_group = VGroup(andrew,andrew_name,andrew_cost)
        
        a_carrots = Rectangle(height=3/2, width=3, color=CARROTS, fill_opacity=1)
        a_spinach = Rectangle(height=3/2, width=3, color=SPINACH, fill_opacity=1)
        andrew_crops = VGroup(a_carrots,a_spinach.next_to(a_carrots,DOWN,buff=0)).move_to(andrew)
            
        p1m = axes.coords_to_point(45, 0)
        p1a = axes.coords_to_point(0, 4)
        p1g = axes.coords_to_point(45, 4)
        dotm = Dot(p1m)
        dotm.z_index = 2
        dota = Dot(p1a)
        dota.z_index = 2
        dotg = Dot(p1g)
        dotg.z_index = 2
        
        spinach_advantage = Tex("Spinach").rotate(np.pi/2).set_color(SPINACH).next_to(molly_group,RIGHT)
        carrot_advantage = Tex("Carrots").rotate(np.pi/2).set_color(CARROTS).next_to(andrew_group,RIGHT)
        
        # ---- Setup
        self.add(dotm,dota,dotg,spinach_advantage,carrot_advantage)
        self.add(axes,molly_group,molly_crops,andrew_group,andrew_crops,ppf_molly_graph,ppf_andrew_graph)
        
        # ---- Show Comparative Advantages
        
        molly_ad = axes.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        andrew_ad = axes.coords_to_point(0,4)
        andrew_ad = Dot(andrew_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        andrew_ad.z_index = 0
        
        self.add(molly_ad, andrew_ad)
        self.add(dotg)
        
        # ---- Show Gains From Specialization
        
        a = axes.coords_to_point(63, 0)
        b = axes.coords_to_point(45, 4)
        c = axes.coords_to_point(0, 9)
        
        gains = Polygon(a,b,c, color=TRADE, fill_opacity=1)
        gains.z_index = 0
        gains_text = Tex('Gains From Specialization').scale(1.2).set_color(TRADE).next_to(gains, UP*3).shift(RIGHT/2)
        
        self.add(gains, gains_text)
        self.wait()
        
        # ---- Setup Questions

        question1 = Tex('But is a guild necessary?').scale(1.3).set_color(FOCUS).next_to(axes, RIGHT, buff=-1/2)
        frame_group = VGroup(axes, question1)
        
        self.play(
            self.camera.frame.animate.shift(RIGHT*5),
            FadeOut(molly_group), FadeOut(molly_crops), 
            FadeOut(andrew_group), FadeOut(andrew_crops),
            FadeOut(spinach_advantage), FadeOut(carrot_advantage),
            FadeOut(gains_text),
            FadeIn(question1)
        )
        
        self.wait()
        
        # ---- Make PPFs
        
        PPF_axis_small = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 50, 15),
                "numbers_with_elongated_ticks": np.arange(0, 50, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 6, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 6, 1),
                "numbers_with_elongated_ticks": np.arange(0, 6, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )
        
        axes_m = PPF_axis_small.copy().move_to(axes).shift(RIGHT)

        molly_name_new = Tex("Molly's PPF").scale(1.5).rotate(np.pi/2).set_color(MOLLY).next_to(axes_m,LEFT)#.set_x(self.camera.frame.get_left()[0]+2/5)

        new_frame_group = VGroup(axes_m, molly_name, question1)
        
        new_molly_ad = axes_m.coords_to_point(45,0)
        new_molly_ad = Dot(new_molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        new_molly_ad.z_index = 0
        
        new_ppf_molly_graph = axes_m.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        
        p1m = axes_m.coords_to_point(45, 0)
        dotm_new = Dot(p1m)
        dotm_new.z_index = 2

        self.play(
            FadeOut(gains), FadeOut(dotg),
            question1.animate.to_edge(UP).set_x(self.camera.frame.get_center()[0]),      
            Transform(molly_ad, new_molly_ad), 
            Transform(ppf_molly_graph, new_ppf_molly_graph),
            Transform(dotm, dotm_new),
            FadeIn(molly_name_new),
            Transform(axes, axes_m),
            FadeOut(ppf_andrew_graph, dota, andrew_ad),
        )
        self.wait()
        vertical_axis = NumberLine(
            x_range=[-5, 5, 1],  # Range from -5 to 5 with step size 1
            length=4,            # Length of the axis
            color=MUTED,         # Color of the line
            include_numbers=False, # Include numbers on the axis
            include_ticks=False,
            label_direction=LEFT  # Place numbers to the left of the line
        ).rotate(PI / 2)  # Rotate by 90 degrees (PI / 2 radians) to make it vertical

        # Correct the orientation of each number label to be horizontal
        #or number in vertical_axis.numbers:
            #number.rotate(-PI / 2)  # Rotate labels back to horizontal orientation
            #number.shift(LEFT * 0.3)

        vertical_carrots = vertical_axis.copy().next_to(axes, RIGHT, buff=2)
        vertical_spinach = vertical_axis.copy().next_to(vertical_carrots, RIGHT, buff=1/2)
        
        # Add the vertical axis to the scene
        self.play(FadeIn(vertical_carrots, vertical_spinach))
        self.wait(2)

        # Create a point to place on the NumberLine
        point = Dot(color=GUIDE)

        # Position the point at the number 2 on the NumberLine
        point_position = vertical_carrots.number_to_point(2)  # Convert number 2 to coordinates
        point.move_to(point_position)  # Move the point to the calculated position

        # Add the point to the scene
        self.add(point)

        self.wait(2)


PPF_axis = style_axes(            
    x_range=[0, 65, 5],
    x_length = 7,
    ticks=True,
    x_axis_config={
        "numbers_to_include": np.arange(0, 65, 15),
        "numbers_with_elongated_ticks": np.arange(0, 65, 10),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":SPINACH,
        },
    },
    y_range=[0, 10, 1],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": np.arange(0, 11, 2),
        "numbers_with_elongated_ticks": np.arange(0, 11, 5),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":CARROTS,
        }
    },
)

PPF_axis_small = style_axes(            
    x_range=[0, 65, 5],
    x_length = 7,
    ticks=True,
    x_axis_config={
        "numbers_to_include": np.arange(0, 50, 45),
        "numbers_with_elongated_ticks": np.arange(0, 50, 10),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":SPINACH,
        },
    },
    y_range=[0, 8, 1],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": np.arange(0, 6, 5),
        "numbers_with_elongated_ticks": np.arange(0, 6, 5),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":CARROTS,
        }
    },
)

vertical_spinach_axis = NumberLine(
    x_range=[0, 50, 1],  # Range from -5 to 5 with step size 1
    length=4,            # Length of the axis
    color=MUTED,         # Color of the line
    include_numbers=False, # Include numbers on the axis
    include_ticks=False,
    label_direction=LEFT  # Place numbers to the left of the line
).rotate(PI / 2)  # Rotate by 90 degrees (PI / 2 radians) to make it vertical

vertical_carrot_axis = NumberLine(
    x_range=[0, 8, 1],  # Range from -5 to 5 with step size 1
    length=4,            # Length of the axis
    color=MUTED,         # Color of the line
    include_numbers=False, # Include numbers on the axis
    include_ticks=False,
    label_direction=LEFT  # Place numbers to the left of the line
).rotate(PI / 2)  # Rotate by 90 degrees (PI / 2 radians) to make it vertical


class animation_4(MovingCameraScene):

    def construct(self):
        
        # ---- Starting Objects
        
        axes = PPF_axis.shift(RIGHT*2).scale(0.8)
        axes_m = PPF_axis_small.copy().move_to(axes).shift(RIGHT)

        question1 = Tex('But is a guild necessary?').scale(1.3).set_color(FOCUS).next_to(axes, RIGHT, buff=-1/2)
        molly_name = Tex("Molly's PPF").scale(1.5).rotate(np.pi/2).set_color(MOLLY).next_to(axes_m,LEFT)
        
        molly_ad = axes_m.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        ppf_molly_graph = axes_m.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        
        p1m = axes_m.coords_to_point(45, 0)
        dotm = Dot(p1m)
        dotm.z_index = 2


        self.camera.frame.shift(RIGHT*5)
        quetion1 = question1.to_edge(UP).set_x(self.camera.frame.get_center()[0])
        self.add(
            question1, molly_name, molly_ad,
            ppf_molly_graph, dotm, axes_m
        )

        p1m_self = axes_m.coords_to_point(45-27, 3)
        dotm_self = Dot(p1m_self)

        # Create a CurvedArrow
        curved_arrow = CurvedArrow(p1m, p1m_self, color=GUIDE, angle=PI / 4).shift(RIGHT/5+UP/5)

        p2m = axes_m.coords_to_point(45, 0)
        dot2m = Dot(p1m)
        dotm.z_index = 2

        m_value = ValueTracker(45)

        def Move_M():
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=1).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=1/4).set_value(x)
            y = PPF_Molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT,buff=0).set_value(y).rotate(np.pi/2)
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            y_intercept = axes_m.coords_to_point(0,0)

            carrot_line = Line(start=p2m, end=x_int, color=SPINACH, stroke_width=8)
            spinach_line = Line(start=y_intercept, end=y_int, color=CARROTS, stroke_width=8)
            
            return VGroup(dot,vline,hline,x_label,y_label,carrot_line,spinach_line)#,exchange_spinach,exchange_carrot)
            
        self.remove(dotm)
        dotm = always_redraw(Move_M)
        self.add(dotm)

        # ---- Op Cost Math 1

        self.play(Create(curved_arrow), m_value.animate.set_value(45-27),run_time=3)

        x = m_value.get_value()
        y = PPF_Molly(x)
        y_ex_p = axes_m.coords_to_point(0,y/2)
        x_ex_p = axes_m.coords_to_point((45+x)/2,0)
        
        exchange_carrot = Tex('{{3}} {{C}}').set_color(CARROTS).scale(0.8).next_to(y_ex_p,RIGHT,buff=1/4).set_value(y)
        exchange_spinach = Tex('{{27}} {{S}}').set_color(SPINACH).scale(0.8).next_to(x_ex_p,UP,buff=1/4).set_value(45-x)

        self.play(FadeIn(exchange_spinach, exchange_carrot))

        self.wait(1/2)

        OR = Tex("or").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        equal = Tex("=").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        
        self.play(FadeIn(OR),exchange_spinach.animate.next_to(OR,RIGHT,buff=1).scale(1.5/0.8),exchange_carrot.animate.next_to(OR,LEFT,buff=1).scale(1.5/0.8))
        self.wait(1/2)
        self.play(Transform(OR,equal))
        self.wait(1/2)
        
        exchange_carrot_new = Tex(r"$\frac{3}{3}$ {{C}}").scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": CARROTS,
            })
        exchange_spinach_new = Tex(r"{{$\frac{27}{3}$}} {{S}}").scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": SPINACH,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)

        exchange_carrot_new = Tex('{{1}} {{C}}').scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": CARROTS,
            })
        exchange_spinach_new = Tex('{{9}} {{S}}').scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": SPINACH,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)

        self.play(FadeOut(exchange_spinach, curved_arrow, OR, exchange_carrot))

        self.wait(1/2)

        # ---- Op Cost Math 2

        p1m_self = axes_m.coords_to_point(45-18, 2)
        dotm_self = Dot(p1m_self)

        # Create a CurvedArrow
        curved_arrow = CurvedArrow(p1m, p1m_self, color=GUIDE, angle=PI / 4).shift(RIGHT/5+UP/5)

        self.play(Create(curved_arrow), m_value.animate.set_value(45-18),run_time=3)

        x = m_value.get_value()
        y = PPF_Molly(x)
        y_ex_p = axes_m.coords_to_point(0,y/2)
        x_ex_p = axes_m.coords_to_point((45+x)/2,0)

        exchange_carrot = Tex('{{2}} {{C}}').set_color(CARROTS).scale(0.8).next_to(y_ex_p,RIGHT,buff=1/4).set_value(y)
        exchange_spinach = Tex('{{18}} {{S}}').set_color(SPINACH).scale(0.8).next_to(x_ex_p,UP,buff=1/4).set_value(45-x)

        self.play(FadeIn(exchange_spinach, exchange_carrot))

        self.wait(1/2)

        OR = Tex("or").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        equal = Tex("=").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        
        self.play(FadeIn(OR),exchange_spinach.animate.next_to(OR,RIGHT,buff=1).scale(1.5/0.8),exchange_carrot.animate.next_to(OR,LEFT,buff=1).scale(1.5/0.8))
        self.wait(1/2)
        self.play(Transform(OR,equal))
        self.wait(1/2)
        
        exchange_carrot_new = Tex(r"$\frac{2}{2}$ {{C}}").scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": CARROTS,
            })
        exchange_spinach_new = Tex(r"{{$\frac{18}{2}$}} {{S}}").scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": SPINACH,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)

        exchange_carrot_new = Tex('{{1}} {{C}}').scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": CARROTS,
            })
        exchange_spinach_new = Tex('{{9}} {{S}}').scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": SPINACH,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)
        
        molly_exchange = VGroup(exchange_spinach, OR, exchange_carrot)
        molly_exchange_new = Tex('1 C = 9 S').set_color(MOLLY).next_to(axes_m,UP,buff=-1)

        self.play(Transform(molly_exchange, molly_exchange_new))
        self.wait(1/2)

        # ---- Trade Deal: Offer Molly 3 instead of 2

        c_X = ValueTracker(3)
        s_X = ValueTracker(27)

        def Move_MX():
            x = s_X.get_value()
            x_int = axes_m.coords_to_point(x,0)

            y = c_X.get_value()
            y_int = axes_m.coords_to_point(0,y)
            
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(GUILD)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            start = axes_m.coords_to_point(0.4,0)
            end = axes_m.coords_to_point(0.4,y)
            carrot_line = Line(start=start, end=end, color=TRADE, stroke_width=8)
            y_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(y_int,RIGHT,buff=0).set_value(y).rotate(np.pi/2)

            start = axes_m.coords_to_point(45,0.4/9)
            end = axes_m.coords_to_point(x,0.4/9)
            spinach_line = Line(start=start, end=end, color=GUILD, stroke_width=8)
            x_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(x_int,UP,buff=1/4).set_value(x)

            return VGroup(dot,vline,hline,y_label,carrot_line,spinach_line,x_label)#,exchange_spinach,exchange_carrot)
            
        dotmx = always_redraw(Move_MX)
        
        exchange_carrot = Tex('{{3}} {{C}}').set_color(GUILD).scale(0.8).next_to(dotmx[4],RIGHT,buff=0)
        exchange_spinach = Tex('{{18}} {{S}}').set_color(GUILD).scale(0.8).next_to(dotmx[5],UP,buff=0)

        self.play(FadeIn(dotmx), FadeIn(exchange_carrot, exchange_spinach), FadeOut(curved_arrow))

        self.wait(1/2)

        OR = Tex("or").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        equal = Tex("=").next_to(axes_m,RIGHT,buff=2).scale(1.5)
        
        self.play(FadeIn(OR),exchange_spinach.animate.next_to(OR,RIGHT,buff=1).scale(1.5/0.8),exchange_carrot.animate.next_to(OR,LEFT,buff=1).scale(1.5/0.8))
        self.wait(1/2)
        self.play(Transform(OR,equal))
        self.wait(1/2)
        
        exchange_carrot_new = Tex(r"$\frac{3}{3}$ {{C}}").scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": GUILD,
            })
        exchange_spinach_new = Tex(r"{{$\frac{18}{3}$}} {{S}}").scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": GUILD,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)

        exchange_carrot_new = Tex('{{1}} {{C}}').scale(1.5).next_to(OR,LEFT,buff=1).set_color_by_tex_to_color_map({
                "C": GUILD,
            })
        exchange_spinach_new = Tex('{{6}} {{S}}').scale(1.5).next_to(OR,RIGHT,buff=1).set_color_by_tex_to_color_map({
                "S": GUILD,
            })
        self.play(Transform(exchange_carrot[0],exchange_carrot_new[0]),Transform(exchange_spinach[0],exchange_spinach_new[0]))
        self.wait(1/2)

        exchange_rate = VGroup(exchange_spinach, OR, exchange_carrot)
        
        exchange_rate_new = Tex('1 C = {{6}} S').set_color(GUILD)
        exchange_rate_new.next_to(molly_exchange, RIGHT, buff=2)
        
        self.play(Transform(exchange_rate, exchange_rate_new))
        self.wait(1/2)

        e_box = SurroundingRectangle(exchange_rate, buff=1/4)
        self.play(Create(e_box))
        
        m_box = SurroundingRectangle(molly_exchange, buff=1/4)
        self.play(Create(m_box))
        
        self.wait(1/2)

        self.play(FadeOut(e_box),FadeOut(m_box))

        #trade_point_new = axes_m.coords_to_point(, )
        #trade_dot_new = Dot(trade_point_new).set_color(GUILD)
        #trade_dot_new.z_index = 3

        self.wait(1/2)

        self.play(
            s_X.animate.set_value(45-27),
            c_X.animate.set_value(27/6),
            m_value.animate.set_value(45-27)
        )

        self.wait(1/2)
        # Then show the trade line when it's good like this

        alpha_m = 0
        alpha_a = 1
        c_x = ValueTracker(1)
        s_x = ValueTracker(6)
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x.get_value()/s_x.get_value()

        trade_line = DashedVMobject(axes_m.plot(trade_molly, color=TRADE, x_range=(0, 45)))

        self.play(FadeIn(trade_line))

        self.wait(1/2)

        # ---- Then change the exchange rate 1 for 4
        
        # exchange rate label
        exchange_rate_new = Tex('1 C = {{4}} S').set_color(GUILD).next_to(molly_exchange, RIGHT, buff=2)

        # exchange rate line
        s_x.set_value(4)
        
        trade_line_new = DashedVMobject(axes_m.plot(trade_molly, color=TRADE, x_range=(0, 45)))

        self.play(
            c_X.animate.set_value(27/4),
            Transform(exchange_rate,exchange_rate_new),
            Transform(trade_line,trade_line_new)
        )
        self.wait(1/2)

        self.play(
            c_X.animate.set_value((45-24)/4),
            s_X.animate.set_value(24)
        )
        self.wait(1/2)


PPF_axis = style_axes(            
    x_range=[0, 65, 5],
    x_length = 7,
    ticks=True,
    x_axis_config={
        "numbers_to_include": np.arange(0, 65, 15),
        "numbers_with_elongated_ticks": np.arange(0, 65, 10),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":SPINACH,
        },
    },
    y_range=[0, 10, 1],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": np.arange(0, 11, 2),
        "numbers_with_elongated_ticks": np.arange(0, 11, 5),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":CARROTS,
        }
    },
)

PPF_axis_small = style_axes(            
    x_range=[0, 65, 5],
    x_length = 7,
    ticks=True,
    x_axis_config={
        "numbers_to_include": np.arange(0, 50, 45),
        "numbers_with_elongated_ticks": np.arange(0, 50, 10),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":SPINACH,
        },
    },
    y_range=[0, 8, 1],
    y_length = 6,
    y_axis_config={
        "numbers_to_include": np.arange(0, 6, 5),
        "numbers_with_elongated_ticks": np.arange(0, 6, 5),
        "decimal_number_config": {
            "num_decimal_places":0,
            "color":CARROTS,
        }
    },
)

vertical_spinach_axis = NumberLine(
    x_range=[0, 50, 1],  # Range from -5 to 5 with step size 1
    length=4,            # Length of the axis
    color=MUTED,         # Color of the line
    include_numbers=False, # Include numbers on the axis
    include_ticks=False,
    label_direction=LEFT  # Place numbers to the left of the line
).rotate(PI / 2)  # Rotate by 90 degrees (PI / 2 radians) to make it vertical

vertical_carrot_axis = NumberLine(
    x_range=[0, 8, 1],  # Range from -5 to 5 with step size 1
    length=4,            # Length of the axis
    color=MUTED,         # Color of the line
    include_numbers=False, # Include numbers on the axis
    include_ticks=False,
    label_direction=LEFT  # Place numbers to the left of the line
).rotate(PI / 2)  # Rotate by 90 degrees (PI / 2 radians) to make it vertical


# shadowed duplicate, kept for the rewrite
class animation_5_v1(MovingCameraScene):

    def construct(self):

        self.camera.frame.shift(RIGHT*5)
        
        # ---- Starting Axes
        
        axes = PPF_axis.shift(RIGHT*2).scale(0.8)
        axes_m = PPF_axis_small.copy().move_to(axes).shift(RIGHT)

        vertical_spinach = vertical_spinach_axis.copy().next_to(axes_m, RIGHT, buff=2)
        vertical_carrots = vertical_carrot_axis.copy().next_to(vertical_spinach, RIGHT, buff=1/2)

        axes_a = PPF_axis_small.copy().next_to(vertical_carrots, buff=1).shift(RIGHT)

        # ---- Starting Text

        question1 = Tex('But is a guild necessary?').scale(1.3).set_color(FOCUS).next_to(axes, RIGHT, buff=-1/2)
        quetion1 = question1.to_edge(UP).set_x(self.camera.frame.get_center()[0])

        molly_name = Tex("Molly's PPF").scale(1.5).rotate(np.pi/2).set_color(MOLLY).next_to(axes_m,LEFT)
        molly_exchange = Tex('1 C = 9 S').set_color(MOLLY).rotate(np.pi/2).next_to(axes_m,RIGHT,buff=1/2)
        
        # ---- Starting Graph Objects
        
        molly_ad = axes_m.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        ppf_molly_graph = axes_m.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        ppf_andrew_graph = axes_a.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))


        alpha_m = 0
        alpha_a = 1
        c_x = ValueTracker(27/4)
        s_x = ValueTracker(27)
        m_value = ValueTracker(45-27)

        def Move_X():
            cx = c_x.get_value()
            sx = s_x.get_value()
            
            c_t_point = Dot(color=GUILD)
            c_t_point_position = vertical_carrots.number_to_point(cx)
            c_t_point.move_to(c_t_point_position)
            c_t_point.z_index = 3

            s_t_point = Dot(color=GUILD)
            s_t_point_position = vertical_spinach.number_to_point(sx)
            s_t_point.move_to(s_t_point_position)
            s_t_point.z_index = 3

            trade_point = axes_m.coords_to_point(45-sx, sx/4)
            trade_dot = Dot(trade_point).set_color(GUILD)
            trade_dot.z_index = 3

            first = Tex("1 C = ")
            second = DecimalNumber(sx/cx, num_decimal_places=0)
            third = Tex(" S")
            exchange_rate = VGroup(first,second,third).arrange(RIGHT).set_color(GUILD)
            exchange_rate = exchange_rate.next_to(VGroup(vertical_spinach, vertical_carrots), DOWN, buff=1/2)

            def trade_molly(s):
                x = s - (1-alpha_m)*45
                return alpha_m * 5 - x * cx/sx
            
            trade_line_m = DashedVMobject(axes_m.plot(trade_molly, color=TRADE, x_range=(0, 45)))

            def trade_andrew(s):
                x = s - (1-alpha_a)*18
                return alpha_a*4 - x*cx/sx
                
            trade_line_a = DashedVMobject(axes_a.plot(trade_andrew, color=TRADE, x_range=(0, 45)))
        
            return VGroup(
                c_t_point, s_t_point, trade_dot,
                trade_line_m, exchange_rate,
                trade_line_a
            )
        dotx = always_redraw(Move_X)

        def Move_M():
            p1m_self = axes_m.coords_to_point(45-27, 3)
            dotm_self = Dot(p1m_self)
    
            p1m = axes_m.coords_to_point(45, 0)
            dotm = Dot(p1m)
            dotm.z_index = 2
    
            p2m = axes_m.coords_to_point(45, 0)
            dot2m = Dot(p1m)
            dotm.z_index = 2
            
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=1).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=1/4).set_value(x)
            
            y = PPF_Molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT,buff=0).set_value(y).rotate(np.pi/2)
            
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            y_intercept = axes_m.coords_to_point(0,0)

            carrot_line = Line(start=p2m, end=x_int, color=SPINACH, stroke_width=8)
            spinach_line = Line(start=y_intercept, end=y_int, color=CARROTS, stroke_width=8)

            start_point = vertical_carrots.n2p(0)
            end_point = vertical_carrots.n2p(y)
            c_line = Line(start=start_point, end=end_point, color=CARROTS, stroke_width=8)
            c_line.z_index = 1
            
            c_label = DecimalNumber(num_decimal_places=1).set_value(y).scale(0.8).set_color(CARROTS)
            c_label.next_to(end_point, RIGHT)
    
            start_point = vertical_spinach.n2p(0)
            end_point = vertical_spinach.n2p(45-x) 
            s_line = Line(start=start_point, end=end_point, color=SPINACH, stroke_width=8)
            s_line.z_index = 1

            s_label = DecimalNumber(num_decimal_places=1).set_value(45-x).scale(0.8).set_color(SPINACH)
            s_label.next_to(end_point, LEFT)
            
            return VGroup(
                dot,vline,hline,x_label,y_label,carrot_line,spinach_line,
                c_line,c_label, s_line, s_label
                         )

        dotm = always_redraw(Move_M)

        def Move_A():
            p1a_self = axes_a.coords_to_point(45-27, 3)
            dota_self = Dot(p1a_self)
    
            p1a = axes_a.coords_to_point(45, 0)
            dota = Dot(p1a)
            dota.z_index = 2
    
            p2a = axes_a.coords_to_point(45, 0)
            dot2a = Dot(p1a)
            dota.z_index = 2
        
            x = m_value.get_value()
            x_int = axes_a.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=1).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=1/4).set_value(x)
            
            y = PPF_Andrew(x)
            y_int = axes_a.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT,buff=0).set_value(y).rotate(np.pi/2)
            
            p = axes_a.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            y_intercept = axes_a.coords_to_point(0,0)

            carrot_line = Line(start=p2a, end=x_int, color=SPINACH, stroke_width=8)
            spinach_line = Line(start=y_intercept, end=y_int, color=CARROTS, stroke_width=8)

            start_point = vertical_carrots.n2p(0)
            end_point = vertical_carrots.n2p(y)
            c_line = Line(start=start_point, end=end_point, color=CARROTS, stroke_width=8)
            c_line.z_index = 1
            
            c_label = DecimalNumber(num_decimal_places=1).set_value(y).scale(0.8).set_color(CARROTS)
            c_label.next_to(end_point, RIGHT)

            start_point = vertical_spinach.n2p(0)
            end_point = vertical_spinach.n2p(45-x) 
            s_line = Line(start=start_point, end=end_point, color=SPINACH, stroke_width=8)
            s_line.z_index = 1

            s_label = DecimalNumber(num_decimal_places=1).set_value(45-x).scale(0.8).set_color(SPINACH)
            s_label.next_to(end_point, LEFT)
            
            return VGroup(
                dot,vline,hline,x_label,y_label,carrot_line,spinach_line,
                c_line,c_label, s_line, s_label
                         )

        dota = always_redraw(Move_A)

        # ---- Add Objects
        
        self.add(
            question1, 
            molly_name, 
            molly_ad,
            ppf_molly_graph, 
            dotm,
            dotx,
            axes_m,
            dotm,
            molly_exchange,
            vertical_carrots, 
            vertical_spinach,
            #c_t_point,
            #s_t_point,
            #trade_dot,
            #exchange_rate,
            #trade_line,
        )

        self.play(
            FadeIn(axes_a, dota, ppf_andrew_graph),
            #self.camera.frame.animate,
            self.camera.frame.animate.set(width=23).shift(RIGHT*4+UP),
            question1.animate.shift(RIGHT*3.5+UP*3).scale(1.5)
        )
        self.wait()

        #self.play(m_value.animate.set_value(0))

# the colored lines on the ppf graph are enough
# take them off the vertical lines and use the vertical lines only later
# how to show trade then?
# show a purple line on the ppf graph, like the orange and green
# do the op cost math thing with trade
# then put the exchange rate right below the question

# show the trade vertical lines with color and a purple dot
# show the purple line on the ppf graphs


# shadowed duplicate, kept for the rewrite
class animation_5_v2(MovingCameraScene):

    def construct(self):
        # ---- Make PPFs
        
        PPF_axis_small = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 50, 45),
                "numbers_with_elongated_ticks": np.arange(0, 50, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 6, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 6, 5),
                "numbers_with_elongated_ticks": np.arange(0, 6, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )
        
        axes_a = PPF_axis_small.copy()
        ppf_andrew_graph = axes_a.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))
        andrew_name = Tex("Andrew").scale(1.2).next_to(axes_a,UP,buff=1/2).set_color(ANDREW)

        axes_m = PPF_axis_small.copy().next_to(axes_a, LEFT*2)
        ppf_molly_graph = axes_m.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        molly_name = Tex("Molly").scale(1.2).next_to(axes_m,UP,buff=1/2).set_color(MOLLY)
        
        molly_ad = axes_m.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        andrew_ad = axes_a.coords_to_point(0,4)
        andrew_ad = Dot(andrew_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        andrew_ad.z_index = 0
        
        p1m = axes_m.coords_to_point(45, 0)
        p1a = axes_a.coords_to_point(0, 4)
        
        dotm = Dot(p1m)
        dotm.z_index = 2
        dota = Dot(p1a)
        dota.z_index = 2
        
        frame_group = VGroup(
            axes_m, dotm, molly_name, ppf_molly_graph, molly_ad,
            axes_a, dota, andrew_name, ppf_andrew_graph, andrew_ad,
        )
        title = Tex('But is a guild necessary?').scale(1.3).set_color(FOCUS).next_to(frame_group, UP, buff=1/2)

        self.add(frame_group, title)
        self.camera.frame.move_to(frame_group).set(width=frame_group.width*1.3),
        
        self.wait()
        
        # ---- Self Trade
        
        m_value = ValueTracker(45)
        a_value = ValueTracker(0)

        def Move_M():
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=2/3).set_value(x)
            y = PPF_Molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT).set_value(y)
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            p2m = axes_m.coords_to_point(45, 0)
            y_intercept = axes_m.coords_to_point(0,0)

            carrot_line = Line(start=p2m, end=x_int, color=SPINACH, stroke_width=8)
            spinach_line = Line(start=y_intercept, end=y_int, color=CARROTS, stroke_width=8)
            

            return VGroup(dot,vline,hline,x_label,y_label, carrot_line, spinach_line)
        
        def Move_A():
            x = a_value.get_value()
            x_int = axes_a.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=2/3).set_value(x)
            y = PPF_Andrew(x)
            y_int = axes_a.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT).set_value(y)
            p = axes_a.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            p2a = axes_a.coords_to_point(0, 0)
            y_intercept = axes_a.coords_to_point(0,4)

            spinach_line = Line(start=p2a, end=x_int, color=SPINACH, stroke_width=8)
            carrot_line = Line(start=y_intercept, end=y_int, color=CARROTS, stroke_width=8)
            
            return VGroup(dot,vline,hline,x_label,y_label, carrot_line, spinach_line)

        self.remove(dotm)
        dotm = always_redraw(Move_M)
        self.add(dotm)
        
        self.play(m_value.animate.set_value(36),run_time=3)
        self.wait()
        
        molly_cost = Tex("1C"," for ","9S").set_color(MOLLY).next_to(molly_name,DOWN)
        self.play(FadeIn(molly_cost))
        self.wait()
        
        m_box = SurroundingRectangle(molly_cost[2], buff=1/4)
        self.play(FadeIn(m_box))
        self.wait()
        
        self.play(m_value.animate.set_value(45),run_time=3)
        new_title = Tex('Molly benefits if she trades away less than 9S.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()

        self.remove(dota)
        dota = always_redraw(Move_A)
        self.add(dota)
        self.remove(dotm)
        
        self.play(a_value.animate.set_value(9/2),run_time=3)
        self.wait()
        
        andrew_cost = Tex("1C"," for ","4.5S").set_color(ANDREW).next_to(andrew_name,DOWN)
        self.play(FadeIn(andrew_cost))
        self.wait()
        
        a_box = SurroundingRectangle(andrew_cost[2], buff=1/4)
        self.play(FadeIn(a_box))
        self.wait()
        
        new_title = Tex('Andrew benefits if he trades for more than 4.5S.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        
        self.play(a_value.animate.set_value(0),run_time=3)
        self.wait()

        self.remove(dota)
        
        # ---- Exchange Rate
        
        c_x = ValueTracker(1)
        s_x = ValueTracker(6)
        def Exchange():
            c = c_x.get_value()
            c_value = DecimalNumber(num_decimal_places=0).set_value(c)
            s = s_x.get_value()
            s_value = DecimalNumber(num_decimal_places=1).set_value(s)

            return Tex(f"{int(c)} C"," for ",f"{round(s,1)} S").set_color(TRADE).scale(1.2).next_to(frame_group,UP, buff=-1/4)
        exchange = always_redraw(Exchange)
        self.play(FadeIn(exchange))
        self.wait()
        
        e_box = SurroundingRectangle(exchange[2], buff=1/4)
        self.play(FadeIn(e_box))
        self.wait()
        
        alpha_m = 0
        alpha_a = 1
        
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x.get_value()/s_x.get_value()
        
        def Trade_M():
            trade_line = DashedVMobject(axes_m.plot(trade_molly, color=TRADE, x_range=(0, 50)))
            
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            y = trade_molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(y_int,LEFT,buff=1).set_value(y)
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(GUILD)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            start = axes_m.coords_to_point(0.4,0)
            end = axes_m.coords_to_point(0.4,y)
            carrot_line = Line(start=start, end=end, color=TRADE, stroke_width=8)
            #y_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(y_int,RIGHT,buff=0).set_value(y).rotate(np.pi/2)

            start = axes_m.coords_to_point(45,0.4/9)
            end = axes_m.coords_to_point(x,0.4/9)
            spinach_line = Line(start=start, end=end, color=GUILD, stroke_width=8)
            x_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(x_int,UP,buff=1/4).set_value(x)
            
            return VGroup(trade_line,dot,vline,hline,y_label,x_label,carrot_line,spinach_line)
        
        trade_m = always_redraw(Trade_M)
        
        
        def trade_andrew(s):
            x = s - (1-alpha_a)*18
            return alpha_a*4 - x*c_x.get_value()/s_x.get_value()
        
        def Trade_A():
            trade_line = DashedVMobject(axes_a.plot(trade_andrew, color=GUILD, x_range=(0, 50)))
            
            x = a_value.get_value()
            x_int = axes_a.coords_to_point(x,0)
            y = trade_andrew(x)
            y_int = axes_a.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(y_int,LEFT,buff=1).set_value(y)
            p = axes_a.coords_to_point(x,y)
            dot = Dot(p).set_color(GUILD)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)

            start = axes_a.coords_to_point(0.4,4)
            end = axes_a.coords_to_point(0.4,y)
            carrot_line = Line(start=start, end=end, color=TRADE, stroke_width=8)
            #y_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(y_int,RIGHT,buff=0).set_value(y).rotate(np.pi/2)

            start = axes_a.coords_to_point(0,0.4/9)
            end = axes_a.coords_to_point(x,0.4/9)
            spinach_line = Line(start=start, end=end, color=GUILD, stroke_width=8)
            x_label = DecimalNumber(num_decimal_places=1).set_color(GUILD).scale(0.8).next_to(x_int,UP,buff=1/4).set_value(x)
            
            return VGroup(trade_line,dot,vline,hline,y_label,x_label,carrot_line,spinach_line)
        
        trade_a = always_redraw(Trade_A)
        
        self.play(FadeIn(trade_m))
        self.play(m_value.animate.set_value(45-27),run_time=2)
        self.wait()
        new_title = Tex('Molly benefits from this exchange rate.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(FadeIn(trade_a), FadeOut(trade_m))
        self.wait()
        self.play(a_value.animate.set_value(9),run_time=2)
        self.wait()
        new_title = Tex('Andrew also benefits from this exchange rate.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0),run_time=2)
        self.wait()
        
        # ---- Trade 2 C for 12 S
        
        self.play(FadeIn(trade_m))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        new_title = Tex('Both benefit.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        # ---- Change the exchange rate

        self.play(FadeOut(title), s_x.animate.set_value(10))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        title = Tex('Only Andrew benefits.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(FadeIn(title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(FadeOut(title),s_x.animate.set_value(4))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        title = Tex('Only Molly benefits.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(FadeIn(title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(FadeOut(title), s_x.animate.set_value(6))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        title = Tex('Both benefit.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(FadeIn(title))
        self.wait()
        #self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        #self.wait()

        # ---- Better than a specific point.

        m_value.set_value(34)
        a_value.set_value(11)

        self.play(
            FadeIn(dotm, dota)
        )
        
        # ---- Unspecialize
        
        # in progress
        
        # ---- Conclusions
        
        new_title = Tex("Exchanging 1C for anything between ", "9S"," and ","4.5S", " works!").set_color(FOCUS).set_color_by_tex_to_color_map({
                "9S": MOLLY,
                "4.5S": ANDREW,
            }).move_to(title)
        self.play(Transform(title, new_title))#, self.camera.frame.animate.move_to(final_group).set(width=final_group.width*1.3))


class animation_5(MovingCameraScene):

    """Two-Sided Trade"""

    def construct(self):
        # ---- Make PPFs
        
        PPF_axis_small = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 50, 45),
                "numbers_with_elongated_ticks": np.arange(0, 50, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 6, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 6, 5),
                "numbers_with_elongated_ticks": np.arange(0, 6, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )
        
        axes_a = PPF_axis_small.copy()
        ppf_andrew_graph = axes_a.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))
        andrew_name = Tex("Andrew").scale(1.2).next_to(axes_a,UP,buff=1/2).set_color(ANDREW)

        axes_m = PPF_axis_small.copy().next_to(axes_a, LEFT*2)
        ppf_molly_graph = axes_m.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        molly_name = Tex("Molly").scale(1.2).next_to(axes_m,UP,buff=1/2).set_color(MOLLY)
        
        molly_ad = axes_m.coords_to_point(45,0)
        molly_ad = Dot(molly_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        molly_ad.z_index = 0
        
        andrew_ad = axes_a.coords_to_point(0,4)
        andrew_ad = Dot(andrew_ad, radius=0.2, stroke_width=0, fill_opacity=0.3, color=INK)
        andrew_ad.z_index = 0
        
        p1m = axes_m.coords_to_point(45, 0)
        p1a = axes_a.coords_to_point(0, 4)
        dotm = Dot(p1m)
        dotm.z_index = 2
        dota = Dot(p1a)
        dota.z_index = 2
        
        frame_group = VGroup(
            axes_m, dotm, molly_name, ppf_molly_graph, molly_ad,
            axes_a, dota, andrew_name, ppf_andrew_graph, andrew_ad,
        )
        title = Tex('But is a guild necessary?').scale(1.3).set_color(FOCUS).next_to(frame_group, UP, buff=1/2)

        self.add(frame_group, title)
        self.camera.frame.move_to(frame_group).set(width=frame_group.width*1.3),
        
        self.wait()
        
        # ---- Self Trade
        
        m_value = ValueTracker(45)
        a_value = ValueTracker(0)

        def Move_M():
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=2/3).set_value(x)
            y = PPF_Molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT).set_value(y)
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)
            
            return VGroup(dot,vline,hline,x_label,y_label)
        
        def Move_A():
            x = a_value.get_value()
            x_int = axes_a.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(SPINACH).scale(0.8).next_to(x_int,DOWN,buff=2/3).set_value(x)
            y = PPF_Andrew(x)
            y_int = axes_a.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT).set_value(y)
            p = axes_a.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)
            
            return VGroup(dot,vline,hline,x_label,y_label)
                
        self.remove(dotm)
        dotm = always_redraw(Move_M)
        self.add(dotm)
        
        self.play(m_value.animate.set_value(36),run_time=3)
        self.wait()
        
        molly_cost = Tex("1C"," for ","9S").set_color(MOLLY).next_to(molly_name,DOWN)
        self.play(FadeIn(molly_cost))
        self.wait()
        
        m_box = SurroundingRectangle(molly_cost[2], buff=1/4)
        m_sign = Tex("-").scale(1.5).next_to(m_box, DOWN).set_color(FOCUS)
        self.play(FadeIn(m_box), FadeIn(m_sign))
        self.wait()
        
        self.play(m_value.animate.set_value(45),run_time=3)
        new_title = Tex('Molly benefits if she trades away less than 9S.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        
        self.remove(dota)
        dota = always_redraw(Move_A)
        self.add(dota)

        self.play(a_value.animate.set_value(9/2),run_time=3)
        self.wait()
        
        andrew_cost = Tex("1C"," for ","4.5S").set_color(ANDREW).next_to(andrew_name,DOWN)
        self.play(FadeIn(andrew_cost))
        self.wait()
        
        a_box = SurroundingRectangle(andrew_cost[2], buff=1/4)
        a_sign = Tex("+").scale(1.5).next_to(a_box, DOWN).set_color(FOCUS)
        self.play(FadeIn(a_box), FadeIn(a_sign))
        self.wait()
        
        new_title = Tex('Andrew benefits if he trades for more than 4.5S.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        
        self.play(a_value.animate.set_value(0),run_time=3)
        self.wait()
        
        # ---- Exchange Rate
        
        c_x = ValueTracker(1)
        s_x = ValueTracker(6)
        def Exchange():
            c = c_x.get_value()
            c_value = DecimalNumber(num_decimal_places=0).set_value(c)
            s = s_x.get_value()
            s_value = DecimalNumber(num_decimal_places=1).set_value(s)

            return Tex(f"{int(c)} C"," for ",f"{round(s,1)} S").set_color(TRADE).scale(1.2).next_to(frame_group,UP, buff=-1/4)
        exchange = always_redraw(Exchange)
        self.play(FadeIn(exchange))
        self.wait()
        
        e_box = SurroundingRectangle(exchange[2], buff=1/4)
        self.play(FadeIn(e_box))
        self.wait()
        
        alpha_m = 0
        alpha_a = 1
        
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x.get_value()/s_x.get_value()
        
        def Trade_M():
            trade_line = DashedVMobject(axes_m.plot(trade_molly, color=TRADE, x_range=(0, 50)))
            
            x = m_value.get_value()
            x_int = axes_m.coords_to_point(x,0)
            y = trade_molly(x)
            y_int = axes_m.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT,buff=1).set_value(y)
            p = axes_m.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)
            
            return VGroup(trade_line,dot,vline,hline,y_label)
        
        trade_m = always_redraw(Trade_M)
        
        
        def trade_andrew(s):
            x = s - (1-alpha_a)*18
            return alpha_a*4 - x*c_x.get_value()/s_x.get_value()
        
        def Trade_A():
            trade_line = DashedVMobject(axes_a.plot(trade_andrew, color=TRADE, x_range=(0, 50)))
            
            x = a_value.get_value()
            x_int = axes_a.coords_to_point(x,0)
            y = trade_andrew(x)
            y_int = axes_a.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(CARROTS).scale(0.8).next_to(y_int,LEFT,buff=1).set_value(y)
            p = axes_a.coords_to_point(x,y)
            dot = Dot(p).set_color(INK)
            dot.z_index = 2
            vline = DashedLine(x_int,p).set_color(MUTED)
            hline = DashedLine(y_int,p).set_color(MUTED)
            
            return VGroup(trade_line,dot,vline,hline,y_label)
        
        trade_a = always_redraw(Trade_A)
        
        self.play(FadeIn(trade_m))
        self.play(m_value.animate.set_value(45-27),run_time=2)
        self.wait()
        new_title = Tex('Molly benefits from this exchange rate.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(FadeIn(trade_a), FadeOut(trade_m))
        self.wait()
        self.play(a_value.animate.set_value(9),run_time=2)
        self.wait()
        new_title = Tex('Andrew also benefits from this exchange rate.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0),run_time=2)
        self.wait()
        
        # ---- Trade 2 C for 12 S
        
        self.play(FadeIn(trade_m))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        new_title = Tex('Both benefit.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        # ---- Change the exchange rate
        
        self.play(s_x.animate.set_value(10))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        new_title = Tex('Only Andrew benefits.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(s_x.animate.set_value(4))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        new_title = Tex('Only Molly benefits.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        self.play(s_x.animate.set_value(6))
        self.wait()
        self.play(a_value.animate.set_value(12), m_value.animate.set_value(45-12),run_time=2)
        self.wait()
        new_title = Tex('Both benefit.').set_color(FOCUS).next_to(frame_group, UP, buff=1/2)
        self.play(Transform(title, new_title))
        self.wait()
        self.play(a_value.animate.set_value(0), m_value.animate.set_value(45),run_time=2)
        self.wait()
        
        # ---- Unspecialize
        
        # in progress
        
        # ---- Conclusions
        
        new_title = Tex("Exchanging 1C for anything between ", "9S"," and ","4.5S", " works!").set_color(FOCUS).set_color_by_tex_to_color_map({
                "9S": MOLLY,
                "4.5S": ANDREW,
            }).move_to(title)
        self.play(Transform(title, new_title))#, self.camera.frame.animate.move_to(final_group).set(width=final_group.width*1.3))


class animation_old(Scene):      

    """Animation 5 | Trade With Another (unused)"""

    def construct(self):
        
        # ---- Definitions
        
        PPF_axis = style_axes(            
            x_range=[0, 65, 5],
            x_length = 7,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 65, 15),
                "numbers_with_elongated_ticks": np.arange(0, 65, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
            y_range=[0, 10, 1],
            y_length = 6,
            y_axis_config={
                "numbers_to_include": np.arange(0, 11, 2),
                "numbers_with_elongated_ticks": np.arange(0, 11, 5),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":CARROTS,
                }
            },
        )

        alpha_m = 2/3
        alpha_a = 1/3
        
        # ---- Starting Objects
        
        axes = PPF_axis.shift(RIGHT*2).scale(0.8)
        
        ppf_molly_graph = axes.plot(PPF_Molly, color=MOLLY, x_range=(0, 45))
        molly = Rectangle(height=3, width=3, color=MOLLY).move_to(LEFT*4.5 + UP*2)
        molly.z_index = 2
        molly_name = Tex("Molly").scale(1.5).next_to(molly,LEFT,buff=-1/2).set_color(MOLLY).rotate(np.pi/2)
        molly_cost = Tex("$1C=9S$").next_to(molly,RIGHT,buff=-0.6).set_color(MOLLY).rotate(np.pi/2)
        molly_group = VGroup(molly,molly_name,molly_cost)
        
        m_carrots = Rectangle(height=alpha_m*3, width=3, color=CARROTS, fill_opacity=1)
        m_spinach = Rectangle(height=(1-alpha_m)*3, width=3, color=SPINACH, fill_opacity=1)
        molly_crops = VGroup(m_carrots,m_spinach.next_to(m_carrots,DOWN,buff=0)).move_to(molly)
        
        ppf_andrew_graph = axes.plot(PPF_Andrew, color=ANDREW, x_range=(0, 18))
        andrew = Rectangle(height=3, width=3, color=ANDREW).move_to(LEFT*4.5 + DOWN*2)
        andrew.z_index = 2
        andrew_name = Tex("Andrew").scale(1.5).next_to(andrew,LEFT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_cost = Tex("$1C=4.5S$").next_to(andrew,RIGHT,buff=-0.8).set_color(ANDREW).rotate(np.pi/2)
        andrew_group = VGroup(andrew,andrew_name,andrew_cost)
        
        a_carrots = Rectangle(height=alpha_a*3, width=3, color=CARROTS, fill_opacity=1)
        a_spinach = Rectangle(height=(1-alpha_a)*3, width=3, color=SPINACH, fill_opacity=1)
        andrew_crops = VGroup(a_carrots,a_spinach.next_to(a_carrots,DOWN,buff=0)).move_to(andrew)
    
        p1m = axes.coords_to_point((1-alpha_m)*45, alpha_m*5)
        p1a = axes.coords_to_point((1-alpha_a)*18, alpha_a*4)
        dotm = Dot(p1m)
        dota = Dot(p1a)
        
        # ---- Setup
        
        self.add(axes,molly_group,molly_crops,andrew_group,andrew_crops,ppf_molly_graph,ppf_andrew_graph,dotm,dota)
        self.wait(1/2)
        
        # ---- Introduce The Exchange Rate
        
        c_x,s_x = 1,20
        exchange = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                "C": CARROTS,
                "S": SPINACH,
            })
        
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x/s_x
        trade_molly_graph = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
        
        def trade_andrew(s):
            x = s - (1-alpha_a)*18
            return alpha_a*4 - x*c_x/s_x
        trade_andrew_graph = DashedVMobject(axes.plot(trade_andrew, color=TRADE, x_range=(0, 50)))
        
        self.play(FadeIn(exchange))
        self.wait(1/2)
        framebox1 = SurroundingRectangle(exchange, buff = 0.3).set_color(TRADE)
        self.play(Create(framebox1))
        self.wait(1/2)
        self.play(dota.animate.set_opacity(0.1),ppf_andrew_graph.animate.set_opacity(0.1))
        self.wait(1/2)
        self.play(Create(trade_molly_graph))
        self.wait(1/2)
        
        c_x,s_x = 1,30
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x/s_x
        trade_molly_graph_new = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
        exchange_new = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                "C": CARROTS,
                "S": SPINACH,
            })
        self.play(Transform(trade_molly_graph,trade_molly_graph_new),Transform(exchange,exchange_new))
        
        c_x,s_x = 1,2
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x/s_x
        trade_molly_graph_new = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
        exchange_new = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                "C": CARROTS,
                "S": SPINACH,
            })
        self.play(Transform(trade_molly_graph,trade_molly_graph_new),Transform(exchange,exchange_new))
        
        b = axes.coords_to_point(45, 0)
        c = axes.coords_to_point(50, trade_molly(50))
        if c_x/s_x > 1/9:
            b = axes.coords_to_point(0, 5)
            c = axes.coords_to_point(0, trade_molly(0))
        trade_region_molly = Polygon(p1m,b,c, color=MOLLY,fill_opacity=0)
        #self.play(Create(trade_region_molly))
        self.play(trade_region_molly.animate.set_fill(MOLLY, opacity=0.5))
        self.wait(1/2)
        
        for c_x,s_x in [[1,80]]: #something's not right with andrew's area when s_x is less than 4.5...
            def trade_molly(s):
                x = s - (1-alpha_m)*45
                return alpha_m*5 - x*c_x/s_x
            def trade_molly_inv(c):
                return alpha_m*5*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_m)*45
            trade_molly_graph_new = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
            exchange_new = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                    "C": CARROTS,
                    "S": SPINACH,})
            self.play(Transform(trade_molly_graph,trade_molly_graph_new),Transform(exchange,exchange_new),FadeOut(trade_region_molly))
            b = axes.coords_to_point(45, 0)
            c = axes.coords_to_point(trade_molly_inv(0),0)
            if c_x/s_x > 1/9:
                b = axes.coords_to_point(0, 5)
                c = axes.coords_to_point(0, trade_molly(0))
            trade_region_molly = Polygon(p1m,b,c, color=MOLLY,fill_opacity=0).set_fill(MOLLY, opacity=0.5)
            self.play(FadeIn(trade_region_molly))
            self.wait(1/2)

            self.play(dota.animate.set_opacity(1),ppf_andrew_graph.animate.set_opacity(1))

            def trade_andrew(s):
                x = s - (1-alpha_a)*18
                return alpha_a*4 - x*c_x/s_x
            def trade_andrew_inv(c):
                return alpha_a*4*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_a)*18
            trade_andrew_graph = DashedVMobject(axes.plot(trade_andrew, color=TRADE, x_range=(0, 50)))

            self.play(Create(trade_andrew_graph))
            b = axes.coords_to_point(0, 4)
            c = axes.coords_to_point(0,0)
            if c_x/s_x < 1/4.5:
                b = axes.coords_to_point(18, 0)
                c = axes.coords_to_point(trade_andrew_inv(0), 0)
            trade_region_andrew = Polygon(p1a,b,c, color=ANDREW,fill_opacity=0).set_fill(ANDREW, opacity=0.5)
            self.play(FadeIn(trade_region_andrew))

            arrow_molly = Arrow(np.array([0, 0, 0]), np.array([2, -1/2, 0]), color=MOLLY, buff=0).next_to(dotm,DOWN+RIGHT,buff=0)
            arrow_andrew = Arrow(np.array([0, 0, 0]), np.array([2, -1/2, 0]), color=ANDREW, buff=0).next_to(dota,DOWN+RIGHT,buff=0)

            self.play(FadeIn(arrow_molly),FadeIn(arrow_andrew))
            self.play(FadeOut(arrow_molly),FadeOut(arrow_andrew))
        

        c_x,s_x = 1,80
        alpha_m = 0
        alpha_a = 1
        
        m_carrots_new = Rectangle(height=alpha_m*3, width=3, color=CARROTS, fill_opacity=1)
        m_spinach_new = Rectangle(height=(1-alpha_m)*3, width=3, color=SPINACH, fill_opacity=1)
        molly_crops_new = VGroup(m_carrots_new,m_spinach_new.next_to(m_carrots_new,DOWN,buff=0)).move_to(molly)
        
        a_carrots_new = Rectangle(height=alpha_a*3, width=3, color=CARROTS, fill_opacity=1)
        a_spinach_new = Rectangle(height=(1-alpha_a)*3, width=3, color=SPINACH, fill_opacity=1)
        andrew_crops_new = VGroup(a_carrots_new,a_spinach_new.next_to(a_carrots_new,DOWN,buff=0)).move_to(andrew)
        
        p1m = axes.coords_to_point((1-alpha_m)*45, alpha_m*5)
        p1a = axes.coords_to_point((1-alpha_a)*18, alpha_a*4)
        dotm_new = Dot(p1m)
        dota_new = Dot(p1a)
        
        def trade_molly(s):
            x = s - (1-alpha_m)*45
            return alpha_m*5 - x*c_x/s_x
        def trade_molly_inv(c):
            return alpha_m*5*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_m)*45
        trade_molly_graph_new = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
        exchange_new = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                "C": CARROTS,
                "S": SPINACH,})        
        def trade_andrew(s):
            x = s - (1-alpha_a)*18
            return alpha_a*4 - x*c_x/s_x
        def trade_andrew_inv(c):
            return alpha_a*4*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_a)*18
        trade_andrew_graph_new = DashedVMobject(axes.plot(trade_andrew, color=TRADE, x_range=(0, 50)))
        self.play(Transform(trade_molly_graph,trade_molly_graph_new),Transform(trade_andrew_graph,trade_andrew_graph_new),
                  Transform(dotm,dotm_new),Transform(dota,dota_new),
                  Transform(exchange,exchange_new),
                  FadeOut(trade_region_molly),FadeOut(trade_region_andrew),
                  Transform(molly_crops,molly_crops_new),Transform(andrew_crops,andrew_crops_new))
        
        b = axes.coords_to_point(45, 0)
        c = axes.coords_to_point(trade_molly_inv(0),0)
        if c_x/s_x > 1/9:
            b = axes.coords_to_point(0, 5)
            c = axes.coords_to_point(0, trade_molly(0))
        trade_region_molly = Polygon(p1m,b,c, color=MOLLY,fill_opacity=0).set_fill(MOLLY, opacity=0.5)
        
        b = axes.coords_to_point(0, 4)
        c = axes.coords_to_point(0,0)
        if c_x/s_x < 1/4.5:
            b = axes.coords_to_point(18, 0)
            c = axes.coords_to_point(trade_andrew_inv(0), 0)
        trade_region_andrew = Polygon(p1a,b,c, color=ANDREW,fill_opacity=0).set_fill(ANDREW, opacity=0.5)
        
        self.play(FadeIn(trade_region_molly),FadeIn(trade_region_andrew))
        self.wait()
        
        
        alpha_m = 0
        alpha_a = 1
        for pair in [[1,6],[1,4.55],[1,9],[1,6]]:
            c_x,s_x = pair[0],pair[1]

            def trade_molly(s):
                x = s - (1-alpha_m)*45
                return alpha_m*5 - x*c_x/s_x
            def trade_molly_inv(c):
                return alpha_m*5*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_m)*45
            trade_molly_graph_new = DashedVMobject(axes.plot(trade_molly, color=TRADE, x_range=(0, 50)))
            exchange_new = Tex(str(c_x)+' {{C}} for '+str(s_x)+' {{S}}').move_to(UP*2+RIGHT*3).scale(1.5).set_color_by_tex_to_color_map({
                    "C": CARROTS,
                    "S": SPINACH,})        
            def trade_andrew(s):
                x = s - (1-alpha_a)*18
                return alpha_a*4 - x*c_x/s_x
            def trade_andrew_inv(c):
                return alpha_a*4*(s_x/c_x) - c*(s_x/c_x) + (1-alpha_a)*18
            trade_andrew_graph_new = DashedVMobject(axes.plot(trade_andrew, color=TRADE, x_range=(0, 50)))
            self.play(Transform(trade_molly_graph,trade_molly_graph_new),Transform(trade_andrew_graph,trade_andrew_graph_new),
                      Transform(exchange,exchange_new),
                      FadeOut(trade_region_molly),FadeOut(trade_region_andrew))

            b = axes.coords_to_point(45, 0)
            c = axes.coords_to_point(trade_molly_inv(0),0)
            if c_x/s_x > 1/9:
                b = axes.coords_to_point(0, 5)
                c = axes.coords_to_point(0, trade_molly(0))
            trade_region_molly = Polygon(p1m,b,c, color=MOLLY,fill_opacity=0).set_fill(MOLLY, opacity=0.5)

            b = axes.coords_to_point(0, 4)
            c = axes.coords_to_point(0,0)
            if c_x/s_x < 1/4.5:
                b = axes.coords_to_point(18, 0)
                c = axes.coords_to_point(trade_andrew_inv(0), 0)
            trade_region_andrew = Polygon(p1a,b,c, color=ANDREW,fill_opacity=0).set_fill(ANDREW, opacity=0.5)

            self.play(FadeIn(trade_region_molly),FadeIn(trade_region_andrew))
            self.wait()
            
        c_x,s_x = 1,6
        dotm_trade = Dot(color=TRADE).move_to(dotm)
        dota_trade = Dot(color=TRADE).move_to(dota)
        for i in [1,2,3,4,3,2]:
            p1m = axes.coords_to_point((1-alpha_m)*45 - s_x/c_x*i, alpha_m*5 + i)
            p1a = axes.coords_to_point((1-alpha_a)*18 + s_x/c_x*i, alpha_a*4 - i)
            self.play(dotm_trade.animate.move_to(p1m),dota_trade.animate.move_to(p1a),)
        self.wait()
        
        alpha_m = 1/3.5
        alpha_a = 2/5
        p1m = axes.coords_to_point((1-alpha_m)*45, alpha_m*5)
        p1a = axes.coords_to_point((1-alpha_a)*18, alpha_a*4)
        dotm = Dot(p1m)
        dota = Dot(p1a)
        self.play(FadeIn(dotm),FadeIn(dota))
        self.wait()
