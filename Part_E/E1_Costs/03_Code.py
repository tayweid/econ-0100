# maniml 03_Code.py -ql -v ERROR animation_0

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

""" Paths """
# Configuration
""" Colors """
CUSTOM_BLACK = '#1f1f1f'
CUSTOM_GREY = '#696969'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY
""" Frames """
PIXEL_HEIGHT = 1080
FPS = 10
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT*2
config.frame_rate = FPS

# Helper Functions and Classes

    def productionFunction(self):
        self.graph_origin = 2*DOWN + 6*LEFT
        self.setup_axes(animate=True)
        self.F = self.get_graph(lambda L : self.func(L,0.5), x_min=0, x_max=100)
        self.play(ShowCreation(self.F), run_time=2)
        
        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,1), x_min=0, x_max=100, color=self.func_color)), run_time=2)
        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,1.3), x_min=0, x_max=100, color=self.func_color)), run_time=2)
        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,0.4), x_min=0, x_max=100, color=self.func_color)), run_time=2)
        
    def totalCosts(self):
        self.graph_origin = 2*DOWN + RIGHT
        self.y_axis_label = "$TC$"
        self.x_axis_label = "$Q$"
        self.setup_axes(animate=True)
        self.y_axis_label = ""
        self.x_axis_label = ""
        
        exp = 0.4
        MC = self.get_graph(lambda q : self.MC(q,exp), color=self.supply_color, x_min=0, x_max=0)
        fc = Dot(self.coords_to_point(0,self.MC(0,exp)))
        fcLabel = Tex(str(int(self.MC(0,exp)*10))).scale(0.7)
        fcLabel.move_to(self.coords_to_point(-1,self.MC(0,exp)),RIGHT)
        self.play(FadeIn(MC),
                  FadeIn(fc),
                  FadeIn(fcLabel))
        
        a = self.coords_to_point(-15, 0)
        b = self.coords_to_point(-15, 10)
        fcLine = Line(a,b, color=self.axes_color)
        fcD = Tex("FC").scale(0.7)
        fcD.next_to(fcLine, LEFT)
        self.play(ShowCreation(fcLine),FadeIn(fcD))
        
        a = self.coords_to_point(-15, 10)
        b = self.coords_to_point(-15, 10)
        self.vcLine = Line(a,b, color=self.avc_color)
        self.vcD = Tex("VC").scale(0.7)
        self.vcD.next_to(self.vcLine, LEFT)
        
        for l in np.arange(20,100,20):
            p = self.func(l,0.4)
            mc = self.MC(p,0.4)
            
            self.graph_origin = 2*DOWN + 6*LEFT
            self.setup_axes()
            a = self.coords_to_point(l,0)
            b = self.coords_to_point(l,p)
            c = self.coords_to_point(0,p)
            pointF = Dot(b)
            vLine = DashedVMobject(Line(a,b, color=self.axes_color))
            hLine = DashedVMobject(Line(b,c, color=self.axes_color))
            lLabel = Tex(str(int(l))).scale(0.7)
            lLabel.move_to(a, UP)
            qLabel = Tex(str(int(p))).scale(0.7)
            qLabel.move_to(c,RIGHT)
            
            self.play(ShowCreation(vLine),FadeIn(lLabel))
            self.play(FadeIn(pointF))
            self.play(ShowCreation(hLine),FadeIn(qLabel))
            
            self.graph_origin = 2*DOWN + RIGHT
            self.setup_axes()
            pointMC = Dot(self.coords_to_point(p,mc))
            MC0 = self.get_graph(lambda q : self.MC(q,exp), color=self.supply_color, x_min=0, x_max=p)

            a = self.coords_to_point(p,0)
            b = self.coords_to_point(p,mc)
            c = self.coords_to_point(0,mc)
            pointF = Dot(b)
            vLine = DashedVMobject(Line(a,b, color=self.axes_color))
            hLine = DashedVMobject(Line(b,c, color=self.axes_color))
            lLabel = Tex(str(int(p))).scale(0.7)
            lLabel.move_to(a, UP)
            qLabel = Tex(str(int(mc)*10)).scale(0.7)
            qLabel.move_to(c,RIGHT)
            
            a = self.coords_to_point(-15, 10)
            b = self.coords_to_point(-15, mc)
            vcLine = Line(a,b, color=self.avc_color)
            vcD = Tex("VC").scale(0.7)
            vcD.next_to(vcLine, LEFT)
            
            self.play(ShowCreation(vLine),FadeIn(lLabel))
            self.play(FadeIn(pointMC),Transform(MC,MC0))
            self.play(ShowCreation(hLine),FadeIn(qLabel))
            self.play(Transform(self.vcLine,vcLine),Transform(self.vcD,vcD))


