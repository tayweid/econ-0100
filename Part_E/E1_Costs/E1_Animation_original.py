# maniml E1_Animation_original.py CostsA
# Faithful first-pass port of 03_Code.py (the 2020-22 Part E Episode 1 code) to maniml. Nothing is
# restyled or retimed; every change is a mechanical compatibility fix marked "# PORT:". Scenes, in file order:
#   CostsA      - production function F(L) bends through four curvatures, then TC is built from F point by
#                 point (L -> Q on the left graph, Q -> TC on the right one) with FC and VC bars. Class header,
#                 CONFIG, construct and the two model helpers were lost and are reconstructed.
#   CostsB      - "Tutorial 5.1 | Production Costs" (YouTube J0Y6XzwSfls): TC with a sliding rise/run triangle
#                 tracing MC; legend equations TC = VC + FC, ATC = AVC + AFC, MC = dTC/dQ; MC, ATC, AVC curves
#                 and the min-ATC dot; AVC merges into ATC; "In the long run all costs are variable."; "MC = MR".
#   animation_0 - part outline card: "Part D | Sellers", then four episode titles flying to a row.
#   animation_1 - three side-by-side graphs under a moving camera: F(L)=L^{1/2}; VC and TC with
#                 "TC = FC + VC"; pink brackets carrying output steps from F into cost steps on TC; ATC/AVC/MC
#                 with "ATC = AFC + AVC"; "In the long run, all costs are variable." and AVC moves onto ATC.
#   animation_2 - production function F drawn on (Inputs, Q) axes, then the axes slide left and empty (Q, P)
#                 axes fade in on the right (input_to_output and inputs_labor_capital are commented out).
#   animation_3 - stub: construct() is `pass`, renders nothing.
#   animation_4 - stub: construct() is `pass`, renders nothing.
# /// script
# requires-python = ">=3.11"
# dependencies = ["seaborn==0.13.2"]
# ///

from manim import *
import numpy as np
import pandas as pd
import seaborn as sns
import warnings
import os
import random
import sys  # PORT: for the _Assets path below

# PORT: the notebook ran `from Video import *` (_archive/03_Code.ipynb, cell 1). Import only the names this
# file uses, so Video.py's own `from manim import *` cannot overwrite the frame constants the shim sets.
sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from Video import Production_Function, Inv_F, VC, FC, TC, AVC, ATC, AFC, MC, circle_it


# ---- PORT: GraphScene compatibility (maniml has no GraphScene)
# ============================================================================
# GraphScene compatibility shim: 2019-20 3b1b manimlib API -> maniml
# ----------------------------------------------------------------------------
# Provides what the old Part E scenes used: GraphScene (CONFIG dicts,
# setup_axes, coords_to_point, point_to_coords, get_graph,
# input_to_graph_point, get_vertical_line_to_graph, ...), TextMobject /
# TexMobject, and the old 3b1b palette. The per-tutorial metaConfig* dicts
# that tutorials.py held are reconstructed above each class that uses them.
# Frame: 2:1 (2160x1080), frame height 8, so every old coordinate lands where
# it did; the old 16:9 videos were 14.2 units wide, this frame is 16.
# A GraphScene draws on black (#000000) whatever config.background_color
# says; set "background_color": None in a CONFIG to leave the config alone.
# E1 copy: setup_axes() adds the two axes on their own and Scene.remove()
# keeps the old no-family-extraction rule (see GraphScene.remove below).
# ============================================================================
import re as _gs_re
import copy as _gs_copy
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
# 2020 videos (same calibration as E2_Animation_original.py).
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
# to GREY_A (#DDDDDD). Same calibration as E2_Animation_original.py (checked
# against the 2020 thumbnail YN4ZkPBS_O8, where uncolored guides read pure white).
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


# Course palette shared by the Part E scenes (read off the 2020 videos;
# entries marked "guess" never appear on screen in a surviving frame).
metaConfigEcon = {
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
    }, metaConfigEcon)

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
        self._gs_in_add = False

    # ------------------------------------------------------------ add / remove
    # Old Scene.remove() dropped exactly the mobjects passed (no family
    # extraction), so removing a group that is not itself on screen did
    # nothing even when its members were; maniml removes the members. CostsB
    # opens with self.remove(self.axes) after a setup_axes() that added the
    # two axes on their own, and the 2020 frame (J0Y6XzwSfls) still shows
    # the axes, so keep the old rule. add() still restructures by family.
    def add(self, *mobjects, **kwargs):
        self._gs_in_add = True
        try:
            return super().add(*mobjects, **kwargs)
        finally:
            self._gs_in_add = False

    def remove(self, *mobjects):
        if not self._gs_in_add:
            mobjects = [m for m in mobjects if self._gs_on_screen(m)]
        return super().remove(*mobjects)

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
        if (not animate and cached is not None
                and self._gs_on_screen(cached[0]) and self._gs_on_screen(cached[1])):
            # Old setup_axes() stacked a fresh copy on every call; reuse the
            # identical one already on screen instead.
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

        # As in manimlib: the axes go on screen as two mobjects (or inside a
        # fresh Write group), never as self.axes itself.
        axes = VGroup(x_axis, y_axis)
        if animate:
            self.play(Write(VGroup(x_axis, y_axis)))
        else:
            self.add(x_axis, y_axis)
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


