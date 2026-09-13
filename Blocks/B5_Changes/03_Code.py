#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Video import *
warnings.filterwarnings('ignore')

""" Paths """
tutorial_path = 'PartB_E4'
if not os.path.exists(tutorial_path):
    os.makedirs(tutorial_path)
config.media_dir = tutorial_path
config.verbosity = 'ERROR'

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


# ## Animation -1 | Last Time...

# In[229]:


get_ipython().run_cell_magic('manim', 'animation_', "\nclass animation_(Scene):\n\n    def construct(self):\n        text = Tex('Last Time...').scale(3)\n        self.play(FadeIn(text), run_time=1/2)\n        self.wait()\n        self.play(FadeOut(text), run_time=1/2)\n        self.wait()\n        \n")


# ## Animation 0 | Intro Sequence

# In[4]:


get_ipython().run_cell_magic('manim', 'animation_', '\nclass animation_(Scene):\n\n    def construct(self):\n        \n        """ Definitions """\n        \n        colors = sns.color_palette("Blues", 50).as_hex()\n\n        size = 1/6\n        n_width = 2\n        n_height = 3\n\n        n_rows = len(range(-n_height,n_height+1))\n        n_cols = len(range(-n_width,n_width+1))\n        w_list = list(range(-n_width,n_width+1))*n_rows\n        h_list = [i for i in range(-n_height,n_height+1) for x in \'a\'*n_cols]\n        block = list(zip(w_list,h_list)) # height: 7, width: 5\n        \n        string = \'MICROECONOMICS\'\n        letters = [raster_font[l] for l in string]\n        \n        """ Run """\n                \n        shift = 0\n        centering = -39\n        squares = []\n        for l in letters:\n            s = [Square(side_length=size, color=config.background_color).move_to(RIGHT*(w + shift*6 + centering)*size + DOWN*h*size) for w,h in [block[i] for i in l]]\n            squares = squares + s\n            shift = shift + 1\n        \n        Squares = VGroup(*squares)\n        \n        self.add(Squares)\n        \n        for i in range(8):\n            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]\n            self.play(*update_squares, run_time=1/10)\n            self.wait(2/10)\n            \n        part_label = Tex(\'{{Part B}} $|$ Episode 4\').set_color(GREY).set_color_by_tex_to_color_map(\n            {"Part B": BLUE,}\n        ).scale(3).next_to(Squares, DOWN*4)\n        group = VGroup(Squares, part_label)\n        self.play(FadeIn(part_label), group.animate.move_to(0))\n        \n        for i in range(8):\n            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]\n            self.play(*update_squares, run_time=1/10)\n            self.wait(2/10)\n')


# In[42]:


""" Axis Pamameters """

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

""" Starting Objects """

title_string = "Where do prices come from?"
title = Tex(title_string).to_edge(UP)

supply_axes = PQ_large.copy().scale(0.6).to_edge(DOWN + LEFT).shift(2.5 * UP / 3 + 5 * RIGHT / 4)
supply_y_label = supply_axes.get_y_axis_label("P")
supply_x_label = supply_axes.get_x_axis_label("Q")
supply_group = [supply_axes, supply_y_label, supply_x_label]

demand_axes = PQ_large.copy().scale(0.6).to_edge(DOWN + RIGHT).shift(2.5 * UP / 3 + 5 * LEFT / 4)
demand_y_label = demand_axes.get_y_axis_label("P")
demand_x_label = demand_axes.get_x_axis_label("Q")
demand_group = [demand_axes, demand_y_label, demand_x_label]

""" Functions """

supply_slope = 5
supply_intercept = 2

def Supply(q):
    return supply_intercept + q / supply_slope

def Inv_Supply(p):
    return (p - supply_intercept) * supply_slope

demand_slope = 5
demand_intercept = 12

def Demand(q):
    return demand_intercept - q / demand_slope

def Inv_Demand(p):
    return (demand_intercept - p) * demand_slope

""" Price """

price = ValueTracker()

""" Supply Curve """

Supply_Line = supply_axes.plot(Supply, x_range=[0, x_max]).set_color(YELLOW)
Supply_Line.z_index = 3

""" Supply Equation """

def supply_title_def():
    return MathTex(r"S: P =" + f"{price.get_value():.0f}" + r"= 2 + \frac{Q_s}{5}").next_to(supply_axes, UP * 2).set_color(YELLOW)
supply_title = supply_title_def()

""" Quantity Supplied """

def dot_s_def(p):
    q = Inv_Supply(p)
    dot = Dot(supply_axes.c2p(q, p)).set_color(RED)
    dot.z_index = 3
    return dot
dot_s = dot_s_def(price.get_value())

def p_line_s_def(p):
    return DashedVMobject(supply_axes.plot(lambda x: p, x_range=[-1, x_max])).set_color(RED)
p_line_s = p_line_s_def(price.get_value())

def p_number_s_def(p):
    return DecimalNumber(num_decimal_places=0).set_value(p).set_color(RED).scale(0.8).next_to(p_line_s, LEFT, buff=1/3)
p_number_s = p_number_s_def(price.get_value())

def p_label_s_def(p):
    if Inv_Demand(p) == Inv_Supply(p):
        return Tex("$P^*$:").set_color(RED).next_to(p_number_s, LEFT, buff=1/4)
    else:
        return Tex("$P$:").set_color(RED).next_to(p_number_s, LEFT, buff=1/4)
p_label_s = p_label_s_def(price.get_value())

def q_line_s_def(p):
    q = Inv_Supply(p)
    return DashedVMobject(Line(supply_axes.c2p(q, 2), supply_axes.c2p(q, p))).set_color(RED)
q_line_s = q_line_s_def(price.get_value())

def q_number_s_def(p):
    q = Inv_Supply(p)
    q_intercept = supply_axes.c2p(q, 0)
    return DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept, DOWN, buff=1/3)
q_number_s = q_number_s_def(price.get_value())

def q_label_s_def(p):
    q = Inv_Supply(p)
    q_intercept = supply_axes.c2p(q, 0)
    return Tex("$Q_s$").set_color(RED).next_to(q_intercept, UP, buff=0)
q_label_s = q_label_s_def(price.get_value())

quantity_supplied_group = [dot_s, p_line_s, p_number_s, p_label_s, q_line_s, q_number_s, q_label_s]

""" Demand Line """

Demand_Line = demand_axes.plot(Demand, x_range=[0, x_max]).set_color(BLUE)
Demand_Line.z_index = 3

""" Demand Equation """

