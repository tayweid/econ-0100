"""Shared scene helpers for F26 animations.

Canonical home for helpers used by more than one animation file. Put this
directory on the path and import from it:

    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
    from scene_helpers import Raster_Font

Deliberately not named ``scenes``: ``Audio_Overview/`` already contains a
``scenes.py``, and a script's own directory precedes appended paths, so a
shared module by that name would be shadowed there.
"""

from manim import *


def Raster_Font(string):
    """Return a list of Squares spelling ``string`` in a 5x7 block font.

    Only the letters below are defined; any other character contributes no
    squares. Squares are background-coloured, so they read as holes punched
    out of whatever sits behind them.
    """
    raster_font = {
        'C': [1,2,3,5,9,10,15,20,25,29,31,32,33],
        'E': [0,1,2,3,4,5,10,15,16,17,18,20,25,30,31,32,33,34],
        'I': [1,2,3,7,12,17,22,27,31,32,33],
        'M': [0,4,5,6,8,9,10,12,14,15,19,20,24,25,29,30,34],
        'N': [0,4,5,6,9,10,12,14,15,18,19,20,24,25,29,30,34],
        'O': [1,2,3,5,9,10,14,15,19,20,24,25,29,31,32,33],
        'R': [0,1,2,3,5,9,10,14,15,16,17,18,20,23,25,29,30,34],
        'S': [1,2,3,5,9,10,16,17,18,24,25,29,31,32,33],
    }
    blocks_indecies = [raster_font.get(letter, []) for letter in string]

    # Block Settings
    block = []
    block_width, block_height = 2, 3
    for h in range(-block_height, block_height + 1):
        for w in range(-block_width, block_width + 1):
            block.append((w, h))

    # Location
    base_shift = 0
    base_center = -39
    block_size = 1/6

    squares = []
    for block_shift, block_indecies in enumerate(blocks_indecies, start=base_shift):
        for index in block_indecies:
            w, h = block[index]
            square = Square(side_length=block_size, color=config.background_color)
            square.move_to(RIGHT * (w + block_shift / block_size + base_center) * block_size + DOWN * h * block_size)
            squares.append(square)

    return squares