class CostsB(GraphScene):
    def marginalCost(self):
        # TC
        self.remove(self.axes)
        self.TCF = lambda q : q**2/100 + 10
        self.TC = self.get_graph(lambda x : self.TCF(x), x_min=5, x_max=110)
        a = self.coords_to_point(135, 100)
        b = self.coords_to_point(135, 85)
        self.TCL = Line(a,b)
        self.TCD = Tex("TC")
        self.TCD.next_to(self.TCL)
    
        self.play(ShowCreation(self.TC), run_time=2)
        self.play(FadeIn(self.TCL),FadeIn(self.TCD))
        
        
        # MC
        self.MCF = lambda q : 2*q/10
        
        p = self.TCF(10)
        dx = self.MCF(10)
        a = self.coords_to_point(10-5, p-5*dx/10)
        b = self.coords_to_point(10-5, p+5*dx/10)
        c = self.coords_to_point(10+5, p+5*dx/10)
        self.pointL = Dot(a)
        self.pointU = Dot(c)
        self.tangent = Line(a,c)
        self.lineUp = DashedVMobject(Line(a,b))
        self.lineOver = DashedVMobject(Line(b,c))
        self.MC = self.get_graph(lambda x : self.MCF(x), x_min=5, x_max=10)
        self.play(FadeIn(self.pointL), FadeIn(self.pointU), FadeIn(self.tangent), FadeIn(self.MC), FadeIn(self.lineUp), FadeIn(self.lineOver))
        
        a = self.coords_to_point(135, 80)
        b = self.coords_to_point(135, 65)
        self.MCL = Line(a,b)
        self.MCD = Tex("MC")
        self.MCD.next_to(self.MCL)
        self.play(FadeIn(self.MCL),FadeIn(self.MCD))
        
        self.rise = Tex("Rise").scale(0.7)
        self.rise.add_updater(lambda d: d.next_to(self.lineUp, LEFT))
        self.add(self.rise)
        
        for q in np.arange(10,110,10):
            MC = self.get_graph(lambda x : self.MCF(x), x_min=5, x_max=q)
            
            p = self.TCF(q)
            dx = self.MCF(q)
            a = self.coords_to_point(q-5, p-5*dx/10)
            b = self.coords_to_point(q-5, p+5*dx/10)
            c = self.coords_to_point(q+5, p+5*dx/10)
            pointL = Dot(a)
            pointU = Dot(c)
            tangent = Line(a,c)
            lineUp = DashedVMobject(Line(a,b))
            lineOver = DashedVMobject(Line(b,c))
            self.play(Transform(self.MC,MC), Transform(self.tangent,tangent), Transform(self.pointL,pointL), Transform(self.pointU,pointU), 
                      Transform(self.lineUp,lineUp), Transform(self.lineOver,lineOver))
            
    def costsEquations(self):
        self.play(FadeOut(self.TC),
                  FadeOut(self.pointL), FadeOut(self.pointU), FadeOut(self.tangent), 
                  FadeOut(self.MC), FadeOut(self.lineUp), FadeOut(self.lineOver), 
                  FadeOut(self.MC), FadeOut(self.rise),
                  FadeOut(self.tangent), FadeOut(self.pointL), 
                  FadeOut(self.pointU), FadeOut(self.lineUp), FadeOut(self.lineOver),
                  )
        
        a = self.coords_to_point(70, 100)
        b = self.coords_to_point(70, 85)
        TCL = Line(a,b)
        TCD = Tex("TC")
        TCD.next_to(TCL)
        
        self.play(Transform(self.TCL,TCL), Transform(self.TCD,TCD))
        
        TCE = Tex("= VC + FC")
        TCE.next_to(TCD)
        
        self.play(FadeIn(TCE))
        #self.wait(3)
        #self.play(FadeOut(TCE),FadeOut(self.TCL),FadeOut(self.TCD))
        a = self.coords_to_point(70, 100)
        b = self.coords_to_point(70, 85)
        self.ATCL = Line(a,b)
        self.ATCD = Tex("ATC")
        self.ATCD.next_to(TCL)
        self.ATCE = Tex("= AVC + AFC")
        self.ATCE.next_to(self.ATCD)
        self.play(ReplacementTransform(self.TCL,self.ATCL),ReplacementTransform(self.TCD,self.ATCD),ReplacementTransform(TCE,self.ATCE))
        
        a = self.coords_to_point(70, 80)
        b = self.coords_to_point(70, 65)
        MCL = Line(a,b)
        MCD = Tex("MC")
        MCD.next_to(MCL)
        
        self.play(Transform(self.MCL,MCL), Transform(self.MCD,MCD))
        
        self.MCE = Tex("$$ = \\frac{\\Delta TC}{\\Delta Q} $$")
        self.MCE.next_to(MCD)
        
        self.play(FadeIn(self.MCE))
        
    def costs(self):
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), x_min=10, x_max=100)
        # AVC
        self.AVCF = lambda q : q/2
        self.AVC = self.get_graph(lambda x : self.AVCF(x), x_min=1, x_max=100)
        
        # MC
        a = self.coords_to_point(135, 80)
        b = self.coords_to_point(135, 65)
        MCL = Line(a,b)
        MCD = Tex("MC")
        MCD.next_to(MCL)
        self.play(Transform(self.MCL,MCL),Transform(self.MCD,MCD),FadeOut(self.MCE))
        
        # ATC
        a = self.coords_to_point(135, 60)
        b = self.coords_to_point(135, 45)
        ATCL = Line(a,b)
        ATCD = Tex("ATC")
        ATCD.next_to(ATCL)
        self.play(Transform(self.ATCL,ATCL),Transform(self.ATCD,ATCD))
        
        # AVC
        a = self.coords_to_point(135, 40)
        b = self.coords_to_point(135, 25)
        self.AVCL = Line(a,b)
        self.AVCD = Tex("AVC")
        self.AVCD.next_to(self.AVCL)
        self.play(ReplacementTransform(self.ATCE,self.AVCL),FadeIn(self.AVCD))
        
        # MC
        self.play(ShowCreation(self.MC), run_time=2)
        self.play(ShowCreation(self.ATC), run_time=2)
        self.play(ShowCreation(self.AVC), run_time=2)
        
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))
        self.play(FadeIn(self.minatc))
        
        
    def playWithCosts(self):
        
        self.play(ReplacementTransform(self.AVC,self.ATC), ReplacementTransform(self.AVCL,self.ATCL), ReplacementTransform(self.AVCD,self.ATCD))
        self.wait(3)
    
    def outro_sequence(self):
        self.play(FadeOut(self.axes),FadeOut(self.minatc),FadeOut(self.MC),FadeOut(self.ATC),
                  FadeOut(self.ATCL),FadeOut(self.ATCD),FadeOut(self.MCL),FadeOut(self.MCD),
                  FadeOut(self.MCL), FadeOut(self.MCD),FadeOut(self.ATCL),
                  FadeOut(self.ATCD))
        
        result = Tex("In the long run all costs are variable.").scale(1.5)
        self.play(FadeIn(result))
        self.wait(4)
        self.play(FadeOut(result))
        result = Tex("MC = MR").scale(1.5)
        self.play(FadeIn(result))


