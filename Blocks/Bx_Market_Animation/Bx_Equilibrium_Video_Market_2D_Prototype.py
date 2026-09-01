# maniml 03_Code.py animation_1

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

PIXEL_HEIGHT = 1080*2
FPS = 10
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT*2
config.frame_rate = FPS

class animation_1(Scene):

    def construct(self):
        
    """ Parameters """
        
        number_of_buyers = 5
        number_of_sellers = 1
        market_size = max(number_of_buyers, number_of_sellers)
        agent_width = 1/2
        move = 0.2
        margin = 0.05
        
    """ Setup """
        
        buyers_name = Tex('Buyers').set_color(BLUE).to_edge(DOWN)
        sellers_name = Tex('Sellers').set_color(YELLOW).to_edge(UP)
        center_line = NumberLine(
            x_range=[0, 10, 10],
            length=10,
            color=GREY,
            include_numbers=False,
            label_direction=UP,
        )
        grid = NumberPlane()
        
        def BUYER(reservation, location):
            l = location
            r = reservation
            w = agent_width - margin
            box = Polygon(grid.c2p(l-w,0), grid.c2p(l-w,-r), grid.c2p(l+w,-r), grid.c2p(l+w,0)).set_color(BLUE)
            #bid = Line(grid.c2p(l-w-margin*2,0), grid.c2p(l+w+margin*2,0)).set_color(RED)
            cs = Line(grid.c2p(l-w,-r), grid.c2p(l+w,-r)).set_color(BLUE)
            
            return VGroup(box, cs)
                    
        def SELLER(reservation, location, surplus):
    """ These really should be classes. """
            
            l = location
            r = reservation
            w = agent_width - margin
            s = surplus
            
            a = grid.c2p(l-w,0)
            b = grid.c2p(l-w,r)
            c = grid.c2p(l+w,r)
            d = grid.c2p(l+w,0)
            e = grid.c2p(l-w-margin*2,r+s)
            f = grid.c2p(l+w+margin*2,r+s)
            g = grid.c2p(l-w,s)
            h = grid.c2p(l+w,s)
            
            box = Polygon(a, b, c, d).set_color(YELLOW)
            area = Polygon(g, e, f, h, fill_color=YELLOW, fill_opacity=1).set_color(YELLOW)
            ps = Line(g, h).set_color(YELLOW)

            ask = Line(e, f).set_color(RED)
            ask.z_index = 2

            return ['SELLER', VGroup(box, ps, ask)]#area, 
        
    """ Agents """
        
        buyer1 = BUYER(2,0)                
        s1, seller1 = SELLER(1,1,1)
        
        self.add(center_line, buyer1, seller1, buyers_name, sellers_name)
        
    """ Set Price """
        # turn this into a function and iterate over agents
        
        ask = round(seller1[-1].get_top()[1], 2)
        buyer_price = round(buyer1.get_top()[1], 2)
        seller_price = round(seller1[0].get_top()[1], 2)
        
        while buyer_price != seller_price:
            
            ask = round(seller1[-1].get_top()[1], 2)
            seller_price = round(seller1[0].get_top()[1], 2)
            
            if seller_price + move <= ask:
                self.play(seller1[-1].animate.shift(DOWN*move))
                
            
            ask = round(seller1[-1].get_top()[1], 2)
            buyer_price = round(buyer1.get_top()[1], 2)
            
            if ask > buyer_price + 0.1:
                if buyer1.get_bottom()[1] + move < 0:
                    self.play(buyer1.animate.shift(UP*move))
                    
            ask = round(seller1[-1].get_top()[1], 2)
            buyer_price = round(buyer1.get_top()[1], 2)
            seller_price = round(seller1[0].get_top()[1], 2)
            
            if buyer_price == seller_price:
                self.play(seller1.animate.shift(LEFT))
        self.wait()
        
    """ Make Price """

        price = seller1[-1].copy()
        top = price.get_top()[1]
        new_price = Line(grid.c2p(-7.1,top), grid.c2p(-7,top)).set_color(RED)
        self.play(Transform(price, new_price))
        self.wait()
        
    """ Make CS """
        
        buyer_location = 0 
        
        cs_base = Line(grid.c2p(7,0), grid.c2p(7.1,0)).set_color(GREY)
        cs_base.z_index = -1
        #self.play(FadeIn(cs_base))

        cs_list = []
        
        for i in [1,2,3]:
        
            cs = buyer1[1].copy()
            cs_top = cs_base.copy().move_to(grid.c2p(0,0))
            top = cs.get_top()[1]
            new_cs = Line(grid.c2p(7,top), grid.c2p(7.1,top)).set_color(BLUE)
            
            self.play(Transform(cs, new_cs), cs_top.animate.move_to(cs_base),*[c.animate.shift(UP*top) for c in cs_list])
            
            cs_list = [cs, cs_top] + cs_list
            
        
    """ Round 1 Structure """
        
        def Move(agent, agents):
            data = agent[1]
            if agent[0] == 'SELLER':
                return agent[1][-1].animate.shift(DOWN)
            
            if agent[0] == 'BUYER':
                return agent[1][-1].animate.shift(UP)
            
        # for a in agents:
        #     if I don't have a deal:
        #         if for a new deal:
        #             take it, move price to the edge
        #         if not:
        #             lower surplus
        #     if I have a deal:
        #         if there's no better open deal:
        #             do nothing
        #         if there's a better deal:
        #             raise surplus
        #             take the better deal
        
        self.play(Move([s1, seller1], []))


