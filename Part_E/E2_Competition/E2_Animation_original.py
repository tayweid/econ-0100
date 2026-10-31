# maniml E2_Animation_original.py PerfectCompA
# Faithful first-pass port of the old E2 code (03_Code.py, classes PerfectCompA
# and PerfectCompB; the old Monopoly class belongs to the E3 port). Scenes:
#   PerfectCompA  "Tutorial 5.2 | Perfect Competition": Week 5 outline intro;
#                 the firm's MC = q and ATC = q/2 + 1000/q with a right-hand
#                 legend; price 80 as the flat MR/MPB; TR and TC boxes, then the
#                 profit rectangle (PROFIT = TR - TC = Q (P - ATC)); q stepped
#                 10 -> 100 and back to 80 with q / ATC / MC readouts and profit.
#   PerfectCompB  "MC = MR" -> "Can competitive firms maintain profits?"; market
#                 (left, MPB = 100 - Q, S = Q/alpha) beside the firm (right) at
#                 P = 80; supply shifts (alpha) carry the market price to min
#                 ATC and the firm's profit to zero; closes on "In the long run,
#                 competitive firms earn zero profit."
# PORT: no _Assets import; the header is here because the old file imports
# seaborn (and pandas), which the ManimLive environment provides.
# /// script
# requires-python = ">=3.11"
# dependencies = ["seaborn==0.13.2"]
# ///

from manim import *

# ---- PORT: GraphScene compatibility (maniml has no GraphScene)
# ============================================================================
# GraphScene compatibility shim: 2019-20 3b1b manimlib API -> maniml
# ----------------------------------------------------------------------------
# Paste this block right after `from manim import *` in a ported file, so the
# file stays self-contained. It provides what the old Part E scenes used:
#   GraphScene (CONFIG dicts, setup_axes, coords_to_point, point_to_coords,
#   get_graph, input_to_graph_point, get_vertical_line_to_graph, ...),
#   TextMobject / TexMobject, and the old 3b1b palette. The lost
#   tutorials.py metaConfig* dicts are reconstructed above each scene class.
# Frame: 2:1 (2160x1080), frame height 8, so every old coordinate lands where
# it did; the old 16:9 videos were 14.2 units wide, this frame is 16.
# A GraphScene draws on black (#000000) whatever config.background_color
# says; set "background_color": None in a CONFIG to leave the config alone.
# ============================================================================
import re as _gs_re
import copy as _gs_copy
import numpy as np
from maniml.mobject.functions import ParametricCurve   # not star-exported

config.pixel_height = 1080
config.pixel_width = 2160
# `from manim import *` copied the 16:9 frame constants into this file before
# the line above widened the frame; refresh this file's copies.
ASPECT_RATIO = config.aspect_ratio
FRAME_WIDTH = config.frame_width
FRAME_X_RADIUS = FRAME_WIDTH / 2
FRAME_SHAPE = (FRAME_WIDTH, config.frame_height)
LEFT_SIDE = FRAME_X_RADIUS * LEFT
RIGHT_SIDE = FRAME_X_RADIUS * RIGHT

# Old 3b1b palette, pinned as hex so a later `from style import *` (which
# shadows BLUE, GREEN, ...) cannot recolor the original-look scenes.
OLD_WHITE = "#FFFFFF"
OLD_BLACK = "#000000"
OLD_GREY = "#888888"
OLD_LIGHT_GREY = "#BBBBBB"
OLD_DARK_GREY = "#444444"
OLD_BLUE = "#58C4DD"
OLD_TEAL = "#5CD0B3"
OLD_GREEN = "#83C167"
OLD_YELLOW = "#FFFF00"
OLD_GOLD = "#F0AC5F"
OLD_ORANGE = "#FF862F"
OLD_RED = "#FC6255"
OLD_MAROON = "#C55F73"
OLD_PURPLE = "#9A72AC"
OLD_PINK = "#D147BD"
# Old names maniml dropped
LIGHT_GREY = globals().get("LIGHT_GREY", OLD_LIGHT_GREY)
DARK_GREY = globals().get("DARK_GREY", OLD_DARK_GREY)

config.background_color = OLD_BLACK


# ---------------------------------------------------------------- text
def _gs_old_text(s):
    """Old TextMobject source -> maniml Tex source.
    $$...$$ (display math inside text) becomes $\\displaystyle ...$; outside
    math, | < > become math glyphs (the old template was T1-encoded, maniml's
    is OT1, where a bare | prints as an em dash)."""
    s = _gs_re.sub(r"\$\$(.+?)\$\$",
                   lambda m: "$\\displaystyle " + m.group(1).strip() + "$",
                   s, flags=_gs_re.S)
    parts = _gs_re.split(r"(?<!\\)\$", s)   # even indices are text, odd are math
    for i in range(0, len(parts), 2):
        parts[i] = _gs_re.sub(r"(?<!\\)([|<>])", r"$\1$", parts[i])
    return "$".join(parts)