class animation_0(Scene):

    """Animation 0 | Intro

This animation introduces the video sequence."""

    def construct(self):
        self.outline()
        
    def outline(self):
        title = Tex('Part D').scale(4)
        center_bar = Tex('$|$').set_color(GREY).to_edge(UP, buff=1).scale(2)
        subtitle = Tex('Sellers').scale(2).next_to(center_bar, RIGHT).set_color(YELLOW)
        self.play(FadeIn(title))

        self.play(title.animate.scale(0.6).next_to(center_bar, LEFT), run_time=1/2)
        self.play(FadeIn(center_bar), run_time=1/4)
        self.play(FadeIn(subtitle))
        
        episode_list = [
            'Episode D1 \\\\ Costs and Production',
            'Episode D2 \\\\ Marginal Revenue',
            'Episode D3 \\\\ Monopolistic Competition',
            'Episode D4 \\\\ Game Theory and Oligopoly'
        ]
        
        _int = 1/(len(episode_list) + 2)
        i = _int
        for episode in episode_list:
            
            ep = Tex(episode).scale(1).next_to(center_bar, DOWN)
            self.play(FadeIn(ep), run_time=1/2)
            up_ep = episode.split(' \\\\ ')[0]
            up_ep = Tex(up_ep).scale(0.5).set_color(YELLOW).move_to(LEFT*10*(1-i-_int/2) + RIGHT*10*(i+_int/2) + DOWN)
            self.play(Transform(ep, up_ep), run_time=1/2)
            
            i += _int
        
        self.wait()
        # next I want a circling box above each episode
        # and I'll add in the video inside the box in post


