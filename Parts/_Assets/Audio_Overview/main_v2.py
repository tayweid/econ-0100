# main.py
from manim import config

# Custom Paths
config.media_dir = "./other_media"
config.video_dir = "./ANIMATIONS"
config.images_dir = "./other_media/images"
config.text_dir = "./other_media/text"

# Custom Colors
CUSTOM_BLACK = '#1f1f1f'
CUSTOM_GREY = '#696969'
DEFINITION = '#FFD700'
config.background_color = CUSTOM_BLACK
config.axes_color = CUSTOM_GREY

# Frame Rate/Resolution
FPS = 10
PIXEL_HEIGHT = 1080
config.frame_rate = FPS
config.pixel_height = PIXEL_HEIGHT
config.pixel_width = PIXEL_HEIGHT * 2

from scenes_v2 import *

if __name__ == "__main__":

    part_chapter = [
        ('Part A', 'Chapter 1'),
        ('Part A', 'Chapter 2'),
        ('Part A', 'Chapter 3'),
        ('Part B', 'Chapter 4'),
        ('Part B', 'Chapter 5'),
        ('Part B', 'Chapter 6'),
        ('Part B', 'Chapter 7'),
        ('Part C', 'Chapter 8'),
        ('Part B', 'Chapter 9'),
        ('Part C', 'Chapter 10'),
        ('Part D', 'Chapter 11'),
        ('Part C', 'Chapter 12'),
        ('Part A', 'Chapter 13'),
        ('Part A', 'Chapter 14'),
        ('Part A', 'Chapter 15'),
        ('Part A', 'Chapter 16'),
        ('Part A', 'Chapter 17'),
        ('Part A', 'Chapter 18'),
        ('Part A', 'Chapter 19'),
        ('Part F', 'Chapter 21'),
    ]

    for part, chpater in part_chapter:
        config.output_file = f"{chpater.replace(' ','_')}_Intro"
        scene = Overview()
        scene.construct(f'{part}',f'{chpater}')
        scene.Intro()
        scene.render()

        config.output_file = f"{chpater.replace(' ','_')}_Loop"
        scene = Overview()
        scene.construct(f'{part}',f'{chpater}')
        scene.Loop()
        scene.render()