# PORT: the old TextMobject/TexMobject scaled TeX by 0.05; maniml's Tex scales
# by 0.001 x font_size, so its default 48 draws text 4% small. 50 matches the
# 2020 video (YN4ZkPBS_O8: title 8.96 units wide; 8.60 at font_size 48).
_GS_OLD_FONT_SIZE = 50


class TextMobject(Tex):
    """Old TextMobject: text mode, $...$ for math, args joined with no space."""

    def __init__(self, *text_parts, **kwargs):
        kwargs.setdefault("color", OLD_WHITE)
        kwargs.setdefault("font_size", _GS_OLD_FONT_SIZE)
        super().__init__(_gs_old_text("".join(str(t) for t in text_parts)), **kwargs)


class TexMobject(MathTex):
    """Old TexMobject: math mode (align*), args joined with a space."""

    def __init__(self, *tex_strings, **kwargs):
        kwargs.setdefault("color", OLD_WHITE)
        kwargs.setdefault("font_size", _GS_OLD_FONT_SIZE)
        strings = [str(t) for t in tex_strings]
        if len(strings) > 1:
            # maniml isolates each arg; a lone control symbol (\; \, \!) or a
            # blank arg can't be isolated (LaTeX error), so leave those out.
            isolate = kwargs.pop("isolate", [])
            isolate = [isolate] if isinstance(isolate, str) else list(isolate)
            isolate += [s for s in strings
                        if s.strip() and not _gs_re.fullmatch(r"\s*\\[^a-zA-Z]\s*", s)]
            super().__init__(" ".join(strings), isolate=isolate, **kwargs)
        else:
            super().__init__(*strings, **kwargs)


# PORT: an old Line with no color was WHITE; maniml's VMobject stroke defaults
# to GREY_A (#DDDDDD). The q guide, DashedVMobject(Line(qP, qPX)), reads pure
# white (255) in YN4ZkPBS_O8.
_gs_maniml_Line = Line


class Line(_gs_maniml_Line):
    """Old Line: stroke defaults to WHITE."""

    def __init__(self, *args, **kwargs):
        if kwargs.get("color") is None and kwargs.get("stroke_color") is None:
            kwargs["color"] = OLD_WHITE
        super().__init__(*args, **kwargs)


class ParametricFunction(ParametricCurve):
    """Old ParametricFunction(function, t_min=0, t_max=1, step_size=0.01)."""

    def __init__(self, function, t_min=0, t_max=1, step_size=0.01, **kwargs):
        super().__init__(function, t_range=(t_min, t_max, step_size), **kwargs)


# ---------------------------------------------------------------- CONFIG
def _gs_merge(base, extra):
    out = dict(base)
    for k, v in extra.items():
        if isinstance(v, dict) and isinstance(out.get(k), dict):
            out[k] = _gs_merge(out[k], v)
        else:
            out[k] = v
    return out


# Default course palette for the shim's GraphScene (read off the 2020 videos;
# entries marked "guess" never appear on screen in a surviving frame). Each
# scene's reconstructed metaConfig* below restates the colors it uses.
_gs_palette = {
    "mc_color": OLD_GREEN,
    "supply_color": OLD_GREEN,      # MC in the cost scenes
    "atc_color": OLD_BLUE,          # Perfect Competition; Monopoly uses orange
    "mr_color": OLD_PINK,
    "mpb_color": OLD_BLUE,
    "pq_color": OLD_PINK,           # guess (price line, built but never shown)
    "tc_color": OLD_ORANGE,
    "avc_color": OLD_YELLOW,        # guess
    "func_color": OLD_BLUE,         # guess (production function)
    "profit_color": OLD_RED,
    "gov_color": OLD_YELLOW,        # DWL/GOV fill (dark olive at 0.1 opacity)
    "dwl_color": OLD_GREY,          # DWL outline
    "result_color": OLD_YELLOW,     # guess
}

