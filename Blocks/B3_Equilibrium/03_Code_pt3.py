# maniml 03_Code.py ProducerSurplus

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

# Configuration
CUSTOM_GREY = '#696969'
CUSTOM_BLACK = '#1f1f1f'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY

PIXEL_HEIGHT = 1080
FPS = 10
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT*2
config.frame_rate = FPS

class ProducerSurplus(GraphScene):
    CONFIG = {
        "x_axis_label": "$Q_d$",
        "y_axis_label": "$P$",
        "x_min": 0,
        "x_max": 100,
        "y_min": 0,
        "y_max": 10,
        "x_axis_width": FRAME_HEIGHT,
        "y_axis_height":FRAME_HEIGHT / 2,
        "x_labeled_nums": [],
        "y_labeled_nums": [2],
        "y_tick_frequency": 10,
        "x_tick_frequency": 50,
        "graph_origin": np.array((-FRAME_X_RADIUS + 1.5*LARGE_BUFF, -FRAME_Y_RADIUS + 2*LARGE_BUFF, 0)),
        "demand_color": BLUE,
        "supply_color": ORANGE,
        "cs_color": PINK,
        "ps_color": YELLOW,
        "pq_color": RED,
        "axes_color": GREY
    }

    """Animation 3 | Finding the Area

Find the area of producer surplus on a supply curve for different prices."""

    def construct(self):
        self.intro_sequence()
        self.wait(3)
        self.create_quantity_supplied(7)
        self.wait(3)
        self.update_quantity_supplied(4)
        self.wait(3)
        self.update_quantity_supplied(7)
        self.wait(3)
        self.create_ps_line(5,7)
        self.wait(3)
        self.quantity_supplied_bar(7)
        self.wait(3)
        self.show_ps(7)
        self.wait(3)
        self.find_ps_area(7)
        self.wait(3)
        self.update_ps_area(5)
        self.wait(3)
        self.update_ps_area(8)
        self.wait(3)
        self.summary()
        
    def SupplyQ(self, price):
        return 10*price - 20
    
    def SupplyP(self,quantity):
        return 2 + quantity /10
                
    def intro_sequence(self):
        title = TextMobject("Tutorial 3.2 | Producer Surplus").scale(1.5)
        self.play(FadeIn(title))
        self.wait(1)
        transform_title = TextMobject("Tutorial 3.2 | Producer Surplus").scale(1.2)
        transform_title.to_corner(UP)
        self.play(
            Transform(title, transform_title))
        self.wait(3)
        self.setup_axes(animate=True)
    
    
    def create_quantity_supplied(self,price):
        SupplyCurve = self.get_graph(self.SupplyP, self.supply_color, x_min=0, x_max=65)
        quantity = self.SupplyQ(price)

        p1 = self.coords_to_point(0, price)
        p2 = self.coords_to_point(quantity, price)
        p3 = self.coords_to_point(quantity, 0)
                
        horzLine = DashedVMobject(Line(p1,p2, color=self.pq_color))
        priceDesc = TextMobject("$p=$"+str(price)).scale(0.8)
        priceDesc.add_updater(lambda d: d.next_to(horzLine, LEFT))
        
        point = Dot(p2, color=self.pq_color)
        
        vertLine = DashedVMobject(Line(p2,p3, color=self.pq_color))
        quantityDesc = TextMobject("$q=$"+str(quantity)).scale(0.8)
        quantityDesc.add_updater(lambda d: d.next_to(vertLine, DOWN))
        
        self.play(ShowCreation(SupplyCurve))
        self.wait(1)
        self.play(ShowCreation(horzLine))
        self.add(point)
        self.play(ShowCreation(vertLine))
        
        self.horzLine = horzLine
        self.priceDesc = priceDesc
        self.point = point
        self.vertLine = vertLine
        self.quantityDesc = quantityDesc
    
    
    def update_quantity_supplied(self,newPrice):
        newQuantity = self.SupplyQ(newPrice)
        
        newp1 = self.coords_to_point(0, newPrice)
        newp2 = self.coords_to_point(newQuantity, newPrice)
        newp3 = self.coords_to_point(newQuantity, 0)
        
        newHorzLine = DashedVMobject(Line(newp1,newp2, color=self.pq_color))
        newPriceDesc = TextMobject("$p=$"+str(newPrice)).scale(0.8)
        newPriceDesc.add_updater(lambda d: d.next_to(newHorzLine, LEFT))
        
        newPoint = Dot(newp2, color=self.pq_color)
        
        newVertLine = DashedVMobject(Line(newp2,newp3, color=self.pq_color))
        newQuantityDesc = TextMobject("$q_s=$"+str(newQuantity)).scale(0.8)
        newQuantityDesc.add_updater(lambda d: d.next_to(newVertLine, DOWN))
        
        self.play(Transform(self.horzLine,newHorzLine),
                  Transform(self.point,newPoint),
                  Transform(self.vertLine,newVertLine),
                  Transform(self.priceDesc,newPriceDesc),
                  Transform(self.quantityDesc,newQuantityDesc))
    
    
    def create_ps_line(self,wts,price):
        quantity = self.SupplyQ(wts)
        
        x1 = self.coords_to_point(quantity, 0)
        x2 = self.coords_to_point(quantity, wts)
        x3 = self.coords_to_point(quantity, price)
        
        expLine = Line(x1,x2, color=GREEN)
        expLineBase = Line(x1,x2, color=GREEN)
        
        psLine = Line(x2,x3, color=self.ps_color)
        psLineBase = Line(x2,x3, color=self.ps_color)
        
        self.play(ShowCreation(expLine), ShowCreation(expLineBase))
        self.wait(1)
        
        self.play(ShowCreation(psLine),ShowCreation(psLineBase))
        self.wait(1)
        
        dx1 = self.coords_to_point(115, 8)
        dx2 = self.coords_to_point(115, 10)
        psLineDesc = Line(dx1,dx2, color=self.ps_color)
        psLabel = TextMobject("PS")
        psLabel.next_to(psLineDesc, RIGHT)
        self.play(Transform(psLine, psLineDesc))
        self.add(psLabel)
        
        self.wait(1)
        
        dx3 = self.coords_to_point(115, 5)
        dx4 = self.coords_to_point(115, 7)
        expLineDesc = Line(dx3,dx4, color=GREEN)
        expLabel = TextMobject("Cost")
        expLabel.next_to(expLineDesc, RIGHT)
        self.play(Transform(expLine, expLineDesc))
        self.add(expLabel)
        
        self.play(FadeOut(expLineBase), FadeOut(psLineBase))
        
        self.expLine = expLine
        self.expLineBase = expLineBase
        self.expLineDesc = expLineDesc
        self.expLabel = expLabel
        self.psLine = psLine
        self.psLineBase = psLineBase
        self.psLineDesc = psLineDesc
        self.psLabel = psLabel
        
    
    def quantity_supplied_bar(self, price):
        quantity = self.SupplyQ(price)
        
        qL = self.coords_to_point(0, -2)
        qU = self.coords_to_point(quantity, -2)
        
        quantityExchanged = Line(qL,qU, color=BLUE)
        quantityExchLabel = TextMobject("Quantity Supplied")
        quantityExchLabel.add_updater(lambda d: d.next_to(quantityExchanged,DOWN))

        self.play(ShowCreation(quantityExchanged))
        self.add(quantityExchLabel)
        
        self.quantityExchanged = quantityExchanged
        self.quantityExchLabel = quantityExchLabel
        
        
    def show_ps(self, price):
        epsilon = 0.1
        wts = self.SupplyP(epsilon)
        quantity = self.SupplyQ(price)
        
        x1 = self.coords_to_point(epsilon, 0)
        x2 = self.coords_to_point(epsilon, wts-0.1)
        x3 = self.coords_to_point(epsilon, wts+0.1)
        x4 = self.coords_to_point(epsilon, price-0.1)

        exp = Line(x1,x2, color=GREEN)
        expLineLabel = Line(x1,x2, color=GREEN)
        ps = Line(x3,x4, color=self.ps_color)
        psLineLabel = Line(x3,x4, color=self.ps_color)
        
        self.play(ShowCreation(exp))        
        self.play(ShowCreation(ps))
        self.exp = exp
        self.expLineLabel = expLineLabel
        self.ps = ps
        self.psLineLabel = psLineLabel
        self.wait(1)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, 2)
        c = self.coords_to_point(quantity, price)
        NewPs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        self.play(Transform(self.ps,NewPs))
        self.wait(1)
        
        a = self.coords_to_point(0, 2)
        b = self.coords_to_point(quantity, price)
        c = self.coords_to_point(quantity, 0)
        d = self.coords_to_point(0, 0)
        NewExp = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = GREEN, color=GREEN)
        self.play(Transform(self.exp,NewExp))

    
    def find_ps_area(self, price):
        quantity = self.SupplyQ(price)

        dx1 = self.coords_to_point(80, 8)
        dx2 = self.coords_to_point(80, 10)
        psLineDesc = Line(dx1,dx2, color=self.ps_color)
        psLabel = TextMobject("PS")
        psLabel.next_to(psLineDesc)
        self.play(Transform(self.psLine, psLineDesc), Transform(self.psLabel,psLabel))
        
        psAreaEquation = TextMobject("$ = \\frac{1}{2} \\times h \\times b $")
        psAreaEquation.next_to(self.psLabel, RIGHT)
        psAreaEquation.set_color(self.ps_color)
        self.play(ReplacementTransform(self.psLineLabel,psAreaEquation))
        self.wait(1)
        
        psAreaValue = TextMobject("$ = \\frac{1}{2} \ \\times $ "+str(price-2)+" $ \\times $ "+str(quantity))
        psAreaValue.next_to(self.psLabel,RIGHT)
        psAreaValue.set_color(self.ps_color)
        self.play(Transform(psAreaEquation,psAreaValue))
        self.wait(1)
        
        psAreaNumber = TextMobject(str(int((price-2)*quantity/2)))
        psAreaNumber.move_to(self.coords_to_point(quantity/4, 3*(2 + price)/5), LEFT)
        psAreaNumber.set_color(self.ps_color)
        self.play(FadeIn(psAreaNumber))
        self.wait(1)
        
        dx3 = self.coords_to_point(80, 5)
        dx4 = self.coords_to_point(80, 7)
        expLineDesc = Line(dx3,dx4, color=GREEN)
        expLabel = TextMobject("Cost")
        expLabel.next_to(expLineDesc)
        self.play(Transform(self.expLine, expLineDesc), Transform(self.expLabel,expLabel))
        
        expAreaEquation = TextMobject("$ = \\frac{1}{2} \\times (h_1 + h_2) \\times b $")
        expAreaEquation.next_to(self.expLabel, RIGHT)
        expAreaEquation.set_color(GREEN)
        self.play(ReplacementTransform(self.expLineLabel,expAreaEquation))
        self.wait(1)
        
        expAreaValue = TextMobject("$ = \\frac{1}{2} \\times (2$ "+" + "+str(int(price))+')'+" $ \\times $ "+' '+str(quantity))
        expAreaValue.next_to(self.expLabel,RIGHT)
        expAreaValue.set_color(GREEN)
        self.play(Transform(expAreaEquation,expAreaValue))
        self.wait(1)
        
        expAreaNumber = TextMobject(str(int((price+2)*quantity/2)))
        expAreaNumber.move_to(self.coords_to_point(quantity/2, 2), LEFT)
        expAreaNumber.set_color(GREEN)
        self.play(FadeIn(expAreaNumber))
        self.wait(1)
        
        self.psAreaEquation = psAreaEquation
        self.psAreaNumber = psAreaNumber
        self.expAreaEquation = expAreaEquation
        self.expAreaNumber = expAreaNumber
        

    def update_ps_area(self, price):
        quantity = self.SupplyQ(price)
        
        newp1 = self.coords_to_point(0, price)
        newp2 = self.coords_to_point(quantity, price)
        newp3 = self.coords_to_point(quantity, 0)
        
        newHorzLine = DashedVMobject(Line(newp1,newp2, color=self.pq_color))
        newPriceDesc = TextMobject("$p=$"+str(price)).scale(0.8)
        newPriceDesc.next_to(newHorzLine, LEFT)
        
        newPoint = Dot(newp2, color=self.pq_color)
        
        newVertLine = DashedVMobject(Line(newp2,newp3, color=self.pq_color))
        newQuantityDesc = TextMobject("$q_s=$"+str(quantity)).scale(0.8)
        newQuantityDesc.next_to(newVertLine, DOWN)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, 2)
        c = self.coords_to_point(quantity, price)
        NewPs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = self.ps_color, color=self.ps_color)
        
        NewPsAreaEquation = TextMobject("$ = \\frac{1}{2} \ \\times $ "+str(price-2)+" $ \\times $ "+str(quantity))
        NewPsAreaEquation.next_to(self.psLabel,RIGHT)
        NewPsAreaEquation.set_color(self.ps_color)
        
        NewPsAreaNumber = TextMobject(str(int((price-2)*quantity/2)))
        NewPsAreaNumber.move_to(self.coords_to_point(quantity/4, 3*(2 + price)/5), LEFT)
        NewPsAreaNumber.set_color(self.ps_color)
        
        a = self.coords_to_point(0, 2)
        b = self.coords_to_point(quantity, price)
        c = self.coords_to_point(quantity, 0)
        d = self.coords_to_point(0, 0)
        NewExp = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = GREEN, color=GREEN)
        
        NewQL = self.coords_to_point(0, -2)
        NewQU = self.coords_to_point(quantity, -2)
        NewQuantityExchanged = Line(NewQL,NewQU, color=BLUE)
        
        NewExpAreaEquation = TextMobject("$ = \\frac{1}{2} \\times (2$ "+" + "+str(int(price))+')'+" $ \\times $ "+' '+str(quantity))
        NewExpAreaEquation.next_to(self.expLabel,RIGHT)
        NewExpAreaEquation.set_color(GREEN)
        
        NewExpAreaNumber = TextMobject(str(int((price+2)*quantity/2)))
        NewExpAreaNumber.move_to(self.coords_to_point(quantity/2, 2), LEFT)
        NewExpAreaNumber.set_color(GREEN)
        
        self.play(Transform(self.horzLine,newHorzLine),
                  Transform(self.point,newPoint),
                  Transform(self.vertLine,newVertLine),
                  Transform(self.priceDesc,newPriceDesc),
                  Transform(self.quantityDesc,newQuantityDesc),
                  Transform(self.ps,NewPs),
                  Transform(self.exp,NewExp),
                  Transform(self.quantityExchanged,NewQuantityExchanged),
                  Transform(self.psAreaEquation,NewPsAreaEquation),
                  Transform(self.psAreaNumber,NewPsAreaNumber),
                  Transform(self.expAreaEquation,NewExpAreaEquation),
                  Transform(self.expAreaNumber,NewExpAreaNumber))
    
    
    def summary(self):
        self.play(FadeOut(self.psLine),
                  FadeOut(self.psLabel),
                  FadeOut(self.psAreaEquation),
                  FadeOut(self.psAreaNumber),
                  FadeOut(self.expLine),
                  FadeOut(self.expLabel),
                  FadeOut(self.expAreaEquation),
                  FadeOut(self.expAreaNumber),
                  FadeOut(self.exp),
                  FadeOut(self.quantityExchanged),
                  FadeOut(self.quantityExchLabel))
        
        summary = TextMobject("PS is represented by the area")
        summary.move_to(self.coords_to_point(65, 10), LEFT)
        self.play(FadeIn(summary))
        summary1 = TextMobject("  1) Below the price")
        summary1.move_to(self.coords_to_point(70, 8), LEFT)
        self.play(FadeIn(summary1))
        summary2 = TextMobject("  2) Above the supply curve")
        summary2.move_to(self.coords_to_point(70, 6.5), LEFT)
        self.play(FadeIn(summary2))
        summary3 = TextMobject("  3) Inside quantity")
        summary3.move_to(self.coords_to_point(70, 5), LEFT)
        self.play(FadeIn(summary3))
        self.wait(3)
        reading = TextMobject("See Mankiw Ch. 7 for more info")
        reading.move_to(self.coords_to_point(65, 10), LEFT)
        self.play(FadeOut(summary),FadeOut(summary1),FadeOut(summary2),FadeOut(summary3),FadeIn(reading))


