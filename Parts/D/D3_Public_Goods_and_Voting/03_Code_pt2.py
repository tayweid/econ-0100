#!/usr/bin/env python
# coding: utf-8

# In[1]:


from Video import *
warnings.filterwarnings('ignore')

""" Paths """
tutorial_path = 'PartD_E2'
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


# # Public Goods | Part D | Episode 2
# 

# ## Animation 0 | Intro Sequence
# 

# In[2]:


get_ipython().run_cell_magic('manim', 'animation_0', '\nclass animation_0(Scene):\n\n    def construct(self):\n        \n        """ Definitions """\n        \n        colors = sns.color_palette("Blues", 50).as_hex()\n\n        size = 1/6\n        n_width = 2\n        n_height = 3\n\n        n_rows = len(range(-n_height,n_height+1))\n        n_cols = len(range(-n_width,n_width+1))\n        w_list = list(range(-n_width,n_width+1))*n_rows\n        h_list = [i for i in range(-n_height,n_height+1) for x in \'a\'*n_cols]\n        block = list(zip(w_list,h_list)) # height: 7, width: 5\n        \n        string = \'MICROECONOMICS\'\n        letters = [raster_font[l] for l in string]\n        \n        """ Run """\n                \n        shift = 0\n        centering = -39\n        squares = []\n        for l in letters:\n            s = [Square(side_length=size, color=config.background_color).move_to(RIGHT*(w + shift*6 + centering)*size + DOWN*h*size) for w,h in [block[i] for i in l]]\n            squares = squares + s\n            shift = shift + 1\n        \n        Squares = VGroup(*squares)\n        \n        self.add(Squares)\n        \n        for i in range(5):\n            update_squares = [s.animate.set_fill(random.sample(colors,1),opacity=1) for s in squares]\n            self.play(*update_squares, run_time=1/10)\n            self.wait(4/10)\n            \n        part_label = Tex(\'{{Part D}} $|$ Public Goods\').set_color(GREY).set_color_by_tex_to_color_map(\n            {"Part D": RED,}\n        ).scale(1.5).next_to(Squares, DOWN)\n        group = VGroup(Squares, part_label)\n        self.play(FadeIn(part_label), group.animate.to_edge(UP, buff=3))\n        self.wait()\n')


# ## Animation 1 | Dumbledor Memorial

# In[4]:


get_ipython().run_cell_magic('manim', 'animation_1', '\nclass animation_1(Scene):\n    def construct(self):\n        \n        # set up the axis in the background\n        # set up five bar charts\n        # set up the cost line\n        # show what happens when the price is zero\n        # non-excludability, show how no one will pay when the price goes up\n        \n        # bring in a property tax\n        # talk about where it would need to be set to pay for the memorial\n        # talk about how it impacts each person\n        # talk about the socially efficient decision\n        \n        \n        # Set up the graph axes\n        x_axis = NumberLine(x_range=[0, 6, 1], include_tip=False, label_direction=DOWN)\n        y_axis = NumberLine(x_range=[0, 100, 10], include_tip=False)\n        graph_origin = x_axis.coords_to_point(0, 0)\n        graph_top = y_axis.coords_to_point(0, 100)\n        graph_height = graph_top[1] - graph_origin[1]\n        graph_width = x_axis.coords_to_point(6, 0)[0] - graph_origin[0]\n        graph_rect = Rectangle(height=graph_height, width=graph_width, stroke_width=2, fill_opacity=0.1, color=WHITE).move_to(graph_origin)\n        self.add(x_axis, y_axis, graph_rect)\n\n        # Define the data\n        mb_values = [20, 60, 70, 90, 90]\n        num_bars = len(mb_values)\n        bar_width = graph_width / num_bars\n        bars = VGroup()\n\n        # Create the bars and add them to the graph\n        for i in range(num_bars):\n            mb = mb_values[i]\n            bar_bottom = graph_origin[1]\n            bar_top = y_axis.coords_to_point(0, mb)\n            bar_height = bar_top[1] - bar_bottom\n            bar = Rectangle(height=bar_height, width=bar_width, stroke_width=2, fill_opacity=0.5, color=BLUE)\n            bar.move_to(graph_origin + i * bar_width * RIGHT)\n            bars.add(bar)\n            mb_label = MathTex(str(mb)).next_to(bar, UP, buff=0.1)\n            self.add(bar, mb_label)\n\n        # Create the price line and add it to the graph\n        price = 60\n        price_line = Line(x_axis.coords_to_point(0, price), x_axis.coords_to_point(num_bars, price), stroke_width=2, color=YELLOW)\n        self.add(price_line)\n\n        # Update the colors of the bars based on the price line\n        for i in range(num_bars):\n            mb = mb_values[i]\n            bar = bars[i]\n            if mb > price:\n                bar.set_color(RED)\n            else:\n                bar.set_color(GREEN)\n            diff = mb - price\n            diff_label = MathTex(str(diff)).next_to(bar, UP, buff=0.1).set_color(BLACK)\n            self.add(diff_label)\n\n        self.wait(2)\n')


# ### Merge and Convert Videos

# In[ ]:


video_path = config.media_dir+'/videos/Videos/1080p10/'

Make_MOV(video_path)