# ---- PORT: ManimCE Axes label placement (animation_1, animation_2)
# maniml's Axes.get_graph_label sets a label off along the curve's normal and its get_axis_labels puts the x
# label below the axis end (ManimGL habits). These scenes were written for ManimCE (2022), which puts a graph
# label to the RIGHT of the curve's last on-screen point and both axis labels up and to the right of the axis
# ends. Without this, VC's label sits on the TC curve and the MC/ATC/AVC labels pile up on their crossing.
def _ce_get_graph_label(self, graph, label="f(x)", x_val=None, direction=RIGHT,
                        buff=MED_SMALL_BUFF, color=None, dot=False, dot_config=None):
    label_object = label if isinstance(label, Mobject) else MathTex(str(label))
    label_object.set_color(graph.get_color() if color is None else color)
    if x_val is None:
        # Search from right to left for the last point below the top of the frame
        for x in np.linspace(self.x_range[1], self.x_range[0], 100):
            point = self.input_to_graph_point(x, graph)
            if point[1] < FRAME_Y_RADIUS:
                break
    else:
        point = self.input_to_graph_point(x_val, graph)
    label_object.next_to(point, direction, buff=buff)
    label_object.shift_onto_screen()
    return label_object


def _ce_axis_label(axes, label, axis, edge, direction, buff=SMALL_BUFF):
    label = label if isinstance(label, Mobject) else MathTex(str(label))
    label.next_to(axis.get_edge_center(edge), direction=direction, buff=buff)
    label.shift_onto_screen(buff=MED_SMALL_BUFF)
    return label


def _ce_get_axis_labels(self, x_label="x", y_label="y"):
    self.axis_labels = VGroup(
        _ce_axis_label(self, x_label, self.get_x_axis(), UR, UR),
        _ce_axis_label(self, y_label, self.get_y_axis(), UR, UP * 0.5 + RIGHT),
    )
    return self.axis_labels


Axes.get_graph_label = _ce_get_graph_label
Axes.get_axis_labels = _ce_get_axis_labels


# ---- PORT: ManimCE v0.13.1 defaults for Axes and Text (animation_1, animation_2)
# The 2022 renders survive: ~/Projects/ECON_0100_Archive_20260815/Animations_alt/Recent/PartE_E1
# (videos/Videos/1080p60/animation_1.mp4 is the notebook's last animation_1 output; the images/ PNGs are
# ManimCE v0.13.1 stills). Against them, maniml's defaults differ where the code passes nothing:
# - Axes: CE drew the axes white, set the numbers at font size 36, and left 0 off both axes (CE Axes
#   defaults numbers_to_exclude to [0], even for numbers_to_include). maniml draws #BBBBBB axes and
#   size-24 numbers, with a 0 on every axis. CE's numbers were TeX digits; maniml sets them as Text,
#   so use CMU Serif (Computer Modern) when it is installed.
# - Text: CE's Text set font_size f at 0.05 * f / 4.8 units per point, where maniml sets it at 0.0076 * f,
#   so CE text is 1.371 times as large. The 2022 machine's Pango default face was DejaVu Serif.
#   matplotlib (pulled in by seaborn, see the header) bundles DejaVu Serif, so register that copy for
#   this run. If it is missing, maniml's default face is used.
_ce_number_font = _ce_text_font = None
try:
    import manimpango as _mp
    if "CMU Serif" in _mp.list_fonts():
        _ce_number_font = "CMU Serif"
    import matplotlib as _mpl
    if _mp.register_font(os.path.join(_mpl.get_data_path(), "fonts", "ttf", "DejaVuSerif.ttf")):
        _ce_text_font = "DejaVu Serif"
except Exception:
    pass
_CE_TEXT_SCALE = 0.05 / (4.8 * 0.0076)
_maniml_create_axis = Axes.create_axis


def _ce_create_axis(self, range_terms, axis_config, length, rotation=0.0):
    axis_config = dict(axis_config)
    axis_config.setdefault("color", "#FFFFFF")
    numbers = axis_config.pop("numbers_to_include", None)
    excluding = axis_config.get("numbers_to_exclude")
    axis = _maniml_create_axis(self, range_terms, axis_config, length, rotation)
    if numbers is not None:
        excluding = [0] if excluding is None else list(excluding)
        font = {"text_config": {"font": _ce_number_font}} if _ce_number_font else {}
        axis.add_numbers([x for x in numbers if x not in excluding], excluding=[], font_size=36, **font)
    return axis


Axes.create_axis = _ce_create_axis
_maniml_Text = Text


class Text(_maniml_Text):
    """ManimCE v0.13.1 Text: DejaVu Serif when available, at CE's size (see above). Only this file's
    Text calls (animation_1) use it."""

    def __init__(self, text, **kwargs):
        if _ce_text_font:
            kwargs.setdefault("font", _ce_text_font)
        super().__init__(text, **kwargs)
        self.scale(_CE_TEXT_SCALE)


""" Paths """
# Configuration
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

# Helper Functions and Classes


