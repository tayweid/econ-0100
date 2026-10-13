#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Video import *
warnings.filterwarnings('ignore')

""" Paths """
tutorial_path = 'PartB_E6'
if not os.path.exists(tutorial_path):
    os.makedirs(tutorial_path)
config.media_dir = tutorial_path
config.verbosity = 'ERROR'
config.text_font = "Roboto Slab"

""" Colors """
CUSTOM_GREY = '#696969'
CUSTOM_BLACK = '#1f1f1f'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY

""" Frames """
PIXEL_HEIGHT = 1080
FPS = 10
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT*2
config.frame_rate = FPS


# In[63]:


""" Timeline """

basic_timeline = NumberLine(
    x_range=[1930, 2000, 70],
    length=12,
    include_tip=False,
    font_size=32,
    numbers_to_include=[1930, 2000],
    decimal_number_config={
        "group_with_commas": False,
        "num_decimal_places": 0
    },
)

timeline = basic_timeline.to_edge(DOWN, buff=1/2)
timeline_label = Text("Year", font_size=32).next_to(timeline, DOWN).shift(UP/2)

time_tracker = ValueTracker(1930)
time_marker = always_redraw(lambda: Triangle(color=WHITE).rotate(np.pi).scale(0.1).next_to(timeline.n2p(time_tracker.get_value()), UP, buff=0.1))

time_indicator = always_redraw(lambda: DecimalNumber(
    time_tracker.get_value(), num_decimal_places=0, group_with_commas=False,
    font_size=32
).next_to(time_marker, UP))

""" International Trade Objects """

basic_axis = Axes(
    x_range=[0, 10, 10],
    y_range=[0, 10, 10],
    x_length=5, 
    y_length=5,
    axis_config={"include_tip": True, "tip_length": 0.01, "include_numbers": False, "font_size": 18},
)
basic_axis.x_axis.tip.scale(0.5)
basic_axis.y_axis.tip.scale(0.5)

domestic_axes = basic_axis.copy().to_corner(UL, buff=1)
domestic_axes_y_label = domestic_axes.get_y_axis_label("P")
domestic_axes_x_label = domestic_axes.get_x_axis_label("Q")
domestic_label = Text("US Market", font_size=32).next_to(domestic_axes, UP)

domestic_supply_curve = domestic_axes.plot(lambda x: 0.5 * x + 2, color=YELLOW)
domestic_demand_curve = domestic_axes.plot(lambda x: 8 -0.5 * x, color=BLUE)

global_axes = basic_axis.copy().to_corner(UR, buff=1)
global_axes_y_label = global_axes.get_y_axis_label("P")
global_axes_x_label = global_axes.get_x_axis_label("Q")
global_label = Text("Global Market", font_size=32).next_to(global_axes, UP)

global_supply_curve = always_redraw(lambda: global_axes.plot(lambda x: 0.5 * x + 7 - (time_tracker.get_value() - 1930) / 10, color=YELLOW))
global_demand_curve = global_axes.plot(lambda x: 8 -0.5 * x, color=BLUE)

""" Equilibrium Objects """

domestic_eq_x = (8 - 2) / (0.5 + 0.5)  # Solving 0.5x + 2 = -0.5x + 8
domestic_eq_y = 0.5 * domestic_eq_x + 2  # Substitute to get price

def get_global_eq_y():
    supply_shift = 7 - (time_tracker.get_value() - 1930) / 10  # Shifting downward
    global_eq_x = (8 - supply_shift) / (0.5 + 0.5)  # Solve 0.5x + supply_shift = -0.5x + 8
    global_eq_y = 0.5 * global_eq_x + supply_shift  # Calculate price at equilibrium
    return global_eq_y

domestic_price = DashedLine(
    start=domestic_axes.c2p(0, domestic_eq_y), end=domestic_axes.c2p(10, domestic_eq_y),
    color=RED
).set_stroke(width=2)

