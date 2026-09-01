# maniml 03_Code.py MonopolisticComp #-low_quality

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

class MonopolisticComp(GraphScene):
    CONFIG = metaConfigMonopoly

    """Tutorial 5.4 | Monopolistically Competitive Firms"""

    def construct(self):
        self.intro_sequence()
        self.initialize(2)
        self.monopoly_sol(2)
        # self.monopoly(alpha,Equilibrium,non-Eq Qaunt,tax,lumpsumTax)
        alpha = 2
        self.monopoly(alpha,True,0,0,0)
        for i in np.arange(0,1,0.1)[::-1]:
            if self.PROFn > 0:
                alpha = alpha - i**4
                self.monopoly(alpha,True,0,0,0)
            if self.PROFn < 0:
                alpha = alpha + i**4
                self.monopoly(alpha,True,0,0,0)
        self.monopoly(alpha,True,0,20,0)
        for i in np.arange(0,1,0.1)[::-1]:
            if self.PROFn > 0:
                alpha = alpha - i**4
                self.monopoly(alpha,True,0,20,0)
            if self.PROFn < 0:
                alpha = alpha + i**4
                self.monopoly(alpha,True,0,20,0)
        
    def intro_sequence(self):
        self.title = TextMobject("Week 5 Outline").scale(1.5)
        self.play(FadeIn(self.title))
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
        
        self.play(Transform(self.title, transform_title.to_corner(UP)),
                  FadeIn(tutorial_1), FadeIn(tutorial_2), FadeIn(tutorial_3), FadeIn(tutorial_4), FadeIn(tutorial_5))
        self.wait(3)
        update = TextMobject("Tutorial 5.4 | Monopolistic Competition").scale(1.1)
        update.to_edge(10*UP+2*LEFT).scale(1.1).set_color(WHITE)
        self.play(Transform(tutorial_4,update),run_time=2)
        transform_title = TextMobject("Tutorial 5.4 | Monopolistic Competition").scale(1.2)
        self.play(Transform(tutorial_4, transform_title.to_corner(UP)),
                  FadeOut(self.title),FadeOut(tutorial_1),FadeOut(tutorial_2),FadeOut(tutorial_3),FadeOut(tutorial_5))
        
        bullet_1 = TextMobject("Many sellers")
        bullet_1.to_edge(4*UP+LEFT).set_color(GREY)
        bullet_2 = TextMobject("Selling differentiated products")
        bullet_2.to_edge(6*UP+LEFT).set_color(GREY)
        bullet_3 = TextMobject("With free (or easy) entry and exit")
        bullet_3.to_edge(8*UP+LEFT).set_color(GREY)

        self.play(FadeIn(bullet_1))
        self.wait(1)
        self.play(FadeIn(bullet_2))
        self.wait(1)
        self.play(FadeIn(bullet_3))
        self.wait(1)
        self.play(FadeOut(bullet_1),FadeOut(bullet_2),FadeOut(bullet_3))
        
        
    def initialize(self,alpha):
        self.graph_origin = 3*DOWN + 5.5*LEFT
        self.setup_axes()
        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=0, x_max=100)
        self.MCD = TextMobject("MC").set_color(self.mc_color).scale(0.7)
        self.MCD.move_to(self.coords_to_point(100,self.MCF(100)),LEFT)
        
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        self.ATCD = TextMobject("ATC").set_color(self.atc_color).scale(0.7)
        self.ATCD.move_to(self.coords_to_point(100,self.ATCF(100)),LEFT)
        
        # MPB
        self.MPBF = lambda q : 100 - q/alpha
        self.MPB = self.get_graph(lambda x : self.MPBF(x), color=self.mpb_color, x_min=0, x_max=min(100,100*alpha))
        self.MPBD = TextMobject("MPB").set_color(self.mpb_color).scale(0.7)
        self.MPBD.move_to(self.coords_to_point(min(100,100*alpha),self.MPBF(min(100,100*alpha))),LEFT)
        
        # MR
        self.MRF = lambda q : 100 - 2*q/alpha
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=0, x_max=min(100,50*alpha))
        self.MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        self.MRD.move_to(self.coords_to_point(50*alpha,self.MRF(50*alpha)+5),LEFT)
        
        # GOV
        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(0, 0)
        c = self.coords_to_point(0, 0)
        d = self.coords_to_point(0, 0)
        self.GOV = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)
        self.GOVD = TextMobject("GOV").set_color(self.gov_color).scale(0.8)
        self.GOVD.next_to(self.GOV,LEFT)
        
        # DWL
        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(0, 0)
        c = self.coords_to_point(0, 0)
        self.DWL = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.dwl_color)
        
        # SHOW
        self.play(ShowCreation(self.MC),ShowCreation(self.MCD), # MC
                  ShowCreation(self.ATC),ShowCreation(self.ATCD), # ATC
                 )
        self.wait(1)
        self.play(ShowCreation(self.MPB),ShowCreation(self.MPBD), # MPB
                  ShowCreation(self.MR),ShowCreation(self.MRD), # MR
                 )
        self.wait(3)

        
    def monopoly_sol(self,alpha):        
        # INTERSECTION POINTS
        q = alpha*100/(alpha+2)
        p = self.MPBF(q)
        atc = self.ATCF(q)
        mc = self.MCF(q)
        
        q0 = self.coords_to_point(q, 0)
        qMIN = self.coords_to_point(q, min(atc,mc))
        qMAX = self.coords_to_point(q, max(atc,mc))
        qMC = self.coords_to_point(q, mc)
        qATC = self.coords_to_point(q, atc)
        qP = self.coords_to_point(q, p)
        
        atcX = self.coords_to_point(0, atc)
        mcX = self.coords_to_point(0, mc)
        pX = self.coords_to_point(0, p)
        
        # INTERSECTION LINES
        self.qLine = DashedVMobject(Line(q0,qMC),color=self.axes_color)
        self.qD = TextMobject("q="+str(int(q))).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.pLine = DashedVMobject(Line(qP,pX, color=self.mpb_color))
        self.pD = TextMobject("p="+str(int(p))).set_color(self.mpb_color).scale(0.8)
        self.pD.next_to(self.pLine,LEFT)
        
        self.atcLine = DashedVMobject(Line(qATC,atcX, color=self.atc_color))
        self.atcD = TextMobject("atc="+str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        self.mcLine = DashedVMobject(Line(qMC,mcX, color=self.mc_color))
        self.mcD = TextMobject("mc="+str(int(mc))).set_color(self.mc_color).scale(0.8)
        self.mcD.next_to(self.mcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(120, 115)
        b = self.coords_to_point(120, 100)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("$$\\Pi = $$").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)
        self.PROFn = int((p-atc)*q)
        
        # SHOW THE MONOPOLISTS SOLUTION
        self.wait(3)
        self.play(ShowCreation(self.qLine),ShowCreation(self.qD))
        self.play(Transform(self.qLine,DashedVMobject(Line(q0,qP),color=self.axes_color)))
        self.play(ShowCreation(self.mcLine),ShowCreation(self.pLine),ShowCreation(self.atcLine),
                  FadeIn(self.mcD),FadeIn(self.pD),FadeIn(self.atcD))
        self.wait(3)
        self.play(FadeIn(self.PROFL),FadeIn(self.PROFD),ShowCreation(self.PROFN),ShowCreation(self.PROFArea))
        self.wait(3)
        
    def monopoly(self,alpha,truth,q,tax,lumpsum):
        # MC
        MCF = lambda q : q + tax
        MC = self.get_graph(lambda x : MCF(x), color=self.mc_color, x_min=0, x_max=100)
        MCD = TextMobject("MC").set_color(self.mc_color).scale(0.7)
        self.MCFTax = lambda q : q
        self.MCTax = DashedVMobject(self.get_graph(lambda x : self.MCFTax(x), color=self.mc_color, x_min=0, x_max=100))
        if tax != 0:
            MCD = TextMobject("MC+Tax").set_color(self.mc_color).scale(0.7)
        MCD.move_to(self.coords_to_point(100,MCF(100)),LEFT)
        
        # ATC
        ATCF = lambda q : q/2 + 1000/q + tax + lumpsum
        ATC = self.get_graph(lambda x : ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        ATCDt = "ATC"
        self.ATCFTax = lambda q : q/2 + 1000/q
        self.ATCTax = DashedVMobject(self.get_graph(lambda x : self.ATCFTax(x), color=self.atc_color, x_min=10, x_max=100))
        if tax != 0:
            ATCDt = ATCDt+"+Tax"
        if lumpsum != 0:
            ATCDt = ATCDt+"+LumpSum"
        ATCD = TextMobject(ATCDt).set_color(self.atc_color).scale(0.7)
        ATCD.move_to(self.coords_to_point(100,ATCF(100)),LEFT)
        
        # MPB
        MPBF = lambda q : 100 - q/alpha
        MPB = self.get_graph(lambda x : MPBF(x), color=self.mpb_color, x_min=0, x_max=min(100,100*alpha))
        MPBD = TextMobject("MPB").set_color(self.mpb_color).scale(0.7)
        MPBD.move_to(self.coords_to_point(min(100,100*alpha),MPBF(min(100,100*alpha))),LEFT)
        
        # MR
        MRF = lambda q : 100 - 2*q/alpha
        MR = self.get_graph(lambda x : MRF(x), color=self.mr_color, x_min=0, x_max=min(100,50*alpha))
        MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        MRD.move_to(self.coords_to_point(50*alpha,MRF(50*alpha)+5),LEFT)
        
        # INTERSECTION POINTS
        if truth:
            q = alpha*(100-tax)/(alpha+2)
        p = MPBF(q)
        atc = ATCF(q)
        mc = MCF(q)
        
        qStar = alpha*(100)/(alpha+1)
        pStar = qStar
        
        q0 = self.coords_to_point(q, 0)
        qMAX = self.coords_to_point(q, max(atc,mc))
        qMC = self.coords_to_point(q, mc)
        qATC = self.coords_to_point(q, atc)
        qP = self.coords_to_point(q, p)
        
        atcX = self.coords_to_point(0, atc)
        mcX = self.coords_to_point(0, mc)
        pX = self.coords_to_point(0, p)
        
        # INTERSECTION LINES
        qLine = DashedVMobject(Line(q0,qP),color=self.axes_color)
        qD = TextMobject("q="+str(int(q))).scale(0.8)
        qD.next_to(qLine,DOWN)
        
        pLine = DashedVMobject(Line(qP,pX, color=self.mr_color))
        pD = TextMobject("p="+str(int(p))).set_color(self.mpb_color).scale(0.8)
        pD.next_to(pLine,LEFT)
        
        atcLine = DashedVMobject(Line(qATC,atcX, color=self.atc_color))
        atcD = TextMobject("atc="+str(int(atc))).set_color(self.atc_color).scale(0.8)
        atcD.next_to(atcLine,LEFT)
        
        mcLine = DashedVMobject(Line(qMC,mcX, color=self.mc_color))
        mcD = TextMobject("mc="+str(int(mc))).set_color(self.mc_color).scale(0.8)
        mcD.next_to(mcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(120, 115)
        b = self.coords_to_point(120, 100)
        PROFL = Line(a,b, color=self.profit_color)
        PROFD = TextMobject("$$\\Pi = $$").set_color(self.profit_color).scale(0.8)
        PROFD.next_to(PROFL,RIGHT)
        PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(PROFD,RIGHT)
        
        self.PROFn = int((p-atc)*q)

        # GOV
        a = self.coords_to_point(0, atc-tax-lumpsum)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, atc-tax-lumpsum)
        GOV = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)
        GOVD = TextMobject("GOV").set_color(self.gov_color).scale(0.8)
        GOVD.next_to(PROFArea,DOWN)
        
        # DWL
        a = self.coords_to_point(q, self.MCFTax(q))
        b = self.coords_to_point(q, p)
        c = self.coords_to_point(qStar, pStar)
        DWL = Polygon(a,b,c, fill_opacity = 0.1, fill_color = self.gov_color, color=self.dwl_color)
        
        # SHOW THE MONOPOLISTS SOLUTION
        if abs(tax)+abs(lumpsum) != 0:
            self.play(FadeIn(self.MCTax),FadeIn(self.ATCTax),
                      Transform(self.MPB,MPB),Transform(self.MPBD,MPBD), # MPB
                      Transform(self.MR,MR),Transform(self.MRD,MRD), # MR
                      Transform(self.MC,MC),Transform(self.MCD,MCD),
                      Transform(self.ATC,ATC),Transform(self.ATCD,ATCD),
                      Transform(self.GOV,GOV),Transform(self.GOVD,GOVD),
                      Transform(self.DWL,DWL),
                      Transform(self.qLine,qLine),Transform(self.qD,qD),
                      Transform(self.pLine,pLine),Transform(self.mcLine,mcLine),Transform(self.atcLine,atcLine),
                      Transform(self.pD,pD),Transform(self.mcD,mcD),Transform(self.atcD,atcD),
                      Transform(self.PROFL,PROFL),Transform(self.PROFD,PROFD),Transform(self.PROFN,PROFN),Transform(self.PROFArea,PROFArea))
        
        if abs(tax)+abs(lumpsum) == 0:
            self.remove(self.MCTax,self.ATCTax,self.GOV,self.GOVD)
            self.play(Transform(self.MPB,MPB),Transform(self.MPBD,MPBD), # MPB
                      Transform(self.MR,MR),Transform(self.MRD,MRD), # MR
                      Transform(self.MC,MC),Transform(self.MCD,MCD),
                      Transform(self.ATC,ATC),Transform(self.ATCD,ATCD),
                      Transform(self.DWL,DWL),
                      Transform(self.qLine,qLine),Transform(self.qD,qD),
                      Transform(self.pLine,pLine),Transform(self.mcLine,mcLine),Transform(self.atcLine,atcLine),
                      Transform(self.pD,pD),Transform(self.mcD,mcD),Transform(self.atcD,atcD),
                      Transform(self.PROFL,PROFL),Transform(self.PROFD,PROFD),Transform(self.PROFN,PROFN),Transform(self.PROFArea,PROFArea))
        self.wait(3)
        
        # Points of tangency and MR = MC in long run
        # Highlight the relative differences in prices and quantity relative to perfect comp
        # Perfect comp finds the minimum atc in the long run. Here since the demand is downward sloping, we're producing at a cost higher than the minimum, which isn't optimal
        # We also have a markup over marginal cost, which isn't good for buyers, and this markup creates a deadweight loss


class MonopolisticCompB(GraphScene):
    CONFIG = metaConfigMonopoly

    def construct(self):
        self.outro()
        
    def outro(self):
        transform_title = TextMobject("Tutorial 5.4 | Monopolistic Competition").scale(1.2)
        self.add(transform_title.to_corner(UP))
        
        #
        bullet_0 = TextMobject("Monopolistically competitive firms:")
        bullet_0.to_edge(4*UP+LEFT).set_color(self.result_color)
        bullet_1 = TextMobject("1. Cannot sustain profits in the long run")
        bullet_1.to_edge(6*UP+3*LEFT).set_color(self.result_color)
        bullet_2 = TextMobject("2. Generate deadweight loss")
        bullet_2.to_edge(8*UP+3*LEFT).set_color(self.result_color)
        bullet_3 = TextMobject("3. Produce above minimum ATC")
        bullet_3.to_edge(10*UP+3*LEFT).set_color(self.result_color)
        bullet_4 = TextMobject("4. And sell at a markup")
        bullet_4.to_edge(12*UP+3*LEFT).set_color(self.result_color)

        self.play(FadeIn(bullet_0))
        self.wait(1)
        self.play(FadeIn(bullet_1))
        self.wait(1)
        self.play(FadeIn(bullet_2))
        self.wait(1)
        self.play(FadeIn(bullet_3))
        self.wait(1)
        self.play(FadeIn(bullet_4))
        self.wait(1)
        self.play(FadeOut(bullet_0),FadeOut(bullet_1),FadeOut(bullet_2),FadeOut(bullet_3),FadeOut(bullet_4))
