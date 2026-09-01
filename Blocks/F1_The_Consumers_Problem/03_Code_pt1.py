# maniml 03_Code.py -ql -v ERROR ThreeDSurfacePlot

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

# Configuration
config.background_color = 'black'

class ThreeDSurfacePlot(ThreeDScene):
    def construct(self):
        resolution_fa = 10
        
        def cobb_douglas(u,v):
            x = u - 5
            y = v - 5
            z = u**(1/2) + v**(1/2) -3
            return np.array([x, y, z])
        
        gauss_plane = Surface(
            cobb_douglas,
            resolution=(resolution_fa, resolution_fa),
            fill_color='#29ABCA',
            v_range=[0.5, 10],
            u_range=[0.5, 10]
        )
        
        axes = ThreeDAxes(x_range=(0, 10, 1), y_range=(0, 10, 1), z_range=(0, 1, 1))
        zlabel = axes.get_z_axis_label(Tex("$Utility$"))
        xlabel = axes.get_x_axis_label(Tex("$Carrots$"))
        ylabel = axes.get_y_axis_label(Tex("$Spinach$"))
        
        self.add(axes, gauss_plane, zlabel, xlabel, ylabel)
        
        self.set_camera_orientation(phi=75 * DEGREES, theta=180 * DEGREES)
        
        self.begin_ambient_camera_rotation()
        self.wait(1)
        self.stop_ambient_camera_rotation()


class FillByValueExample(ThreeDScene):
    def construct(self):
        resolution_fa = 10
        self.set_camera_orientation(phi=75 * DEGREES, theta=-160 * DEGREES)
        
        axes = ThreeDAxes(x_range=(0, 5, 1), y_range=(0, 5, 1), z_range=(-1, 1, 0.5))
        
        def param_surface(u, v):
            x = u
            y = v
            z = x + y
            return z
        
        surface_plane = Surface(
            lambda u, v: axes.c2p(u, v, param_surface(u, v)),
            resolution=(resolution_fa, resolution_fa),
            v_range=[0, 5],
            u_range=[0, 5],
            )
        surface_plane.set_style(fill_opacity=1)
        surface_plane.set_fill_by_value(axes=axes, colorscale=[(RED, -0.5), (YELLOW, 0), (GREEN, 0.5)], axis=2)
        self.add(axes, surface_plane)
        
        self.begin_ambient_camera_rotation(rate=0.1)
        self.wait(1)


class animation_0(Scene):
    def construct(self):
        title = Tex("Part E ").scale(2)
        subtitle = Tex("$|$ Consumer Choice",color=GREY).scale(2).next_to(title,RIGHT)
        title_group = VGroup(title,subtitle).move_to(UP*2)
        topic_list = [
            "{{1.}} Preferences",
            "{{2.}} Indiference Curves",
            "{{3.}} Utility",
            "{{4.}} Marginal Rate of Substitution",
            #"{{5.}} Constrained Choice"
        ]
        
        topic_list = [Tex(t).scale(1.5).set_color_by_tex_to_color_map({
                "1": BLUE,
                "2": BLUE,
                "3": BLUE,
                "4": BLUE,
                "5": BLUE,
            }) for t in topic_list]
        self.play(FadeIn(title))
        self.play(AddTextWordByWord(subtitle, run_time=2), rate_func=linear)
        self.wait()

        for i in range(len(topic_list)):
            self.play(AddTextWordByWord(topic_list[i].to_edge((i*1.5+7)*UP+LEFT), run_time=2), rate_func=linear)
        self.wait(2)


