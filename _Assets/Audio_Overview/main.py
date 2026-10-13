# main.py
from manim import config
from scenes import Overview

if __name__ == "__main__":
    config.media_dir = "./other_media"
    config.video_dir = "./ANIMATIONS"
    config.verbosity = 'ERROR'

    # Set custom colors
    CUSTOM_BLACK = '#1f1f1f'
    CUSTOM_GREY = '#696969'
    DEFINITION = '#FFD700'
    config.background_color = CUSTOM_BLACK
    config.axes_color = CUSTOM_GREY

    # Set frame and resolution settings
    PIXEL_HEIGHT = 1080
    FPS = 10
    config.pixel_height = PIXEL_HEIGHT
    config.pixel_width = PIXEL_HEIGHT * 2
    config.frame_rate = FPS
    
    # Create an instance of HelloWorld
    scene = Overview()
    scene.construct()
    scene.play_intro()

    scene.render()