class GraphScene(Scene):
    """The old manimlib GraphScene on maniml.

    CONFIG dicts merge down the class hierarchy (subclass wins, nested dicts
    merge) and land as attributes, as digest_config did. Defaults are the
    manimlib ones except the axis grid, which is the course's: Q 0-100 over 8
    units, P 0-100 over 5 units, ticks only at the ends, grey axes, Q/P
    labels, the shared palette above."""

    CONFIG = _gs_merge({
        "x_min": 0,
        "x_max": 100,
        "x_axis_width": 8,
        "x_tick_frequency": 100,
        "x_leftmost_tick": None,
        "x_labeled_nums": None,
        "x_axis_label": "$Q$",
        "y_min": 0,
        "y_max": 100,
        "y_axis_height": 5,
        "y_tick_frequency": 100,
        "y_bottom_tick": None,
        "y_labeled_nums": None,
        "y_axis_label": "$P$",
        "axes_color": OLD_GREY,
        "graph_origin": 2.5 * DOWN + 4 * LEFT,
        "exclude_zero_label": True,
        "default_graph_colors": [OLD_BLUE, OLD_GREEN, OLD_YELLOW],
        "default_derivative_color": OLD_GREEN,
        "default_input_color": OLD_YELLOW,
        "num_graph_anchor_points": 100,
        "tick_size": 0.1,
        "axes_stroke_width": 4,
        "graph_stroke_width": 4,
        "number_font_size": 36,     # old number_scale_val 0.75
        "background_color": OLD_BLACK,
    }, _gs_palette)

    _gs_reserved = {"camera_config", "file_writer_config", "window", "camera",
                    "frame", "mobjects", "time", "file_writer"}

    def __init__(self, *args, **kwargs):
        merged = {}
        for klass in reversed(type(self).__mro__):
            cfg = klass.__dict__.get("CONFIG")
            if isinstance(cfg, dict):
                merged = _gs_merge(merged, cfg)
        bg = merged.get("background_color",
                        (merged.get("camera_config") or {}).get("background_color"))
        if bg is not None:
            self.default_camera_config = dict(type(self).default_camera_config,
                                              background_color=bg)
        super().__init__(*args, **kwargs)
        for key, value in merged.items():
            if key not in self._gs_reserved:
                setattr(self, key, _gs_copy.deepcopy(value))
        if bg is not None:
            self.set_background_color(bg)
        self._gs_color_index = 0
        self._gs_axes_cache = {}

    # ------------------------------------------------------------ axes
    def _gs_number_line(self, lo, hi, length, freq, first_tick, elongated, to_number):
        line = NumberLine(
            x_range=(lo, hi, freq), width=length, color=self.axes_color,
            stroke_width=self.axes_stroke_width, include_ticks=False,
            include_tip=False, line_to_number_direction=to_number,
        )
        ticks = VGroup()
        start = lo if first_tick is None else first_tick
        for x in np.arange(start, hi + freq / 2, freq):
            big = any(np.isclose(x, e) for e in elongated)
            ticks.add(line.get_tick(x, self.tick_size * (2 if big else 1)))
        line.add(ticks)
        line.ticks = ticks
        line.tick_marks = ticks
        return line

    def _gs_on_screen(self, mob):
        return any(f is mob for m in self.mobjects for f in m.get_family())

    def setup_axes(self, animate=False):
        origin = np.array(self.graph_origin, dtype=float)
        x_nums = list(self.x_labeled_nums or [])
        y_nums = list(self.y_labeled_nums or [])
        key = (tuple(np.round(origin, 6)), self.x_min, self.x_max, self.x_axis_width,
               self.x_tick_frequency, self.x_leftmost_tick, tuple(x_nums), self.x_axis_label,
               self.y_min, self.y_max, self.y_axis_height, self.y_tick_frequency,
               self.y_bottom_tick, tuple(y_nums), self.y_axis_label, str(self.axes_color))
        cached = self._gs_axes_cache.get(key)
        if not animate and cached is not None and self._gs_on_screen(cached):
            # Old setup_axes() stacked a fresh copy on every call; reuse the
            # identical one already on screen, so FadeOut(self.axes) clears it.
            # PORT: re-add it so it moves to the top, where the old fresh copy
            # was drawn (PerfectCompB's axes sit over its profit box's edge).
            self.add(cached)
            self.axes = cached
            self.x_axis, self.y_axis = cached
            return

        x_axis = self._gs_number_line(self.x_min, self.x_max, self.x_axis_width,
                                      self.x_tick_frequency, self.x_leftmost_tick,
                                      x_nums, DOWN)
        x_axis.shift(origin - x_axis.number_to_point(0))
        if x_nums:
            if self.exclude_zero_label:
                x_nums = [x for x in x_nums if x != 0]
            x_axis.add_numbers([round(x, 4) for x in x_nums], excluding=[],
                               font_size=self.number_font_size)
        if self.x_axis_label:
            x_label = TextMobject(self.x_axis_label)
            x_label.next_to(x_axis.ticks if len(x_axis.ticks) else x_axis,
                            UP + RIGHT, buff=SMALL_BUFF)
            x_label.shift_onto_screen()
            x_axis.add(x_label)
            self.x_axis_label_mob = x_label

        y_axis = self._gs_number_line(self.y_min, self.y_max, self.y_axis_height,
                                      self.y_tick_frequency, self.y_bottom_tick,
                                      y_nums, LEFT)
        y_axis.shift(origin - y_axis.number_to_point(0))
        y_axis.rotate(np.pi / 2, about_point=y_axis.number_to_point(0))
        if y_nums:
            if self.exclude_zero_label:
                y_nums = [y for y in y_nums if y != 0]
            y_axis.add_numbers([round(y, 4) for y in y_nums], excluding=[],
                               font_size=self.number_font_size)
        if self.y_axis_label:
            y_label = TextMobject(self.y_axis_label)
            y_label.next_to(y_axis.get_corner(UP + RIGHT), UP + RIGHT, buff=SMALL_BUFF)
            y_label.shift_onto_screen()
            y_axis.add(y_label)
            self.y_axis_label_mob = y_label

        axes = VGroup(x_axis, y_axis)
        if animate:
            self.play(Write(axes))
        else:
            self.add(axes)
        self.axes = axes
        self.x_axis, self.y_axis = x_axis, y_axis
        self._gs_axes_cache[key] = axes

    # ------------------------------------------------------------ coordinates
    def coords_to_point(self, x, y):
        assert hasattr(self, "x_axis") and hasattr(self, "y_axis"), \
            "call setup_axes() before coords_to_point()"
        result = self.x_axis.number_to_point(x)[0] * RIGHT
        result += self.y_axis.number_to_point(y)[1] * UP
        return result

    c2p = coords_to_point

    def point_to_coords(self, point):
        return (self.x_axis.point_to_number(point),
                self.y_axis.point_to_number(point))

    p2c = point_to_coords

    # ------------------------------------------------------------ graphs
    def _gs_next_graph_color(self):
        colors = list(self.default_graph_colors) or [OLD_BLUE]
        i = getattr(self, "_gs_color_index", 0)
        self._gs_color_index = i + 1
        return colors[i % len(colors)]

    def get_graph(self, func, color=None, x_min=None, x_max=None, **kwargs):
        if color is None:
            color = self._gs_next_graph_color()
        x_min = self.x_min if x_min is None else x_min
        x_max = self.x_max if x_max is None else x_max
        n = kwargs.pop("num_graph_anchor_points", self.num_graph_anchor_points)
        step_size = kwargs.pop("step_size", None)     # old alpha step
        if step_size:
            n = max(1, int(round(1 / step_size)))
        kwargs.setdefault("stroke_width", self.graph_stroke_width)
        y_cap = self.y_max

        def point(x):
            y = func(x)
            if not np.isfinite(y):
                y = y_cap
            return self.coords_to_point(x, y)

        lo, hi = sorted((float(x_min), float(x_max)))
        if hi - lo < 1e-9:
            # x_min == x_max: a zero-length curve, so it can Transform out later
            p = point(lo)
            graph = VMobject(color=color, **kwargs)
            graph.set_points_as_corners([p, p])
        else:
            graph = ParametricCurve(point, t_range=(lo, hi, (hi - lo) / n),
                                    color=color, **kwargs)
            if x_max < x_min:
                graph.reverse_points()
        graph.underlying_function = func
        graph.x_range = (x_min, x_max)
        return graph

    def input_to_graph_point(self, x, graph):
        return self.coords_to_point(x, graph.underlying_function(x))

    def angle_of_tangent(self, x, graph, dx=0.01):
        vect = self.input_to_graph_point(x + dx, graph) - self.input_to_graph_point(x, graph)
        return angle_of_vector(vect)

    def slope_of_tangent(self, *args, **kwargs):
        return np.tan(self.angle_of_tangent(*args, **kwargs))

    def get_vertical_line_to_graph(self, x, graph, line_class=Line, **line_kwargs):
        line_kwargs.setdefault("color", graph.get_color())
        return line_class(self.coords_to_point(x, 0),
                          self.input_to_graph_point(x, graph), **line_kwargs)

    def get_vertical_lines_to_graph(self, graph, x_min=None, x_max=None,
                                    num_lines=20, **kwargs):
        x_min = self.x_min if x_min is None else x_min
        x_max = self.x_max if x_max is None else x_max
        return VGroup(*[self.get_vertical_line_to_graph(x, graph, **kwargs)
                        for x in np.linspace(x_min, x_max, num_lines)])