# PORT: reconstructed; tutorials.metaConfig* is lost. The class header above productionFunction() and
# totalCosts() was cut from 03_Code.py (the file never parsed); the notebook copy (_archive/03_Code.ipynb,
# cell 12) has it as `class animation_A(Scene)`, which cannot run the GraphScene calls inside, so the class
# is CostsA(GraphScene) after its sibling CostsB. Values: graph_origin is set in the methods (2 DOWN + 6 LEFT
# for F, 2 DOWN + RIGHT for TC), so each graph is 5 x 5 units, as in animation_1's side-by-side rewrite, to
# keep them apart; Q and TC run 0-100 as in CostsB; L/Q labels for F (totalCosts sets TC/Q itself); colors
# are the course palette guesses (no frame of this scene survives).
metaConfigCostsA = {
    "x_min": 0,
    "x_max": 100,
    "x_axis_width": 5,
    "y_min": 0,
    "y_max": 100,
    "y_axis_height": 5,
    "x_axis_label": "$L$",
    "y_axis_label": "$Q$",
    "graph_origin": 2 * DOWN + 6 * LEFT,
    "axes_color": OLD_GREY,
    "func_color": OLD_BLUE,
    "supply_color": OLD_GREEN,
    "avc_color": OLD_YELLOW,
    "default_graph_colors": [OLD_BLUE, OLD_GREEN, OLD_YELLOW],
}


class CostsA(GraphScene):
    CONFIG = metaConfigCostsA

    # PORT: reconstructed; the construct is lost. It calls the two surviving methods in file order.
    def construct(self):
        self.productionFunction()
        self.totalCosts()

    # PORT: reconstructed helper (lost with the class). F(L) = 100 (L/100)^exp, so every curvature runs
    # (0, 0) to (100, 100) on the 0-100 axes and totalCosts' labels read 20/40/60/80 -> 52/69/81/91.
    def func(self, L, exp):
        return 100 * (L / 100) ** exp

    # PORT: reconstructed helper (lost with the class). Despite the name it is the total cost of q built
    # from F: TC(q) = FC + w L(q) with L(q) = F^-1(q), FC = 10 and w = 1 (axis units of $10, so the code's
    # labels "int(...)*10" read FC = 100 and TC = 300, 500, 700, 900 at L = 20, 40, 60, 80).
    def MC(self, q, exp):
        return 10 + 100 * (q / 100) ** (1 / exp)

    def productionFunction(self):
        self.graph_origin = 2*DOWN + 6*LEFT
        self.setup_axes(animate=True)
        self.F = self.get_graph(lambda L : self.func(L,0.5), x_min=0, x_max=100)
        self.play(ShowCreation(self.F), run_time=2)

        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,1), x_min=0, x_max=100, color=self.func_color)), run_time=2)
        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,1.3), x_min=0, x_max=100, color=self.func_color)), run_time=2)
        self.play(Transform(self.F,self.get_graph(lambda L : self.func(L,0.4), x_min=0, x_max=100, color=self.func_color)), run_time=2)

    def totalCosts(self):
        self.graph_origin = 2*DOWN + RIGHT
        self.y_axis_label = "$TC$"
        self.x_axis_label = "$Q$"
        self.setup_axes(animate=True)
        self.y_axis_label = ""
        self.x_axis_label = ""

        exp = 0.4
        MC = self.get_graph(lambda q : self.MC(q,exp), color=self.supply_color, x_min=0, x_max=0)
        fc = Dot(self.coords_to_point(0,self.MC(0,exp)))
        fcLabel = Tex(str(int(self.MC(0,exp)*10))).scale(0.7)
        fcLabel.move_to(self.coords_to_point(-1,self.MC(0,exp)),RIGHT)
        self.play(FadeIn(MC),
                  FadeIn(fc),
                  FadeIn(fcLabel))

        a = self.coords_to_point(-15, 0)
        b = self.coords_to_point(-15, 10)
        fcLine = Line(a,b, color=self.axes_color)
        fcD = Tex("FC").scale(0.7)
        fcD.next_to(fcLine, LEFT)
        self.play(ShowCreation(fcLine),FadeIn(fcD))

        a = self.coords_to_point(-15, 10)
        b = self.coords_to_point(-15, 10)
        self.vcLine = Line(a,b, color=self.avc_color)
        self.vcD = Tex("VC").scale(0.7)
        self.vcD.next_to(self.vcLine, LEFT)

        for l in np.arange(20,100,20):
            p = self.func(l,0.4)
            mc = self.MC(p,0.4)

            self.graph_origin = 2*DOWN + 6*LEFT
            self.setup_axes()
            a = self.coords_to_point(l,0)
            b = self.coords_to_point(l,p)
            c = self.coords_to_point(0,p)
            pointF = Dot(b)
            vLine = DashedVMobject(Line(a,b, color=self.axes_color))
            hLine = DashedVMobject(Line(b,c, color=self.axes_color))
            lLabel = Tex(str(int(l))).scale(0.7)
            lLabel.move_to(a, UP)
            qLabel = Tex(str(int(p))).scale(0.7)
            qLabel.move_to(c,RIGHT)

            self.play(ShowCreation(vLine),FadeIn(lLabel))
            self.play(FadeIn(pointF))
            self.play(ShowCreation(hLine),FadeIn(qLabel))

            self.graph_origin = 2*DOWN + RIGHT
            self.setup_axes()
            pointMC = Dot(self.coords_to_point(p,mc))
            MC0 = self.get_graph(lambda q : self.MC(q,exp), color=self.supply_color, x_min=0, x_max=p)

            a = self.coords_to_point(p,0)
            b = self.coords_to_point(p,mc)
            c = self.coords_to_point(0,mc)
            pointF = Dot(b)
            vLine = DashedVMobject(Line(a,b, color=self.axes_color))
            hLine = DashedVMobject(Line(b,c, color=self.axes_color))
            lLabel = Tex(str(int(p))).scale(0.7)
            lLabel.move_to(a, UP)
            qLabel = Tex(str(int(mc)*10)).scale(0.7)
            qLabel.move_to(c,RIGHT)

            a = self.coords_to_point(-15, 10)
            b = self.coords_to_point(-15, mc)
            vcLine = Line(a,b, color=self.avc_color)
            vcD = Tex("VC").scale(0.7)
            vcD.next_to(vcLine, LEFT)

            self.play(ShowCreation(vLine),FadeIn(lLabel))
            self.play(FadeIn(pointMC),Transform(MC,MC0))
            self.play(ShowCreation(hLine),FadeIn(qLabel))
            self.play(Transform(self.vcLine,vcLine),Transform(self.vcD,vcD))