global_price = always_redraw(lambda: DashedLine(
    start=global_axes.c2p(0, get_global_eq_y()), end=global_axes.c2p(10, get_global_eq_y()),
    color=RED
).set_stroke(width=2))

domestic_price_label = MathTex(r"P^*", font_size=32, color=RED).next_to(domestic_price, LEFT, buff=0.1)
global_price_label = always_redraw(lambda: MathTex(r"P_G", font_size=32, color=RED).next_to(global_price, LEFT, buff=0.1))

# Domestic quantity label
domestic_quantity_label = MathTex(r"Q^*", font_size=32, color=WHITE).next_to(
    domestic_axes.c2p(domestic_eq_x, 0), DOWN, buff=0.1
)

# Global quantity label, updating position as supply shifts
global_quantity_label = always_redraw(lambda: MathTex(r"Q_G", font_size=32, color=WHITE).next_to(
    global_axes.c2p((8 - (7 - (time_tracker.get_value() - 1930) / 10)) / (0.5 + 0.5), 0), DOWN, buff=0.1
))

# Domestic equilibrium lines (dashed) and dot
domestic_eq_vline = DashedLine(
    start=domestic_axes.c2p(domestic_eq_x, 0), 
    end=domestic_axes.c2p(domestic_eq_x, domestic_eq_y),
    color=WHITE
)
domestic_eq_hline = DashedLine(
    start=domestic_axes.c2p(0, domestic_eq_y), 
    end=domestic_axes.c2p(domestic_eq_x, domestic_eq_y),
    color=WHITE
)
domestic_eq_dot = Dot(domestic_axes.c2p(domestic_eq_x, domestic_eq_y), color=WHITE)

# Global equilibrium lines (dashed) and dot
global_eq_vline = always_redraw(lambda: DashedLine(
    start=global_axes.c2p((8 - (7 - (time_tracker.get_value() - 1930) / 10)) / (0.5 + 0.5), 0),
    end=global_axes.c2p((8 - (7 - (time_tracker.get_value() - 1930) / 10)) / (0.5 + 0.5), get_global_eq_y()),
    color=WHITE
))
global_eq_hline = always_redraw(lambda: DashedLine(
    start=global_axes.c2p(0, get_global_eq_y()),
    end=global_axes.c2p((8 - (7 - (time_tracker.get_value() - 1930) / 10)) / (0.5 + 0.5), get_global_eq_y()),
    color=WHITE
))
global_eq_dot = always_redraw(lambda: Dot(global_axes.c2p(
    (8 - (7 - (time_tracker.get_value() - 1930) / 10)) / (0.5 + 0.5), get_global_eq_y()), color=WHITE
))


# In[64]:


get_ipython().run_cell_magic('manim', 'InternationalTradeScene', '\nclass InternationalTradeScene(Scene):\n    def construct(self):\n\n        self.play(FadeIn(domestic_axes, domestic_label, domestic_supply_curve, domestic_demand_curve))\n        self.wait()\n        \n        self.play(FadeIn(domestic_quantity_label, domestic_price, domestic_price_label))\n        self.wait()\n        \n        self.play(FadeIn(domestic_eq_vline, domestic_eq_hline, domestic_eq_dot))\n        self.wait()\n        \n        self.play(FadeIn(global_axes, global_label, global_supply_curve, global_demand_curve))\n        self.wait()\n        \n        self.play(FadeIn(global_price, global_price_label, global_quantity_label))\n        self.wait()\n\n        self.play(FadeIn(global_eq_vline, global_eq_hline, global_eq_dot))\n        self.wait()\n        \n        self.play(FadeIn(timeline, timeline_label, time_indicator, time_marker))\n        self.wait()\n\n        self.play(time_tracker.animate.set_value(1980), run_time=10, rate_func=linear)\n        self.wait()\n')


# In[ ]:


video_path = config.media_dir+'/videos/tutorials/1080p60/'

manim_to_mov(video_path)