def demand_title_def():
    return MathTex(r"D: P =" + f"{price.get_value():.0f}" + r"= 12 - \frac{Q_b}{5}").next_to(demand_axes, UP * 2).set_color(BLUE)
demand_title = demand_title_def()

""" Quantity Demanded """

def dot_d_def(p):
    q = Inv_Demand(p)
    dot = Dot(demand_axes.c2p(q, p)).set_color(RED)
    dot.z_index = 3
    return dot
dot_d = dot_d_def(price.get_value())

def p_line_d_def(p):
    return DashedVMobject(demand_axes.plot(lambda x: p, x_range=[-1, x_max])).set_color(RED)
p_line_d = p_line_d_def(price.get_value())

def p_number_d_def(p):
    return DecimalNumber(num_decimal_places=0).set_value(p).set_color(RED).scale(0.8).next_to(p_line_d, LEFT, buff=1/3)
p_number_d = p_number_d_def(price.get_value())

def p_label_d_def(p):
    if Inv_Demand(p) == Inv_Supply(p):
        return Tex("$P^*$:").set_color(RED).next_to(p_number_d, LEFT, buff=1/4)
    else:
        return Tex("$P$:").set_color(RED).next_to(p_number_d, LEFT, buff=1/4)
p_label_d = p_label_d_def(price.get_value())

def q_line_d_def(p):
    q = Inv_Demand(p)
    return DashedVMobject(Line(demand_axes.c2p(q, 2), demand_axes.c2p(q, p))).set_color(RED)
q_line_d = q_line_d_def(price.get_value())

def q_number_d_def(p):
    q = Inv_Demand(p)
    q_intercept = demand_axes.c2p(q, 0)
    return DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept, DOWN, buff=1/3)
q_number_d = q_number_d_def(price.get_value())

def q_label_d_def(p):
    q = Inv_Demand(p)
    q_intercept = demand_axes.c2p(q, 0)
    return Tex("$Q_b$").set_color(RED).next_to(q_intercept, UP, buff=0)
q_label_d = q_label_d_def(price.get_value())

quantity_demanded_group = [dot_d, p_line_d, p_number_d, p_label_d, q_line_d, q_number_d, q_label_d]

""" Exchange """

def shortage_line_def(p):
    qb = Inv_Demand(p)
    qs = Inv_Supply(p)
    if qb > qs:
        shortage_line = Line(demand_axes.c2p(qb, 0), demand_axes.c2p(qs, 0)).set_color(PINK)
    elif qb < qs:
        shortage_line = Line(supply_axes.c2p(qb, 0), supply_axes.c2p(qs, 0)).set_color(PINK)
    else:
        shortage_line = Line(demand_axes.c2p(qb, 0), demand_axes.c2p(qs, 0)).set_color(RED)
    return shortage_line
shortage_line = shortage_line_def(price.get_value())

def shortage_label_def(p):
    qb = Inv_Demand(p)
    qs = Inv_Supply(p)
    if qb > qs:
        shortage_label = Tex('Shortage').scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
    elif qb < qs:
        shortage_label = Tex('Surplus').scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
        qx = qb
    else:
        shortage_label = Tex('').scale(0.5).set_color(PINK).next_to(shortage_line, UP, buff=0)
    return shortage_label
shortage_label = shortage_label_def(price.get_value())

def supply_qx_label_def(p):
    qx = min(Inv_Demand(p), Inv_Supply(p))
    supply_qx = supply_axes.c2p(qx, 0)
    if Inv_Demand(p) == Inv_Supply(p):
        return Tex("$Q^*$").set_color(RED).next_to(supply_qx, DOWN, buff=3/4)
    else:
        return Tex("$Q_x$").set_color(RED).next_to(supply_qx, DOWN, buff=3/4)
supply_qx_label = supply_qx_label_def(price.get_value())

def supply_qx_dot_def(p):
    qx = min(Inv_Demand(p), Inv_Supply(p))
    supply_qx = supply_axes.c2p(qx, 0)
    line = Line(supply_axes.c2p(qx, -0.5), supply_axes.c2p(qx, 0.5)).set_color(RED)
    line.z_index = 1
    return line
supply_qx_dot = supply_qx_dot_def(price.get_value())

def demand_qx_label_def(p):
    qx = min(Inv_Demand(p), Inv_Supply(p))
    demand_qx = demand_axes.c2p(qx, 0)
    if Inv_Demand(p) == Inv_Supply(p):
        return Tex("$Q^*$").set_color(RED).next_to(demand_qx, DOWN, buff=3/4)
    else:
        return Tex("$Q_x$").set_color(RED).next_to(demand_qx, DOWN, buff=3/4)
demand_qx_label = demand_qx_label_def(price.get_value())

def demand_qx_dot_def(p):
    qx = min(Inv_Demand(p), Inv_Supply(p))
    supply_qx = demand_axes.c2p(qx, 0)
    line = Line(demand_axes.c2p(qx, -0.5), demand_axes.c2p(qx, 0.5)).set_color(RED)
    line.z_index = 1
    return line
demand_qx_dot = demand_qx_dot_def(price.get_value())

exchange_group = [shortage_line, shortage_label, supply_qx_label, demand_qx_label, demand_qx_dot]

""" Producer Surplus """

def ps_def(p):
    q = min(Inv_Supply(p), Inv_Demand(p))
    lines = []
    
    for i in np.arange(2/3, q, 2/3):
        i_p = Supply(i)
        
        ps_line = Line(supply_axes.c2p(i,p), supply_axes.c2p(i,i_p)).set_color(YELLOW).set_opacity(0.5)
        ps_line.z_index = -1
        lines.append(ps_line)
        
    return VGroup(*lines)
ps = ps_def(price.get_value())

""" Consumer Surplus """

def cs_def(p):
    q = min(Inv_Supply(p), Inv_Demand(p))
    lines = []
    
    for i in np.arange(2/3, q, 2/3):
        i_p = Demand(i)
        
        cs_line = Line(supply_axes.c2p(i,p), supply_axes.c2p(i,i_p)).set_color(BLUE).set_opacity(0.5)
        cs_line.z_index = -1
        lines.append(cs_line)
        
    return VGroup(*lines)
cs = cs_def(price.get_value())

""" Update Helpers """