# PORT: reconstructed; tutorials.metaConfig* is lost. Read off the 2020 frame (J0Y6XzwSfls, "Tutorial 5.1 |
# Production Costs"): origin 3 DOWN + 6 LEFT, Q 0-100 over 8 units, P 0-100 over 5 units (the legend at
# Q = 135 sits at x = 4.8, as in the frame), grey axes with P/Q labels and end ticks, black ground. CostsB
# never passes a color, so every curve takes the next default_graph_colors entry, as the old get_graph did:
# TC orange and the first MC green match the frame; blue and yellow complete the cycle (guesses).
metaConfigCostsB = {
    "x_min": 0,
    "x_max": 100,
    "x_axis_width": 8,
    "y_min": 0,
    "y_max": 100,
    "y_axis_height": 5,
    "x_axis_label": "$Q$",
    "y_axis_label": "$P$",
    "graph_origin": 3 * DOWN + 6 * LEFT,
    "axes_color": OLD_GREY,
    "default_graph_colors": [OLD_ORANGE, OLD_GREEN, OLD_BLUE, OLD_YELLOW],
}


class CostsB(GraphScene):
    CONFIG = metaConfigCostsB  # PORT: reconstructed (see the dict above)

    # PORT: reconstructed; CostsB has no construct in 03_Code.py or the notebook. The notebook's 2021 render
    # log reads "Rendered CostsB ... Played 34 animations", which is exactly setup_axes() (no animation) plus
    # these five methods in file order. The title is added the way PerfectCompB.intro_sequence (E2) adds its
    # own, with self.add, because the 2020 frame shows it.
    def construct(self):
        self.transform_title = TextMobject("Tutorial 5.1 | Production Costs").scale(1.2)
        self.transform_title.to_corner(UP)
        self.add(self.transform_title)
        self.setup_axes()
        self.marginalCost()
        self.costsEquations()
        self.costs()
        self.playWithCosts()
        self.outro_sequence()

    def marginalCost(self):
        # TC
        self.remove(self.axes)
        self.TCF = lambda q : q**2/100 + 10
        self.TC = self.get_graph(lambda x : self.TCF(x), x_min=5, x_max=110)
        a = self.coords_to_point(135, 100)
        b = self.coords_to_point(135, 85)
        self.TCL = Line(a,b)
        self.TCD = Tex("TC")
        self.TCD.next_to(self.TCL)

        self.play(ShowCreation(self.TC), run_time=2)
        self.play(FadeIn(self.TCL),FadeIn(self.TCD))


        # MC
        self.MCF = lambda q : 2*q/10

        p = self.TCF(10)
        dx = self.MCF(10)
        a = self.coords_to_point(10-5, p-5*dx/10)
        b = self.coords_to_point(10-5, p+5*dx/10)
        c = self.coords_to_point(10+5, p+5*dx/10)
        self.pointL = Dot(a)
        self.pointU = Dot(c)
        self.tangent = Line(a,c)
        self.lineUp = DashedVMobject(Line(a,b))
        self.lineOver = DashedVMobject(Line(b,c))
        self.MC = self.get_graph(lambda x : self.MCF(x), x_min=5, x_max=10)
        self.play(FadeIn(self.pointL), FadeIn(self.pointU), FadeIn(self.tangent), FadeIn(self.MC), FadeIn(self.lineUp), FadeIn(self.lineOver))

        a = self.coords_to_point(135, 80)
        b = self.coords_to_point(135, 65)
        self.MCL = Line(a,b)
        self.MCD = Tex("MC")
        self.MCD.next_to(self.MCL)
        self.play(FadeIn(self.MCL),FadeIn(self.MCD))

        self.rise = Tex("Rise").scale(0.7)
        # PORT: plays correctly (the --render video tracks the rise line), but checkpoint stills and checkpoint
        # jumps show "Rise" at its last spot near the title: a restored checkpoint reruns this updater
        # against the live self.lineUp, which has already reached Q = 100.
        self.rise.add_updater(lambda d: d.next_to(self.lineUp, LEFT))
        self.add(self.rise)

        for q in np.arange(10,110,10):
            MC = self.get_graph(lambda x : self.MCF(x), x_min=5, x_max=q)

            p = self.TCF(q)
            dx = self.MCF(q)
            a = self.coords_to_point(q-5, p-5*dx/10)
            b = self.coords_to_point(q-5, p+5*dx/10)
            c = self.coords_to_point(q+5, p+5*dx/10)
            pointL = Dot(a)
            pointU = Dot(c)
            tangent = Line(a,c)
            lineUp = DashedVMobject(Line(a,b))
            lineOver = DashedVMobject(Line(b,c))
            self.play(Transform(self.MC,MC), Transform(self.tangent,tangent), Transform(self.pointL,pointL), Transform(self.pointU,pointU),
                      Transform(self.lineUp,lineUp), Transform(self.lineOver,lineOver))

    def costsEquations(self):
        self.play(FadeOut(self.TC),
                  FadeOut(self.pointL), FadeOut(self.pointU), FadeOut(self.tangent),
                  FadeOut(self.MC), FadeOut(self.lineUp), FadeOut(self.lineOver),
                  FadeOut(self.MC), FadeOut(self.rise),
                  FadeOut(self.tangent), FadeOut(self.pointL),
                  FadeOut(self.pointU), FadeOut(self.lineUp), FadeOut(self.lineOver),
                  )

        a = self.coords_to_point(70, 100)
        b = self.coords_to_point(70, 85)
        TCL = Line(a,b)
        TCD = Tex("TC")
        TCD.next_to(TCL)

        self.play(Transform(self.TCL,TCL), Transform(self.TCD,TCD))

        TCE = Tex("= VC + FC")
        TCE.next_to(TCD)

        self.play(FadeIn(TCE))
        #self.wait(3)
        #self.play(FadeOut(TCE),FadeOut(self.TCL),FadeOut(self.TCD))
        a = self.coords_to_point(70, 100)
        b = self.coords_to_point(70, 85)
        self.ATCL = Line(a,b)
        self.ATCD = Tex("ATC")
        self.ATCD.next_to(TCL)
        self.ATCE = Tex("= AVC + AFC")
        self.ATCE.next_to(self.ATCD)
        self.play(ReplacementTransform(self.TCL,self.ATCL),ReplacementTransform(self.TCD,self.ATCD),ReplacementTransform(TCE,self.ATCE))

        a = self.coords_to_point(70, 80)
        b = self.coords_to_point(70, 65)
        MCL = Line(a,b)
        MCD = Tex("MC")
        MCD.next_to(MCL)

        self.play(Transform(self.MCL,MCL), Transform(self.MCD,MCD))

        self.MCE = Tex("$$ = \\frac{\\Delta TC}{\\Delta Q} $$")
        self.MCE.next_to(MCD)

        self.play(FadeIn(self.MCE))

    def costs(self):
        # MC
        self.MCF = lambda q : q
        self.MC = self.get_graph(lambda x : self.MCF(x), x_min=1, x_max=100)
        # ATC
        self.ATCF = lambda q : q/2 + 1000/q
        self.ATC = self.get_graph(lambda x : self.ATCF(x), x_min=10, x_max=100)
        # AVC
        self.AVCF = lambda q : q/2
        self.AVC = self.get_graph(lambda x : self.AVCF(x), x_min=1, x_max=100)

        # MC
        a = self.coords_to_point(135, 80)
        b = self.coords_to_point(135, 65)
        MCL = Line(a,b)
        MCD = Tex("MC")
        MCD.next_to(MCL)
        self.play(Transform(self.MCL,MCL),Transform(self.MCD,MCD),FadeOut(self.MCE))

        # ATC
        a = self.coords_to_point(135, 60)
        b = self.coords_to_point(135, 45)
        ATCL = Line(a,b)
        ATCD = Tex("ATC")
        ATCD.next_to(ATCL)
        self.play(Transform(self.ATCL,ATCL),Transform(self.ATCD,ATCD))

        # AVC
        a = self.coords_to_point(135, 40)
        b = self.coords_to_point(135, 25)
        self.AVCL = Line(a,b)
        self.AVCD = Tex("AVC")
        self.AVCD.next_to(self.AVCL)
        self.play(ReplacementTransform(self.ATCE,self.AVCL),FadeIn(self.AVCD))

        # MC
        self.play(ShowCreation(self.MC), run_time=2)
        self.play(ShowCreation(self.ATC), run_time=2)
        self.play(ShowCreation(self.AVC), run_time=2)

        self.minatc = Dot(self.coords_to_point(np.sqrt(2000), self.MCF(np.sqrt(2000))))
        self.play(FadeIn(self.minatc))


    def playWithCosts(self):

        self.play(ReplacementTransform(self.AVC,self.ATC), ReplacementTransform(self.AVCL,self.ATCL), ReplacementTransform(self.AVCD,self.ATCD))
        self.wait(3)

    def outro_sequence(self):
        self.play(FadeOut(self.axes),FadeOut(self.minatc),FadeOut(self.MC),FadeOut(self.ATC),
                  FadeOut(self.ATCL),FadeOut(self.ATCD),FadeOut(self.MCL),FadeOut(self.MCD),
                  FadeOut(self.MCL), FadeOut(self.MCD),FadeOut(self.ATCL),
                  FadeOut(self.ATCD))

        result = Tex("In the long run all costs are variable.").scale(1.5)
        self.play(FadeIn(result))
        self.wait(4)
        self.play(FadeOut(result))
        result = Tex("MC = MR").scale(1.5)
        self.play(FadeIn(result))


