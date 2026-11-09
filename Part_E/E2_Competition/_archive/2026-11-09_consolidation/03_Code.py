# maniml 03_Code.py PerfectCompA #-low_quality

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

import warnings
# Configuration
config.background_color = 'white'

class PerfectCompA(GraphScene):
    CONFIG = metaConfigPerfectCompA

    """Tutorial 5.2 | Perfect Competition"""

    def construct(self):
        self.intro_sequence()
        self.wait(3)
        self.drawCosts()
        self.wait(3)
        self.drawMR(80)

    def intro_sequence(self):
        title = TextMobject("Week 5 Outline").scale(1.5)
        self.play(FadeIn(title))
        transform_title = TextMobject("Week 5 Outline").scale(1.2)
        tutorial_1 = TextMobject("Tutorial 5.1 | Production Costs")
        tutorial_1.to_edge(4*UP+LEFT).set_color(GREY)
        tutorial_2 = TextMobject("Tutorial 5.2 | Competitive Firms")
        tutorial_2.to_edge(6*UP+LEFT).set_color(GREY)
        tutorial_3 = TextMobject("Tutorial 5.3 | Monopoly")
        tutorial_3.to_edge(8*UP+LEFT).set_color(GREY)
        tutorial_4 = TextMobject("Tutorial 5.4 | Monopolistic Competition")
        tutorial_4.to_edge(10*UP+LEFT).set_color(GREY)
        tutorial_5 = TextMobject("Tutorial 5.5 | Oligopoly and Duopoly")
        tutorial_5.to_edge(12*UP+LEFT).set_color(GREY)
        self.play(Transform(title, transform_title.to_corner(UP)),
                  FadeIn(tutorial_1), FadeIn(tutorial_2), FadeIn(tutorial_3), FadeIn(tutorial_4), FadeIn(tutorial_5))
        self.wait(3)
        transform_title = TextMobject("Tutorial 5.2 | Perfect Competition").scale(1.2)
        self.play(Transform(tutorial_2, transform_title.to_corner(UP)),
                  FadeOut(title),FadeOut(tutorial_1),FadeOut(tutorial_3),FadeOut(tutorial_4),FadeOut(tutorial_5))
        
        self.graph_origin = 3.3*DOWN + 5*LEFT
        self.setup_axes()
        
        
    def drawCosts(self):        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        
        # MC
        a = self.coords_to_point(125, 80)
        b = self.coords_to_point(125, 65)
        self.MCL = Line(a,b, color=self.mc_color)
        self.MCD = TextMobject("MC").set_color(self.mc_color)
        self.MCD.next_to(self.MCL)
        self.play(ShowCreation(self.MC),ShowCreation(self.MCL),ShowCreation(self.MCD))
        
        # ATC
        a = self.coords_to_point(125, 60)
        b = self.coords_to_point(125, 45)
        self.ATCL = Line(a,b, color=self.atc_color)
        self.ATCD = TextMobject("ATC").set_color(self.atc_color)
        self.ATCD.next_to(self.ATCL)
        self.play(ShowCreation(self.ATC),ShowCreation(self.ATCL),ShowCreation(self.ATCD))
        
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))
        self.play(FadeIn(self.minatc))
    
    def drawMR(self,p):
        # MR
        self.MRF = lambda q : p
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=1, x_max=100)
        self.PD = TextMobject("P="+str(p)).set_color(self.mr_color).scale(0.8)
        self.PD.next_to(self.MR,LEFT)
        self.MBD = TextMobject("MPB").set_color(self.mr_color).scale(0.8)
        self.MBD.next_to(self.MR,RIGHT)

        # PRICE
        self.PF = lambda q : p
        self.P = self.get_graph(lambda x : self.PF(x), color=self.pq_color, x_min=10, x_max=100)
        
        # INITIAL QUANTITY
        q = 10
        atc = self.ATCF(q)
        mc = self.MCF(q)
        
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # LINES
        self.qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        self.qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        self.atcD = TextMobject("ATC ="+str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        self.mcLine = DashedVMobject(Line(mcP,mcPX, color=self.axes_color))
        self.mcD = TextMobject("MC ="+str(int(mc))).set_color(self.mc_color).scale(0.8)
        self.mcD.next_to(self.mcLine,LEFT)
        
        self.play(FadeIn(self.qLine),FadeIn(self.qD),
                  FadeIn(self.atcD),FadeIn(self.mcLine),FadeIn(self.mcD))
        
        # MR
        a = self.coords_to_point(125, 100)
        b = self.coords_to_point(125, 85)
        self.MRL = Line(a,b, color=self.mr_color)
        self.MRD = TextMobject("MR").set_color(self.mr_color)
        self.MRD.next_to(self.MRL)
        self.play(ShowCreation(self.PD),ShowCreation(self.MBD),ShowCreation(self.MR),ShowCreation(self.MRL),ShowCreation(self.MRD))
        
        # TR & TC
        a = self.coords_to_point(1, 1)
        b = self.coords_to_point(1, p)
        c = self.coords_to_point(q-1, p)
        d = self.coords_to_point(q-1, 1)
        self.TRArea = Polygon(a,b,c,d, fill_opacity = 0, fill_color = self.mr_color, color=self.mr_color)

        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, 0)
        self.TCArea = Polygon(a,b,c,d, fill_opacity = 0, fill_color = self.tc_color, color=self.tc_color)
        
        self.play(ShowCreation(self.TRArea),ShowCreation(self.TCArea))
        self.wait(3)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(20, 120)
        b = self.coords_to_point(20, 105)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("PROFIT = TR - TC").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)

        self.play(ShowCreation(self.PROFArea),FadeIn(self.PROFL),FadeIn(self.PROFD))
        self.wait(3)
        
        # REFRAME PROFIT
        PROFD = TextMobject("PROFIT = Q (P - ATC)").set_color(self.profit_color).scale(0.8)
        PROFD.next_to(self.PROFL,RIGHT)
        self.play(Transform(self.PROFD,PROFD))
        self.wait(3)
        
        PROFD = TextMobject("PROFIT =").set_color(self.profit_color).scale(0.8)
        PROFD.next_to(self.PROFL,RIGHT)
        
        PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(PROFD,RIGHT)
        self.play(Transform(self.PROFD,PROFD),ReplacementTransform(self.TCArea,self.PROFN),FadeOut(self.TRArea))
        
        # UPDATE SEQUENCE
        q_list = list(np.arange(10,110,10)) + [90,80]
        for q in q_list:
            atc = self.ATCF(q)
            mc = self.MCF(q)

            qP = self.coords_to_point(q, 0)
            qPX = self.coords_to_point(q, max(atc,mc))
            atcP = self.coords_to_point(q, atc)
            atcPX = self.coords_to_point(0, atc)
            mcP = self.coords_to_point(q, mc)
            mcPX = self.coords_to_point(0, mc)

            qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
            qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
            qD.next_to(qLine,DOWN)

            atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
            atcD = TextMobject("ATC ="+str(int(atc))).set_color(self.atc_color).scale(0.8)
            atcD.next_to(atcLine,LEFT)

            mcLine = DashedVMobject(Line(mcP,mcPX, color=self.axes_color))
            mcD = TextMobject("MC ="+str(int(mc))).set_color(self.mc_color).scale(0.8)
            mcD.next_to(mcLine,LEFT)
            
            # PROFIT
            a = self.coords_to_point(0, p)
            b = self.coords_to_point(0, atc)
            c = self.coords_to_point(q, atc)
            d = self.coords_to_point(q, p)
            PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
            PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
            PROFN.next_to(self.PROFD,RIGHT)
            
            self.play(Transform(self.qLine,qLine),Transform(self.qD,qD),
                      Transform(self.atcD,atcD),Transform(self.mcLine,mcLine),Transform(self.mcD,mcD),
                      Transform(self.PROFArea,PROFArea),Transform(self.PROFN,PROFN))
            self.wait(3)
        
        # CLOSE OUT
        self.play(FadeOut(self.qLine),FadeOut(self.qD),FadeOut(self.atcLine),FadeOut(self.atcD),FadeOut(self.mcLine),FadeOut(self.mcD),
                  FadeOut(self.MR),FadeOut(self.MRL),FadeOut(self.MRD),
                  FadeOut(self.PD),FadeOut(self.MBD),
                  FadeOut(self.MC),FadeOut(self.MCL),FadeOut(self.MCD),
                  FadeOut(self.ATC),FadeOut(self.ATCL),FadeOut(self.ATCD),
                  FadeOut(self.PROFL),FadeOut(self.PROFD),FadeOut(self.PROFArea),FadeOut(self.PROFN),
                  FadeOut(self.minatc),FadeOut(self.axes))