class ConsumerSurplus(GraphScene):
    CONFIG = configuration

    def construct(self):
        self.intro_sequence()
        self.wait(3)
        self.create_quantity_demanded(5)
        self.wait(3)
        self.update_quantity_demanded(6)
        self.wait(3)
        self.update_quantity_demanded(5)
        self.wait(3)
        self.create_cs_line(8,5)
        self.wait(3)
        self.quantity_bought(5)
        self.wait(3)
        self.show_cs(5)
        self.wait(3)
        self.find_cs_area(5)
        self.wait(3)
        self.update_cs_area(6)
        self.wait(3)
        self.update_cs_area(3)
        self.wait(3)
        self.summary()
        
    def DemandQ(self, price):
        return 100 - 10*price
    
    def DemandP(self,quantity):
        return (10 - quantity/10)
                
    def intro_sequence(self):
        title = TextMobject("Tutorial 3.1 | Consumer Surplus").scale(1.5)
        self.play(FadeIn(title))
        self.wait(1)
        transform_title = TextMobject("Tutorial 3.1 | Consumer Surplus").scale(1.2)
        transform_title.to_corner(UP)
        self.play(
            Transform(title, transform_title))
        self.wait(3)
        self.setup_axes(animate=True)
    
    
    def create_quantity_demanded(self,price):
        DemandCurve = self.get_graph(self.DemandP, self.demand_color, x_min=0, x_max=100)
        quantity = self.DemandQ(price)

        p1 = self.coords_to_point(0, price)
        p2 = self.coords_to_point(quantity, price)
        p3 = self.coords_to_point(quantity, 0)
                
        horzLine = DashedVMobject(Line(p1,p2, color=self.pq_color))
        priceDesc = TextMobject("$p=$"+str(price)).scale(0.8)
        priceDesc.add_updater(lambda d: d.next_to(horzLine, LEFT))
        
        point = Dot(p2, color=self.pq_color)
        
        vertLine = DashedVMobject(Line(p2,p3, color=self.pq_color))
        quantityDesc = TextMobject("$q=$"+str(quantity)).scale(0.8)
        quantityDesc.add_updater(lambda d: d.next_to(vertLine, DOWN))
        
        self.play(ShowCreation(DemandCurve))
        self.wait(1)
        self.play(ShowCreation(horzLine))
        self.add(point)
        self.play(ShowCreation(vertLine))
        
        self.horzLine = horzLine
        self.priceDesc = priceDesc
        self.point = point
        self.vertLine = vertLine
        self.quantityDesc = quantityDesc
    
    
    def update_quantity_demanded(self,newPrice):
        newQuantity = self.DemandQ(newPrice)
        
        newp1 = self.coords_to_point(0, newPrice)
        newp2 = self.coords_to_point(newQuantity, newPrice)
        newp3 = self.coords_to_point(newQuantity, 0)
        
        newHorzLine = DashedVMobject(Line(newp1,newp2, color=self.pq_color))
        newPriceDesc = TextMobject("$p=$"+str(newPrice)).scale(0.8)
        newPriceDesc.add_updater(lambda d: d.next_to(newHorzLine, LEFT))
        
        newPoint = Dot(newp2, color=self.pq_color)
        
        newVertLine = DashedVMobject(Line(newp2,newp3, color=self.pq_color))
        newQuantityDesc = TextMobject("$q_d=$"+str(newQuantity)).scale(0.8)
        newQuantityDesc.add_updater(lambda d: d.next_to(newVertLine, DOWN))
        
        self.play(Transform(self.horzLine,newHorzLine),
                  Transform(self.point,newPoint),
                  Transform(self.vertLine,newVertLine),
                  Transform(self.priceDesc,newPriceDesc),
                  Transform(self.quantityDesc,newQuantityDesc))
    
    
    def create_cs_line(self,wtp,price):
        quantity = self.DemandQ(wtp)
        
        x1 = self.coords_to_point(quantity, 0)
        x2 = self.coords_to_point(quantity, price)
        x3 = self.coords_to_point(quantity, wtp)
        
        expLine = Line(x1,x2, color=GREEN)
        expLineBase = Line(x1,x2, color=GREEN)
        
        csLine = Line(x2,x3, color=PINK)
        csLineBase = Line(x2,x3, color=PINK)
        
        self.play(ShowCreation(expLine), ShowCreation(expLineBase))
        self.wait(1)
        
        self.play(ShowCreation(csLine),ShowCreation(csLineBase))
        self.wait(1)
        
        dx1 = self.coords_to_point(115, 8)
        dx2 = self.coords_to_point(115, 10)
        csLineDesc = Line(dx1,dx2, color=PINK)
        csLabel = TextMobject("CS")
        csLabel.next_to(csLineDesc, RIGHT)
        self.play(Transform(csLine, csLineDesc))
        self.add(csLabel)
        
        self.wait(1)
        
        dx3 = self.coords_to_point(115, 5)
        dx4 = self.coords_to_point(115, 7)
        expLineDesc = Line(dx3,dx4, color=GREEN)
        expLabel = TextMobject("Expenditure")
        expLabel.next_to(expLineDesc, RIGHT)
        self.play(Transform(expLine, expLineDesc))
        self.add(expLabel)
        
        self.play(FadeOut(expLineBase), FadeOut(csLineBase))
        
        self.expLine = expLine
        self.expLineBase = expLineBase
        self.expLineDesc = expLineDesc
        self.expLabel = expLabel
        self.csLine = csLine
        self.csLineBase = csLineBase
        self.csLineDesc = csLineDesc
        self.csLabel = csLabel
        
    
    def quantity_bought(self, price):
        quantity = self.DemandQ(price)
        
        qL = self.coords_to_point(0, -2)
        qU = self.coords_to_point(quantity, -2)
        
        quantityExchanged = Line(qL,qU, color=BLUE)
        quantityExchLabel = TextMobject("Quantity Demanded")
        quantityExchLabel.add_updater(lambda d: d.next_to(quantityExchanged,DOWN))

        self.play(ShowCreation(quantityExchanged))
        self.add(quantityExchLabel)
        
        self.quantityExchanged = quantityExchanged
        self.quantityExchLabel = quantityExchLabel
        
        
    def show_cs(self, price):
        epsilon = 0.1
        wtp = self.DemandP(epsilon)
        quantity = self.DemandQ(price)
        
        x1 = self.coords_to_point(epsilon, 0)
        x2 = self.coords_to_point(epsilon, price-0.1)
        x3 = self.coords_to_point(epsilon, price+0.1)
        x4 = self.coords_to_point(epsilon, wtp-0.1)

        exp = Line(x1,x2, color=GREEN)
        expLineLabel = Line(x1,x2, color=GREEN)
        cs = Line(x3,x4, color=PINK)
        csLineLabel = Line(x3,x4, color=PINK)
        
        self.play(ShowCreation(exp))        
        self.play(ShowCreation(cs))
        self.exp = exp
        self.expLineLabel = expLineLabel
        self.cs = cs
        self.csLineLabel = csLineLabel
        self.wait(1)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, 10)
        c = self.coords_to_point(quantity, price)
        NewCs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = PINK, color=PINK)
        self.play(Transform(self.cs,NewCs))
        self.wait(1)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(quantity, price)
        c = self.coords_to_point(quantity, 0)
        d = self.coords_to_point(0, 0)
        NewExp = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = GREEN, color=GREEN)
        self.play(Transform(self.exp,NewExp))

    
    def find_cs_area(self, price):
        quantity = self.DemandQ(price)

        dx1 = self.coords_to_point(70, 8)
        dx2 = self.coords_to_point(70, 10)
        csLineDesc = Line(dx1,dx2, color=PINK)
        csLabel = TextMobject("CS")
        csLabel.next_to(csLineDesc)
        self.play(Transform(self.csLine, csLineDesc), Transform(self.csLabel,csLabel))
        
        csAreaEquation = TextMobject("$ = \\frac{1}{2} \\times h \\times b $")
        csAreaEquation.next_to(self.csLabel, RIGHT)
        csAreaEquation.set_color(PINK)
        self.play(ReplacementTransform(self.csLineLabel,csAreaEquation))
        self.wait(1)
        
        csAreaValue = TextMobject("$ = \\frac{1}{2} \\times $"+str(10 - price)+" $ \\times $"+str(quantity))
        csAreaValue.next_to(self.csLabel,RIGHT)
        csAreaValue.set_color(PINK)
        self.play(Transform(csAreaEquation,csAreaValue))
        self.wait(1)
        
        csAreaNumber = TextMobject(str(int(price*quantity/2)))
        csAreaNumber.move_to(self.coords_to_point(3, (10 + price)/2), LEFT)
        csAreaNumber.set_color(PINK)
        self.play(FadeIn(csAreaNumber))
        self.wait(1)
        
        dx3 = self.coords_to_point(70, 5)
        dx4 = self.coords_to_point(70, 7)
        expLineDesc = Line(dx3,dx4, color=GREEN)
        expLabel = TextMobject("Expenditure")
        expLabel.next_to(expLineDesc)
        self.play(Transform(self.expLine, expLineDesc), Transform(self.expLabel,expLabel))
        
        expAreaEquation = TextMobject("$ = h \\times b $")
        expAreaEquation.next_to(self.expLabel, RIGHT)
        expAreaEquation.set_color(GREEN)
        self.play(ReplacementTransform(self.expLineLabel,expAreaEquation))
        self.wait(1)
        
        expAreaValue = TextMobject("$ = $ "+str(price)+"$ \\times $"+str(quantity))
        expAreaValue.next_to(self.expLabel,RIGHT)
        expAreaValue.set_color(GREEN)
        self.play(Transform(expAreaEquation,expAreaValue))
        self.wait(1)
        
        expAreaNumber = TextMobject(str(int(price*quantity)))
        expAreaNumber.move_to(self.coords_to_point(3, price/2), LEFT)
        expAreaNumber.set_color(GREEN)
        self.play(FadeIn(expAreaNumber))
        self.wait(1)
        
        self.csAreaEquation = csAreaEquation
        self.csAreaNumber = csAreaNumber
        self.expAreaEquation = expAreaEquation
        self.expAreaNumber = expAreaNumber
        

    def update_cs_area(self, price):
        quantity = self.DemandQ(price)
        
        newp1 = self.coords_to_point(0, price)
        newp2 = self.coords_to_point(quantity, price)
        newp3 = self.coords_to_point(quantity, 0)
        
        newHorzLine = DashedVMobject(Line(newp1,newp2, color=self.pq_color))
        newPriceDesc = TextMobject("$p=$"+str(price)).scale(0.8)
        #newPriceDesc.add_updater(lambda d: d.next_to(newHorzLine, LEFT))
        newPriceDesc.next_to(newHorzLine, LEFT)
        
        newPoint = Dot(newp2, color=self.pq_color)
        
        newVertLine = DashedVMobject(Line(newp2,newp3, color=self.pq_color))
        newQuantityDesc = TextMobject("$q_d=$"+str(quantity)).scale(0.8)
        #newQuantityDesc.add_updater(lambda d: d.next_to(newVertLine, DOWN))
        newQuantityDesc.next_to(newVertLine, DOWN)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, 10)
        c = self.coords_to_point(quantity, price)
        NewCs = Polygon(a,b,c, fill_opacity = 0.2, fill_color = PINK, color=PINK)
        
        NewCsAreaEquation = TextMobject("$ = \\frac{1}{2} \\times $"+str(10 - price)+" $ \\times $"+str(quantity))
        NewCsAreaEquation.next_to(self.csLabel,RIGHT)
        NewCsAreaEquation.set_color(PINK)
        
        NewCsAreaNumber = TextMobject(str(int((10-price)*quantity/2)))
        NewCsAreaNumber.move_to(self.coords_to_point(3, (10 + price)/2), LEFT)
        NewCsAreaNumber.set_color(PINK)
        
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(quantity, price)
        c = self.coords_to_point(quantity, 0)
        d = self.coords_to_point(0, 0)
        NewExp = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = GREEN, color=GREEN)
        
        NewQL = self.coords_to_point(0, -2)
        NewQU = self.coords_to_point(quantity, -2)
        NewQuantityExchanged = Line(NewQL,NewQU, color=BLUE)
        
        NewExpAreaEquation = TextMobject("$ = $ "+str(price)+"$ \\times $"+str(quantity))
        NewExpAreaEquation.next_to(self.expLabel,RIGHT)
        NewExpAreaEquation.set_color(GREEN)
        
        NewExpAreaNumber = TextMobject(str(int(price*quantity)))
        NewExpAreaNumber.move_to(self.coords_to_point(3, price/2), LEFT)
        NewExpAreaNumber.set_color(GREEN)
        
        self.play(Transform(self.horzLine,newHorzLine),
                  Transform(self.point,newPoint),
                  Transform(self.vertLine,newVertLine),
                  Transform(self.priceDesc,newPriceDesc),
                  Transform(self.quantityDesc,newQuantityDesc),
                  Transform(self.cs,NewCs),
                  Transform(self.exp,NewExp),
                  Transform(self.quantityExchanged,NewQuantityExchanged),
                  Transform(self.csAreaEquation,NewCsAreaEquation),
                  Transform(self.csAreaNumber,NewCsAreaNumber),
                  Transform(self.expAreaEquation,NewExpAreaEquation),
                  Transform(self.expAreaNumber,NewExpAreaNumber))
        
    def summary(self):
        self.play(FadeOut(self.csLine),
                  FadeOut(self.csLabel),
                  FadeOut(self.csAreaEquation),
                  FadeOut(self.csAreaNumber),
                  FadeOut(self.expLine),
                  FadeOut(self.expLabel),
                  FadeOut(self.expAreaEquation),
                  FadeOut(self.expAreaNumber),
                  FadeOut(self.exp),
                  FadeOut(self.quantityExchanged),
                  FadeOut(self.quantityExchLabel))
        
        summary = TextMobject("CS is represented by the area")
        summary.move_to(self.coords_to_point(65, 10), LEFT)
        self.play(FadeIn(summary))
        summary1 = TextMobject("  1) Below the demand curve")
        summary1.move_to(self.coords_to_point(70, 8), LEFT)
        self.play(FadeIn(summary1))
        summary2 = TextMobject("  2) Above the price")
        summary2.move_to(self.coords_to_point(70, 6.5), LEFT)
        self.play(FadeIn(summary2))
        summary3 = TextMobject("  3) Inside quantity")
        summary3.move_to(self.coords_to_point(70, 5), LEFT)
        self.play(FadeIn(summary3))
        
        reading = TextMobject("See Mankiw Ch. 7 for more info")
        reading.move_to(self.coords_to_point(65, 10), LEFT)
        self.play(FadeOut(summary),FadeOut(summary1),FadeOut(summary2),FadeOut(summary3),FadeIn(reading))