""" Parameters """

number_of_buyers = 5
number_of_sellers = 1
market_size = max(number_of_buyers, number_of_sellers)
agent_width = 1/2
move = 0.2
margin = 0.05

    """ Agents """

class SELLER:
    def __init__(self, grid, location, reservation, ask):
        
        self.type = 'SELLER'
        self.grid = grid
        
        self.l = location # horizontal location on the line
        self.w = agent_width - margin # how wide the seller looks in horizontal space

        self.a = ask # how much the seller asks for
        self.r = reservation # the sellers cost
        self.s = ask - reservation # how much surplus value the seller starts asking for
        
        a = grid.c2p(self.l - self.w, 0)
        b = grid.c2p(self.l + self.w, 0)
        
        c = grid.c2p(self.l - self.w, self.s)
        d = grid.c2p(self.l + self.w, self.s)

        e = grid.c2p(self.l - self.w, self.a)
        f = grid.c2p(self.l + self.w, self.a)
        
        self.box = Polygon(c, e, f, d).set_color(YELLOW)
        
        g = grid.c2p(self.l - self.w - margin*2, self.a)
        h = grid.c2p(self.l + self.w + margin*2, self.a)
        
        self.area = Polygon(a, c, d, b).set_fill(YELLOW).set_opacity(1).set_color(YELLOW)

        self.ask = Line(g, h).set_color(RED)
        self.ask.z_index = 2
        
        self.group = VGroup(self.area, self.box, self.ask)

    def Add(self):
        return FadeIn(self.group)
    
    def Reprice(self):
    """ If there's no deal, lower price. If there's a deal, raise price. """
        
        self.a = self.a - move
        self.s = self.a - self.r
        
        a = grid.c2p(self.l - self.w, 0)
        b = grid.c2p(self.l + self.w, 0)
        
        c = grid.c2p(self.l - self.w, self.s)
        d = grid.c2p(self.l + self.w, self.s)

        e = grid.c2p(self.l - self.w, self.a)
        f = grid.c2p(self.l + self.w, self.a)
        
        self.box = Polygon(c, e, f, d).set_color(YELLOW)
        
        g = grid.c2p(self.l - self.w - margin*2, self.a)
        h = grid.c2p(self.l + self.w + margin*2, self.a)
        
        self.area = Polygon(a, c, d, b).set_fill(YELLOW).set_opacity(1).set_color(YELLOW)

        self.ask = Line(g, h).set_color(RED)
        self.ask.z_index = 2
        
        new_group = VGroup(self.area, self.box, self.ask)
        
        return Transform(self.group, new_group)
    
    def PS(self):
    """ Return the coordinates for PS. """
        
        location = self.l
        top = self.s
        
        return [location, top]
    
    def Price(self):
    """ Return the coordinates for the Price. """
        
        location = self.l
        ask = self.a
        
        return [location, ask]

class BUYER:
    def __init__(self, grid, location, reservation, offer):
        
        self.type = 'BUYER'
        self.grid = grid
        
        self.l = location # horizontal location on the line
        self.w = agent_width - margin # how wide the buyer looks in horizontal space

        self.o = offer # how much the buyer is offering
        self.r = - reservation # their break even price
        self.s = self.o + self.r # surplus value
        
        a = grid.c2p(self.l - self.w, self.s)
        b = grid.c2p(self.l - self.w, self.o)
        c = grid.c2p(self.l + self.w, self.o)
        d = grid.c2p(self.l + self.w, self.s)
        
        self.box = Polygon(a, b, c, d).set_color(BLUE)
        
        e = grid.c2p(self.l - self.w, 0)
        f = grid.c2p(self.l + self.w, 0)
                
        self.area = Polygon(a, d, f, e).set_fill(BLUE).set_opacity(1).set_color(BLUE)
        
        self.group = VGroup(self.box, self.area)

    def Add(self):
        return FadeIn(self.group)
    
    def Reprice(self):
    """ If there's no deal, raise price. If there's a deal, lower price and break deal. """
        
        self.o = self.o + move
        self.s = self.o + self.r
        
        a = grid.c2p(self.l - self.w, self.s)
        b = grid.c2p(self.l - self.w, self.o)
        c = grid.c2p(self.l + self.w, self.o)
        d = grid.c2p(self.l + self.w, self.s)
        
        self.box = Polygon(a, b, c, d).set_color(BLUE)
        
        e = grid.c2p(self.l - self.w, 0)
        f = grid.c2p(self.l + self.w, 0)
        
        self.area = Polygon(a, d, f, e).set_fill(BLUE).set_opacity(1).set_color(BLUE)

        new_group = VGroup(self.box, self.area)
        
        return Transform(self.group, new_group)
    
    def CS(self):
    """ Return the coordinates for CS. """
        
        location = self.l
        bottom = self.s
        
        return [location, bottom]
    
    def Accept(self):
    """ Accept the seller's offer. """
        
        new_location = 0 # still need to find this
        
        self.l = new_location # horizontal location on the line
        
        a = grid.c2p(self.l - self.w, self.s)
        b = grid.c2p(self.l - self.w, self.o)
        c = grid.c2p(self.l + self.w, self.o)
        d = grid.c2p(self.l + self.w, self.s)
        
        self.box = Polygon(a, b, c, d).set_color(BLUE)
        
        e = grid.c2p(self.l - self.w, 0)
        f = grid.c2p(self.l + self.w, 0)
                
        self.area = Polygon(a, d, f, e).set_fill(BLUE).set_opacity(1).set_color(BLUE)

        new_group = VGroup(self.box, self.area)
        
        return Transform(self.group, new_group)

    """ """