class animation_1(Scene):
    """Animation 1 | Preferences

Introduce preferences as a ranking of alternatives."""

    def construct(self):
        
        definition = Tex("DEFINITION.").move_to(UP).set_color(YELLOW)
        pref_def_1 = Tex("{{Preferences}} are a ranking of different combinations,").set_color_by_tex_to_color_map({
                "Preferences": BLUE,
            }).next_to(definition, DOWN*2)
        pref_def_2 = Tex(" or bundles of alternatives/goods/services/options.").next_to(pref_def_1, DOWN)
        
        self.add(definition)
        self.play(AddTextWordByWord(pref_def_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(pref_def_2, run_time=4), rate_func=linear)
        
        def_group = VGroup(definition,pref_def_1,pref_def_2)
        framebox = SurroundingRectangle(def_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.play(FadeOut(def_group))

        assumption_1_a = Tex("1. If $ a \succsim b $,").move_to(UP*3)
        assumption_1_b = Tex("then $ a $ is weakly preferred to $ b $.").next_to(assumption_1_a, DOWN)
        assumption_2_a = Tex("2. If $ a \succ b $,").next_to(assumption_1_b, DOWN*4)
        assumption_2_b = Tex("then $ a $ is strictly preferred to $ b $.").next_to(assumption_2_a, DOWN)
        assumption_3_a = Tex("3. If $ a \sim b $,").next_to(assumption_2_b, DOWN*4)
        assumption_3_b = Tex("then $ a $ and $ b $ are equally ranked.").next_to(assumption_3_a, DOWN)
        
        self.play(AddTextWordByWord(assumption_1_a, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(assumption_1_b, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(VGroup(assumption_1_a,assumption_1_b), buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()
        
        self.play(AddTextWordByWord(assumption_2_a, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(assumption_2_b, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(VGroup(assumption_2_a,assumption_2_b), buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()
        
        self.play(AddTextWordByWord(assumption_3_a, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(assumption_3_b, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(VGroup(assumption_3_a,assumption_3_b), buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()


class animation_2(Scene):

    """Animation 2 | Primitives 

Introduce the primitives behind choices."""

    def construct(self):
        assumption_1_a = Tex("1. An individual has preferences determining how much").move_to(UP*3)
        assumption_1_b = Tex("pleasure they get from different goods and services.").next_to(assumption_1_a, DOWN)
        assumption_2 = Tex("2. Consumers face constraints on their choices.").next_to(assumption_1_b, DOWN*4)
        assumption_3_a = Tex("3. Consumers maximize their pleasure").next_to(assumption_2, DOWN*4)
        assumption_3_b = Tex("from consumption, subject to constraints.").next_to(assumption_3_a, DOWN)
        
        self.play(AddTextWordByWord(assumption_1_a, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(assumption_1_b, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(VGroup(assumption_1_a,assumption_1_b), buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()
        
        self.play(AddTextWordByWord(assumption_2, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(assumption_2, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()
        
        self.play(AddTextWordByWord(assumption_3_a, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(assumption_3_b, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(VGroup(assumption_3_a,assumption_3_b), buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.wait()


class animation_3(Scene):

    """Animation 3 | Indifference Curves

Introduce indifference curves as a way to capture preference rankings."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        self.add(axes, grid_labels)
        
        points = {'a':[13,9],'b':[11,7],'c':[5,20],'d':[5,7],'e':[10,10],'f':[13,18],
                  'g':[20,5]}
        dots = {}
        for point_l in points:
            point = points[point_l]
            x = axes.coords_to_point(point[0],point[1])
            dots[point_l] = [Dot(x, color=WHITE),Tex(point_l).next_to(x,RIGHT/2+UP/2)]
        for dot_l in dots:
            dot = dots[dot_l]
            self.bring_to_front(dot[0])
            self.play(FadeIn(dot[0]),FadeIn(dot[1]))
            
        self.wait()
        
        key = 'e'
        point = points[key]
        origin = axes.coords_to_point(0,0)
        p = axes.coords_to_point(point[0],point[1])
        corner = axes.coords_to_point(20,20)
        v1 = axes.coords_to_point(point[0],0)
        v2 = axes.coords_to_point(point[0],20)
        h1 = axes.coords_to_point(0,point[1])
        h2 = axes.coords_to_point(20,point[1])
        vline = DashedLine(v1, v2)
        hline = DashedLine(h1, h2)
        self.bring_to_back(vline,hline)
        self.play(Create(vline),Create(hline),
                  Transform(dots[key][0],dots[key][0].set_color(YELLOW)))
        
        lower = Polygon(origin,v1,p,h1, color=RED).set_fill(RED, opacity=0.5)
        upper = Polygon(p,v2,corner,h2, color=GREEN).set_fill(GREEN, opacity=0.5)
        self.bring_to_back(upper,lower)
        self.play(FadeIn(upper),FadeIn(lower))

        self.wait()
        
        ubar = 10
        def cobb_douglas(x):
            return (x**(-1/2) * ubar)**2
        I_curve = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        #self.bring_to_front(dots['c'][0],dots['g'][0])
        self.bring_to_back(I_curve)
        self.play(Create(I_curve),
                  Transform(dots['c'][0],dots['c'][0].set_color(YELLOW)),
                  Transform(dots['g'][0],dots['g'][0].set_color(YELLOW)))
        self.wait()
        self.play(Transform(dots['f'][0],dots['f'][0].set_color(GREEN)),
                  Transform(dots['a'][0],dots['a'][0].set_color(GREEN)))
        self.wait()
        self.play(Transform(dots['b'][0],dots['b'][0].set_color(RED)),
                  Transform(dots['d'][0],dots['d'][0].set_color(RED)))
        self.wait()
        self.play(FadeOut(upper),FadeOut(lower),FadeOut(vline),FadeOut(hline))
        for key in dots:
            self.play(FadeOut(dots[key][1], run_time=0.01))
        self.wait()
        
        def cobb_douglas_ubar(x,y):
            return x**(1/2) * y**(1/2)
        for ubar in sorted(set([cobb_douglas_ubar(points[key][0],points[key][1]) for key in points])):
            def cobb_douglas(x):
                return (x**(-1/2) * ubar)**2
            I_curve_new = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
            self.play(Transform(I_curve,I_curve_new))
            for key in points:
                if cobb_douglas_ubar(points[key][0],points[key][1]) > ubar:
                    self.play(Transform(dots[key][0],dots[key][0].set_color(GREEN), run_time=0.01))
                if cobb_douglas_ubar(points[key][0],points[key][1]) == ubar:
                    self.play(Transform(dots[key][0],dots[key][0].set_color(YELLOW), run_time=0.01))
                if cobb_douglas_ubar(points[key][0],points[key][1]) < ubar:
                    self.play(Transform(dots[key][0],dots[key][0].set_color(RED), run_time=0.01))
            self.wait()


class animation_4(Scene):

    """Animation 4 | Indifference Curve Properties 1 & 2

Introduce properties 1 and 2 of indifference curves: 1) further from the origin is better, 2) every bundle lies on an indifference curve."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        
        definition = Tex("DEFINITION.").move_to(UP).set_color(YELLOW)
        i_curve_def_1 = Tex("An {{Indifference Curve}} shows the set of bundles of two goods").set_color_by_tex_to_color_map({
                "Indifference Curve": BLUE,
            }).next_to(definition, DOWN*2)
        i_curve_def_2 = Tex("between which a consumer is indifferent.").next_to(i_curve_def_1, DOWN)
        
        self.add(definition)
        self.play(AddTextWordByWord(i_curve_def_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(i_curve_def_2, run_time=4), rate_func=linear)
        
        def_group = VGroup(definition,i_curve_def_1,i_curve_def_2)
        framebox = SurroundingRectangle(def_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.play(FadeOut(def_group))
        
        self.wait()
        
        self.add(axes, grid_labels)
        
        N = 50
        x = np.random.randint(100,2000,size=N)/100
        y = np.random.randint(100,2000,size=N)/100
        
        points = [[x[i],y[i]] for i in range(N)]
        dots = []
        for point in points:
            x = axes.coords_to_point(point[0],point[1])
            dots.append(Dot(x, color=WHITE))
        for dot in dots:
            self.bring_to_front(dot)
            self.play(FadeIn(dot, run_time=0))
        
        ubar = 10
        def cobb_douglas(x):
            return (x**(-1/2) * ubar)**2
        I_curve = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        
            
        def cobb_douglas_ubar(x,y):
            return x**(1/2) * y**(1/2)
        for ubar in list(set([cobb_douglas_ubar(point[0],point[1]) for point in points]))[::10]:
            def cobb_douglas(x):
                return (x**(-1/2) * ubar)**2
            I_curve_new = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
            self.play(Transform(I_curve,I_curve_new))
            for i in range(N):
                if cobb_douglas_ubar(points[i][0],points[i][1]) > ubar:
                    self.play(Transform(dots[i],dots[i].set_color(GREEN), run_time=0))
                if cobb_douglas_ubar(points[i][0],points[i][1]) == ubar:
                    self.play(Transform(dots[i],dots[i].set_color(YELLOW), run_time=0))
                if cobb_douglas_ubar(points[i][0],points[i][1]) < ubar:
                    self.play(Transform(dots[i],dots[i].set_color(RED), run_time=0))
            self.wait()
            
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.5)
        self.play(FadeIn(blur_background))
        
        prop_1 = Tex("Property 1.").move_to(UP*3).set_color(YELLOW)
        prop_1_text = Tex("Bundles on I-Curves further from the origin are preferred.").next_to(prop_1, DOWN*2)
        self.play(FadeIn(prop_1))
        self.play(AddTextWordByWord(prop_1_text, run_time=4), rate_func=linear)
        
        prop_group = VGroup(prop_1,prop_1_text)
        framebox = SurroundingRectangle(prop_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        prop_2 = Tex("Property 2.").set_color(YELLOW).next_to(prop_1_text, DOWN*3)
        prop_2_text = Tex("Every bundle lies on an indifference curve.").next_to(prop_2, DOWN*2)
        self.play(FadeIn(prop_2))
        self.play(AddTextWordByWord(prop_2_text, run_time=4), rate_func=linear)
        
        prop_group = VGroup(prop_2,prop_2_text)
        framebox = SurroundingRectangle(prop_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)


class animation_5(Scene):
    """Animation 5 | Indifference Curve Property 3

Introduce property 3 of indifference curves: they cannot cross."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        def cobb_douglas(x):
            return 100/x
        I_curve = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        
        def cobb_douglas_ubar(x,y):
            return x**(1/2) * y**(1/2)

        a_x = 21/2 - 41**(1/2)/2
        a_y = 100/a_x
        points = {'a':[a_x,a_y],'b':[20,5],'c':[16,25/2]}
        dots = {}
        for point_l in points:
            point = points[point_l]
            x = axes.coords_to_point(point[0],point[1])
            dots[point_l] = [Dot(x, color=WHITE),Tex(point_l).next_to(x,RIGHT/2+UP/2)]
        for dot_l in dots:
            dot = dots[dot_l]
            self.bring_to_front(dot[0])
            self.play(FadeIn(dot[0]),FadeIn(dot[1]))
            self.wait()
        
        a_group = VGroup(dots['a'][0],dots['a'][1])
        b_group = VGroup(dots['b'][0],dots['b'][1])
        c_group = VGroup(dots['c'][0],dots['c'][1])
        self.play(Create(I_curve),
                  Transform(a_group,a_group.set_color(YELLOW)),
                  Transform(b_group,b_group.set_color(YELLOW)),
                  Transform(c_group,c_group.set_color(GREEN)))
        framebox = SurroundingRectangle(c_group, buff = 0.3).set_color(GREEN)
        self.play(Create(framebox))
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox))
        self.wait()
        
        def cobb_douglas_alt(x):
            return x**(-1/2) * 10 + 10
        I_curve_alt = axes.get_graph(cobb_douglas_alt, color=BLUE, x_range=(1/2, 20))
        self.bring_to_back(I_curve_alt)
        self.play(Create(I_curve_alt),FadeOut(I_curve),FadeIn(DashedVMobject(I_curve)),
                  Transform(a_group,a_group.set_color(YELLOW)),
                  Transform(b_group,b_group.set_color(RED)),
                  Transform(c_group,c_group.set_color(YELLOW)))
        
        framebox = SurroundingRectangle(b_group, buff = 0.3).set_color(RED)
        self.play(Create(framebox))
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox))
        self.wait()
        self.wait()
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.5)
        self.play(FadeIn(blur_background))
        
        prop_3 = Tex("Property 3.").move_to(UP).set_color(YELLOW)
        prop_3_text = Tex("Indifference curves cannot cross.").next_to(prop_3, DOWN*2)
        self.play(FadeIn(prop_3))
        self.play(AddTextWordByWord(prop_3_text, run_time=4), rate_func=linear)
        
        prop_group = VGroup(prop_3,prop_3_text)
        framebox = SurroundingRectangle(prop_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        self.play(FadeOut(blur_background),FadeOut(prop_3),FadeOut(prop_3_text),
                  FadeOut(I_curve_alt),FadeIn(I_curve),FadeOut(DashedVMobject(I_curve)),
                  FadeOut(dots['a'][0]),FadeOut(dots['a'][1]),
                  FadeOut(dots['b'][0]),FadeOut(dots['b'][1]),
                  FadeOut(dots['c'][0]),FadeOut(dots['c'][1]))


class animation_6(Scene):        
    """Animation 6 | Indifference Curve Property 4

Introduce property 4 of indifference curves: they slope downward."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        def cobb_douglas(x):
            return 100/x
        I_curve = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        self.add(I_curve)
            
        pointer_value = ValueTracker(6)
        
        def move_the_dot():
            x = pointer_value.get_value()
            x_int = axes.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(BLUE).next_to(x_int,DOWN).set_value(x)
            y = cobb_douglas(x)
            y_int = axes.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(RED).next_to(y_int,LEFT).set_value(y)
            p = axes.coords_to_point(x,y)
            dot = Dot(p).set_color(YELLOW)
            vline = DashedLine(x_int,p).set_color(GREY)
            hline = DashedLine(y_int,p).set_color(GREY)
            return VGroup(dot,vline,hline,x_label,y_label)
        
        moving_dot = always_redraw(move_the_dot)
        
        self.add(moving_dot)
        self.play(pointer_value.animate.set_value(17),run_time=3)
        self.play(pointer_value.animate.set_value(6),run_time=3)
        
        self.wait()
        self.play(FadeOut(moving_dot))

        def cobb_douglas(x):
            return x
        I_curve_new = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        self.play(Transform(I_curve,I_curve_new))
        #self.play(FadeIn(moving_dot))
        
        self.play(pointer_value.animate.set_value(17),run_time=3)
        self.play(pointer_value.animate.set_value(6),run_time=3)
        
        self.wait()
        self.play(FadeOut(moving_dot))

        def cobb_douglas(x):
            return 100/x
        I_curve_new = axes.get_graph(cobb_douglas, color=PINK, x_range=(1/2, 20))
        self.play(Transform(I_curve,I_curve_new))
        #self.play(FadeIn(moving_dot))
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.5)
        self.play(FadeIn(blur_background))
        
        prop_4 = Tex("Property 4.").move_to(UP).set_color(YELLOW)
        prop_4_text = Tex("Indifference curves slope downward.").next_to(prop_4, DOWN*2)
        self.play(FadeIn(prop_4))
        self.play(AddTextWordByWord(prop_4_text, run_time=4), rate_func=linear)
        
        prop_group = VGroup(prop_4,prop_4_text)
        framebox = SurroundingRectangle(prop_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        self.play(FadeOut(blur_background),FadeOut(prop_4),FadeOut(prop_4_text))


class animation_7(Scene):
    """Animation 7 | Indifference Curve Property 5

Introduce property 5 of indifference curves: they cannot be thick."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        step = 0
        def cobb_douglas_thick(x):
            return 100/x + step
        I_curve = axes.get_graph(cobb_douglas_thick, color=PINK, x_range=(5, 20))
        self.add(I_curve)
        
        I_curve_thick = []
        for step in np.arange(0,2,0.1):
            I_curve_thick.append(axes.get_graph(cobb_douglas_thick, color=PINK, x_range=(5, 20)))
            self.play(FadeIn(I_curve_thick[-1]),run_time=0.01)
            
        def cobb_douglas(x):
            return 100/x
        x = axes.coords_to_point(15,cobb_douglas(15))
        dot_x = Dot(x, color=YELLOW)
        self.play(FadeIn(dot_x))
        
        y = axes.coords_to_point(15.5,cobb_douglas(15.5)+1.5)
        dot_y = Dot(x, color=GREEN)
        self.play(dot_y.animate.move_to(y))
        
        self.wait(2)
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.5)
        self.play(FadeIn(blur_background))
        
        prop_5 = Tex("Property 5.").move_to(UP).set_color(YELLOW)
        prop_5_text = Tex("Indifference curves cannot be thick.").next_to(prop_5, DOWN*2)
        self.play(FadeIn(prop_5))
        self.play(AddTextWordByWord(prop_5_text, run_time=4), rate_func=linear)
        
        prop_group = VGroup(prop_5,prop_5_text)
        framebox = SurroundingRectangle(prop_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        self.wait()


class animation_8(Scene):
    """Animation 8 | Utility

Introduce utility as a way to capture preferences."""

    def construct(self):
        
        definition = Tex("DEFINITION.").move_to(UP).set_color(YELLOW)
        i_curve_def_1 = Tex("A {{Utility Function}} is a function that if").set_color_by_tex_to_color_map({
                "Utility Function": BLUE,
            }).next_to(definition, DOWN*2)
        i_curve_def_2 = Tex("$ a \succ b, $ then $ u(a) > u(b) $.").next_to(i_curve_def_1, DOWN)
        
        self.add(definition)
        self.play(AddTextWordByWord(i_curve_def_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(i_curve_def_2, run_time=4), rate_func=linear)
        
        def_group = VGroup(definition,i_curve_def_1,i_curve_def_2)
        framebox = SurroundingRectangle(def_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.play(FadeOut(def_group))
        
        self.wait()


class animation_9(Scene):
    """Animation 9 | Marginal Rate of Substitution

Introduce MRS."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        alpha = 1/2
        ubar = 8
        def indifference_curve(a):
            return ubar**(1/(1-alpha))*a**(-alpha/(1-alpha))
        indifference = axes.get_graph(indifference_curve, color=PURPLE, x_range=(1, 20))
        indifference_lab = axes.get_graph_label(indifference, label = ubar)
        
        self.add(indifference,indifference_lab)
        self.play(FadeOut(indifference_lab))
        
        pointer_value = ValueTracker(3)
        
        def move_the_dot_line():
            x = pointer_value.get_value()
            x_int = axes.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=1).set_color(BLUE).next_to(x_int,DOWN).set_value(x)
            y = indifference_curve(x)
            y_int = axes.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=1).set_color(GREEN).next_to(y_int,LEFT).set_value(y)
            p = axes.coords_to_point(x,y)
            dot = Dot(p).set_color(YELLOW)
            vline = DashedLine(x_int,p).set_color(GREY)
            hline = DashedLine(y_int,p).set_color(GREY)
            
            def indifference_der(a):
                return (-alpha/(1-alpha))*ubar**(1/(1-alpha))*a**(-alpha/(1-alpha)-1)
            
            def derivative_func(k):
                return indifference_der(x)*k+(y-indifference_der(x)*x)
            derivative = axes.get_graph(derivative_func, color=YELLOW, x_range=(0, 20))
            d_label = axes.get_graph_label(derivative, label = "MRS")
            return VGroup(dot,vline,hline,x_label,y_label,derivative,d_label)
        
        moving_dot = always_redraw(move_the_dot_line)
        
        self.add(moving_dot)
        self.play(pointer_value.animate.set_value(17),run_time=2)
        self.play(pointer_value.animate.set_value(3),run_time=2)
        self.play(pointer_value.animate.set_value(10),run_time=2)
        self.wait()


class animantion_10(Scene):

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        alpha = 1/2
        ubar = 8
        def indifference_curve(a):
            return ubar**(1/(1-alpha))*a**(-alpha/(1-alpha))
        indifference = axes.get_graph(indifference_curve, color=PURPLE, x_range=(1, 20))
        self.add(indifference)
        
        pointer_value = ValueTracker(10)
        
        def move_the_dot_line():
            x = pointer_value.get_value()
            x_int = axes.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(BLUE).next_to(x_int,DOWN).set_value(x)
            y = indifference_curve(x)
            y_int = axes.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(GREEN).next_to(y_int,LEFT).set_value(y)
            p = axes.coords_to_point(x,y)
            dot = Dot(p).set_color(YELLOW)
            vline = DashedLine(x_int,p).set_color(GREY)
            hline = DashedLine(y_int,p).set_color(GREY)
            
            def indifference_der(a):
                return (-alpha/(1-alpha))*ubar**(1/(1-alpha))*a**(-alpha/(1-alpha)-1)
            
            def derivative_func(k):
                return indifference_der(x)*k+(y-indifference_der(x)*x)
            derivative = axes.get_graph(derivative_func, color=YELLOW, x_range=(0, 20))
            d_label = axes.get_graph_label(derivative, label = "MRS")
            return VGroup(dot,vline,hline,x_label,y_label,derivative,d_label)
        
        moving_dot = always_redraw(move_the_dot_line)
        
        self.add(moving_dot)
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.8)
        self.play(FadeIn(blur_background))
        
        mu = Tex("Definition.").move_to(UP*2).set_color(YELLOW)
        mu_text_1 = Tex("Given $ U = U(x,y) $, the marginal utility of a good, $x$,").next_to(mu, DOWN*2)
        mu_text_2 = Tex("is the extra utility the consumer gets from").next_to(mu_text_1, DOWN)
        mu_text_3 = Tex("a small increase in $x$.").next_to(mu_text_2, DOWN)
        equation = Tex("$ \dfrac{\partial U}{\partial X} = U_x $").next_to(mu_text_3, DOWN)
        
        self.play(FadeIn(mu))
        self.play(AddTextWordByWord(mu_text_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mu_text_2, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mu_text_3, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(equation, run_time=4), rate_func=linear)
        
        """
        mu_group = VGroup(mu,mu_text_1,mu_text_2,mu_text_3,equation)
        mu_subgroup = VGroup(mu,mu_text_1,mu_text_2,mu_text_3)
        framebox = SurroundingRectangle(mu_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        self.play(FadeOut(mu_subgroup),equation.animate.move_to(UP))
        
        equation_l = [
            MathTex("U(A,B)","=","\\bar{U}"),
            MathTex("U(A, {{H}} (A))","=","\\bar{U}"),
            MathTex("\\frac{\\partial U}{\\partial A} + \\frac{\\partial U}{\\partial B}\\frac{dH}{dA}","=","\\frac{\\partial \\bar{U}}{\\partial A}"),
            MathTex("\\frac{\\partial U}{\\partial A} + \\frac{\\partial U}{\\partial B}\\frac{dH}{dA} = 0"),
            MathTex("\\frac{dH}{dA} = -\\frac{\\frac{\\partial U}{\\partial B}}{\\frac{\\partial U}{\\partial A}}")
        ]
        self.play(Transform(equation,equation_l[0].move_to(UP*2)))
        self.play(Transform(equation,equation_l[1].move_to(UP*2)))
        self.wait()
        
        kw = {"path_arc": PI / 2}
        self.play(Transform(equation_l[1], equation_l[2].next_to(equation_l[1], DOWN), **kw))
        self.play(Transform(equation_l[2], equation_l[3].next_to(equation_l[2], DOWN), **kw))
        self.play(Transform(equation_l[3].copy(), equation_l[4].next_to(equation_l[3], DOWN), **kw))
        self.wait()
        """


class animation_(Scene):
    def construct(self):
        to_isolate = ["U", "{{A}}", "B", "="]
        base_equation = MathTex("B","=","{{ \\bar{U} }} ^{\\frac{1}{1-{{\\alpha}} }}","{{A}} ^{-\\frac{\\alpha}{1-{{ {{\\alpha}} }}")
        base_equation.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": GREEN,
            })
        self.add(base_equation)

        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("Y")
        x_label = axes.get_x_axis_label("X")
        grid_labels = VGroup(x_label, y_label)
        
        self.add(axes, grid_labels)
        
        alpha = 1/2
        ubar = 10
        def indifference_curve(a):
            return ubar**(1/(1-alpha))*a**(-alpha/(1-alpha))
        indifference = axes.get_graph(indifference_curve, color=PURPLE, x_range=(1, 20))
        indifference_lab = axes.get_graph_label(indifference, label = "\\bar{U}")
        self.play(Create(indifference),base_equation.animate.move_to(UP*2+RIGHT*4))
        self.play(Create(indifference_lab))
        self.wait()
        
        u_exp = 1/(1-alpha)
        a_exp = -alpha/(1-alpha)
        equation = MathTex("B","=","{{ \\bar{U} }} ^{"+str(round(u_exp,1))+"}","{{A}} ^{ "+str(round(a_exp,1))+" }}")
        equation.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": GREEN,
            })
        self.play(Transform(base_equation,equation.move_to(base_equation)))
        self.wait()
        
        equation = MathTex("B","=","{{ "+str(ubar)+" }} ^{"+str(round(u_exp,1))+"}","{{A}} ^{ "+str(round(a_exp,1))+" }}")
        equation.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": GREEN,
            })
        indifference_lab_new = axes.get_graph_label(indifference, label = ubar)
        self.play(Transform(base_equation,equation.move_to(base_equation)),Transform(indifference_lab,indifference_lab_new))
        self.wait()
        
        pairs = [[1/4,10], [3/4,10], [1/2,10], [1/2,2], [1/2,5], [1/2,8]]
        for pair in pairs:
            alpha,ubar = pair[0],pair[1]
            u_exp, a_exp = 1/(1-alpha), -alpha/(1-alpha)

            def indifference_curve(a):
                return ubar**(1/(1-alpha))*a**(-alpha/(1-alpha))
            indifference_new = axes.get_graph(indifference_curve, color=PURPLE, x_range=(1, 20))
            indifference_lab_new = axes.get_graph_label(indifference_new, label = ubar)

            equation = MathTex("B","=","{{ "+str(ubar)+" }} ^{"+str(round(u_exp,1))+"}","{{A}} ^{ "+str(round(a_exp,1))+" }}")
            equation.set_color_by_tex_to_color_map({
                    "A": BLUE,
                    "B": GREEN,
                })
            self.play(Transform(indifference,indifference_new),
                      Transform(indifference_lab,indifference_lab_new),
                      Transform(base_equation,equation.move_to(base_equation)))
            self.wait()
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.5)
        self.play(FadeIn(blur_background))
        
        mrs = Tex("Definition.").move_to(UP).set_color(YELLOW)
        mrs_text_1 = Tex("A consumer’s marginal rate of substitution (MRS) is").next_to(mrs, DOWN*2)
        mrs_text_2 = Tex("the maximum number of units of the y-axis good").next_to(mrs_text_1, DOWN)
        mrs_text_3 = Tex("the consumer is willing to give up").next_to(mrs_text_2, DOWN)
        mrs_text_4 = Tex("to get one more unit of the x-axis good.").next_to(mrs_text_3, DOWN)
        self.play(FadeIn(mrs))
        self.play(AddTextWordByWord(mrs_text_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mrs_text_2, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mrs_text_3, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mrs_text_4, run_time=4), rate_func=linear)
        
        mrs_group = VGroup(mrs,mrs_text_1,mrs_text_2,mrs_text_3,mrs_text_4)
        framebox = SurroundingRectangle(mrs_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        
        self.play(FadeOut(mrs_group),FadeOut(blur_background))


class animation_11(Scene):
    """Animation 1 | Budget Constraint

Introduce the budget constraint to define the choice set."""

    def construct(self):
        axes = Axes(
            x_range=[0, 20, 10],
            x_length = 9,
            #axis_config={"color": BLACK},
            x_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":ORANGE,
                },
            },
            y_range=[0, 20, 10],
            y_axis_config={
                "numbers_to_include": [],#np.arange(0, 20, 10),
                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),
                "decimal_number_config": {
                    "num_decimal_places":0,
                    #"color":GREEN,
                }
            },
            tips=False,
        )
        # Labels for the x-axis and y-axis.
        y_label = axes.get_y_axis_label("B")
        x_label = axes.get_x_axis_label("A")
        grid_labels = VGroup(x_label, y_label)
        
        bc = Tex("Definition.").move_to(UP*2).set_color(YELLOW)
        bc_text_1 = Tex("Assuming that individuals can’t borrow or save,").next_to(bc, DOWN*2)
        bc_text_2 = Tex("then the budget constraint is implicitly defined").next_to(bc_text_1, DOWN)
        bc_text_3 = Tex("by the sum of expenditures.").next_to(bc_text_2, DOWN)
        equation = Tex("$ Y = p_A q_A + p_B q_B $").next_to(bc_text_3, DOWN)
        bc_group = VGroup(bc,bc_text_1,bc_text_2,bc_text_3,equation)
        bc_subgroup = VGroup(bc,bc_text_1,bc_text_2,bc_text_3)
        
        self.play(FadeIn(bc))
        self.play(AddTextWordByWord(bc_text_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(bc_text_2, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(bc_text_3, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(equation, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(bc_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)

        budget_equation = MathTex("p_A q_A","+","p_B q_B","=","Y").move_to(UP*2+RIGHT*2)
        self.play(FadeOut(bc_subgroup))
        self.play(Transform(equation,budget_equation))

        self.add(axes, grid_labels)
        p_a = 1
        p_b = 1
        Y = 15
        def budget_curve(a):
            return (Y-p_a*a)/p_b
        
        budget = axes.get_graph(budget_curve, color=PURPLE, x_range=(0, Y/p_b))
        
        self.play(Create(budget),FadeIn(budget_equation))
        
        pointer_value = ValueTracker(10)
        
        def move_the_dot():
            x = pointer_value.get_value()
            x_int = axes.coords_to_point(x,0)
            x_label = DecimalNumber(num_decimal_places=2).set_color(BLUE).next_to(x_int,DOWN).set_value(x)
            y = budget_curve(x)
            y_int = axes.coords_to_point(0,y)
            y_label = DecimalNumber(num_decimal_places=2).set_color(GREEN).next_to(y_int,LEFT).set_value(y)
            p = axes.coords_to_point(x,y)
            dot = Dot(p).set_color(YELLOW)
            vline = DashedLine(x_int,p).set_color(GREY)
            hline = DashedLine(y_int,p).set_color(GREY)
            return VGroup(dot,vline,hline,x_label,y_label)
        
        moving_dot = always_redraw(move_the_dot)
        
        self.add(moving_dot)
        self.play(pointer_value.animate.set_value(3),run_time=2)
        self.play(pointer_value.animate.set_value(11),run_time=2)
        
        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.8)
        self.play(FadeIn(blur_background))
        
        mrt = Tex("Definition.").move_to(UP*2).set_color(YELLOW)
        mrt_text_1 = Tex("Marginal Rate of Transformation ($ MRT $)").next_to(mrt, DOWN*2)
        mrt_text_2 = Tex(" is the slope of the budget line.").next_to(mrt_text_1, DOWN)
        equation = Tex("$ MRT = -\\frac{p_A}{p_B} $").next_to(mrt_text_2, DOWN)
        mrt_group = VGroup(mrt,mrt_text_1,mrt_text_2,equation)
        mrt_subgroup = VGroup(mrt,mrt_text_1,mrt_text_2)
        
        self.play(FadeIn(mrt))
        self.play(AddTextWordByWord(mrt_text_1, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(mrt_text_2, run_time=4), rate_func=linear)
        self.play(AddTextWordByWord(equation, run_time=4), rate_func=linear)
        
        framebox = SurroundingRectangle(mrt_group, buff = 0.3).set_color(BLUE)
        self.play(Create(framebox),run_time=3)
        framebox.flip(RIGHT)
        self.play(Uncreate(framebox),run_time=3)
        self.play(FadeOut(blur_background),FadeOut(mrt_group))
        
        self.play(pointer_value.animate.set_value(2),run_time=2)
        self.play(pointer_value.animate.set_value(14),run_time=2)