class animation_0(Scene):

    """Animation 0 | Intro

This animation introduces the video sequence."""

    def construct(self):
        self.outline()

    def outline(self):
        title = Tex('Part D').scale(4)
        center_bar = Tex('$|$').set_color(GREY).to_edge(UP, buff=1).scale(2)
        subtitle = Tex('Sellers').scale(2).next_to(center_bar, RIGHT).set_color(YELLOW)
        self.play(FadeIn(title))

        self.play(title.animate.scale(0.6).next_to(center_bar, LEFT), run_time=1/2)
        self.play(FadeIn(center_bar), run_time=1/4)
        self.play(FadeIn(subtitle))

        episode_list = [
            'Episode D1 \\\\ Costs and Production',
            'Episode D2 \\\\ Marginal Revenue',
            'Episode D3 \\\\ Monopolistic Competition',
            'Episode D4 \\\\ Game Theory and Oligopoly'
        ]

        _int = 1/(len(episode_list) + 2)
        i = _int
        for episode in episode_list:

            ep = Tex(episode).scale(1).next_to(center_bar, DOWN)
            self.play(FadeIn(ep), run_time=1/2)
            up_ep = episode.split(' \\\\ ')[0]
            up_ep = Tex(up_ep).scale(0.5).set_color(YELLOW).move_to(LEFT*10*(1-i-_int/2) + RIGHT*10*(i+_int/2) + DOWN)
            self.play(Transform(ep, up_ep), run_time=1/2)

            i += _int

        self.wait()
        # next I want a circling box above each episode
        # and I'll add in the video inside the box in post


