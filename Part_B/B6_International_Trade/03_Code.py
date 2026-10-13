# maniml 03_Code.py Tarrifs

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

config.background_color = 'white'

class Tarrifs(GraphScene):
    CONFIG = {
        "x_axis_label": "$Q$",
        "y_axis_label": "$P$",
        "x_min": 0,
        "x_max": 100,
        "y_min": 0,
        "y_max": 10,
        "x_axis_width": FRAME_HEIGHT,
        "y_axis_height":FRAME_HEIGHT / 2,
        "x_labeled_nums": [],
        "y_labeled_nums": [2,10],
        "y_tick_frequency": 10,
        "x_tick_frequency": 100,
        "graph_origin": np.array((-FRAME_X_RADIUS + 1.8*LARGE_BUFF, -FRAME_Y_RADIUS + 2*LARGE_BUFF, 0)),
        "demand_color": BLUE,
        "supply_color": ORANGE,
        "expenditure_color": GREEN,
        "cs_color": PINK,
        "ps_color": YELLOW,
        "surplus_color": BLUE,
        "pq_color": RED,
        "axes_color": GREY,
        "dwl_color": GREY,
        "gov_color": RED,
    }

    """Tutorial 3.6 | International Trade and Tarrifs"""

    def construct(self):
        self.intro_sequence()
        self.wait(3)
        self.initialize_eq()
        self.wait(3)
        self.tariff(7,0)
        self.wait(3)
        self.tariff(9,0)
        self.wait(3)
        self.tariff(8,0)
        self.wait(3)
        self.tariff(7,0)
        self.wait(3)
        self.tariff(8,0)
        self.wait(3)
        self.tariff(9,0)
        self.wait(3)
        self.tariff(5,0)
        self.wait(3)
        self.tariff(3,0)
        self.wait(3)
        self.tariff(4,0)
        self.wait(3)
        self.tariff(5,0)
        self.wait(3)
        self.tariff(4,0)
        self.wait(3)
        self.tariff(3,0)
        self.wait(3)
        self.tariff(4,0)
        self.wait(3)
        self.welfare(4,0)
        self.wait(3)
        self.update(4,0)
        self.wait(3)
        self.update(4,1)
        self.wait(3)
        self.update(8,1)
        self.wait(3)
        self.update(9,2)
        self.wait(3)
        self.update(9,1)
        self.wait(3)
        self.update(8,1)
        self.wait(3)
        self.update(7,1)
        self.wait(3)
        self.update(6,0)
        self.wait(3)
        self.update(2,1)
        self.wait(3)
        self.update(2,2)
        self.wait(3)
        self.update(2,3)
        self.wait(3)
        self.update(2,4)
        self.wait(3)
        self.update(3,3)
        self.wait(3)
        self.update(4,2)
        self.wait(3)
        self.update(5,1)
        self.wait(3)
        self.update(5,0)
        self.wait(3)
        self.update(4,0)
        self.wait(3)
        self.update(3,0)
        self.wait(3)
        self.update(4,0)
        
        
    def DemandQ(self, priceD):
        return 100 - 10*priceD
    
    def DemandP(self,quantityD):
        return (10 - quantityD/10)
    
    def SupplyQ(self, priceS):
        return 10*priceS - 20
    
    def SupplyP(self,quantityS):
        return 2 + quantityS /10
        
    def intro_sequence(self):
        title = TextMobject("Tutorial 3.6 | International Trade").scale(1.5)
        self.play(FadeIn(title))
        self.wait(1)
        transform_title = TextMobject("Tutorial 3.6 | International Trade").scale(1.2)
        transform_title.to_corner(UP)
        self.play(
            Transform(title, transform_title))
        self.wait(3)
        self.setup_axes(animate=True)
        
    def initialize_eq(self):
        self.DemandCurveEq = self.get_graph(self.DemandP, self.demand_color, x_min=0, x_max=100)
        self.DemandCurveEqL = TextMobject("Demand").scale(0.8)
        self.DemandCurveEqL.set_color(self.demand_color)
        self.DemandCurveEqL.move_to(self.coords_to_point(83, 3),LEFT)
        self.DemandCurve = self.get_graph(self.DemandP, self.demand_color, x_min=0, x_max=100)
        self.SupplyCurveEq = self.get_graph(self.SupplyP, self.supply_color, x_min=0, x_max=80)
        self.SupplyCurveEqL = TextMobject("Supply").scale(0.8)
        self.SupplyCurveEqL.set_color(self.supply_color)
        self.SupplyCurveEqL.move_to(self.coords_to_point(83, 10),LEFT)
        self.SupplyCurve = self.get_graph(self.SupplyP, self.supply_color, x_min=0, x_max=80)
        
        eqp1 = self.coords_to_point(0, 6)
        eqp2 = self.coords_to_point(40, 6)
        eqp3 = self.coords_to_point(40, 0)
        
        self.horzLineEq = DashedVMobject(Line(eqp1,eqp2, color=self.axes_color))
        self.vertLineEq = DashedVMobject(Line(eqp2,eqp3, color=self.axes_color))

        self.vertLineS = DashedVMobject(Line(eqp2,eqp3, color=self.axes_color))
        self.quantS = TextMobject(str(40)).scale(0.7)
        self.quantS.add_updater(lambda d: d.next_to(self.vertLineS, DOWN))
        
        self.vertLineB = DashedVMobject(Line(eqp2,eqp3, color=self.axes_color))
        self.quantB = TextMobject(str(40)).scale(0.7)
        self.quantB.add_updater(lambda d: d.next_to(self.vertLineB, DOWN))
        
        self.horzLineS =  DashedVMobject(Line(eqp1,eqp2, color=self.axes_color))
        self.priceS = TextMobject("$p_S=$ "+str(6)).scale(0.7)
        self.priceS.add_updater(lambda d: d.next_to(self.horzLineS, LEFT+DOWN))
        
        self.horzLineB =  DashedVMobject(Line(eqp1,eqp2, color=self.axes_color))
        self.priceB = TextMobject("$p_B=$ "+str(6)).scale(0.7)
        self.priceB.add_updater(lambda d: d.next_to(self.horzLineB, LEFT+UP))
        
        qL = self.coords_to_point(0, -2)
        qU = self.coords_to_point(6, -2)
        
        self.domestic = Line(qL,qU, color=self.axes_color)
        self.domesticL = TextMobject("Domestic").scale(0.6)
        self.domesticL.add_updater(lambda d: d.next_to(self.domestic,DOWN))
        
        self.trade = Line(qL,qU, color=self.axes_color)
        self.tradeL = TextMobject("Trade").scale(0.6)
        #self.tradeL.add_updater(lambda d: d.next_to(self.trade,DOWN))
        
        # WELFARE
        
        a = self.coords_to_point(130, 10)
        b = self.coords_to_point(130, 8.5)
        self.csL = Line(a,b, color=self.cs_color)
        
        self.csD = TextMobject("CS")
        self.csD.next_to(self.csL,LEFT)
        self.csD.set_color(self.cs_color)
        
        a = self.coords_to_point(130, 8)
        b = self.coords_to_point(130, 6.5)
        self.psL = Line(a,b, color=self.ps_color)
        
        self.psD = TextMobject("PS")
        self.psD.next_to(self.psL,LEFT)
        self.psD.set_color(self.ps_color)

        a = self.coords_to_point(130, 6)
        b = self.coords_to_point(130, 4.5)
        self.govL = Line(a,b, color=self.gov_color)
        
        self.govD = TextMobject("GOV")
        self.govD.next_to(self.govL,LEFT)
        self.govD.set_color(self.gov_color)
        
        a = self.coords_to_point(130, 4)
        b = self.coords_to_point(130, 2.5)
        self.dwlL = Line(a,b, color=self.dwl_color)
        
        self.dwlD = TextMobject("DWL")
        self.dwlD.next_to(self.dwlL,LEFT)
        self.dwlD.set_color(self.dwl_color)
        
        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(100, 0)
        self.priceG = Line(a,b, color=self.pq_color)
        self.priceGL = TextMobject("$p_G=$").scale(0.7)
        self.priceGL.next_to(self.priceG,LEFT)
        
        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(100, 0)
        self.priceGT = Line(a,b, color=self.pq_color)
        self.priceGTL = TextMobject("$p_T=$").scale(0.7)
        self.priceGTL.next_to(self.priceGT,LEFT)
        
        self.play(ShowCreation(self.DemandCurveEq))
        self.add(self.SupplyCurveEqL)
        self.add(self.DemandCurveEqL)
        self.play(ShowCreation(self.SupplyCurveEq),ShowCreation(self.SupplyCurveEqL))
        self.play(ShowCreation(self.horzLineEq))
        self.play(ShowCreation(self.vertLineEq))
        
    
    def tariff(self, price, tariff):
        if price > 6: # exports
            tradeL = TextMobject("Exports").scale(0.6)
            priceE = price
            price = max(price - tariff,6)
        if price <= 6: # imports
            tradeL = TextMobject("Imports").scale(0.6)
            priceE = price
            price = min(price + tariff,6)
        qS = self.SupplyQ(price)
        qB = self.DemandQ(price)
        
        qSp1 = self.coords_to_point(qS, 0)
        qSp2 = self.coords_to_point(qS, price)
        vertLineS = DashedVMobject(Line(qSp1,qSp2, color=self.supply_color))
        quantS = TextMobject(str(qS)).scale(0.7)
        quantS.next_to(vertLineS, DOWN)

        qBp1 = self.coords_to_point(qB, 0)
        qBp2 = self.coords_to_point(qB, price)
        vertLineB = DashedVMobject(Line(qBp1,qBp2, color=self.demand_color))
        quantB = TextMobject(str(qB)).scale(0.7)
        quantB.next_to(vertLineB, DOWN)
        
        qL = self.coords_to_point(0, -2)
        qM1 = self.coords_to_point(min(qS,qB)-0.5, -2)
        qM2 = self.coords_to_point(min(qS,qB)+0.5, -2)
        qU = self.coords_to_point(max(qS,qB), -2)
        domestic = Line(qL,qM1, color=self.axes_color)
        trade = Line(qM2,qU, color=self.axes_color)
        tradeL.add_updater(lambda d: d.next_to(trade,DOWN))
            
        a = self.coords_to_point(0, priceE)
        b = self.coords_to_point(100, priceE)
        priceG = Line(a,b, color=self.pq_color)
        priceGL = TextMobject("$p_G=$"+str(price)).scale(0.7)
        priceGL.set_color(self.pq_color)
        priceGL.next_to(priceG, LEFT)
        
        a = self.coords_to_point(0, priceE)
        b = self.coords_to_point(100, priceE)
        priceGT = DashedVMobject(Line(a,b, color=self.pq_color))
        priceGTL = TextMobject("$p_G=$"+str(priceE)).scale(0.7)
        priceGTL.set_color(self.pq_color)
        priceGTL.next_to(priceGT, LEFT)
        if tariff > 0:
            priceGTL = TextMobject("$p_T=$"+str(priceE)).scale(0.7)
            priceGTL.set_color(self.pq_color)
            priceGTL.next_to(priceGT, LEFT)
        
        self.add(self.domesticL)
        
        self.play(
                    Transform(self.quantS,quantS), Transform(self.priceG, priceG),
                    Transform(self.quantB,quantB), Transform(self.priceGL,priceGL), 
                    Transform(self.priceGT, priceGT), Transform(self.priceGTL,priceGTL),
                    Transform(self.vertLineS,vertLineS), Transform(self.trade,trade), Transform(self.tradeL,tradeL),
                    Transform(self.vertLineB,vertLineB), Transform(self.domestic,domestic),
                    #Transform(self.horzLineS,horzLineS), Transform(self.priceS,priceS),
                    #Transform(self.horzLineB,horzLineB), Transform(self.priceB,priceB)
        )
        
        
    def welfare(self, price, tariff):
        if price > 6: # exports
            tradeL = TextMobject("Exports").scale(0.6)
            priceE = price
            price = max(price - tariff,6)
        if price <= 6: # imports
            tradeL = TextMobject("Imports").scale(0.6)
            priceE = price
            price = min(price + tariff,6)
        qS = self.SupplyQ(price)
        qB = self.DemandQ(price)
        
        qSp1 = self.coords_to_point(qS, 0)
        qSp2 = self.coords_to_point(qS, price)
        vertLineS = DashedVMobject(Line(qSp1,qSp2, color=self.supply_color))
        quantS = TextMobject(str(qS)).scale(0.7)
        quantS.next_to(vertLineS, DOWN)

        qBp1 = self.coords_to_point(qB, 0)
        qBp2 = self.coords_to_point(qB, price)
        vertLineB = DashedVMobject(Line(qBp1,qBp2, color=self.demand_color))
        quantB = TextMobject(str(qB)).scale(0.7)
        quantB.next_to(vertLineB, DOWN)
        
        # CS
        a = self.coords_to_point(0, 10)
        b = self.coords_to_point(qB, price)
        c = self.coords_to_point(0, price)
        self.cs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.cs_color, color=self.cs_color)
        self.csN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.cs_color, color=self.cs_color)
        
        csN = TextMobject(str(int((10-price)*qB/2)))
        csN.next_to(self.csL, RIGHT)
        csN.set_color(self.cs_color)
        
        self.add(self.csL,self.csD)
        self.play(FadeIn(self.cs),Transform(self.csN,csN))
        self.wait(3)
        
        # PS
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(qS, price)
        c = self.coords_to_point(0, 2)
        self.ps = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        self.psN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        
        psN = TextMobject(str(int((price-2)*qS/2)))
        psN.next_to(self.psL, RIGHT)
        psN.set_color(self.ps_color)
        
        self.add(self.psL,self.psD)
        self.play(FadeIn(self.ps),Transform(self.psN,psN))
        self.wait(3)
        
        # GOV
        a = self.coords_to_point(min(qS,qB),priceE)
        b = self.coords_to_point(min(qS,qB),price)
        c = self.coords_to_point(max(qS,qB),price)
        d = self.coords_to_point(max(qS,qB),priceE)
        self.gov = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)
        self.govN = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)

        govN = TextMobject(str(int(abs(qS-qB)*tariff)))
        govN.next_to(self.govL, RIGHT)
        govN.set_color(self.gov_color)

        self.add(self.govL,self.govD)
        self.play(FadeIn(self.gov),Transform(self.govN,govN))
        self.wait(3)
        
        # DWL
        altS = self.SupplyQ(priceE)
        altB = self.DemandQ(priceE)
        a = self.coords_to_point(min(qS,qB),price)
        b = self.coords_to_point(min(qS,qB),priceE)
        c = self.coords_to_point(min(altS,altB),priceE)
        self.dwl1 = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        a = self.coords_to_point(max(qS,qB),price)
        b = self.coords_to_point(max(qS,qB),priceE)
        c = self.coords_to_point(max(altS,altB),priceE)
        self.dwl2 = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        self.dwlN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        dwlN = TextMobject(str(int((abs(altS-qS)+abs(altB-qB))*abs(price-priceE)/2)))
        dwlN.next_to(self.dwlL, RIGHT)
        dwlN.set_color(self.dwl_color)
        
        self.add(self.dwlL,self.dwlD)
        self.play(FadeIn(self.dwl1),FadeIn(self.dwl2),Transform(self.dwlN,dwlN))  

        
    def update(self,price,tariff):
        
        if price > 6: # exports
            tradeL = TextMobject("Exports").scale(0.6)
            priceE = price
            price = max(price - tariff,6)
        if price <= 6: # imports
            tradeL = TextMobject("Imports").scale(0.6)
            priceE = price
            price = min(price + tariff,6)
        qS = self.SupplyQ(price)
        qB = self.DemandQ(price)
        
        qSp1 = self.coords_to_point(qS, 0)
        qSp2 = self.coords_to_point(qS, price)
        vertLineS = DashedVMobject(Line(qSp1,qSp2, color=self.supply_color))
        quantS = TextMobject(str(qS)).scale(0.7)
        quantS.next_to(vertLineS, DOWN)

        qBp1 = self.coords_to_point(qB, 0)
        qBp2 = self.coords_to_point(qB, price)
        vertLineB = DashedVMobject(Line(qBp1,qBp2, color=self.demand_color))
        quantB = TextMobject(str(qB)).scale(0.7)
        quantB.next_to(vertLineB, DOWN)
        
        qL = self.coords_to_point(0, -2)
        qM1 = self.coords_to_point(min(qS,qB)-0.5, -2)
        qM2 = self.coords_to_point(min(qS,qB)+0.5, -2)
        qU = self.coords_to_point(max(qS,qB), -2)
        domestic = Line(qL,qM1, color=self.axes_color)
        trade = Line(qM2,qU, color=self.axes_color)
        tradeL.add_updater(lambda d: d.next_to(trade,DOWN))
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(100, price)
        priceG = Line(a,b, color=self.pq_color)
        priceGL = TextMobject("$p_T=$"+str(price)).scale(0.7)
        priceGL.set_color(self.pq_color)
        priceGL.next_to(priceG, LEFT)
        
        a = self.coords_to_point(0, priceE)
        b = self.coords_to_point(100, priceE)
        priceGT = DashedVMobject(Line(a,b, color=self.pq_color))
        priceGTL = TextMobject("$p_T=$"+str(priceE)).scale(0.7)
        priceGTL.set_color(self.pq_color)
        priceGTL.next_to(priceGT, LEFT)
        if tariff > 0:
            priceGTL = TextMobject("$p_G=$"+str(priceE)).scale(0.7)
            priceGTL.set_color(self.pq_color)
            priceGTL.next_to(priceGT, LEFT)
        
        # CS
        a = self.coords_to_point(0, 10)
        b = self.coords_to_point(qB, price)
        c = self.coords_to_point(0, price)
        cs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.cs_color, color=self.cs_color)
        csN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.cs_color, color=self.cs_color)
        
        csN = TextMobject(str(int((10-price)*qB/2)))
        csN.next_to(self.csL, RIGHT)
        csN.set_color(self.cs_color)
        
        # PS
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(qS, price)
        c = self.coords_to_point(0, 2)
        ps = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        psN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        
        psN = TextMobject(str(int((price-2)*qS/2)))
        psN.next_to(self.psL, RIGHT)
        psN.set_color(self.ps_color)
        
        # GOV
        a = self.coords_to_point(min(qS,qB),priceE)
        b = self.coords_to_point(min(qS,qB),price)
        c = self.coords_to_point(max(qS,qB),price)
        d = self.coords_to_point(max(qS,qB),priceE)
        gov = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)
        govN = Polygon(a,b,c,d, fill_opacity = 0.1, fill_color = self.gov_color, color=self.gov_color)

        govN = TextMobject(str(int(abs(qS-qB)*tariff)))
        govN.next_to(self.govL, RIGHT)
        govN.set_color(self.gov_color)
        
        # DWL
        altS = self.SupplyQ(priceE)
        altB = self.DemandQ(priceE)
        a = self.coords_to_point(min(qS,qB),price)
        b = self.coords_to_point(min(qS,qB),priceE)
        c = self.coords_to_point(min(altS,altB),priceE)
        dwl1 = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        a = self.coords_to_point(max(qS,qB),price)
        b = self.coords_to_point(max(qS,qB),priceE)
        c = self.coords_to_point(max(altS,altB),priceE)
        dwl2 = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        dwlN = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.dwl_color, color=self.dwl_color)
        dwlN = TextMobject(str(int((abs(altS-qS)+abs(altB-qB))*abs(price-priceE)/2)))
        dwlN.next_to(self.dwlL, RIGHT)
        dwlN.set_color(self.dwl_color)
        
        self.add(self.govL,self.govD)
        self.add(self.dwlL,self.dwlD)        
        self.add(self.csL,self.csD)
        self.add(self.psL,self.psD)
        self.play(Transform(self.cs,cs),Transform(self.csN,csN),
                  Transform(self.ps,ps),Transform(self.psN,psN),
                  Transform(self.gov,gov),Transform(self.govN,govN),
                  Transform(self.dwl1,dwl1),Transform(self.dwl2,dwl2),Transform(self.dwlN,dwlN),
                  Transform(self.quantS,quantS), Transform(self.priceG, priceG),
                  Transform(self.quantB,quantB), Transform(self.priceGL,priceGL),
                  Transform(self.priceGT, priceGT), Transform(self.priceGTL,priceGTL),
                  Transform(self.vertLineS,vertLineS), Transform(self.trade,trade), Transform(self.tradeL,tradeL),
                  Transform(self.vertLineB,vertLineB), Transform(self.domestic,domestic),
                 )
