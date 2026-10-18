"""Three visual layers for Part B: a 3D world, attached labels, flat models.

This small ManimL adapter keeps renderer details out of the lesson scenes.
The native-fill workaround below is temporary; it changes no engine files.
"""

from functools import wraps

import numpy as np
from manim import DEGREES, DOWN, Scene, Tex, ThreeDScene, UP, VGroup, VMobject
from maniml.rendering.shader_wrapper import VShaderWrapper
from style import INK, SCALE_TICK


def _repair_native_flat_fill():
    """Prevent the preceding 3D fill from clipping flat text and diagrams.

    ManimL's native fill compositor reads a shared scratch depth texture even
    when depth testing is off. A preceding 3D fill leaves that texture empty
    outside its own shape, so flat text gets clipped to the floor. Give each
    non-depth fill a valid depth everywhere before the compositor reads it.
    Browser rendering uses a separate renderer and is unaffected.
    """
    original = VShaderWrapper.render_fill
    if getattr(original, '_market_flat_fill', False):
        return  # Importing or hot-reloading the scene must not stack wrappers.

    @wraps(original)
    def render_fill(wrapper):
        previous_fbo = wrapper.ctx.fbo
        if not wrapper.depth_test and previous_fbo is not None:
            try:
                wrapper.fill_canvas[2].clear(0.5)
            finally:
                # Clearing the scratch framebuffer may bind it. The original
                # renderer must still see the scene framebuffer as its target.
                previous_fbo.use()
        return original(wrapper)

    render_fill._market_flat_fill = True
    VShaderWrapper.render_fill = render_fill


_repair_native_flat_fill()


def fixed(mob):
    """Flat material: bypass the 3D camera and depth buffer."""
    mob.fix_in_frame()
    mob.deactivate_depth_test()
    return mob


def add_market_objects(scene, *mobjects, **kwargs):
    """Preserve flat glyphs while giving world geometry real depth.

    Assigned as add() on each scene, so FadeIn/Write also use this rule.
    ThreeDScene's recursive triangulation is for the world, not SVG text.
    """
    for mob in mobjects:
        if mob.is_fixed_in_frame():
            Scene.add(scene, mob)
        else:
            ThreeDScene.add(scene, mob, **kwargs)
            # A world Group can contain vector lines/borders. ManimL applies
            # this flag to VGroup children, but misses children of plain Group.
            # WebGPU needs the explicit 3D path even for an unfilled line.
            for child in mob.get_family():
                if isinstance(child, VMobject):
                    child.use_triangulated_fill = True
    return scene


def camera_home(scene):
    """A stable, shallow 3D view. No camera orbit while students read."""
    scene.set_camera_orientation(phi=55 * DEGREES, theta=-8 * DEGREES,
                                 focal_distance=50)


def screen_point(frame, point):
    """Project a world anchor using the same perspective as ManimL's shader."""
    p = frame.to_fixed_frame_point(point)
    distance = frame.get_focal_distance() / frame.get_scale()
    return np.array([p[0], p[1], 0]) / (1 - p[2] / distance)


def attached_label(scene, body, text):
    """One upright label that follows its own restored body after a seek."""
    lines = text.split('|')
    if len(lines) > 1:
        label = VGroup(*[Tex(line.strip()) for line in lines])
        label.arrange(DOWN, buff=0.08)
    else:
        label = Tex(text)
    label = fixed(label.scale(SCALE_TICK).set_color(INK))
    label.anchor = body
    label.offset = UP * (0.65 if len(lines) > 1 else 0.43)

    def follow(mob):
        # Read the anchor from the label, rather than closing over the old body.
        mob.move_to(screen_point(scene.camera.frame, mob.anchor.get_center())
                    + mob.offset)

    label.add_updater(follow)
    label.update()
    return label