class animation_1(MovingCameraScene):
    """Animation 1 | The Production Function Generates Costs

This animation uses the production function to generate total cost."""

    def construct(self):
        axes_f_group, axes_f = self.Make_Production_Function()
        axes_c_group, axes_c = self.Add_Costs(axes_f_group)
        self.Create_TC_From_F(axes_f, axes_c)
        axes_ac_group, axes_ac, avc = self.Add_Average_Costs(axes_f_group, axes_c_group)
        self.Results(axes_c_group, axes_ac_group, axes_ac, avc)

    def Make_Production_Function(self):
        axes_f = Axes(
            x_range=[0, 100, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 100, 20),
            },

            y_range=[0, 10],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },
            tips=False,
        )

        axes_f_labels = axes_f.get_axis_labels('L','Q')
        F = axes_f.get_graph(lambda L: Production_Function(L), color=BLUE)
        F_label = axes_f.get_graph_label(F, label="F(L)=L^{1/2}")
        F_group = VGroup(axes_f, axes_f_labels, F, F_label).move_to(0)
        axes_f_title = Text('Production Function').next_to(F_group,UP, buff=1/2)
        axes_f_group = VGroup(axes_f, axes_f_labels, F, F_label, axes_f_title).scale(0.7).move_to(0)

        self.play(FadeIn(axes_f_group))
        return axes_f_group, axes_f

    def Trace_F(axes_f_group):
        """ Move a point along F """

        # add a point
        # move it out and back along F
        # fade it out

        pass

    def Add_Costs(self, axes_f_group):

        axes_c = Axes(
            x_range=[0, 10, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },

            y_range=[0, 280],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 320, 40),
            },
            tips=False,
        )

        axes_c_labels = axes_c.get_axis_labels('Q','')
        vc = axes_c.get_graph(lambda Q: VC(Q), color=ORANGE)
        VC_label = axes_c.get_graph_label(vc, label=r"VC=w\cdot L")  # PORT: r-string, same text (silences an escape warning)
        tc = axes_c.get_graph(lambda Q: TC(Q), color=RED)
        TC_label = axes_c.get_graph_label(tc, label="TC")
        Cost_group = VGroup(axes_c, axes_c_labels, vc, VC_label, tc, TC_label).move_to(0)
        axes_c_title = Text('TC = FC + VC').next_to(Cost_group,UP, buff=1/2)
        axes_c_group = VGroup(axes_c, axes_c_labels, vc, VC_label, tc, TC_label, axes_c_title).scale(0.7).next_to(axes_f_group, RIGHT, buff=1)

        self.play(FadeIn(axes_c_group), self.camera.frame.animate.move_to(VGroup(axes_f_group, axes_c_group)))
        return axes_c_group, axes_c

    def Create_TC_From_F(self, axes_f, axes_c):
        """ Use F to create TC """

        a = axes_c.coords_to_point(-0.1, 0)
        b = axes_c.coords_to_point(-0.1, FC(0))
        FCLine = Line(a,b, color=GREEN)
        FCDesc = Tex("FC", color=GREEN).scale(0.7)
        FCDesc.next_to(FCLine, RIGHT)

        self.play(FadeIn(FCLine), FadeIn(FCDesc))

        LIST = []
        q_last = 0
        for q in np.arange(2,12,2):

            a = axes_f.coords_to_point(-1, q_last+0.1)
            b = axes_f.coords_to_point(-1, q-0.1)

            VLine = Line(a,b, color=PINK)
            VLine_Copy = Line(a,b, color=PINK)

            c = axes_f.coords_to_point(Inv_F(q_last)+1, -0.1)
            d = axes_f.coords_to_point(Inv_F(q)-1, -0.1)

            HLine = Line(c,d, color=PINK)
            LIST.append(HLine)
            HLine_Copy = Line(c,d, color=PINK)
            LIST.append(HLine_Copy)

            self.play(Create(VLine), Create(HLine), Create(VLine_Copy), Create(HLine_Copy))

            a = axes_c.coords_to_point(q_last+0.1, -1)
            b = axes_c.coords_to_point(q-0.1, -1)

            NewVLine = Line(a,b, color=PINK)
            LIST.append(NewVLine)

            c = axes_c.coords_to_point(-0.1, VC(q_last)+FC(0)+1)
            d = axes_c.coords_to_point(-0.1, VC(q)+FC(0)-1)

            NewHLine = Line(c,d, color=PINK)
            LIST.append(NewHLine)

            self.play(Transform(VLine, NewVLine), Transform(HLine, NewHLine))

            q_last = q
        self.play(FadeOut(*LIST))


    def Add_Average_Costs(self, axes_f_group, axes_c_group):
        # this really should be different, constructing ATC
        # start with a point at q=0, show the equation relating TC and ATC
        # then trace out ATC with an animating changing of the fraction
        # do something with mc?...

        axes_ac = Axes(
            x_range=[1, 10, 1],
            x_length = 5,
            x_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 12, 2),
            },

            y_range=[1, 80],
            y_length = 5,
            y_axis_config={
                "include_ticks":False,
                "numbers_to_include": np.arange(0, 90, 10),
            },
            tips=False,
        )

        axes_ac_labels = axes_ac.get_axis_labels('Q', '')
        avc = axes_ac.get_graph(lambda Q: AVC(Q), color=ORANGE)
        AVC_label = axes_ac.get_graph_label(avc, label="AVC")
        atc = axes_ac.get_graph(lambda Q: ATC(Q), color=RED)
        ATC_label = axes_ac.get_graph_label(atc, label="ATC")
        mc = axes_ac.get_graph(lambda Q: MC(Q), color=PURPLE)
        MC_label = axes_ac.get_graph_label(mc, label="MC")
        Cost_group = VGroup(axes_ac, axes_ac_labels, avc, AVC_label, atc, ATC_label, mc, MC_label).move_to(0)
        axes_ac_title = Text('ATC = AFC + AVC').next_to(Cost_group,UP, buff=1/2)
        axes_ac_group = VGroup(axes_ac, axes_ac_labels, avc, AVC_label, atc, ATC_label, mc, MC_label, axes_ac_title).scale(0.7).next_to(axes_c_group, buff=1)

        self.play(FadeIn(axes_ac_group), FadeOut(axes_f_group), self.camera.frame.animate.move_to(VGroup(axes_c_group, axes_ac_group)))
        return axes_ac_group, axes_ac, avc

    def Results(self, axes_c_group, axes_ac_group, axes_ac, avc):
        self.play(FadeOut(axes_c_group), self.camera.frame.animate.move_to(axes_ac_group))
        self.wait()

        LR_Desc = Text('In the long run, all costs are variable.').set_color(YELLOW).next_to(axes_ac_group, UP, buff=1/2)
        self.play(Create(LR_Desc))
        self.wait()

        LR_avc = axes_ac.get_graph(lambda Q: ATC(Q), color=ORANGE)
        self.play(Transform(avc, LR_avc))

        # in the long run all costs are variable
        # punchline for next time: MC = MR


