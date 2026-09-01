#!/usr/bin/env python
# coding: utf-8

# In[2]:


from Video import *
warnings.filterwarnings('ignore')

""" Paths """
tutorial_path = 'PartC_E3'
if not os.path.exists(tutorial_path):
    os.makedirs(tutorial_path)
config.media_dir = tutorial_path
config.verbosity = 'ERROR'

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


# # Public Goods | Episode 3 | Part C
# 
# This video does a simulation of public goods, and maps it into game theory, using a Lindhal equilibrium, and using voting.
# 

# ## Animation 1 | Animation Name
# 
# This is the description of the animation and what it aims to accomplish. 

# ## Tutorial 4.3 | Public Goods and Voting

# In[ ]:


# Taxonomy
# Public goods 


# ## Tutorial 4.4 | Baby Game Theory and the Tragedy of the Commons

# ### Convert MP4 Videos to MOV

# In[ ]:


video_path = config.media_dir+'/videos/tutorials/1080p60/'

manim_to_mov(video_path)