class animation_1(MovingCameraScene):
    """Animation 1 | The Production Function Generates Costs

This animation uses the production function to generate total cost."""

    def construct(self):
        axes_f_group, axes_f = self.Make_Production_Function()
        axes_c_group, axes_c = self.Add_Costs(axes_f_group)
        self.Create_TC_From_F(axes_f, axes_c)
        axes_ac_group, axes_ac, avc = self.Add_Average_Costs(axes_f_group, axes_c_group)
        self.Results(axes_c_group, axes_ac_group, axes_ac, avc)
        
    def Make_Production_Function(self):
        axes_f = Axes(
            x_range=[0, 100, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 100, 20),
            },

            y_range=[0, 10],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },
            tips=False,
        )
        
        axes_f_labels = axes_f.get_axis_labels('L','Q')
        F = axes_f.get_graph(lambda L: Production_Function(L), color=BLUE)
        F_label = axes_f.get_graph_label(F, label="F(L)=L^{1/2}")
        F_group = VGroup(axes_f, axes_f_labels, F, F_label).move_to(0)
        axes_f_title = Text('Production Function').next_to(F_group,UP, buff=1/2)
        axes_f_group = VGroup(axes_f, axes_f_labels, F, F_label, axes_f_title).scale(0.7).move_to(0)
        
        self.play(FadeIn(axes_f_group))
        return axes_f_group, axes_f
    
    def Trace_F(axes_f_group):
        """ Move a point along F """
        
        # add a point
        # move it out and back along F
        # fade it out
        
        pass
        
    def Add_Costs(self, axes_f_group):
        
        axes_c = Axes(
            x_range=[0, 10, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },

            y_range=[0, 280],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 320, 40),
            },
            tips=False,
        )
        
        axes_c_labels = axes_c.get_axis_labels('Q','')
        vc = axes_c.get_graph(lambda Q: VC(Q), color=ORANGE)
        VC_label = axes_c.get_graph_label(vc, label="VC=w\cdot L")
        tc = axes_c.get_graph(lambda Q: TC(Q), color=RED)
        TC_label = axes_c.get_graph_label(tc, label="TC")
        Cost_group = VGroup(axes_c, axes_c_labels, vc, VC_label, tc, TC_label).move_to(0)
        axes_c_title = Text('TC = FC + VC').next_to(Cost_group,UP, buff=1/2)
        axes_c_group = VGroup(axes_c, axes_c_labels, vc, VC_label, tc, TC_label, axes_c_title).scale(0.7).next_to(axes_f_group, RIGHT, buff=1)
        
        self.play(FadeIn(axes_c_group), self.camera.frame.animate.move_to(VGroup(axes_f_group, axes_c_group)))
        return axes_c_group, axes_c
    
    def Create_TC_From_F(self, axes_f, axes_c):
        """ Use F to create TC """
        
        a = axes_c.coords_to_point(-0.1, 0)
        b = axes_c.coords_to_point(-0.1, FC(0))
        FCLine = Line(a,b, color=GREEN)
        FCDesc = Tex("FC", color=GREEN).scale(0.7)
        FCDesc.next_to(FCLine, RIGHT)
        
        self.play(FadeIn(FCLine), FadeIn(FCDesc))
        
        LIST = []
        q_last = 0
        for q in np.arange(2,12,2):
        
            a = axes_f.coords_to_point(-1, q_last+0.1)
            b = axes_f.coords_to_point(-1, q-0.1)

            VLine = Line(a,b, color=PINK)
            VLine_Copy = Line(a,b, color=PINK)

            c = axes_f.coords_to_point(Inv_F(q_last)+1, -0.1)
            d = axes_f.coords_to_point(Inv_F(q)-1, -0.1)
            
            HLine = Line(c,d, color=PINK)
            LIST.append(HLine)
            HLine_Copy = Line(c,d, color=PINK)
            LIST.append(HLine_Copy)
            
            self.play(Create(VLine), Create(HLine), Create(VLine_Copy), Create(HLine_Copy))
            
            a = axes_c.coords_to_point(q_last+0.1, -1)
            b = axes_c.coords_to_point(q-0.1, -1)
            
            NewVLine = Line(a,b, color=PINK)
            LIST.append(NewVLine)
            
            c = axes_c.coords_to_point(-0.1, VC(q_last)+FC(0)+1)
            d = axes_c.coords_to_point(-0.1, VC(q)+FC(0)-1)
            
            NewHLine = Line(c,d, color=PINK)
            LIST.append(NewHLine)

            self.play(Transform(VLine, NewVLine), Transform(HLine, NewHLine))
            
            q_last = q
        self.play(FadeOut(*LIST))
            
        
    def Add_Average_Costs(self, axes_f_group, axes_c_group):
        # this really should be different, constructing ATC
        # start with a point at q=0, show the equation relating TC and ATC
        # then trace out ATC with an animating changing of the fraction
        # do something with mc?...
        
        axes_ac = Axes(
            x_range=[1, 10, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },

            y_range=[1, 80],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 90, 10),
            },
            tips=False,
        )
        
        axes_ac_labels = axes_ac.get_axis_labels('Q', '')
        avc = axes_ac.get_graph(lambda Q: AVC(Q), color=ORANGE)
        AVC_label = axes_ac.get_graph_label(avc, label="AVC")
        atc = axes_ac.get_graph(lambda Q: ATC(Q), color=RED)
        ATC_label = axes_ac.get_graph_label(atc, label="ATC")
        mc = axes_ac.get_graph(lambda Q: MC(Q), color=PURPLE)
        MC_label = axes_ac.get_graph_label(mc, label="MC")
        Cost_group = VGroup(axes_ac, axes_ac_labels, avc, AVC_label, atc, ATC_label, mc, MC_label).move_to(0)
        axes_ac_title = Text('ATC = AFC + AVC').next_to(Cost_group,UP, buff=1/2)
        axes_ac_group = VGroup(axes_ac, axes_ac_labels, avc, AVC_label, atc, ATC_label, mc, MC_label, axes_ac_title).scale(0.7).next_to(axes_c_group, buff=1)
        
        self.play(FadeIn(axes_ac_group), FadeOut(axes_f_group), self.camera.frame.animate.move_to(VGroup(axes_c_group, axes_ac_group)))
        return axes_ac_group, axes_ac, avc
    
    def Results(self, axes_c_group, axes_ac_group, axes_ac, avc):
        self.play(FadeOut(axes_c_group), self.camera.frame.animate.move_to(axes_ac_group))
        self.wait()
        
        LR_Desc = Text('In the long run, all costs are variable.').set_color(YELLOW).next_to(axes_ac_group, UP, buff=1/2)
        self.play(Create(LR_Desc))
        self.wait()
        
        LR_avc = axes_ac.get_graph(lambda Q: ATC(Q), color=ORANGE)
        self.play(Transform(avc, LR_avc))
        
        # in the long run all costs are variable
        # punchline for next time: MC = MR