# ======================================================= end GraphScene shim

import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random

import warnings
# Configuration
config.background_color = 'white'
# PORT: the line above is kept as written, but the old videos are on black;
# the shim's GraphScene sets each scene's background from its CONFIG (black).

# PORT: reconstructed; tutorials.metaConfig* is lost. Axis grid, origin and
# colors read off the Tutorial 5.2 thumbnail (YN4ZkPBS_O8): Q 0-100 over 8
# units, P 0-100 over 5, ticks only at the ends, grey axes with Q/P labels,
# origin 3.3 DOWN + 5 LEFT (the same value intro_sequence sets), so the legend
# lines at Q = 125 sit at the right edge as in the video.
metaConfigPerfectCompA = {
    "x_min": 0,
    "x_max": 100,
    "x_axis_width": 8,
    "x_tick_frequency": 100,
    "x_axis_label": "$Q$",
    "y_min": 0,
    "y_max": 100,
    "y_axis_height": 5,
    "y_tick_frequency": 100,
    "y_axis_label": "$P$",
    "graph_origin": 3.3 * DOWN + 5 * LEFT,
    "axes_color": OLD_GREY,
    "background_color": OLD_BLACK,
    "mc_color": OLD_GREEN,
    "atc_color": OLD_BLUE,
    "mr_color": OLD_PINK,
    "pq_color": OLD_PINK,       # guess: the price graph self.P is built, never shown
    "tc_color": OLD_ORANGE,     # guess: TC is orange in Tutorial 5.1
    "profit_color": OLD_RED,
}