center_line = NumberLine(
    x_range=[0, 10, 10],
    length=10,
    color=GREY,
    include_numbers=False,
    label_direction=UP,
)

grid = NumberPlane()

buyers_name = Tex('Buyers').set_color(BLUE).to_edge(DOWN)
sellers_name = Tex('Sellers').set_color(YELLOW).to_edge(UP)

    """ Run """

class animation_(Scene):
    def construct(self):

    """ Setup """

        s = SELLER(grid,0,1,2)
        b = BUYER(grid,1,3,1)
        
        self.add(center_line, buyers_name, sellers_name)
        
        self.play(s.Add())
        self.play(b.Add())
        
        self.play(s.Reprice())
        self.play(b.Reprice())

        self.play(s.Reprice())
        self.play(b.Reprice())

        self.play(s.Reprice())
        self.play(b.Accept())
        
        def Show_Price(location, price):
            left = location - agent_width - margin*2
            right = location + agent_width + margin*2
            
            line = Line(grid.c2p(left, price), grid.c2p(right, price)).set_color(RED)
            new_line = Line(grid.c2p(-7.1, price), grid.c2p(-7, price)).set_color(RED)
            return [FadeIn(line), Transform(line, new_line)]
        self.play(*Show_Price(*s.Price()))
        
        def Show_CS(location,bottom):
            cs = Line(grid.c2p(location, 0), grid.c2p(location, bottom)).set_color(BLUE)
            new_cs = Line(grid.c2p(7, 0), grid.c2p(7, bottom)).set_color(BLUE)
            return [FadeIn(cs), Transform(cs, new_cs)]
        self.play(*Show_CS(*b.CS()))
        
        def Show_PS(location,top):
            ps = Line(grid.c2p(location, 0), grid.c2p(location, top)).set_color(YELLOW)
            new_ps = Line(grid.c2p(7, 0), grid.c2p(7, top)).set_color(YELLOW)
            return [FadeIn(ps), Transform(ps, new_ps)]
        self.play(*Show_PS(*s.PS()))
        
        self.wait()


class __(Scene):

    """Animation -1 | Last Time..."""

    def construct(self):
        text = Tex('Last Time...').scale(3)
        self.play(FadeIn(text), run_time=1/2)
        self.wait()
        self.play(FadeOut(text), run_time=1/2)
        self.wait()


class animation_0(Scene):

    """Animation 0 | Intro Sequence"""

    def construct(self):
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
        
        # I need a way to center the word. This just takes the length of the word and finds a centering point c.
        # 
        
        shift = 0
        centering = -39
        squares = []
        for l in letters:
            s = [Square(side_length=size, color=config.background_color).move_to(RIGHT*(w + shift*6 + centering)*size + DOWN*h*size) for w,h in [block[i] for i in l]]
            squares = squares + s
            shift = shift + 1
        
        self.add(*squares)
        
        
        opacity_list = np.random.binomial(1, 0.2, len(squares))
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=o) for s,o in zip(squares, opacity_list)]
            self.play(*update_squares, run_time=1/10)
            
            opacity_list = opacity_list + np.random.binomial(1, 0.2, len(squares))
        
        
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]
            self.play(*update_squares, run_time=1/10)
        
        
        opacity_list = np.random.binomial(1, 0.8, len(squares))
        for i in range(15):
            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=o) for s,o in zip(squares, opacity_list)]
            self.play(*update_squares, run_time=1/10)
            
            opacity_list = opacity_list - np.random.binomial(1, 0.2, len(squares))
            
        self.wait()