class PerfectCompB(GraphScene):
    #CONFIG = metaConfigPerfectCompB

    def construct(self):
        self.intro_sequence()
        self.initialize(80)
        self.competitiveMarkets(2)
        equilibrium_alpha = np.sqrt(2000)/(100-np.sqrt(2000))
        self.competitiveMarkets(equilibrium_alpha+0.2)
        self.competitiveMarkets(equilibrium_alpha+0.3)
        self.competitiveMarkets(equilibrium_alpha+0.4)
        self.competitiveMarkets(equilibrium_alpha+0.5)
        self.competitiveMarkets(equilibrium_alpha+0.45)
        self.competitiveMarkets(equilibrium_alpha+0.44)
        self.competitiveMarkets(equilibrium_alpha+0.43)
        self.competitiveMarkets(equilibrium_alpha+0.42)
        self.competitiveMarkets(equilibrium_alpha+0.423)
        self.competitiveMarkets(equilibrium_alpha+0.424)
        self.competitiveMarkets(equilibrium_alpha+0.425)
        self.competitiveMarkets(equilibrium_alpha+0.426)
        self.outro()
        
    def intro_sequence(self):
        self.transform_title = TextMobject("Tutorial 5.2 | Perfect Competition").scale(1.2)
        self.transform_title.to_corner(UP)
        self.add(self.transform_title)
        result = TextMobject("MC = MR").scale(1.5).set_color(self.result_color)
        self.play(FadeIn(result))
        self.wait(4)
        question = TextMobject("Can competitive firms maintain profits?").scale(1.5)
        self.play(Transform(result,question))
        self.wait(4)
        self.play(FadeOut(result))

        
    def initialize(self,p):
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        self.MRF = lambda q : p
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MC
        self.MCD = TextMobject("MC").set_color(self.mc_color).scale(0.7)
        self.MCD.move_to(self.coords_to_point(100,self.MCF(100)),LEFT)
        # ATC
        self.ATCD = TextMobject("ATC").set_color(self.atc_color).scale(0.7)
        self.ATCD.move_to(self.coords_to_point(100,self.ATCF(100)),LEFT)
        # MR
        self.MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        self.MRD.move_to(self.coords_to_point(100,self.MRF(100)),LEFT)
        # PRICE
        self.PD = TextMobject(str(p)).set_color(self.mr_color).scale(0.8)
        self.PD.next_to(self.MR,LEFT)
        

        # EQUILIBRIUM POINT 
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))

        q = p
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        self.qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        self.qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        self.atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(30, 130)
        b = self.coords_to_point(30, 115)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("$$\\Pi^* = $$").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(ShowCreation(self.MR),ShowCreation(self.MRD), # MR
                  ShowCreation(self.MC),ShowCreation(self.MCD), # MC
                  ShowCreation(self.ATC),ShowCreation(self.ATCD), # ATC
                  ShowCreation(self.PD),#ShowCreation(self.MPBD), # PRICE AND MPB
                  ShowCreation(self.qLine),ShowCreation(self.qD),ShowCreation(self.atcLine),ShowCreation(self.atcD),
                  FadeIn(self.PROFL),FadeIn(self.PROFD),ShowCreation(self.PROFN),ShowCreation(self.PROFArea), # PROFIT AND CALCULATION
                  ShowCreation(self.minatc)
                 )
        
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        self.MPBF = lambda q : 100 - q
        self.MPB = self.get_graph(lambda x : self.MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        alpha = 1/4
        self.MPCF = lambda q : q/alpha
        self.MPC = self.get_graph(lambda x : self.MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        self.MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        self.MPBD.move_to(self.coords_to_point(100,self.MPBF(100)),LEFT)
        # MPC
        self.MPCD = TextMobject("S").set_color(self.mc_color).scale(0.8)
        self.MPCD.move_to(self.coords_to_point(100,self.MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        self.PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        self.PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        self.PMD.next_to(self.PLine,LEFT)
        
        self.QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        self.QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        self.QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(ShowCreation(self.MPB),ShowCreation(self.MPBD), # MPB
                  ShowCreation(self.MPC),ShowCreation(self.MPCD), # MPC
                  ShowCreation(self.PLine),ShowCreation(self.PMD),
                  ShowCreation(self.QLine),ShowCreation(self.QD),
                 )
        
    def competitiveMarkets(self,alpha):
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        MPBF = lambda q : 100 - q
        MPB = self.get_graph(lambda x : MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        MPCF = lambda q : q/alpha
        MPC = self.get_graph(lambda x : MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        MPBD.move_to(self.coords_to_point(100,MPBF(100)),LEFT)
        # MPC
        MPCD = TextMobject("S").set_color(self.mc_color).scale(0.7)
        MPCD.move_to(self.coords_to_point(100,MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PMD.next_to(PLine,LEFT)
        
        QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(Transform(self.MPB,MPB),Transform(self.MPBD,MPBD), # MPB
                  Transform(self.MPC,MPC),Transform(self.MPCD,MPCD), # MPC
                  Transform(self.PLine,PLine),Transform(self.PMD,PMD),
                  Transform(self.QLine,QLine),Transform(self.QD,QD),
                 )
        
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        MCF = lambda q : q
        MC = self.get_graph(lambda x : MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        ATCF = lambda q : q/2 + 1000/q
        ATC = self.get_graph(lambda x : ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        MRF = lambda q : price
        MR = self.get_graph(lambda x : MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MR
        MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        MRD.move_to(self.coords_to_point(100,MRF(100)),LEFT)
        # PRICE
        PD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PD.next_to(MR,LEFT)

        q = price
        ### THis needs work
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        qD.next_to(qLine,DOWN)
        
        atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        atcD.next_to(atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, price)
        PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        PROFN = TextMobject(str(int((price-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(Transform(self.MR,MR),Transform(self.MRD,MRD), # MR
                  Transform(self.PD,PD), # PRICE AND MPB
                  Transform(self.qLine,qLine),Transform(self.qD,qD),Transform(self.atcLine,atcLine),Transform(self.atcD,atcD),
                  Transform(self.PROFN,PROFN),Transform(self.PROFArea,PROFArea), # PROFIT AND CALCULATION
                 )
        
    def outro(self):
        self.play(FadeOut(self.PROFL),FadeOut(self.PROFD),FadeOut(self.PROFN))
        result = TextMobject("In the long run, competitive firms earn zero profit.")
        result.next_to(self.transform_title,DOWN).set_color(self.result_color)
        self.play(FadeIn(result))


class Monopoly(GraphScene):
    CONFIG = metaConfigMonopoly

    """Tutorial 5.3 | Monopoly"""

    def construct(self):
        self.intro_sequence()
        #self.initialize(80)
        #self.monopoly()
        
    def intro_sequence(self):
        title = TextMobject("Week 5 Outline").scale(1.5)
        self.play(FadeIn(title))
        transform_title = TextMobject("Week 5 Outline").scale(1.2)
        tutorial_1 = TextMobject("Tutorial 5.1 | Production Costs")
        tutorial_1.to_edge(4*UP+LEFT).set_color(GREY)
        tutorial_2 = TextMobject("Tutorial 5.2 | Competitive Firms")
        tutorial_2.to_edge(6*UP+LEFT).set_color(GREY)
        tutorial_3 = TextMobject("Tutorial 5.3 | Monopoly")
        tutorial_3.to_edge(8*UP+LEFT).set_color(GREY)
        tutorial_4 = TextMobject("Tutorial 5.4 | Monopolistic Competition")
        tutorial_4.to_edge(10*UP+LEFT).set_color(GREY)
        tutorial_5 = TextMobject("Tutorial 5.5 | Oligopoly and Duopoly")
        tutorial_5.to_edge(12*UP+LEFT).set_color(GREY)
        self.play(Transform(title, transform_title.to_corner(UP)),
                  FadeIn(tutorial_1), FadeIn(tutorial_2), FadeIn(tutorial_3), FadeIn(tutorial_4), FadeIn(tutorial_5))
        self.wait(1)
        
        update = TextMobject("Tutorial 5.3 | Monopoly")
        update.to_edge(8*UP+2*LEFT).scale(1.1).set_color(WHITE)
        self.play(Transform(tutorial_3,update),run_time=2)
        self.wait(2)
        update = TextMobject("Tutorial 5.3 | Monopoly")
        update.to_edge(8*UP+LEFT).set_color(GREY)
        self.play(Transform(tutorial_3,update),run_time=2)
        self.wait(1)
        transform_title = TextMobject("Tutorial 5.3 | Monopoly").scale(1.2)
        self.play(Transform(tutorial_3, transform_title.to_corner(UP)),
                  FadeOut(title),FadeOut(tutorial_1),FadeOut(tutorial_2),FadeOut(tutorial_4),FadeOut(tutorial_5))
        
        self.graph_origin = 3.3*DOWN + 5*LEFT
        self.setup_axes()

        
    def initialize(self,p):
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        self.MRF = lambda q : p
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MC
        self.MCD = TextMobject("MC").set_color(self.mc_color).scale(0.7)
        self.MCD.move_to(self.coords_to_point(100,self.MCF(100)),LEFT)
        # ATC
        self.ATCD = TextMobject("ATC").set_color(self.atc_color).scale(0.7)
        self.ATCD.move_to(self.coords_to_point(100,self.ATCF(100)),LEFT)
        # MR
        self.MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        self.MRD.move_to(self.coords_to_point(100,self.MRF(100)),LEFT)
        # PRICE
        self.PD = TextMobject(str(p)).set_color(self.mr_color).scale(0.8)
        self.PD.next_to(self.MR,LEFT)
        

        # EQUILIBRIUM POINT 
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))

        q = p
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        self.qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        self.qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        self.atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(30, 130)
        b = self.coords_to_point(30, 115)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("$$\\Pi^* = $$").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(ShowCreation(self.MR),ShowCreation(self.MRD), # MR
                  ShowCreation(self.MC),ShowCreation(self.MCD), # MC
                  ShowCreation(self.ATC),ShowCreation(self.ATCD), # ATC
                  ShowCreation(self.PD),#ShowCreation(self.MPBD), # PRICE AND MPB
                  ShowCreation(self.qLine),ShowCreation(self.qD),ShowCreation(self.atcLine),ShowCreation(self.atcD),
                  FadeIn(self.PROFL),FadeIn(self.PROFD),ShowCreation(self.PROFN),ShowCreation(self.PROFArea), # PROFIT AND CALCULATION
                  ShowCreation(self.minatc)
                 )
        
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        self.MPBF = lambda q : 100 - q
        self.MPB = self.get_graph(lambda x : self.MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        alpha = 1/4
        self.MPCF = lambda q : q/alpha
        self.MPC = self.get_graph(lambda x : self.MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        self.MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        self.MPBD.move_to(self.coords_to_point(100,self.MPBF(100)),LEFT)
        # MPC
        self.MPCD = TextMobject("S").set_color(self.mc_color).scale(0.8)
        self.MPCD.move_to(self.coords_to_point(100,self.MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        self.PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        self.PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        self.PMD.next_to(self.PLine,LEFT)
        
        self.QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        self.QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        self.QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(ShowCreation(self.MPB),ShowCreation(self.MPBD), # MPB
                  ShowCreation(self.MPC),ShowCreation(self.MPCD), # MPC
                  ShowCreation(self.PLine),ShowCreation(self.PMD),
                  ShowCreation(self.QLine),ShowCreation(self.QD),
                 )
        
    def monopoly(self,alpha):
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        MPBF = lambda q : 100 - q
        MPB = self.get_graph(lambda x : MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        MPCF = lambda q : q/alpha
        MPC = self.get_graph(lambda x : MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        MPBD.move_to(self.coords_to_point(100,MPBF(100)),LEFT)
        # MPC
        MPCD = TextMobject("S").set_color(self.mc_color).scale(0.7)
        MPCD.move_to(self.coords_to_point(100,MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PMD.next_to(PLine,LEFT)
        
        QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(Transform(self.MPB,MPB),Transform(self.MPBD,MPBD), # MPB
                  Transform(self.MPC,MPC),Transform(self.MPCD,MPCD), # MPC
                  Transform(self.PLine,PLine),Transform(self.PMD,PMD),
                  Transform(self.QLine,QLine),Transform(self.QD,QD),
                 )
        
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        MCF = lambda q : q
        MC = self.get_graph(lambda x : MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        ATCF = lambda q : q/2 + 1000/q
        ATC = self.get_graph(lambda x : ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        MRF = lambda q : price
        MR = self.get_graph(lambda x : MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MR
        MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        MRD.move_to(self.coords_to_point(100,MRF(100)),LEFT)
        # PRICE
        PD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PD.next_to(MR,LEFT)

        q = price
        ### THis needs work
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        qD.next_to(qLine,DOWN)
        
        atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        atcD.next_to(atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, price)
        PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        PROFN = TextMobject(str(int((price-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(Transform(self.MR,MR),Transform(self.MRD,MRD), # MR
                  Transform(self.PD,PD), # PRICE AND MPB
                  Transform(self.qLine,qLine),Transform(self.qD,qD),Transform(self.atcLine,atcLine),Transform(self.atcD,atcD),
                  Transform(self.PROFN,PROFN),Transform(self.PROFArea,PROFArea), # PROFIT AND CALCULATION
                 )
        
    def outro(self):
        self.play(FadeOut(self.PROFL),FadeOut(self.PROFD),FadeOut(self.PROFN))
        result = TextMobject("In the long run, competitive firms earn zero profit.")
        result.next_to(self.transform_title,DOWN).set_color(self.result_color)
        self.play(FadeIn(result))