class PerfectCompA(GraphScene):
    CONFIG = metaConfigPerfectCompA

    """Tutorial 5.2 | Perfect Competition"""

    def construct(self):
        self.intro_sequence()
        self.wait(3)
        self.drawCosts()
        self.wait(3)
        self.drawMR(80)

    def intro_sequence(self):
        title = TextMobject("Week 5 Outline").scale(1.5)
        self.play(FadeIn(title))
        transform_title = TextMobject("Week 5 Outline").scale(1.2)
        tutorial_1 = TextMobject("Tutorial 5.1 | Production Costs")
        tutorial_1.to_edge(4*UP+LEFT).set_color(GREY)
        tutorial_2 = TextMobject("Tutorial 5.2 | Competitive Firms")
        tutorial_2.to_edge(6*UP+LEFT).set_color(GREY)
        tutorial_3 = TextMobject("Tutorial 5.3 | Monopoly")
        tutorial_3.to_edge(8*UP+LEFT).set_color(GREY)
        tutorial_4 = TextMobject("Tutorial 5.4 | Monopolistic Competition")
        tutorial_4.to_edge(10*UP+LEFT).set_color(GREY)
        tutorial_5 = TextMobject("Tutorial 5.5 | Oligopoly and Duopoly")
        tutorial_5.to_edge(12*UP+LEFT).set_color(GREY)
        self.play(Transform(title, transform_title.to_corner(UP)),
                  FadeIn(tutorial_1), FadeIn(tutorial_2), FadeIn(tutorial_3), FadeIn(tutorial_4), FadeIn(tutorial_5))
        self.wait(3)
        transform_title = TextMobject("Tutorial 5.2 | Perfect Competition").scale(1.2)
        self.play(Transform(tutorial_2, transform_title.to_corner(UP)),
                  FadeOut(title),FadeOut(tutorial_1),FadeOut(tutorial_3),FadeOut(tutorial_4),FadeOut(tutorial_5))
        
        self.graph_origin = 3.3*DOWN + 5*LEFT
        self.setup_axes()
        
        
    def drawCosts(self):        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        
        # MC
        a = self.coords_to_point(125, 80)
        b = self.coords_to_point(125, 65)
        self.MCL = Line(a,b, color=self.mc_color)
        self.MCD = TextMobject("MC").set_color(self.mc_color)
        self.MCD.next_to(self.MCL)
        self.play(ShowCreation(self.MC),ShowCreation(self.MCL),ShowCreation(self.MCD))
        
        # ATC
        a = self.coords_to_point(125, 60)
        b = self.coords_to_point(125, 45)
        self.ATCL = Line(a,b, color=self.atc_color)
        self.ATCD = TextMobject("ATC").set_color(self.atc_color)
        self.ATCD.next_to(self.ATCL)
        self.play(ShowCreation(self.ATC),ShowCreation(self.ATCL),ShowCreation(self.ATCD))
        
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))
        self.play(FadeIn(self.minatc))
    
    def drawMR(self,p):
        # MR
        self.MRF = lambda q : p
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=1, x_max=100)
        self.PD = TextMobject("P="+str(p)).set_color(self.mr_color).scale(0.8)
        self.PD.next_to(self.MR,LEFT)
        self.MBD = TextMobject("MPB").set_color(self.mr_color).scale(0.8)
        self.MBD.next_to(self.MR,RIGHT)

        # PRICE
        self.PF = lambda q : p
        self.P = self.get_graph(lambda x : self.PF(x), color=self.pq_color, x_min=10, x_max=100)
        
        # INITIAL QUANTITY
        q = 10
        atc = self.ATCF(q)
        mc = self.MCF(q)
        
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # LINES
        self.qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        self.qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        self.atcD = TextMobject("ATC ="+str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        self.mcLine = DashedVMobject(Line(mcP,mcPX, color=self.axes_color))
        self.mcD = TextMobject("MC ="+str(int(mc))).set_color(self.mc_color).scale(0.8)
        self.mcD.next_to(self.mcLine,LEFT)
        
        self.play(FadeIn(self.qLine),FadeIn(self.qD),
                  FadeIn(self.atcD),FadeIn(self.mcLine),FadeIn(self.mcD))
        
        # MR
        a = self.coords_to_point(125, 100)
        b = self.coords_to_point(125, 85)
        self.MRL = Line(a,b, color=self.mr_color)
        self.MRD = TextMobject("MR").set_color(self.mr_color)
        self.MRD.next_to(self.MRL)
        self.play(ShowCreation(self.PD),ShowCreation(self.MBD),ShowCreation(self.MR),ShowCreation(self.MRL),ShowCreation(self.MRD))
        
        # TR & TC
        a = self.coords_to_point(1, 1)
        b = self.coords_to_point(1, p)
        c = self.coords_to_point(q-1, p)
        d = self.coords_to_point(q-1, 1)
        self.TRArea = Polygon(a,b,c,d, fill_opacity = 0, fill_color = self.mr_color, color=self.mr_color)

        a = self.coords_to_point(0, 0)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, 0)
        self.TCArea = Polygon(a,b,c,d, fill_opacity = 0, fill_color = self.tc_color, color=self.tc_color)
        
        self.play(ShowCreation(self.TRArea),ShowCreation(self.TCArea))
        self.wait(3)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(20, 120)
        b = self.coords_to_point(20, 105)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("PROFIT = TR - TC").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)

        self.play(ShowCreation(self.PROFArea),FadeIn(self.PROFL),FadeIn(self.PROFD))
        self.wait(3)
        
        # REFRAME PROFIT
        PROFD = TextMobject("PROFIT = Q (P - ATC)").set_color(self.profit_color).scale(0.8)
        PROFD.next_to(self.PROFL,RIGHT)
        self.play(Transform(self.PROFD,PROFD))
        self.wait(3)
        
        PROFD = TextMobject("PROFIT =").set_color(self.profit_color).scale(0.8)
        PROFD.next_to(self.PROFL,RIGHT)
        
        PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(PROFD,RIGHT)
        self.play(Transform(self.PROFD,PROFD),ReplacementTransform(self.TCArea,self.PROFN),FadeOut(self.TRArea))
        
        # UPDATE SEQUENCE
        q_list = list(np.arange(10,110,10)) + [90,80]
        for q in q_list:
            atc = self.ATCF(q)
            mc = self.MCF(q)

            qP = self.coords_to_point(q, 0)
            qPX = self.coords_to_point(q, max(atc,mc))
            atcP = self.coords_to_point(q, atc)
            atcPX = self.coords_to_point(0, atc)
            mcP = self.coords_to_point(q, mc)
            mcPX = self.coords_to_point(0, mc)

            qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
            qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
            qD.next_to(qLine,DOWN)

            atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
            atcD = TextMobject("ATC ="+str(int(atc))).set_color(self.atc_color).scale(0.8)
            atcD.next_to(atcLine,LEFT)

            mcLine = DashedVMobject(Line(mcP,mcPX, color=self.axes_color))
            mcD = TextMobject("MC ="+str(int(mc))).set_color(self.mc_color).scale(0.8)
            mcD.next_to(mcLine,LEFT)
            
            # PROFIT
            a = self.coords_to_point(0, p)
            b = self.coords_to_point(0, atc)
            c = self.coords_to_point(q, atc)
            d = self.coords_to_point(q, p)
            PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
            PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
            PROFN.next_to(self.PROFD,RIGHT)
            
            self.play(Transform(self.qLine,qLine),Transform(self.qD,qD),
                      Transform(self.atcD,atcD),Transform(self.mcLine,mcLine),Transform(self.mcD,mcD),
                      Transform(self.PROFArea,PROFArea),Transform(self.PROFN,PROFN))
            self.wait(3)
        
        # CLOSE OUT
        self.play(FadeOut(self.qLine),FadeOut(self.qD),FadeOut(self.atcLine),FadeOut(self.atcD),FadeOut(self.mcLine),FadeOut(self.mcD),
                  FadeOut(self.MR),FadeOut(self.MRL),FadeOut(self.MRD),
                  FadeOut(self.PD),FadeOut(self.MBD),
                  FadeOut(self.MC),FadeOut(self.MCL),FadeOut(self.MCD),
                  FadeOut(self.ATC),FadeOut(self.ATCL),FadeOut(self.ATCD),
                  FadeOut(self.PROFL),FadeOut(self.PROFD),FadeOut(self.PROFArea),FadeOut(self.PROFN),
                  FadeOut(self.minatc),FadeOut(self.axes))