# PORT: production_func is defined nowhere (the notebook's own run of animation_2 stopped with
# "NameError: name 'production_func' is not defined"). Reconstructed as CostsA.func, the only other
# production function taking (input, exponent) on 0-100 axes: F(x) = 100 (x/100)^a.
def production_func(x, a):
    return 100 * (x / 100) ** a


class animation_2(Scene):

    def create_production_function(self, F, F_label):
        self.play(Create(F))
        self.play(Create(F_label), run_time = 1/4)

    def inputs_labor_capital(self, axes, axes_labels):
        self.play(Transform(axes_labels, axes.get_axis_labels('L,K','Q')))

        point = Dot(DOWN*2 + RIGHT*0.75)
        circle_it(self, 1/3, point)

        point = Dot(DOWN*2 + RIGHT*1.4)
        circle_it(self, 1/3, point)

        self.play(Transform(axes_labels, axes.get_axis_labels('L','Q')))

    def construct(self):
        axes = Axes(
            x_range=[0, 100, 10],
            x_length = 5,
            x_axis_config={
                "include_ticks":True,
            },

            y_range=[0, 100],
            y_length = 5,
            y_axis_config={
                "include_ticks":False
            },
            tips=True,
        ).shift(LEFT*2)
        axes_labels = axes.get_axis_labels('Inputs','Q')
        F = axes.get_graph(lambda x: production_func(x, 0.5), color=BLUE)
        F_label = axes.get_graph_label(F, label="F")

        hlines, vlines, marginal_inputs, marginal_outputs = [], [], [], []

        axes_c = Axes(
            x_range=[0, 100, 10],
            x_length = 5,
            x_axis_config={
                "include_ticks":True,
            },

            y_range=[0, 100],
            y_length = 5,
            y_axis_config={
                "include_ticks":False
            },
            tips=True,
        ).shift(RIGHT*3.5)
        axes_c_labels = axes_c.get_axis_labels('Q','P')

        """ Animation Sequence """
        self.add(axes, axes_labels)

        self.create_production_function(F, F_label)

        #self.inputs_labor_capital(axes, axes_labels)
        #self.input_to_output(axes, F, hlines, vlines, marginal_inputs, marginal_outputs)
        self.introduce_costs(axes, axes_labels, axes_c, axes_c_labels, F, F_label, hlines, vlines, marginal_inputs, marginal_outputs)


    def input_to_output(self, axes, F, hlines, vlines, marginal_inputs, marginal_outputs):
        base_value = ValueTracker(0)

        base_dot = Dot(axes.coords_to_point(0, production_func(0,0.5)), color=RED)
        base_dot.add_updater(lambda m:
                             m.move_to(
                                axes.c2p(base_value.get_value(),
                                production_func(base_value.get_value(),0.5))
            ))

        # PORT: not ported (construct never calls this method). maniml's Vector rejects ManimCE's
        # max_stroke_width_to_length_ratio, so both Vector(...) lines raise TypeError if this is switched
        # back on; in ManimCE a ratio of 0 drew only the arrowheads. Dropping the argument runs the beat
        # with full arrows (checked in a scratch copy).
        output_arrow = Vector(RIGHT, max_stroke_width_to_length_ratio=0)
        output_arrow.add_updater(
            lambda m: m.next_to(
                        axes.c2p(0,production_func(base_value.get_value(),0.5)),
                        LEFT
            ))

        input_line = Line(
            axes.c2p(0.1, 0),
            axes.c2p(0, 0),
        ).set_color(GREY)
        input_line.add_updater(
            lambda m: m.put_start_and_end_on(
                          axes.c2p(base_value.get_value(), 0),
                          axes.c2p(base_value.get_value(), production_func(base_value.get_value(),0.5))
            ))

        input_arrow = Vector(UP, max_stroke_width_to_length_ratio=0)
        input_arrow.add_updater(
            lambda m: m.next_to(
                        axes.c2p(base_value.get_value(), 0),
                        DOWN
            ))

        output_line = Line(
            axes.c2p(0.1, 0),
            axes.c2p(0, 0),
        ).set_color(GREY)
        self.add(output_line)
        output_line.add_updater(
            lambda m: m.put_start_and_end_on(
                          axes.c2p(0, production_func(base_value.get_value(),0.5)),
                          axes.c2p(base_value.get_value(), production_func(base_value.get_value(),0.5))
            ))

        self.add(input_arrow, input_line, output_arrow, output_line, base_dot)

        self.play(base_value.animate.set_value(90))
        self.play(base_value.animate.set_value(5), run_time=2)

        input_values, last_value = [20, 40, 60], 0
        for input_value in input_values:
            self.play(base_value.animate.set_value(input_value))

            marginal_input = Line(
                axes.c2p(input_value-1, -1),
                axes.c2p(last_value+1, -1))
            marginal_inputs.append(marginal_input)
            self.play(FadeIn(marginal_input))

            marginal_return = Line(
                axes.c2p(-1, production_func(input_value,0.5)-1),
                axes.c2p(-1, production_func(last_value,0.5)+1))
            marginal_outputs.append(marginal_return)
            self.play(FadeIn(marginal_return))

            hline = axes.get_horizontal_line(axes.c2p(input_value, production_func(input_value,0.5)))
            hlines.append(hline)
            vline = axes.get_vertical_line(axes.c2p(input_value, production_func(input_value,0.5)))
            vlines.append(vline)
            self.add(hline,vline)

            last_value = input_value

    def introduce_costs(self, axes, axes_labels, axes_c, axes_c_labels, F, F_label, hlines, vlines, marginal_inputs, marginal_outputs):

        shift = 1.5
        self.play(
            axes.animate.shift(LEFT*shift),
            axes_labels.animate.shift(LEFT*shift),
            VGroup(F,F_label).animate.shift(LEFT*shift),
            VGroup(*hlines).animate.shift(LEFT*shift),
            VGroup(*vlines).animate.shift(LEFT*shift),
            VGroup(*marginal_inputs).animate.shift(LEFT*shift),
            VGroup(*marginal_outputs).animate.shift(LEFT*shift)
        )

        self.play(FadeIn(axes_c), FadeIn(axes_c_labels))



    def create_variable_cost_curve(self):
        pass


class animation_3(Scene):

    """Animation 3 | Cost Curves

This animation develops the main cost curves."""

    def construct(self):
        pass

    def some_accounting(self):
        pass

    def create_averages(self):
        pass

    def create_marginal_cost(self):
        pass

    def create_marginal_revenue(self):
        pass


class animation_4(Scene):

    """Animation 4 | Marginal Revenue

This animation introduces marginal revenue and the firm's optimal quantity choice."""

    def construct(self):
        pass

    def create_marginal_revenue(self):
        pass
