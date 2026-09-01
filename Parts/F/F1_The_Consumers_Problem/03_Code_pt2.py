#!/usr/bin/env python
# coding: utf-8

# # Tutorial C2 | The Budget Constraint
# 
# This video introduces the budget constraint as a way to use prices to represent the inherent scarcity we face.
# 

# In[1]:


from Video import *
warnings.filterwarnings('ignore')

config.background_color = 'black'
config.media_dir = 'PartC_E2'


# ## Animation 1 | Budget Constraint
# 
# Introduce the budget constraint to define the choice set.

# In[2]:


get_ipython().run_cell_magic('manim', '-qh -v ERROR animation_1', '\nclass animation_1(Scene):\n    def construct(self):\n        axes = Axes(\n            x_range=[0, 20, 10],\n            x_length = 9,\n            #axis_config={"color": BLACK},\n            x_axis_config={\n                "numbers_to_include": [],#np.arange(0, 20, 10),\n                #"numbers_with_elongated_ticks": np.arange(0, 60, 10),\n                "decimal_number_config": {\n                    "num_decimal_places":0,\n                    #"color":ORANGE,\n                },\n            },\n            y_range=[0, 20, 10],\n            y_axis_config={\n                "numbers_to_include": [],#np.arange(0, 20, 10),\n                #"numbers_with_elongated_ticks": np.arange(0, 7, 1),\n                "decimal_number_config": {\n                    "num_decimal_places":0,\n                    #"color":GREEN,\n                }\n            },\n            tips=False,\n        )\n        # Labels for the x-axis and y-axis.\n        y_label = axes.get_y_axis_label("B")\n        x_label = axes.get_x_axis_label("A")\n        grid_labels = VGroup(x_label, y_label)\n        \n        bc = Tex("Definition.").move_to(UP*2).set_color(YELLOW)\n        bc_text_1 = Tex("Assuming that individuals can’t borrow or save,").next_to(bc, DOWN*2)\n        bc_text_2 = Tex("then the budget constraint is implicitly defined").next_to(bc_text_1, DOWN)\n        bc_text_3 = Tex("by the sum of expenditures.").next_to(bc_text_2, DOWN)\n        equation = Tex("$ Y = p_A q_A + p_B q_B $").next_to(bc_text_3, DOWN)\n        bc_group = VGroup(bc,bc_text_1,bc_text_2,bc_text_3,equation)\n        bc_subgroup = VGroup(bc,bc_text_1,bc_text_2,bc_text_3)\n        \n        self.play(FadeIn(bc))\n        self.play(AddTextWordByWord(bc_text_1, run_time=4), rate_func=linear)\n        self.play(AddTextWordByWord(bc_text_2, run_time=4), rate_func=linear)\n        self.play(AddTextWordByWord(bc_text_3, run_time=4), rate_func=linear)\n        self.play(AddTextWordByWord(equation, run_time=4), rate_func=linear)\n        \n        framebox = SurroundingRectangle(bc_group, buff = 0.3).set_color(BLUE)\n        self.play(Create(framebox),run_time=3)\n        framebox.flip(RIGHT)\n        self.play(Uncreate(framebox),run_time=3)\n\n        budget_equation = MathTex("p_A q_A","+","p_B q_B","=","Y").move_to(UP*2+RIGHT*2)\n        self.play(FadeOut(bc_subgroup))\n        self.play(Transform(equation,budget_equation))\n\n        self.add(axes, grid_labels)\n        p_a = 1\n        p_b = 1\n        Y = 15\n        def budget_curve(a):\n            return (Y-p_a*a)/p_b\n        \n        budget = axes.get_graph(budget_curve, color=PURPLE, x_range=(0, Y/p_b))\n        \n        self.play(Create(budget),FadeIn(budget_equation))\n        \n        pointer_value = ValueTracker(10)\n        \n        def move_the_dot():\n            x = pointer_value.get_value()\n            x_int = axes.coords_to_point(x,0)\n            x_label = DecimalNumber(num_decimal_places=2).set_color(BLUE).next_to(x_int,DOWN).set_value(x)\n            y = budget_curve(x)\n            y_int = axes.coords_to_point(0,y)\n            y_label = DecimalNumber(num_decimal_places=2).set_color(GREEN).next_to(y_int,LEFT).set_value(y)\n            p = axes.coords_to_point(x,y)\n            dot = Dot(p).set_color(YELLOW)\n            vline = DashedLine(x_int,p).set_color(GREY)\n            hline = DashedLine(y_int,p).set_color(GREY)\n            return VGroup(dot,vline,hline,x_label,y_label)\n        \n        moving_dot = always_redraw(move_the_dot)\n        \n        self.add(moving_dot)\n        self.play(pointer_value.animate.set_value(3),run_time=2)\n        self.play(pointer_value.animate.set_value(11),run_time=2)\n        \n        blur_background = Rectangle(height=50,width=50).set_fill(BLACK, opacity=0.8)\n        self.play(FadeIn(blur_background))\n        \n        mrt = Tex("Definition.").move_to(UP*2).set_color(YELLOW)\n        mrt_text_1 = Tex("Marginal Rate of Transformation ($ MRT $)").next_to(mrt, DOWN*2)\n        mrt_text_2 = Tex(" is the slope of the budget line.").next_to(mrt_text_1, DOWN)\n        equation = Tex("$ MRT = -\\\\frac{p_A}{p_B} $").next_to(mrt_text_2, DOWN)\n        mrt_group = VGroup(mrt,mrt_text_1,mrt_text_2,equation)\n        mrt_subgroup = VGroup(mrt,mrt_text_1,mrt_text_2)\n        \n        self.play(FadeIn(mrt))\n        self.play(AddTextWordByWord(mrt_text_1, run_time=4), rate_func=linear)\n        self.play(AddTextWordByWord(mrt_text_2, run_time=4), rate_func=linear)\n        self.play(AddTextWordByWord(equation, run_time=4), rate_func=linear)\n        \n        framebox = SurroundingRectangle(mrt_group, buff = 0.3).set_color(BLUE)\n        self.play(Create(framebox),run_time=3)\n        framebox.flip(RIGHT)\n        self.play(Uncreate(framebox),run_time=3)\n        self.play(FadeOut(blur_background),FadeOut(mrt_group))\n        \n        self.play(pointer_value.animate.set_value(2),run_time=2)\n        self.play(pointer_value.animate.set_value(14),run_time=2)\n')


# ### Convert MP4 Videos to MOV

# In[ ]:


video_path = config.media_dir+'/videos/tutorials/1080p60/'

manim_to_mov(video_path)