# PORT: reconstructed; tutorials.metaConfig* is lost. PerfectCompB's CONFIG
# line was already commented out in the old file (its last saved notebook run
# stopped at a NameError before drawing anything), so there is no frame of
# this scene to measure. Colors are PerfectCompA's. The axis size is worked
# out from the code's own coordinates: the market sits at 6 LEFT and the firm
# at 1 RIGHT, so each graph must be narrower than 7 units; with Q 0-100 over
# 5 units the market's dashed price line (drawn to Q = 125) stops just short
# of the firm's price label, and the firm's MC/ATC/MR labels at Q = 100 end
# inside the old 16:9 frame (x < 7.1). P 0-100 over 4 units keeps the Pi*
# legend (P = 115-130 on the firm's axes) clear of the title.
metaConfigPerfectCompB = {
    "x_min": 0,
    "x_max": 100,
    "x_axis_width": 5,
    "x_tick_frequency": 100,
    "x_axis_label": "$Q$",
    "y_min": 0,
    "y_max": 100,
    "y_axis_height": 4,
    "y_tick_frequency": 100,
    "y_axis_label": "$P$",
    "graph_origin": 3 * DOWN + RIGHT,   # initialize() resets it before each graph
    "axes_color": OLD_GREY,
    "background_color": OLD_BLACK,
    "mc_color": OLD_GREEN,
    "atc_color": OLD_BLUE,
    "mr_color": OLD_PINK,
    "profit_color": OLD_RED,
    "result_color": OLD_YELLOW,  # guess: E1's result sentences are yellow
}

