# maniml 03_Code.py animation_0

from manim import *
import numpy as np
import os, sys, warnings
import random

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *          # palette tokens, frame config, beat(), title(), bumper(), ...
from style import axes as style_axes
from Video import *          # PPF_Molly / PPF_Andrew / PPF_Guild

warnings.filterwarnings('ignore')


class animation_0(Scene):

    """Animation 0 | Intro Sequence"""

    def construct(self):
        bumper(self, 'A', 4)


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
            [0, 65, 5],
            [0, 10, 1],
            x_length=7,
            y_length=6,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 65, 15),
                "numbers_with_elongated_ticks": np.arange(0, 65, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
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


class animation_old(Scene):

    """Animation 5 | Trade With Another (unused)"""

    def construct(self):

        # ---- Definitions

        PPF_axis = style_axes(
            [0, 65, 5],
            [0, 10, 1],
            x_length=7,
            y_length=6,
            ticks=True,
            x_axis_config={
                "numbers_to_include": np.arange(0, 65, 15),
                "numbers_with_elongated_ticks": np.arange(0, 65, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    "color":SPINACH,
                },
            },
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
        framebox1 = SurroundingRectangle(exchange, buff = 0.3).set_color(FOCUS)
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