updater_dict = {
    supply_title: lambda m: m.become(supply_title_def()),
    dot_s: lambda m: m.become(dot_s_def(price.get_value())),
    p_line_s: lambda m: m.become(p_line_s_def(price.get_value())),
    p_number_s: lambda m: m.become(p_number_s_def(price.get_value())),
    p_label_s: lambda m: m.become(p_label_s_def(price.get_value())),
    q_line_s: lambda m: m.become(q_line_s_def(price.get_value())),
    q_number_s: lambda m: m.become(q_number_s_def(price.get_value())),
    q_label_s: lambda m: m.become(q_label_s_def(price.get_value())),
    demand_title: lambda m: m.become(demand_title_def()),
    dot_d: lambda m: m.become(dot_d_def(price.get_value())),
    p_line_d: lambda m: m.become(p_line_d_def(price.get_value())),
    p_number_d: lambda m: m.become(p_number_d_def(price.get_value())),
    p_label_d: lambda m: m.become(p_label_d_def(price.get_value())),
    q_line_d: lambda m: m.become(q_line_d_def(price.get_value())),
    q_number_d: lambda m: m.become(q_number_d_def(price.get_value())),
    q_label_d: lambda m: m.become(q_label_d_def(price.get_value())),
    shortage_line: lambda m: m.become(shortage_line_def(price.get_value())),
    shortage_label: lambda m: m.become(shortage_label_def(price.get_value())),
    supply_qx_label: lambda m: m.become(supply_qx_label_def(price.get_value())),
    supply_qx_dot: lambda m: m.become(supply_qx_dot_def(price.get_value())),
    demand_qx_label: lambda m: m.become(demand_qx_label_def(price.get_value())),
    demand_qx_dot: lambda m: m.become(demand_qx_dot_def(price.get_value())),
    ps: lambda m: m.become(ps_def(price.get_value())),
    cs: lambda m: m.become(cs_def(price.get_value())),
}

def Add_Updater(mobjects: list):
    for m in mobjects:
        try:
            m.add_updater(updater_dict[m])
        except:
            print('pass')

def Remove_Updater(mobjects: list):
    for m in mobjects:
        try:
            m.remove_updater(updater_dict[m])
        except:
            pass

def swait(scene, time=1/2):
    scene.wait(time)


# In[44]:


get_ipython().run_cell_magic('manim', 'animation_1', '\nclass animation_1(MovingCameraScene):\n    def swait(self, time=1/2):\n        self.wait(time)\n    def construct(self):\n        price = ValueTracker(5)\n\n        self.play(FadeIn(title, *supply_group, *demand_group))\n        self.wait(1/2)\n        self.play(FadeIn(Supply_Line))\n        self.wait(1/2)\n        self.play(FadeIn(supply_title))\n        self.wait(1/2)\n        self.play(FadeIn(*quantity_supplied_group))\n\n        Add_Updater(supply_title)\n        self.wait(1/2)\n\n        self.play(price.animate.set_value(10))\n        self.wait(1/2)\n        \n        self.play(FadeIn(Demand_Line))\n        self.wait(1/2)\n        self.play(FadeIn(demand_title))\n        self.wait(1/2)\n        self.play(FadeIn(*quantity_demanded_group))\n        self.wait(1/2)\n')


# In[19]:


get_ipython().run_cell_magic('manim', 'animation_1', '\nclass animation_1(MovingCameraScene):\n\n    def construct(self):\n\n        """ Start """\n\n        self.play(FadeIn(shortage_line, shortage_label, supply_qx_label, supply_qx_dot, demand_qx_label, demand_qx_dot))\n        self.wait()\n        \n        for p in [9, 4, 5, 7]:\n            self.play(price.animate.set_value(p))\n            self.wait()\n\n        """ Supply and Demand Graph """\n        \n        new_demand_axes = demand_axes.copy().move_to(supply_axes)\n\n        supply_title.remove_updater(supply_title_update)\n        demand_title.remove_updater(demand_title_update)\n        q_line_d.remove_updater(q_line_d_update)\n\n        p = price.get_value()\n        q = Inv_Demand(p)\n        q_line_d_new = DashedVMobject(Line(supply_axes.c2p(q, 0), supply_axes.c2p(q, p))).set_color(RED)\n        \n        equals = MathTex(r"=").next_to(demand_axes,UP).shift(DOWN*2).set_color(WHITE)\n        new_supply_title = MathTex(r"2 + \\frac{Q^*}{5}").next_to(equals, LEFT).set_color(YELLOW)\n        new_demand_title = MathTex(r"12 - \\frac{Q^*}{5}").next_to(equals, RIGHT).set_color(BLUE)\n\n        new_title_string = "Equilibrium: $Q_s = Q_b = Q^*$"\n        new_title = Tex(new_title_string).to_edge(UP)\n\n        self.play(\n            demand_axes.animate.move_to(supply_axes),\n            FadeOut(demand_grid_labels, q_label_d, q_label_s, q_line_s),\n            Transform(Demand_Line, new_demand_axes.plot(Demand, x_range=[0, x_max]).set_color(BLUE)),\n            FadeIn(equals),\n            Transform(q_line_d, q_line_d_new),\n            Transform(supply_title, new_supply_title),\n            Transform(demand_title, new_demand_title),\n            Transform(title, new_title),\n        )\n        self.wait()\n        self.play(Create(cs))\n        self.wait()\n        self.play(Create(ps))\n        self.wait()\n        \n')


# In[228]:


get_ipython().run_cell_magic('manim', 'animation_2', '\nclass animation_2(MovingCameraScene):\n\n    def construct(self):\n        \n        """ Starting Objects """\n        \n        title_string = "How `good\' are markets anyway?"\n        title = Tex(title_string).to_edge(UP)\n\n        axes = PQ_large.copy().scale(0.7).to_edge(DOWN).shift(0.9*UP+LEFT*2)\n        y_label = axes.get_y_axis_label("P")\n        x_label = axes.get_x_axis_label("Q")\n        grid_labels = VGroup(x_label, y_label)\n\n        """ Functions """\n        \n        supply_slope = 5\n        supply_intercept = 2\n\n        def Supply(q):\n            return supply_intercept + q / supply_slope\n\n        def Inv_Supply(p):\n            return (p - supply_intercept) * supply_slope\n\n        demand_slope = 5\n        demand_intercept = 12\n\n        def Demand(q):\n            return demand_intercept - q / demand_slope\n\n        def Inv_Demand(p):\n            return (demand_intercept - p) * demand_slope\n\n        """ Price """\n        \n        price = ValueTracker(4)\n\n        """ Supply and Demand Curves """\n        \n        Supply_Line = axes.plot(Supply, x_range=[0, x_max]).set_color(YELLOW)\n        Supply_Line.z_index = 3\n        \n        Demand_Line = axes.plot(Demand, x_range=[0, x_max]).set_color(BLUE)\n        Demand_Line.z_index = 3\n\n        """ Equations """\n        \n        def supply_title_def():\n            return MathTex(r"S: P = 2 + \\frac{Q_s}{5}").next_to(axes, UP).shift(2.5*DOWN).to_edge(RIGHT).set_color(YELLOW)\n        supply_title = supply_title_def()\n\n        def demand_title_def():\n            return MathTex(r"D: P = 12 - \\frac{Q_b}{5}").next_to(axes, UP).shift(4*DOWN).to_edge(RIGHT).set_color(BLUE)\n        demand_title = demand_title_def()\n\n        """ Start """\n        \n        self.play(FadeIn(title, axes, grid_labels, Supply_Line, Demand_Line, supply_title, demand_title))\n\n        """ Quantity Supplied """\n\n        def dot_s_def(p):\n            q = Inv_Supply(p)\n            dot = Dot(axes.c2p(q, p)).set_color(RED)\n            dot.z_index = 3\n            return dot\n        dot_s = dot_s_def(price.get_value())\n        dot_s.add_updater(lambda m: m.become(dot_s_def(price.get_value())))\n\n        #def p_line_s_def(p):\n        #    return DashedVMobject(axes.plot(lambda x: p, x_range=[-1, x_max])).set_color(RED)\n        #p_line_s = p_line_s_def(price.get_value())\n        #p_line_s.add_updater(lambda m: m.become(p_line_s_def(price.get_value())))\n\n        #def p_number_s_def(p):\n        #    return Line(axes.c2p(-2.5, p), axes.c2p(2, p), stroke_width=5).set_color(RED)\n        #p_number_s = p_number_s_def(price.get_value())\n        #p_number_s.add_updater(lambda m: m.become(p_number_s_def(price.get_value())))\n\n        #def p_label_s_def(p):\n        #    if Inv_Demand(p) == Inv_Supply(p):\n        #        return Tex("$P^*$").set_color(RED).next_to(p_number_s, LEFT, buff=1/3+0.1)\n        #    else:\n        #        return Tex("$P$").set_color(RED).next_to(p_number_s, LEFT, buff=1/3+0.1)\n        #p_label_s = p_label_s_def(price.get_value())\n        #p_label_s.add_updater(lambda m: m.become(p_label_s_def(price.get_value())))\n\n        def q_line_s_def(p):\n            q = Inv_Supply(p)\n            return DashedVMobject(Line(axes.c2p(q, 0), axes.c2p(q, p))).set_color(RED)\n        q_line_s = q_line_s_def(price.get_value())\n        q_line_s.add_updater(lambda m: m.become(q_line_s_def(price.get_value())))\n\n        def q_number_s_def(p):\n            q = Inv_Supply(p)\n            q_intercept = axes.c2p(q, 0)\n            return DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept, DOWN, buff=1/3+0.1)\n        q_number_s = q_number_s_def(price.get_value())\n        q_number_s.add_updater(lambda m: m.become(q_number_s_def(price.get_value())))\n\n        def q_dot_s_def(p):\n            q = Inv_Supply(p)\n            line = Line(axes.c2p(q, -0.5), axes.c2p(q, 0.5)).set_color(RED)\n            line.z_index = 1\n            return line\n        q_dot_s = q_dot_s_def(price.get_value())\n        q_dot_s.add_updater(lambda m: m.become(q_dot_s_def(price.get_value())))\n\n        def q_label_s_def(p):\n            q = Inv_Supply(p)\n            q_intercept = axes.c2p(q, 0)\n            if Inv_Demand(p) == Inv_Supply(p):\n                return Tex("$Q^*$").set_color(RED).next_to(q_intercept, DOWN, buff=3/4)\n            else:\n                return Tex("$Q_s$").set_color(RED).next_to(q_intercept, DOWN, buff=3/4)\n        q_label_s = q_label_s_def(price.get_value())\n        q_label_s.add_updater(lambda m: m.become(q_label_s_def(price.get_value())))\n\n        """ Quantity Demanded """\n\n        def dot_d_def(p):\n            q = Inv_Demand(p)\n            dot = Dot(axes.c2p(q, p)).set_color(RED)\n            dot.z_index = 3\n            return dot\n        dot_d = dot_d_def(price.get_value())\n        dot_d.add_updater(lambda m: m.become(dot_d_def(price.get_value())))\n\n        def p_line_d_def(p):\n            return DashedVMobject(axes.plot(lambda x: p, x_range=[-1, x_max])).set_color(RED)\n        p_line_d = p_line_d_def(price.get_value())\n        p_line_d.add_updater(lambda m: m.become(p_line_d_def(price.get_value())))\n\n        def p_number_d_def(p):\n            return Line(axes.c2p(-2.5, p), axes.c2p(2, p), stroke_width=5).set_color(RED)\n        p_number_d = p_number_d_def(price.get_value())\n        p_number_d.add_updater(lambda m: m.become(p_number_d_def(price.get_value())))\n\n        def p_label_d_def(p):\n            if Inv_Demand(p) == Inv_Supply(p):\n                return Tex("$P^*$").set_color(RED).next_to(p_number_d, LEFT, buff=1/3+0.1)\n            else:\n                return Tex("$P$").set_color(RED).next_to(p_number_d, LEFT, buff=1/3+0.1)\n        p_label_d = p_label_d_def(price.get_value())\n        p_label_d.add_updater(lambda m: m.become(p_label_d_def(price.get_value())))\n\n        def q_line_d_def(p):\n            q = Inv_Demand(p)\n            return DashedVMobject(Line(axes.c2p(q, 0), axes.c2p(q, p))).set_color(RED)\n        q_line_d = q_line_d_def(price.get_value())\n        def q_line_d_update(m):\n            m.become(q_line_d_def(price.get_value()))\n        q_line_d.add_updater(q_line_d_update)\n\n        def q_number_d_def(p):\n            q = Inv_Demand(p)\n            q_intercept = axes.c2p(q, 0)\n            return DecimalNumber(num_decimal_places=0).set_value(q).set_color(RED).scale(0.8).next_to(q_intercept, DOWN, buff=1/3+0.1)\n        q_number_d = q_number_d_def(price.get_value())\n        q_number_d.add_updater(lambda m: m.become(q_number_d_def(price.get_value())))\n\n        def q_dot_d_def(p):\n            q = Inv_Demand(p)\n            line = Line(axes.c2p(q, -0.5), axes.c2p(q, 0.5)).set_color(RED)\n            line.z_index = 1\n            return line\n        q_dot_d = q_dot_d_def(price.get_value())\n        q_dot_d.add_updater(lambda m: m.become(q_dot_d_def(price.get_value())))\n\n        def q_label_d_def(p):\n            q = Inv_Demand(p)\n            q_intercept = axes.c2p(q, 0)\n            if Inv_Demand(p) == Inv_Supply(p):\n                return Tex("$Q^*$").set_color(RED).next_to(q_intercept, DOWN, buff=3/4)\n            else:\n                return Tex("$Q_b$").set_color(RED).next_to(q_intercept, DOWN, buff=3/4)\n        q_label_d = q_label_d_def(price.get_value())\n        q_label_d.add_updater(lambda m: m.become(q_label_d_def(price.get_value())))\n\n        """ Exchange """\n\n        def shortage_line_def(p):\n            qb = Inv_Demand(p)\n            qs = Inv_Supply(p)\n            if qb > qs:\n                shortage_line = Line(axes.c2p(qb, 0), axes.c2p(qs, 0)).set_color(PINK)\n            elif qb < qs:\n                shortage_line = Line(axes.c2p(qb, 0), axes.c2p(qs, 0)).set_color(PINK)\n            else:\n                shortage_line = Line(axes.c2p(qb, 0), axes.c2p(qs, 0)).set_color(RED)\n            return shortage_line\n        shortage_line = shortage_line_def(price.get_value())\n        shortage_line.add_updater(lambda m: m.become(shortage_line_def(price.get_value())))\n\n        def shortage_label_def(p):\n            qb = Inv_Demand(p)\n            qs = Inv_Supply(p)\n            if qb > qs:\n                shortage_label = Tex(\'Shortage\').scale(0.6).set_color(PINK).next_to(shortage_line, UP, buff=0)\n            elif qb < qs:\n                shortage_label = Tex(\'Surplus\').scale(0.6).set_color(PINK).next_to(shortage_line, UP, buff=0)\n                qx = qb\n            else:\n                shortage_label = Tex(\'\').scale(0.6).set_color(PINK).next_to(shortage_line, UP, buff=0)\n            return shortage_label\n        shortage_label = shortage_label_def(price.get_value())\n        shortage_label.add_updater(lambda m: m.become(shortage_label_def(price.get_value())))\n\n        """ Producer Surplus """\n        \n        def ps_def(p):\n            q = min(Inv_Supply(p), Inv_Demand(p))\n            lines = []\n            \n            for i in np.arange(2/3, q, 2/3):\n                i_p = Supply(i)\n                \n                ps_line = Line(axes.c2p(i,p), axes.c2p(i,i_p)).set_color(YELLOW).set_opacity(0.5)\n                ps_line.z_index = -1\n                lines.append(ps_line)\n                \n            return VGroup(*lines)\n        ps = ps_def(price.get_value())\n        ps.add_updater(lambda m: m.become(ps_def(price.get_value())))\n\n        """ Consumer Surplus """\n        \n        def cs_def(p):\n            q = min(Inv_Supply(p), Inv_Demand(p))\n            lines = []\n            \n            for i in np.arange(2/3, q, 2/3):\n                i_p = Demand(i)\n                \n                cs_line = Line(axes.c2p(i,p), axes.c2p(i,i_p)).set_color(BLUE).set_opacity(0.5)\n                cs_line.z_index = -1\n                lines.append(cs_line)\n                \n            return VGroup(*lines)\n        cs = cs_def(price.get_value())\n        cs.add_updater(lambda m: m.become(cs_def(price.get_value())))\n\n        """ DWL """\n        \n        def dwl_def(p):\n            q = min(Inv_Supply(p), Inv_Demand(p))\n            lines = []\n            \n            for i in np.arange(q, 25, 2/3):                \n                dwl_line = Line(axes.c2p(i,Supply(i)), axes.c2p(i,Demand(i))).set_color(GREY).set_opacity(0.5)\n                dwl_line.z_index = -1\n                lines.append(dwl_line)\n                \n            return VGroup(*lines)\n        dwl = dwl_def(price.get_value())\n        dwl.add_updater(lambda m: m.become(dwl_def(price.get_value())))\n\n        """ Price Ceiling """\n\n        price_ceiling = ValueTracker(5)\n\n        def price_ceiling_def(p):\n            line = Line(axes.c2p(-0.2, 0), axes.c2p(-0.2, p), stroke_width=10).set_color(GREEN)\n            line.z_index = -1\n            return line\n        price_ceiling_line = price_ceiling_def(price_ceiling.get_value())\n        price_ceiling_line.add_updater(lambda m: m.become(price_ceiling_def(price_ceiling.get_value())))\n\n        def price_ceiling_dot_def(p):\n            line = Line(axes.c2p(-2.5, p), axes.c2p(2, p), stroke_width=5).set_color(GREEN)\n            line.z_index = -1\n            return line\n        price_ceiling_dot = price_ceiling_dot_def(price_ceiling.get_value())\n        price_ceiling_dot.add_updater(lambda m: m.become(price_ceiling_dot_def(price_ceiling.get_value())))\n\n        def price_ceiling_label_def():\n            return Tex(\'Legal\').scale(0.6).set_color(GREEN).rotate(np.pi/2).next_to(price_ceiling_line, LEFT, buff=0.3)\n        price_ceiling_label = price_ceiling_label_def()\n        price_ceiling_label.add_updater(lambda m: m.become(price_ceiling_label_def()))\n\n        """ Price Floor """\n\n        price_floor = ValueTracker(10)\n\n        def price_floor_def(p):\n            line = Line(axes.c2p(-0.2, p), axes.c2p(-0.2, 14), stroke_width=10).set_color(GREEN)\n            line.z_index = -1\n            return line\n        price_floor_line = price_floor_def(price_floor.get_value())\n        price_floor_line.add_updater(lambda m: m.become(price_floor_def(price_floor.get_value())))\n\n        def price_floor_dot_def(p):\n            line = Line(axes.c2p(-2.5, p), axes.c2p(2, p), stroke_width=5).set_color(GREEN)\n            line.z_index = -1\n            return line\n        price_floor_dot = price_floor_dot_def(price_floor.get_value())\n        price_floor_dot.add_updater(lambda m: m.become(price_floor_dot_def(price_floor.get_value())))\n\n        def price_floor_label_def():\n            return Tex(\'Legal\').scale(0.6).set_color(GREEN).rotate(np.pi/2).next_to(price_floor_line, LEFT, buff=0.3)\n        price_floor_label = price_floor_label_def()\n        price_floor_label.add_updater(lambda m: m.become(price_floor_label_def()))\n\n        """ Price Ceiling """\n\n        new_title_string = "{{Welfare Analysis}}: the study of the benefits of markets."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Welfare Analysis": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        new_title_string = "{{Price Controls}}: government price restrictions."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Price Controls": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        new_title_string = "Can the government improve the market with a {{Price Ceiling}}?"\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Price Ceiling": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        self.play(FadeIn(price_ceiling_line, price_ceiling_label, price_ceiling_dot))\n        self.wait()\n        self.play(FadeIn(p_label_d, p_line_d, p_number_d))\n        self.wait()\n        self.play(FadeIn(dot_d, q_line_d, q_number_d, q_dot_d, q_label_d))\n        self.wait()\n        self.play(FadeIn(dot_s, q_line_s, q_number_s, q_dot_s, q_label_s))\n        self.wait()\n        self.play(FadeIn(shortage_line, shortage_label))\n        self.wait()\n        \n        new_title_string = "Buyers and sellers push as close as possible to {{Equilibrium}}."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Equilibrium": PURPLE,}).to_edge(UP).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        self.play(price.animate.set_value(5))\n        self.wait()\n        \n        new_title_string = "A binding {{Price Celing}} creates a shortage."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Price Ceiling": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        new_title_string = "How `good\' is this market?"\n        new_title = Tex(new_title_string).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        self.play(Create(ps))\n        self.wait()\n        self.play(Create(cs))\n        self.wait()\n        self.play(Create(dwl))\n        self.wait()\n\n        new_title_string = "A shortage creates {{Deadweight Loss}}."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Deadweight Loss": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        new_title_string = "{{Deadweight Loss}}: a loss of surplus value for society as a whole."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Deadweight Loss": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        self.play(price.animate.set_value(7), price_ceiling.animate.set_value(7))\n        self.wait()\n        \n        new_title_string = "There is no DWL in {{Competitive Markets}} with no externalities."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Competitive Markets": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        """ Price Floor """\n\n        new_title_string = "Can the government improve the market with a {{Price Floor}}?"\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Price Floor": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        self.play(FadeOut(\n                    price_ceiling_line, price_ceiling_label, price_ceiling_dot,\n                    p_label_d, p_line_d, p_number_d,\n                    dot_d, q_line_d, q_number_d, q_dot_d, q_label_d,\n                    dot_s, q_line_s, q_number_s, q_dot_s, q_label_s,\n                    shortage_line, shortage_label,\n                    ps, cs, dwl\n                    ),\n                  Transform(title, new_title)\n                 )\n        self.wait()\n\n        price.set_value(11)\n        \n        self.play(FadeIn(price_floor_line, price_floor_label, price_floor_dot))\n        self.wait()\n        self.play(FadeIn(p_label_d, p_line_d, p_number_d))\n        self.wait()\n        self.play(FadeIn(dot_d, q_line_d, q_number_d, q_dot_d, q_label_d))\n        self.wait()\n        self.play(FadeIn(dot_s, q_line_s, q_number_s, q_dot_s, q_label_s))\n        self.wait()\n        self.play(FadeIn(shortage_line, shortage_label))\n        self.wait()\n\n        new_title_string = "Buyers and sellers push as close as possible to equilibrium."\n        new_title = Tex(new_title_string).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        self.play(price.animate.set_value(10))\n        self.wait()\n        \n        new_title_string = "A binding Price Floor creates a surplus."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Price Floor": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        new_title_string = "How `good\' is this market?"\n        new_title = Tex(new_title_string).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        self.play(Create(ps))\n        self.wait()\n        self.play(Create(cs))\n        self.wait()\n\n        new_title_string = "A surplus also creates {{Deadweight Loss}}."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Deadweight Loss": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n        self.play(Create(dwl))\n        self.wait()\n        \n        self.play(price.animate.set_value(7), price_floor.animate.set_value(7))\n        self.wait()\n        \n        new_title_string = "There is no DWL in {{Competitive Markets}} with no externalities."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Competitive Markets": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n        \n')