class PerfectCompB(GraphScene):
    #CONFIG = metaConfigPerfectCompB
    # PORT: activated; the scene reads self.mc_color, self.result_color, ...,
    # which only a metaConfig ever supplied.
    CONFIG = metaConfigPerfectCompB

    def construct(self):
        self.intro_sequence()
        self.initialize(80)
        self.competitiveMarkets(2)
        equilibrium_alpha = np.sqrt(2000)/(100-np.sqrt(2000))
        self.competitiveMarkets(equilibrium_alpha+0.2)
        self.competitiveMarkets(equilibrium_alpha+0.3)
        self.competitiveMarkets(equilibrium_alpha+0.4)
        self.competitiveMarkets(equilibrium_alpha+0.5)
        self.competitiveMarkets(equilibrium_alpha+0.45)
        self.competitiveMarkets(equilibrium_alpha+0.44)
        self.competitiveMarkets(equilibrium_alpha+0.43)
        self.competitiveMarkets(equilibrium_alpha+0.42)
        self.competitiveMarkets(equilibrium_alpha+0.423)
        self.competitiveMarkets(equilibrium_alpha+0.424)
        self.competitiveMarkets(equilibrium_alpha+0.425)
        self.competitiveMarkets(equilibrium_alpha+0.426)
        self.outro()
        
    def intro_sequence(self):
        self.transform_title = TextMobject("Tutorial 5.2 | Perfect Competition").scale(1.2)
        self.transform_title.to_corner(UP)
        self.add(self.transform_title)
        result = TextMobject("MC = MR").scale(1.5).set_color(self.result_color)
        self.play(FadeIn(result))
        self.wait(4)
        question = TextMobject("Can competitive firms maintain profits?").scale(1.5)
        self.play(Transform(result,question))
        self.wait(4)
        self.play(FadeOut(result))

        
    def initialize(self,p):
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        self.MRF = lambda q : p
        self.MR = self.get_graph(lambda x : self.MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MC
        self.MCD = TextMobject("MC").set_color(self.mc_color).scale(0.7)
        self.MCD.move_to(self.coords_to_point(100,self.MCF(100)),LEFT)
        # ATC
        self.ATCD = TextMobject("ATC").set_color(self.atc_color).scale(0.7)
        self.ATCD.move_to(self.coords_to_point(100,self.ATCF(100)),LEFT)
        # MR
        self.MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        self.MRD.move_to(self.coords_to_point(100,self.MRF(100)),LEFT)
        # PRICE
        self.PD = TextMobject(str(p)).set_color(self.mr_color).scale(0.8)
        self.PD.next_to(self.MR,LEFT)
        

        # EQUILIBRIUM POINT 
        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))

        q = p
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        self.qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        self.qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        self.qD.next_to(self.qLine,DOWN)
        
        self.atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        self.atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        self.atcD.next_to(self.atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, p)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, p)
        self.PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        a = self.coords_to_point(30, 130)
        b = self.coords_to_point(30, 115)
        self.PROFL = Line(a,b, color=self.profit_color)
        self.PROFD = TextMobject("$$\\Pi^* = $$").set_color(self.profit_color).scale(0.8)
        self.PROFD.next_to(self.PROFL,RIGHT)
        self.PROFN = TextMobject(str(int((p-atc)*q))).set_color(self.profit_color).scale(0.8)
        self.PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(ShowCreation(self.MR),ShowCreation(self.MRD), # MR
                  ShowCreation(self.MC),ShowCreation(self.MCD), # MC
                  ShowCreation(self.ATC),ShowCreation(self.ATCD), # ATC
                  ShowCreation(self.PD),#ShowCreation(self.MPBD), # PRICE AND MPB
                  ShowCreation(self.qLine),ShowCreation(self.qD),ShowCreation(self.atcLine),ShowCreation(self.atcD),
                  FadeIn(self.PROFL),FadeIn(self.PROFD),ShowCreation(self.PROFN),ShowCreation(self.PROFArea), # PROFIT AND CALCULATION
                  ShowCreation(self.minatc)
                 )
        
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        self.MPBF = lambda q : 100 - q
        self.MPB = self.get_graph(lambda x : self.MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        alpha = 1/4
        self.MPCF = lambda q : q/alpha
        self.MPC = self.get_graph(lambda x : self.MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        self.MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        self.MPBD.move_to(self.coords_to_point(100,self.MPBF(100)),LEFT)
        # MPC
        self.MPCD = TextMobject("S").set_color(self.mc_color).scale(0.8)
        self.MPCD.move_to(self.coords_to_point(100,self.MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        self.PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        self.PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        self.PMD.next_to(self.PLine,LEFT)
        
        self.QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        self.QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        self.QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(ShowCreation(self.MPB),ShowCreation(self.MPBD), # MPB
                  ShowCreation(self.MPC),ShowCreation(self.MPCD), # MPC
                  ShowCreation(self.PLine),ShowCreation(self.PMD),
                  ShowCreation(self.QLine),ShowCreation(self.QD),
                 )
        
    def competitiveMarkets(self,alpha):
        #############
        # MARKET SIDE
        
        self.graph_origin = 3*DOWN + 6*LEFT
        self.setup_axes()
        
        # MPB
        MPBF = lambda q : 100 - q
        MPB = self.get_graph(lambda x : MPBF(x), color=self.mr_color, x_min=1, x_max=100)
        # MPC
        MPCF = lambda q : q/alpha
        MPC = self.get_graph(lambda x : MPCF(x), color=self.mc_color, x_min=1, x_max=100)
        
        # MPB
        MPBD = TextMobject("MPB").set_color(self.mr_color).scale(0.7)
        MPBD.move_to(self.coords_to_point(100,MPBF(100)),LEFT)
        # MPC
        MPCD = TextMobject("S").set_color(self.mc_color).scale(0.7)
        MPCD.move_to(self.coords_to_point(100,MPCF(100)),LEFT)
        
        # INTERSECTION LINES
        price = 100/(alpha+1)
        quant = 100*alpha/(alpha+1)
        EQa = self.coords_to_point(0, price)
        EQb = self.coords_to_point(125, price)
        EQc = self.coords_to_point(quant, price)
        EQd = self.coords_to_point(quant, 0)
        
        PLine = DashedVMobject(Line(EQa,EQb, color=self.mr_color))
        PMD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PMD.next_to(PLine,LEFT)
        
        QLine = DashedVMobject(Line(EQc,EQd, color=self.axes_color))
        QD = TextMobject("$$Q^*$$").set_color(self.axes_color).scale(0.8)
        QD.add_updater(lambda d: d.next_to(self.QLine,DOWN))
        
        self.play(Transform(self.MPB,MPB),Transform(self.MPBD,MPBD), # MPB
                  Transform(self.MPC,MPC),Transform(self.MPCD,MPCD), # MPC
                  Transform(self.PLine,PLine),Transform(self.PMD,PMD),
                  Transform(self.QLine,QLine),Transform(self.QD,QD),
                 )
        
        #############
        # FIRM SIDE
        
        self.graph_origin = 3*DOWN + RIGHT
        self.setup_axes()
        
        # MC
        MCF = lambda q : q
        MC = self.get_graph(lambda x : MCF(x), color=self.mc_color, x_min=1, x_max=100)
        # ATC
        ATCF = lambda q : q/2 + 1000/q
        ATC = self.get_graph(lambda x : ATCF(x), color=self.atc_color, x_min=10, x_max=100)
        # MR
        MRF = lambda q : price
        MR = self.get_graph(lambda x : MRF(x), color=self.mr_color, x_min=1, x_max=100)
        
        # MR
        MRD = TextMobject("MR").set_color(self.mr_color).scale(0.7)
        MRD.move_to(self.coords_to_point(100,MRF(100)),LEFT)
        # PRICE
        PD = TextMobject(str(int(price))).set_color(self.mr_color).scale(0.8)
        PD.next_to(MR,LEFT)

        q = price
        ### THis needs work
        atc = self.ATCF(q)
        mc = self.MCF(q)
        qP = self.coords_to_point(q, 0)
        qPX = self.coords_to_point(q, max(atc,mc))
        atcP = self.coords_to_point(q, atc)
        atcPX = self.coords_to_point(0, atc)
        mcP = self.coords_to_point(q, mc)
        mcPX = self.coords_to_point(0, mc)
        
        # INTERSECTION LINES
        qLine = DashedVMobject(Line(qP,qPX),color=self.axes_color)
        qD = TextMobject("q ="+str(int(q))).set_color(self.atc_color).scale(0.8)
        qD.next_to(qLine,DOWN)
        
        atcLine = DashedVMobject(Line(atcP,atcPX, color=self.axes_color))
        atcD = TextMobject(str(int(atc))).set_color(self.atc_color).scale(0.8)
        atcD.next_to(atcLine,LEFT)
        
        # PROFIT
        a = self.coords_to_point(0, price)
        b = self.coords_to_point(0, atc)
        c = self.coords_to_point(q, atc)
        d = self.coords_to_point(q, price)
        PROFArea = Polygon(a,b,c,d, fill_opacity = 0.2, fill_color = self.profit_color, color=self.profit_color)
        
        PROFN = TextMobject(str(int((price-atc)*q))).set_color(self.profit_color).scale(0.8)
        PROFN.next_to(self.PROFD,RIGHT)
        
        # SHOW
        self.play(Transform(self.MR,MR),Transform(self.MRD,MRD), # MR
                  Transform(self.PD,PD), # PRICE AND MPB
                  Transform(self.qLine,qLine),Transform(self.qD,qD),Transform(self.atcLine,atcLine),Transform(self.atcD,atcD),
                  Transform(self.PROFN,PROFN),Transform(self.PROFArea,PROFArea), # PROFIT AND CALCULATION
                 )
        
    def outro(self):
        self.play(FadeOut(self.PROFL),FadeOut(self.PROFD),FadeOut(self.PROFN))
        result = TextMobject("In the long run, competitive firms earn zero profit.")
        result.next_to(self.transform_title,DOWN).set_color(self.result_color)
        self.play(FadeIn(result))