class animation_2(Scene):
    
    def create_production_function(self, F, F_label):
        self.play(Create(F))
        self.play(Create(F_label), run_time = 1/4)
        
    def inputs_labor_capital(self, axes, axes_labels):
        self.play(Transform(axes_labels, axes.get_axis_labels('L,K','Q')))

        point = Dot(DOWN*2 + RIGHT*0.75)
        circle_it(self, 1/3, point)
        
        point = Dot(DOWN*2 + RIGHT*1.4)
        circle_it(self, 1/3, point)
        
        self.play(Transform(axes_labels, axes.get_axis_labels('L','Q')))

    def construct(self):
        axes = Axes(
            x_range=[0, 100, 10],
            x_length = 5,
            x_axis_config={
                "include_ticks":True,
            },

            y_range=[0, 100],
            y_length = 5,
            y_axis_config={
                "include_ticks":False
            },
            tips=True,
        ).shift(LEFT*2)
        axes_labels = axes.get_axis_labels('Inputs','Q')
        F = axes.get_graph(lambda x: production_func(x, 0.5), color=BLUE)
        F_label = axes.get_graph_label(F, label="F")
        
        hlines, vlines, marginal_inputs, marginal_outputs = [], [], [], []
        
        axes_c = Axes(
            x_range=[0, 100, 10],
            x_length = 5,
            x_axis_config={
                "include_ticks":True,
            },

            y_range=[0, 100],
            y_length = 5,
            y_axis_config={
                "include_ticks":False
            },
            tips=True,
        ).shift(RIGHT*3.5)
        axes_c_labels = axes_c.get_axis_labels('Q','P')
        
        """ Animation Sequence """
        self.add(axes, axes_labels)
        
        self.create_production_function(F, F_label)
        
        #self.inputs_labor_capital(axes, axes_labels)
        #self.input_to_output(axes, F, hlines, vlines, marginal_inputs, marginal_outputs)
        self.introduce_costs(axes, axes_labels, axes_c, axes_c_labels, F, F_label, hlines, vlines, marginal_inputs, marginal_outputs)
        
        
    def input_to_output(self, axes, F, hlines, vlines, marginal_inputs, marginal_outputs):
        base_value = ValueTracker(0)
        
        base_dot = Dot(axes.coords_to_point(0, production_func(0,0.5)), color=RED)
        base_dot.add_updater(lambda m:
                             m.move_to(
                                axes.c2p(base_value.get_value(), 
                                production_func(base_value.get_value(),0.5))
            ))
        
        output_arrow = Vector(RIGHT, max_stroke_width_to_length_ratio=0)
        output_arrow.add_updater(
            lambda m: m.next_to(
                        axes.c2p(0,production_func(base_value.get_value(),0.5)),
                        LEFT
            ))

        input_line = Line(
            axes.c2p(0.1, 0),
            axes.c2p(0, 0),
        ).set_color(GREY)
        input_line.add_updater(
            lambda m: m.put_start_and_end_on(
                          axes.c2p(base_value.get_value(), 0),
                          axes.c2p(base_value.get_value(), production_func(base_value.get_value(),0.5))
            ))
        
        input_arrow = Vector(UP, max_stroke_width_to_length_ratio=0)
        input_arrow.add_updater(
            lambda m: m.next_to(
                        axes.c2p(base_value.get_value(), 0),
                        DOWN
            ))
        
        output_line = Line(
            axes.c2p(0.1, 0),
            axes.c2p(0, 0),
        ).set_color(GREY)
        self.add(output_line)
        output_line.add_updater(
            lambda m: m.put_start_and_end_on(
                          axes.c2p(0, production_func(base_value.get_value(),0.5)),
                          axes.c2p(base_value.get_value(), production_func(base_value.get_value(),0.5))
            ))

        self.add(input_arrow, input_line, output_arrow, output_line, base_dot)
        
        self.play(base_value.animate.set_value(90))
        self.play(base_value.animate.set_value(5), run_time=2)
        
        input_values, last_value = [20, 40, 60], 0
        for input_value in input_values:
            self.play(base_value.animate.set_value(input_value))
            
            marginal_input = Line(
                axes.c2p(input_value-1, -1),
                axes.c2p(last_value+1, -1))
            marginal_inputs.append(marginal_input)
            self.play(FadeIn(marginal_input))
            
            marginal_return = Line(
                axes.c2p(-1, production_func(input_value,0.5)-1),
                axes.c2p(-1, production_func(last_value,0.5)+1))
            marginal_outputs.append(marginal_return)
            self.play(FadeIn(marginal_return))
            
            hline = axes.get_horizontal_line(axes.c2p(input_value, production_func(input_value,0.5)))
            hlines.append(hline)
            vline = axes.get_vertical_line(axes.c2p(input_value, production_func(input_value,0.5)))
            vlines.append(vline)
            self.add(hline,vline)
            
            last_value = input_value
        
    def introduce_costs(self, axes, axes_labels, axes_c, axes_c_labels, F, F_label, hlines, vlines, marginal_inputs, marginal_outputs):
        
        shift = 1.5
        self.play(
            axes.animate.shift(LEFT*shift),
            axes_labels.animate.shift(LEFT*shift),
            VGroup(F,F_label).animate.shift(LEFT*shift),
            VGroup(*hlines).animate.shift(LEFT*shift),
            VGroup(*vlines).animate.shift(LEFT*shift),
            VGroup(*marginal_inputs).animate.shift(LEFT*shift),
            VGroup(*marginal_outputs).animate.shift(LEFT*shift)
        )
        
        self.play(FadeIn(axes_c), FadeIn(axes_c_labels))
        
        
    
    def create_variable_cost_curve(self):
        pass


class animation_3(Scene):
    
    """Animation 3 | Cost Curves

This animation develops the main cost curves."""

    def construct(self):
        pass
    
    def some_accounting(self):
        pass
    
    def create_averages(self):
        pass
    
    def create_marginal_cost(self):
        pass
    
    def create_marginal_revenue(self):
        pass


class animation_4(Scene):
    
    """Animation 4 | Marginal Revenue

This animation introduces marginal revenue and the firm's optimal quantity choice."""

    def construct(self):
        pass
    
    def create_marginal_revenue(self):
        pass