# In[209]:


get_ipython().run_cell_magic('manim', 'animation_3', '\nclass animation_3(MovingCameraScene):\n\n    def construct(self):\n        \n        """ First Welfare Theorem """\n        \n        definition_1 = Tex("{{First Welfare Theorem}}: competitive markets").set_color_by_tex_to_color_map({\n            "First Welfare Theorem": YELLOW\n        }).to_edge(LEFT).shift(UP/2+RIGHT)\n        definition_2 = Tex("with no externalities maximize welfare.").to_edge(LEFT).shift(DOWN/2+RIGHT*2)\n        self.play(AddTextWordByWord(definition_1))\n        self.play(AddTextWordByWord(definition_2))\n        self.wait()\n        self.play(FadeOut(definition_1, definition_2))\n')


# In[5]:


get_ipython().run_cell_magic('manim', 'animation_4', '\nclass animation_4(MovingCameraScene):\n\n    def construct(self):\n        \n        """ Starting Objects """\n        \n        title_string = "How do prices change?"\n        title = Tex(title_string).to_edge(UP)\n\n        axes = PQ_large.copy().scale(0.7).to_edge(DOWN).shift(0.9*UP+LEFT*2)\n        y_label = axes.get_y_axis_label("P")\n        x_label = axes.get_x_axis_label("Q")\n        grid_labels = VGroup(x_label, y_label)\n\n        """ Price and Parameters """\n        \n        price = ValueTracker(7)\n        l = ValueTracker(0)\n        m = ValueTracker(0)\n\n        """ Functions """\n        \n        supply_slope = 5\n        supply_intercept = 2\n\n        def Supply(q):\n            return supply_intercept + l.get_value() + q / supply_slope\n\n        def Inv_Supply(p):\n            return (p - supply_intercept - l.get_value()) * supply_slope\n\n        demand_slope = 5\n        demand_intercept = 12\n\n        def Demand(q):\n            return demand_intercept + m.get_value() - q / demand_slope\n\n        def Inv_Demand(p):\n            return (demand_intercept + m.get_value() - p) * demand_slope\n\n        """ Equations """\n        \n        def supply_title_def():\n            return MathTex(r"S: P = 2 + z_s + \\frac{Q_s}{5}").next_to(axes, UP).shift(2.5*DOWN).to_edge(RIGHT).set_color(YELLOW)\n        supply_title = supply_title_def()\n\n        def demand_title_def():\n            return MathTex(r"D: P = 12 + z_b - \\frac{Q_b}{5}").next_to(axes, UP).shift(4*DOWN).to_edge(RIGHT).set_color(BLUE)\n        demand_title = demand_title_def()\n\n        """ Supply and Demand Curves """\n        \n        Supply_Line = axes.plot(Supply, x_range=[0, x_max]).set_color(YELLOW)\n        Supply_Line.z_index = 3\n        \n        Demand_Line = axes.plot(Demand, x_range=[0, x_max]).set_color(BLUE)\n        Demand_Line.z_index = 3\n\n        """ Quantity Demanded """\n\n        def dot_d_def(p):\n            q = Inv_Demand(p)\n            dot = Dot(axes.c2p(q, p)).set_color(RED)\n            dot.z_index = 3\n            return dot\n        dot_d = dot_d_def(price.get_value())\n        dot_d.add_updater(lambda m: m.become(dot_d_def(price.get_value())))\n\n        def p_line_d_def(p):\n            return DashedVMobject(axes.plot(lambda x: p, x_range=[-1, x_max])).set_color(RED)\n        p_line_d = p_line_d_def(price.get_value())\n        p_line_d.add_updater(lambda m: m.become(p_line_d_def(price.get_value())))\n\n        def p_number_d_def(p):\n            return Line(axes.c2p(-2.5, p), axes.c2p(2, p), stroke_width=5).set_color(RED)\n        p_number_d = p_number_d_def(price.get_value())\n        p_number_d.add_updater(lambda m: m.become(p_number_d_def(price.get_value())))\n\n        def p_label_d_def(p):\n            if Inv_Demand(p) == Inv_Supply(p):\n                return Tex("$P^*$").set_color(RED).next_to(p_number_d, LEFT, buff=1/3+0.1)\n            else:\n                return Tex("$P$").set_color(RED).next_to(p_number_d, LEFT, buff=1/3+0.1)\n        p_label_d = p_label_d_def(price.get_value())\n        p_label_d.add_updater(lambda m: m.become(p_label_d_def(price.get_value())))\n\n        def q_line_d_def(p):\n            q = Inv_Demand(p)\n            return DashedVMobject(Line(axes.c2p(q, 0), axes.c2p(q, p))).set_color(RED)\n        q_line_d = q_line_d_def(price.get_value())\n        def q_line_d_update(m):\n            m.become(q_line_d_def(price.get_value()))\n        q_line_d.add_updater(q_line_d_update)\n\n        def q_dot_d_def(p):\n            q = Inv_Demand(p)\n            line = Line(axes.c2p(q, -0.5), axes.c2p(q, 0.5)).set_color(RED)\n            line.z_index = 1\n            return line\n        q_dot_d = q_dot_d_def(price.get_value())\n        q_dot_d.add_updater(lambda m: m.become(q_dot_d_def(price.get_value())))\n\n        def q_label_d_def(p):\n            q = Inv_Demand(p)\n            q_intercept = axes.c2p(q, 0)\n            if Inv_Demand(p) == Inv_Supply(p):\n                return Tex("$Q^*$").set_color(RED).next_to(q_intercept, DOWN, buff=1/3+0.1)\n            else:\n                return Tex("$Q_b$").set_color(RED).next_to(q_intercept, DOWN, buff=3/4)\n        q_label_d = q_label_d_def(price.get_value())\n        q_label_d.add_updater(lambda m: m.become(q_label_d_def(price.get_value())))\n\n        """ Equilibrium """\n\n        def p_star():\n            return supply_intercept + l.get_value() + (demand_intercept - supply_intercept + m.get_value() - l.get_value())/2\n\n        def q_star():\n            return 5 * (demand_intercept - supply_intercept + m.get_value() - l.get_value()) / 2\n\n        """ Comparative Statics """\n        \n        self.play(FadeIn(\n            title, axes, grid_labels, Supply_Line, Demand_Line, supply_title, demand_title,\n            dot_d, p_line_d, p_number_d, p_label_d, q_line_d, q_dot_d, q_label_d\n        ))\n        self.wait()\n\n        new_title_string = "{{Comparative Statics}}: how external forces change equilibrium."\n        new_title = Tex(new_title_string).set_color_by_tex_to_color_map({"Comparative Statics": PURPLE,}).to_edge(UP)\n        self.play(Transform(title, new_title))\n        self.wait()\n\n        self.play(FadeOut(\n            axes, grid_labels, Supply_Line, Demand_Line, supply_title, demand_title,\n            dot_d, p_line_d, p_number_d, p_label_d, q_line_d, q_dot_d, q_label_d\n        ),\n                  title.animate.move_to(ORIGIN)\n                 )\n        self.wait()\n')


# ## OLD 1
# 

# In[90]:


get_ipython().run_cell_magic('manim', 'animation_1', '\nclass animation_1(MovingCameraScene):\n\n    def construct(self):\n        \n        """ Definitions """\n        \n        PQ_axis = Axes(            \n            x_range=[0, 1000, 500],\n            x_length = 7,\n            axis_config={"color": WHITE},\n            x_axis_config={\n                "numbers_to_include": np.arange(0, 1000, 500),\n                "decimal_number_config": {\n                    "num_decimal_places":0,\n                },\n            },\n            y_range=[0, 100, 50],\n            y_length = 6,\n            y_axis_config={\n                "numbers_to_include": [100,50,0],\n                "decimal_number_config": {\n                    "num_decimal_places":0,\n                }\n            },\n            tips=False,\n        )\n        \n        """ Starting Objects """\n        \n        axes = PQ_axis.copy().scale(0.8).to_edge(DOWN).shift(UP/2)\n\n        y_label = axes.get_y_axis_label("P")\n        x_label = axes.get_x_axis_label("Q")\n        grid_labels = VGroup(x_label, y_label)\n        \n        self.play(FadeIn(axes), FadeIn(grid_labels))\n        \n        """ Starting Equilibrium """\n        \n        title = Tex("{{Comparative Statics}}: how external forces change equilibrium.").set_color_by_tex_to_color_map(\n            {"Comparative Statics": YELLOW,}\n        ).to_edge(UP)\n        self.play(FadeIn(title))\n        \n        demand_intercept = ValueTracker(100)\n        def Demand(q):\n            return demand_intercept.get_value() - q/10\n        def Inv_Demand(p):\n            return (demand_intercept.get_value() - p) * 10\n        def Demand_Line():\n            return axes.plot(Demand, x_range=[0, Inv_Demand(0)]).set_color(BLUE)        \n        demand = always_redraw(Demand_Line)\n        \n        demand_base = Demand_Line().set_color(GREY)\n        demand_base.z_index = -1\n        \n        supply_intercept = ValueTracker(10)\n        def Supply(q):\n            return supply_intercept.get_value() + q/10\n        def Inv_Supply(p):\n            return (supply_intercept.get_value() + p) * 10\n        def Supply_Line():\n            return axes.plot(Supply, x_range=[0, Inv_Supply(80)]).set_color(YELLOW)        \n        supply = always_redraw(Supply_Line)\n        \n        supply_base = Supply_Line().set_color(GREY)\n        supply_base.z_index = -1\n        \n        def Equilibrium_Price():\n            return supply_intercept.get_value() + (demand_intercept.get_value() - supply_intercept.get_value())/2\n        \n        price_value = ValueTracker(Equilibrium_Price())\n        def Price_Line():\n            price_value.set_value(Equilibrium_Price())\n            return axes.plot(lambda x:price_value.get_value(), x_range=[0,1000]).set_color(RED) \n        price = always_redraw(Price_Line)\n        \n        price_base = Price_Line().set_color(GREY)\n        price_base.z_index = -1\n        \n        def Quantity_Demanded():\n            p = price_value.get_value()\n            q = Inv_Demand(p)\n            point = axes.c2p(q, p)\n            dot = Dot(point).set_color(RED)\n            dot.z_index = 3\n            line = axes.get_vertical_line(axes.input_to_graph_point(q, demand), color=RED)\n            return VGroup(dot, line)\n        quantity_demanded = always_redraw(Quantity_Demanded)\n        \n        def Quantity_Exchanged(p):\n            qs = Inv_Supply(p)\n            qd = Inv_Demand(p)\n            return min(qs, qd)\n                \n        self.play(FadeIn(demand), FadeIn(demand_base), \n                  FadeIn(supply), FadeIn(supply_base),\n                  FadeIn(price), FadeIn(quantity_demanded))\n        self.wait()\n        \n        """ Comparative Statics """\n        \n        self.play(demand_intercept.animate.set_value(90))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(70))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(100))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(20))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(30))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(10))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(20))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(70))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(10), demand_intercept.animate.set_value(100))\n        self.wait()\n        \n        """ Welfare Analysis """\n        \n        new_title = Tex("{{Welfare Analysis}}: the study of the benefits of markets.").set_color_by_tex_to_color_map(\n            {"Welfare Analysis": YELLOW,}\n        ).to_edge(UP)\n        self.play(Transform(title, new_title))\n        \n        def Consumer_Surplus():\n            area = axes.get_area(Demand_Line(), [0, Quantity_Exchanged(Equilibrium_Price())], bounded_graph=Price_Line(), color=BLUE, opacity=0.5)\n            area.z_index = -3\n            return area\n        CS = always_redraw(Consumer_Surplus)\n        CS_base = Consumer_Surplus().set_color(GREY)\n        \n        self.play(FadeIn(CS), FadeIn(CS_base))\n        self.wait()\n        \n        self.play(demand_intercept.animate.set_value(90))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(70))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(100))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(20))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(30))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(10))\n        self.wait()\n        \n        self.play(FadeOut(CS), FadeOut(CS_base))\n        \n        def Producer_Surplus():\n            area = axes.get_area(Supply_Line(), [0, Quantity_Exchanged(Equilibrium_Price())], bounded_graph=Price_Line(), color=YELLOW, opacity=0.5)\n            area.z_index = -3\n            return area\n        PS = always_redraw(Producer_Surplus)\n        \n        PS_base = Producer_Surplus().set_color(GREY)\n        \n        self.play(FadeIn(PS), FadeIn(PS_base))\n        self.wait()\n        \n        self.play(demand_intercept.animate.set_value(90))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(70))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(100))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(20))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(30))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(10))\n        self.wait()\n        \n        self.play(FadeOut(PS), FadeOut(PS_base))\n        \n        def Total_Surplus():\n            area = axes.get_area(Supply_Line(), [0, Quantity_Exchanged(Equilibrium_Price())], bounded_graph=Demand_Line(), color=PURPLE, opacity=0.5)\n            area.z_index = -3\n            return area\n        TS = always_redraw(Total_Surplus)\n        \n        TS_base = Total_Surplus().set_color(GREY)\n\n        self.play(FadeIn(TS), FadeIn(TS_base))\n        self.wait()\n\n        self.play(demand_intercept.animate.set_value(90))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(70))\n        self.wait()\n        self.play(demand_intercept.animate.set_value(100))\n        self.wait()\n        \n        self.play(supply_intercept.animate.set_value(20))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(30))\n        self.wait()\n        self.play(supply_intercept.animate.set_value(10))\n        self.wait()\n        \n        self.play(FadeOut(TS), FadeOut(TS_base))\n\n        """ Price Control """\n        \n        price_value.suspend_updating()\n        \n        new_title = Tex(\n            "{{Price Controls}}: government price restrictions.",\n        ).set_color_by_tex_to_color_map(\n            {"Price Controls": YELLOW,}\n        ).to_edge(UP)\n        self.play(Transform(title, new_title))\n        \n        self.remove(price)\n        \n        price_value = ValueTracker(Equilibrium_Price())\n        def Price_Line():\n            return axes.plot(lambda x:price_value.get_value(), x_range=[0,1000]).set_color(RED) \n        price = always_redraw(Price_Line)\n        \n        def Quantity_Supplied():\n            p = price_value.get_value()\n            q = Inv_Supply(p)\n            point = axes.c2p(q, p)\n            dot = Dot(point).set_color(RED)\n            dot.z_index = 3\n            line = axes.get_vertical_line(axes.input_to_graph_point(q, supply), color=RED)\n            return VGroup(dot, line)\n        quantity_supplied = always_redraw(Quantity_Supplied)\n        \n        self.add(price, quantity_supplied)\n        \n        self.play(FadeIn(CS), FadeIn(PS), FadeIn(TS_base))\n        self.wait()\n        \n        self.play(price_value.animate.set_value(40))\n        \n        \n')


# ### Merge and Convert Videos

# In[6]:


video_path = config.media_dir+'/videos/ANIMATIONS/1080p10/'

Make_MOV(video_path)

