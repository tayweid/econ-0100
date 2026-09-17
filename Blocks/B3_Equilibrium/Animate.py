# maniml Animate.py PriceDiscovery
# Episode B3 companion | Price discovery in 3D.
# Beat IDs match 02_Companion_Storyboard.md. Read construct() top to bottom.
# Sim/ supplies the 3D adapter (fixed frame, projection, camera); the matching
# mechanics run inline here for now — the storyboard's market_model.py rules
# and tests are still pending, and no existing file is touched by this scene.
#
# Animator defaults, all swappable constants below:
#   - TEN_MB/TEN_MC use the storyboard's value pools (MB 12..3, MC 2..11) in a
#     scrambled arrival order. Sorted arrival gives zero displacements (every
#     pair meets at exactly $7), and beat 3.a wants threads to form, snap, and
#     reform; this order gives five snaps, one two-step chain, late fails, and
#     settled prices on [7, 7.5], straddling the crossing.
#   - The 2.b rerun data (MB 11, MC 8) keeps every price an integer:
#     7 standing, 9 to outbid, 9 for the displaced rematch.
#   - 15 fps per the style guide and B2; Sim/'s earlier bundles ran 60.
#   - Staging (per Taylor's viewer notes, 2026-09-16): bare plane, no lanes;
#     head-bars directly over the people; no ID labels; each person is a
#     half-transparent ground disk with the sphere hovering above it; a
#     displacement swap circles the two buyers around each other; in the
#     ten-a-side run every walker first visits the lookout ring at the
#     platform's center and views a ray to every seller — ask on the best
#     one, feasible asks grey, unaffordable ones fainter still. 2.b zooms
#     in on the switch decision (pause 2.b.i): the camera pushes in, the
#     rest of the stage dims, and comparison chips carry the two choices —
#     the seller's $9 > $7, the buyer's $9 < $11 — before the snap.
#     Check lines are dashed with dots under both shadows; they FOLLOW the
#     walking buyer (become-updater, B2's idiom) and solidify into the match
#     thread by a crossfade at contact — in the run, the chosen ray is that
#     dashed line. A challenger pulls up beside the incumbent, who steps
#     over, both facing the seller. The panel draws every match as its
#     PS/CS split — SUPPLY fill below the red price tick, DEMAND above —
#     on the SELLER's quantity column, and every run survey is its own
#     pausepoint (3.a.N, 3.b.N) with each seller's effective ask marked on
#     the graph (best pink, workable grey, unaffordable faint).
#     (Sim/README pinned the camera partly around a seek-restore caveat;
#     Taylor unpinned it 2026-09-16 — check backward seeks over 2.b.i.)
#   - Dollar tags and price labels are world text, billboarded with a ONE-TIME
#     orientation matrix (BILLBOARD): right while the camera only zooms/pans.
#     For future orientation moves, live billboarding needs engine support
#     (CE's add_fixed_orientation_mobjects; requested from manimlive-2d
#     2026-09-16) — swap apply_matrix(BILLBOARD) for it when it lands.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects, camera_home, screen_point


class PriceDiscovery(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        camera_home(self)
        # World-anchored text takes the camera's orientation once (billboard):
        # it scales under any zoom like the world, but stays flat to the screen.
        BILLBOARD = self.camera.frame.get_orientation().as_matrix()

        # ---- The cast. Values are dollars for one unit; positions only stage the view.
        PAIR_MB, PAIR_MC = 10, 4        # 1.a — OneTrade's numbers, so the scenes rhyme
        JOIN_MB, JOIN_MC = 12, 2        # 2.a — the newcomers who still meet at $7
        RERUN_MB, RERUN_MC = 11, 8      # 2.b — the newcomers who make displacement pay
        TEN_MB = [12, 7, 11, 5, 10, 6, 8, 9, 4, 3]      # B1..B10, entry order
        TEN_MC = [3, 6, 9, 8, 7, 2, 5, 10, 11, 4]       # S1..S10

        # ---- Layout and treatment constants.
        FLOOR_AT = np.array([-3.8, -0.35, 0])
        BUYER_X, SELLER_X = -6.2, -1.5
        HOVER = 0.42                    # sphere float height; the ground disk stays on the plane
        VIEW_AT = np.array([-4.4, -0.35, 0])    # the lookout: where a walker surveys the asks
        MEET, QUEUE = 1.55, 2.4         # stand-off distances in front of a seller
        SIDE = 0.3                      # sideways step when a challenger pulls up beside a matched buyer
        TEN_ROWS = list(np.linspace(2.25, -2.7, 10))
        PAIR_ROWS = [TEN_ROWS[2], TEN_ROWS[9]]
        # Head-bars and dollar tags are world objects (they magnify under a
        # camera zoom, like the people); only the panel and captions stay
        # screen-fixed.
        BAR_SCALE, BAR_W = 0.13, 0.12               # world units per dollar, pair beats
        TEN_BAR_SCALE, TEN_BAR_W = 0.10, 0.06       # world units per dollar, ten-a-side
        BAR_LIFT = 0.72                 # world height of a bar's base, above the sphere
        DIM_BAR, LIT_BAR = 0.4, 0.95    # world bars: unmatched vs matched
        DIM_TWIN, LIT_TWIN = 0.45, 1.0  # panel twins: unmatched vs matched
        PANEL_AT = RIGHT * 4.5 + DOWN * 0.2
        DEFINITION_SCALE = 0.7443       # B2's fixed bottom-line size
        DEFINITION_BOTTOM = 0.05

        # ---- 0.a · Platform | The whole market assembles; the panel sorts it.
        head = fixed(title('Where do prices come from?'))
        plane = Rectangle3D(width=7.5, height=5.8, color=MUTED,
                            opacity=0.18, resolution=(2, 2)).move_to(FLOOR_AT)
        edges = Rectangle(width=7.5, height=5.8, color=MUTED,
                          stroke_width=1.5).move_to(FLOOR_AT + OUT * 0.01)
        floor = Group(plane, edges)
        self.play(FadeIn(head), FadeIn(floor))

        crowd_bodies, crowd_bars = {}, {}
        for side, xs, vals, color in [('B', BUYER_X, TEN_MB, DEMAND),
                                      ('S', SELLER_X, TEN_MC, SUPPLY)]:
            for i, value in enumerate(vals):
                base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                              opacity=0.5).set_color(color)
                base.move_to([xs, TEN_ROWS[i], 0.02])
                ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
                ball.move_to([xs, TEN_ROWS[i], HOVER])
                body = Group(base, ball)
                bar_h = value * TEN_BAR_SCALE
                bar = Rectangle3D(width=TEN_BAR_W, height=bar_h, resolution=(2, 2),
                                  opacity=DIM_BAR).set_color(color)
                bar.rotate(90 * DEGREES, RIGHT)
                bar.anchor = body
                bar.z_center = BAR_LIFT + bar_h / 2
                bar.add_updater(lambda m: m.move_to(
                    [m.anchor.get_center()[0], m.anchor.get_center()[1], m.z_center]))
                bar.update()
                crowd_bodies[side, i] = body
                crowd_bars[side, i] = bar
        for side in ['B', 'S']:
            self.play(*[FadeIn(crowd_bodies[side, i]) for i in range(10)], run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(crowd_bars[side, i], IN)
                                    for i in range(10)], lag_ratio=0.06), run_time=1.4)

        ten_ax = style_axes(x_range=[0, 10, 1], y_range=[0, 14, 2],
                            x_length=4.6, y_length=4.1).move_to(PANEL_AT)
        ten_caps = VGroup(
            Tex(narration('Dollars / unit')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(ten_ax.y_axis, UP, buff=0.2),
            Tex(narration('Units')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(ten_ax.c2p(10, 0), RIGHT, buff=0.18))
        ten_ticks = VGroup(*[Tex(str(p)).scale(SCALE_TICK).set_color(MUTED)
                             .next_to(ten_ax.c2p(0, p), LEFT, buff=0.13) for p in [0, 4, 8, 12]],
                           *[Tex(str(q)).scale(SCALE_TICK).set_color(MUTED)
                             .next_to(ten_ax.c2p(q, 0), DOWN, buff=0.1) for q in [2, 4, 6, 8, 10]])
        ten_panel = fixed(VGroup(ten_ax, ten_caps, ten_ticks))
        # Twins enter on entry-order slots (a jagged crowd), then sort into the
        # two staircases: descending MB rank for demand, ascending MC for supply.
        d_slot = {i: rank for rank, i in
                  enumerate(sorted(range(10), key=lambda i: -TEN_MB[i]))}
        s_slot = {j: rank for rank, j in
                  enumerate(sorted(range(10), key=lambda j: TEN_MC[j]))}
        crowd_twins = {}
        for side, vals, slots, color in [('B', TEN_MB, d_slot, DEMAND),
                                         ('S', TEN_MC, s_slot, SUPPLY)]:
            for i, value in enumerate(vals):
                twin = fixed(Line(ten_ax.c2p(i, value), ten_ax.c2p(i + 1, value),
                                  color=color, stroke_width=5).set_opacity(DIM_TWIN))
                crowd_twins[side, i] = twin
        self.play(FadeIn(ten_panel), *[FadeIn(t) for t in crowd_twins.values()])
        self.play(*[crowd_twins['B', i].animate.shift(
                        ten_ax.c2p(d_slot[i], 0) - ten_ax.c2p(i, 0)) for i in range(10)],
                  *[crowd_twins['S', j].animate.shift(
                        ten_ax.c2p(s_slot[j], 0) - ten_ax.c2p(j, 0)) for j in range(10)],
                  run_time=2)
        d_lab = fixed(Tex('D').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, min(TEN_MB)), RIGHT, buff=0.15))
        s_lab = fixed(Tex('S').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, max(TEN_MC)), RIGHT, buff=0.15))
        self.play(FadeIn(d_lab), FadeIn(s_lab))
        self.pause('0.a')

        # ---- Strip to the pair. The title and floor stay; everything else goes.
        for bar in crowd_bars.values():
            bar.clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects if m is not head and m is not floor])

        # ---- 1.a · One buyer, one seller | Walk, meet, match at 7.
        pair_ax = style_axes(x_range=[0, 2, 1], y_range=[0, 14, 2],
                             x_length=2.6, y_length=4.1).move_to(PANEL_AT)
        pair_caps = VGroup(
            Tex(narration('Dollars / unit')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(pair_ax.y_axis, UP, buff=0.2),
            Tex(narration('Units')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(pair_ax.c2p(2, 0), RIGHT, buff=0.18))
        pair_ticks = VGroup(*[Tex(str(p)).scale(SCALE_TICK).set_color(MUTED)
                              .next_to(pair_ax.c2p(0, p), LEFT, buff=0.13) for p in [0, 4, 8, 12]],
                            *[Tex(str(q)).scale(SCALE_TICK).set_color(MUTED)
                              .next_to(pair_ax.c2p(q, 0), DOWN, buff=0.1) for q in [1, 2]])
        pair_panel = fixed(VGroup(pair_ax, pair_caps, pair_ticks))
        self.play(FadeIn(pair_panel))

        # One agent at a time; bodies, head-bars, and panel twins share a key.
        bodies, bars, values, twins = {}, {}, {}, {}
        for key, value, x, row, color in [('B1', PAIR_MB, BUYER_X, PAIR_ROWS[0], DEMAND),
                                          ('S1', PAIR_MC, SELLER_X, PAIR_ROWS[0], SUPPLY)]:
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=0.5).set_color(color)
            base.move_to([x, row, 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([x, row, HOVER])
            bodies[key] = Group(base, ball)
            bar_h = value * BAR_SCALE
            bar = Rectangle3D(width=BAR_W, height=bar_h, resolution=(2, 2),
                              opacity=DIM_BAR).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT)
            bar.anchor = bodies[key]
            bar.z_center = BAR_LIFT + bar_h / 2
            bar.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.z_center]))
            bar.update()
            bars[key] = bar
            tag = Tex(rf'\${value:g}').scale(SCALE_TICK).set_color(INK)
            tag.apply_matrix(BILLBOARD)
            tag.anchor, tag.top_z = bodies[key], BAR_LIFT + bar_h + 0.32
            tag.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.top_z]))
            tag.update()
            values[key] = tag
            twins[key] = fixed(Line(pair_ax.c2p(0, value), pair_ax.c2p(1, value),
                                    color=color, stroke_width=6).set_opacity(DIM_TWIN))
        mb_lab = fixed(Tex('MB').scale(SCALE_TICK).set_color(INK)
                       .next_to(pair_ax.c2p(1, PAIR_MB), RIGHT, buff=0.12))
        mc_lab = fixed(Tex('MC').scale(SCALE_TICK).set_color(INK)
                       .next_to(pair_ax.c2p(1, PAIR_MC), RIGHT, buff=0.12))
        self.play(FadeIn(bodies['B1']), GrowFromEdge(bars['B1'], IN),
                  FadeIn(values['B1']),
                  FadeIn(twins['B1']), FadeIn(mb_lab))
        self.play(FadeIn(bodies['S1']), GrowFromEdge(bars['S1'], IN),
                  FadeIn(values['S1']),
                  FadeIn(twins['S1']), FadeIn(mc_lab))

        # B1 walks the seller line — one seller today. The dashed check line,
        # dotted under both shadows, morphs into the solid match thread as he
        # closes the distance.
        self.play(bodies['B1'].animate.move_to(
            bodies['S1'].get_center() + LEFT * QUEUE), run_time=2)
        tent = VGroup(
            DashedLine([*bodies['B1'].get_center()[:2], 0.03],
                       [*bodies['S1'].get_center()[:2], 0.03],
                       color=TRADE, stroke_width=2.5),
            Dot([*bodies['B1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.55)
        tent.follow = bodies['B1']
        tent.end_pt = [*bodies['S1'].get_center()[:2], 0.03]
        tent.add_updater(lambda m: (
            m[0].become(DashedLine([*m.follow.get_center()[:2], 0.03], m.end_pt,
                                   color=TRADE, stroke_width=2.5).set_opacity(0.55)),
            m[1].move_to([*m.follow.get_center()[:2], 0.03])))
        self.add(tent)
        self.wait(0.6)
        price = (PAIR_MB + PAIR_MC) / 2
        meet_at = bodies['S1'].get_center() + LEFT * MEET
        thread = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag.apply_matrix(BILLBOARD).move_to(
            (meet_at + bodies['S1'].get_center()) / 2 + OUT * 0.3)
        tick = fixed(Line(pair_ax.c2p(0.1, price), pair_ax.c2p(0.9, price),
                          color=GUIDE, stroke_width=3.5))
        tick_tag = fixed(Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
                         .next_to(tick, UP, buff=0.1))
        # The match on the panel: the column splits into PS below and CS
        # above, separated by the red price.
        ps_fill = fixed(Polygon(pair_ax.c2p(0, PAIR_MC), pair_ax.c2p(1, PAIR_MC),
                                pair_ax.c2p(1, price), pair_ax.c2p(0, price),
                                stroke_width=0).set_fill(SUPPLY, AREA_OPACITY))
        cs_fill = fixed(Polygon(pair_ax.c2p(0, price), pair_ax.c2p(1, price),
                                pair_ax.c2p(1, PAIR_MB), pair_ax.c2p(0, PAIR_MB),
                                stroke_width=0).set_fill(DEMAND, AREA_OPACITY))
        split = fixed(Tex(r'They split the difference: $P = (10 + 4)/2 = \$7$.')
                      .scale(DEFINITION_SCALE).set_color(INK))
        split.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(bodies['B1'].animate.move_to(meet_at), run_time=1)
        tent.clear_updaters()
        self.play(FadeOut(tent), FadeIn(thread),
                  FadeIn(ps_fill), FadeIn(cs_fill), FadeIn(tick), FadeIn(tick_tag),
                  FadeIn(deal_tag),
                  bars['B1'].animate.set_opacity(LIT_BAR),
                  bars['S1'].animate.set_opacity(LIT_BAR),
                  twins['B1'].animate.set_opacity(LIT_TWIN),
                  twins['S1'].animate.set_opacity(LIT_TWIN),
                  FadeIn(split))
        self.bring_to_front(tick, tick_tag)
        self.pause('1.a')

        # ---- 1.b · The window | Any price between 4 and 10 would have worked.
        window = fixed(Polygon(pair_ax.c2p(0, PAIR_MC), pair_ax.c2p(1, PAIR_MC),
                               pair_ax.c2p(1, PAIR_MB), pair_ax.c2p(0, PAIR_MB),
                               stroke_color=MUTED, stroke_width=2))
        lo_lab = fixed(Tex(r'\$4').scale(SCALE_TICK * 0.85).set_color(CAPTION)
                       .next_to(pair_ax.c2p(0, PAIR_MC), LEFT, buff=0.5))
        hi_lab = fixed(Tex(r'\$10').scale(SCALE_TICK * 0.85).set_color(CAPTION)
                       .next_to(pair_ax.c2p(0, PAIR_MB), LEFT, buff=0.5))
        window_line = fixed(Tex(r'Any price from \$4 to \$10 works for both;'
                                r' the midpoint is just their split.')
                            .scale(DEFINITION_SCALE).set_color(INK))
        window_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(split)
        self.play(FadeIn(window), FadeIn(lo_lab), FadeIn(hi_lab), FadeIn(window_line))
        self.bring_to_front(tick, tick_tag)
        self.pause('1.b')

        # ---- 2.a · Two and two | The newcomer walks past the taken seller.
        self.play(FadeOut(window), FadeOut(lo_lab), FadeOut(hi_lab),
                  FadeOut(window_line), FadeOut(mb_lab), FadeOut(mc_lab))
        for key, value, x, row, color in [('B2', JOIN_MB, BUYER_X, PAIR_ROWS[1], DEMAND),
                                          ('S2', JOIN_MC, SELLER_X, PAIR_ROWS[1], SUPPLY)]:
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=0.5).set_color(color)
            base.move_to([x, row, 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([x, row, HOVER])
            bodies[key] = Group(base, ball)
            bar_h = value * BAR_SCALE
            bar = Rectangle3D(width=BAR_W, height=bar_h, resolution=(2, 2),
                              opacity=DIM_BAR).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT)
            bar.anchor = bodies[key]
            bar.z_center = BAR_LIFT + bar_h / 2
            bar.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.z_center]))
            bar.update()
            bars[key] = bar
            tag = Tex(rf'\${value:g}').scale(SCALE_TICK).set_color(INK)
            tag.apply_matrix(BILLBOARD)
            tag.anchor, tag.top_z = bodies[key], BAR_LIFT + bar_h + 0.32
            tag.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.top_z]))
            tag.update()
            values[key] = tag
            twins[key] = fixed(Line(pair_ax.c2p(1, value), pair_ax.c2p(2, value),
                                    color=color, stroke_width=6).set_opacity(DIM_TWIN))
        ask_line = fixed(Tex(r"A seller's ask is their deal price if taken,"
                             r' else their cost.')
                         .scale(DEFINITION_SCALE).set_color(INK))
        ask_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(bodies['B2']), GrowFromEdge(bars['B2'], IN),
                  FadeIn(values['B2']), FadeIn(twins['B2']),
                  FadeIn(bodies['S2']), GrowFromEdge(bars['S2'], IN),
                  FadeIn(values['S2']), FadeIn(twins['S2']),
                  FadeIn(ask_line))
        # The panel sorts the newcomers in: MB 12 to the front of demand,
        # MC 2 to the front of supply; the standing $7 tick rides along.
        slot_shift = pair_ax.c2p(1, 0) - pair_ax.c2p(0, 0)
        self.play(twins['B2'].animate.shift(-slot_shift),
                  twins['B1'].animate.shift(slot_shift),
                  twins['S2'].animate.shift(-slot_shift),
                  twins['S1'].animate.shift(slot_shift),
                  tick.animate.shift(slot_shift), tick_tag.animate.shift(slot_shift),
                  ps_fill.animate.shift(slot_shift), cs_fill.animate.shift(slot_shift),
                  run_time=1.5)

        # B2 walks the line: he pulls up BESIDE the matched buyer to check the
        # taken seller — B1 steps over, both face S1 — then moves on to the
        # cheaper ask, and B1 re-centers.
        center_at = bodies['S1'].get_center() + LEFT * MEET
        beside_at = center_at + UP * SIDE + LEFT * 0.2
        nudged_at = center_at + DOWN * SIDE
        thread_nudged = VGroup(
            Line([*nudged_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*nudged_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        self.play(bodies['B2'].animate.move_to(beside_at),
                  bodies['B1'].animate.move_to(nudged_at),
                  ReplacementTransform(thread, thread_nudged),
                  deal_tag.animate.shift(DOWN * (SIDE / 2)), run_time=1.5)
        thread = thread_nudged
        tent = VGroup(
            DashedLine([*bodies['B2'].get_center()[:2], 0.03],
                       [*bodies['S1'].get_center()[:2], 0.03],
                       color=TRADE, stroke_width=2.5),
            Dot([*bodies['B2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.55)
        self.add(tent)
        self.wait(0.6)
        glance = tent
        thread_back = VGroup(
            Line([*center_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*center_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        self.play(bodies['B2'].animate.move_to(
                      bodies['S2'].get_center() + LEFT * QUEUE),
                  bodies['B1'].animate.move_to(center_at),
                  ReplacementTransform(thread, thread_back),
                  deal_tag.animate.shift(UP * (SIDE / 2)),
                  FadeOut(glance), run_time=1.5)
        thread = thread_back
        tent = VGroup(
            DashedLine([*bodies['B2'].get_center()[:2], 0.03],
                       [*bodies['S2'].get_center()[:2], 0.03],
                       color=TRADE, stroke_width=2.5),
            Dot([*bodies['B2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.55)
        tent.follow = bodies['B2']
        tent.end_pt = [*bodies['S2'].get_center()[:2], 0.03]
        tent.add_updater(lambda m: (
            m[0].become(DashedLine([*m.follow.get_center()[:2], 0.03], m.end_pt,
                                   color=TRADE, stroke_width=2.5).set_opacity(0.55)),
            m[1].move_to([*m.follow.get_center()[:2], 0.03])))
        self.add(tent)
        self.wait(0.6)
        price = (JOIN_MB + JOIN_MC) / 2
        meet_at = bodies['S2'].get_center() + LEFT * MEET
        thread2 = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S2'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag2 = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag2.apply_matrix(BILLBOARD).move_to(
            (meet_at + bodies['S2'].get_center()) / 2 + OUT * 0.3)
        ps_fill2 = fixed(Polygon(pair_ax.c2p(0, JOIN_MC), pair_ax.c2p(1, JOIN_MC),
                                 pair_ax.c2p(1, price), pair_ax.c2p(0, price),
                                 stroke_width=0).set_fill(SUPPLY, AREA_OPACITY))
        cs_fill2 = fixed(Polygon(pair_ax.c2p(0, price), pair_ax.c2p(1, price),
                                 pair_ax.c2p(1, JOIN_MB), pair_ax.c2p(0, JOIN_MB),
                                 stroke_width=0).set_fill(DEMAND, AREA_OPACITY))
        tick2 = fixed(Line(pair_ax.c2p(0.1, price), pair_ax.c2p(0.9, price),
                           color=GUIDE, stroke_width=3.5))
        tick2_tag = fixed(Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
                          .next_to(tick2, UP, buff=0.1))
        past_line = fixed(Tex(r'The newcomer walks past the taken seller to the'
                              r' cheaper ask --- and still pays \$7.')
                          .scale(DEFINITION_SCALE).set_color(INK))
        past_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(ask_line)
        self.play(bodies['B2'].animate.move_to(meet_at), run_time=1)
        tent.clear_updaters()
        self.play(FadeOut(tent), FadeIn(thread2),
                  FadeIn(ps_fill2), FadeIn(cs_fill2), FadeIn(tick2), FadeIn(tick2_tag),
                  FadeIn(deal_tag2),
                  bars['B2'].animate.set_opacity(LIT_BAR),
                  bars['S2'].animate.set_opacity(LIT_BAR),
                  twins['B2'].animate.set_opacity(LIT_TWIN),
                  twins['S2'].animate.set_opacity(LIT_TWIN),
                  FadeIn(past_line))
        self.bring_to_front(tick2, tick2_tag, tick, tick_tag)
        self.pause('2.a')

        # ---- 2.b · The switch | Rerun: the newcomer outbids the standing deal.
        rerun_line = fixed(Tex(r'Rerun: same start, different newcomers.')
                           .scale(DEFINITION_SCALE).set_color(INK))
        rerun_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(past_line)
        for key in ['B2', 'S2']:
            bars[key].clear_updaters()
            values[key].clear_updaters()
        # B1 keeps the standing $7 deal with S1; only the newcomers change.
        # S1's twin returns to the front of supply (MC 4 beats the new MC 8),
        # so the standing tick stretches across the pair's slots: B1 at demand
        # slot 1, S1 at supply slot 0.
        self.play(FadeOut(bodies['B2']), FadeOut(bars['B2']), FadeOut(values['B2']),
                  FadeOut(twins['B2']),
                  FadeOut(bodies['S2']), FadeOut(bars['S2']), FadeOut(values['S2']),
                  FadeOut(twins['S2']),
                  FadeOut(thread2), FadeOut(deal_tag2),
                  FadeOut(tick2), FadeOut(tick2_tag),
                  FadeOut(ps_fill2), FadeOut(cs_fill2), FadeIn(rerun_line))
        # A matched pair keeps one quantity column: the whole deal stack —
        # S1's step, B1's step, the PS/CS split, the tick — slides together.
        self.play(twins['S1'].animate.shift(-slot_shift),
                  twins['B1'].animate.shift(-slot_shift),
                  ps_fill.animate.shift(-slot_shift),
                  cs_fill.animate.shift(-slot_shift),
                  tick.animate.put_start_and_end_on(pair_ax.c2p(0.1, 7),
                                                    pair_ax.c2p(0.9, 7)),
                  tick_tag.animate.move_to(
                      (pair_ax.c2p(0.1, 7) + pair_ax.c2p(0.9, 7)) / 2 + UP * 0.22),
                  run_time=1.2)
        for key, value, x, row, color in [('B2', RERUN_MB, BUYER_X, PAIR_ROWS[1], DEMAND),
                                          ('S2', RERUN_MC, SELLER_X, PAIR_ROWS[1], SUPPLY)]:
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=0.5).set_color(color)
            base.move_to([x, row, 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([x, row, HOVER])
            bodies[key] = Group(base, ball)
            bar_h = value * BAR_SCALE
            bar = Rectangle3D(width=BAR_W, height=bar_h, resolution=(2, 2),
                              opacity=DIM_BAR).set_color(color)
            bar.rotate(90 * DEGREES, RIGHT)
            bar.anchor = bodies[key]
            bar.z_center = BAR_LIFT + bar_h / 2
            bar.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.z_center]))
            bar.update()
            bars[key] = bar
            tag = Tex(rf'\${value:g}').scale(SCALE_TICK).set_color(INK)
            tag.apply_matrix(BILLBOARD)
            tag.anchor, tag.top_z = bodies[key], BAR_LIFT + bar_h + 0.32
            tag.add_updater(lambda m: m.move_to(
                [m.anchor.get_center()[0], m.anchor.get_center()[1], m.top_z]))
            tag.update()
            values[key] = tag
        twins['B2'] = fixed(Line(pair_ax.c2p(0, RERUN_MB), pair_ax.c2p(1, RERUN_MB),
                                 color=DEMAND, stroke_width=6).set_opacity(DIM_TWIN))
        twins['S2'] = fixed(Line(pair_ax.c2p(1, RERUN_MC), pair_ax.c2p(2, RERUN_MC),
                                 color=SUPPLY, stroke_width=6).set_opacity(DIM_TWIN))
        self.play(FadeIn(bodies['B2']), GrowFromEdge(bars['B2'], IN),
                  FadeIn(values['B2']), FadeIn(twins['B2']),
                  FadeIn(bodies['S2']), GrowFromEdge(bars['S2'], IN),
                  FadeIn(values['S2']), FadeIn(twins['S2']))

        # B2 walks: the taken seller's ask of $7 beats the fresh MC of 8.
        # He pulls up beside the matched buyer; B1 steps over, and both sit
        # facing S1 — the solid deal and the dashed challenge side by side.
        center_at = bodies['S1'].get_center() + LEFT * MEET
        beside_at = center_at + UP * SIDE + LEFT * 0.2
        nudged_at = center_at + DOWN * SIDE
        thread_nudged = VGroup(
            Line([*nudged_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*nudged_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        tent = VGroup(
            DashedLine([*bodies['B2'].get_center()[:2], 0.03],
                       [*bodies['S1'].get_center()[:2], 0.03],
                       color=TRADE, stroke_width=2.5),
            Dot([*bodies['B2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.55)
        tent.follow = bodies['B2']
        tent.end_pt = [*bodies['S1'].get_center()[:2], 0.03]
        tent.add_updater(lambda m: (
            m[0].become(DashedLine([*m.follow.get_center()[:2], 0.03], m.end_pt,
                                   color=TRADE, stroke_width=2.5).set_opacity(0.55)),
            m[1].move_to([*m.follow.get_center()[:2], 0.03])))
        self.add(tent)
        self.play(bodies['B2'].animate.move_to(beside_at),
                  bodies['B1'].animate.move_to(nudged_at),
                  ReplacementTransform(thread, thread_nudged),
                  deal_tag.animate.shift(DOWN * (SIDE / 2)), run_time=1.5)
        thread = thread_nudged
        self.wait(0.3)

        # ---- 2.b.i · The decision, up close | Dim the rest, push the camera in,
        # and weigh the $9 offer from both sides. Bars and value tags follow the
        # zoom on their own. Per manimlive-2d (2026-09-16): frame center/scale
        # survive backward seeks, but never bind self.camera.frame to a variable
        # across a pause (checkpoints deep-copy it) — animate it inline and pull
        # back to explicit home values instead of save_state/Restore.
        gain_line = fixed(Tex(r'Both sides of the switch gain.')
                          .scale(DEFINITION_SCALE).set_color(INK))
        gain_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(rerun_line)
        self.play(bodies['B1'][0].animate.set_opacity(0.15),
                  bodies['B1'][1].animate.set_opacity(0.3),
                  bars['B1'].animate.set_opacity(0.15),
                  values['B1'].animate.set_opacity(0.08),
                  bodies['S2'][0].animate.set_opacity(0.15),
                  bodies['S2'][1].animate.set_opacity(0.3),
                  bars['S2'].animate.set_opacity(0.15),
                  values['S2'].animate.set_opacity(0.08),
                  FadeOut(deal_tag), FadeIn(gain_line), run_time=0.7)
        self.play(self.camera.frame.animate.scale(0.62).move_to(
            (bodies['B2'].get_center() + bodies['S1'].get_center()) / 2
            + OUT * 0.7), run_time=1.3)
        focus_mid = screen_point(self.camera.frame,
                                 (bodies['B2'].get_center()
                                  + bodies['S1'].get_center()) / 2)
        offer_tag = Tex(r'\$9?').scale(0.65).set_color(GUIDE)
        offer_tag.apply_matrix(BILLBOARD).move_to(
            (bodies['B2'].get_center() + bodies['S1'].get_center()) / 2 + OUT * 0.4)
        chip_b_text = Tex(r'pays \$9 $<$ \$11').scale(SCALE_CAPTION).set_color(INK)
        chip_b = fixed(VGroup(SurroundingRectangle(chip_b_text, buff=0.18,
                                                   color=DEMAND, stroke_width=2),
                              chip_b_text).move_to(focus_mid + LEFT * 0.4 + DOWN * 0.95))
        chip_s_text = Tex(r'gets \$9 $>$ \$7').scale(SCALE_CAPTION).set_color(INK)
        chip_s = fixed(VGroup(SurroundingRectangle(chip_s_text, buff=0.18,
                                                   color=SUPPLY, stroke_width=2),
                              chip_s_text).move_to(focus_mid + LEFT * 0.4 + DOWN * 1.75))
        self.play(FadeIn(chip_b), FadeIn(chip_s), FadeIn(offer_tag), run_time=0.7)
        self.pause('2.b.i')

        self.play(self.camera.frame.animate.set_height(FRAME_HEIGHT).move_to(ORIGIN),
                  FadeOut(chip_b), FadeOut(chip_s), FadeOut(offer_tag), run_time=1.2)
        self.play(bodies['B1'][0].animate.set_opacity(0.5),
                  bodies['B1'][1].animate.set_opacity(1),
                  bars['B1'].animate.set_opacity(LIT_BAR),
                  values['B1'].animate.set_opacity(1),
                  bodies['S2'][0].animate.set_opacity(0.5),
                  bodies['S2'][1].animate.set_opacity(1),
                  bars['S2'].animate.set_opacity(DIM_BAR),
                  values['S2'].animate.set_opacity(1),
                  FadeIn(deal_tag), run_time=0.6)

        # The snap: the outbid at $9 breaks B1's thread; S1 takes the better
        # offer, and the two buyers circle around each other instead of crossing.
        price = (7 + RERUN_MB) / 2
        meet_at = bodies['S1'].get_center() + LEFT * MEET
        thread2 = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag2 = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag2.apply_matrix(BILLBOARD).move_to(
            (meet_at + bodies['S1'].get_center()) / 2 + OUT * 0.3)
        tick2 = fixed(Line(pair_ax.c2p(0.1, price), pair_ax.c2p(0.9, price),
                           color=GUIDE, stroke_width=3.5))
        tick2_tag = fixed(Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
                          .next_to(tick2, UP, buff=0.1))
        ps_fill2 = fixed(Polygon(pair_ax.c2p(0, PAIR_MC), pair_ax.c2p(1, PAIR_MC),
                                 pair_ax.c2p(1, price), pair_ax.c2p(0, price),
                                 stroke_width=0).set_fill(SUPPLY, AREA_OPACITY))
        cs_fill2 = fixed(Polygon(pair_ax.c2p(0, price), pair_ax.c2p(1, price),
                                 pair_ax.c2p(1, RERUN_MB), pair_ax.c2p(0, RERUN_MB),
                                 stroke_width=0).set_fill(DEMAND, AREA_OPACITY))
        outbid_line = fixed(Tex(r'Beating the standing deal: $P = (7 + 11)/2 = \$9$.')
                            .scale(DEFINITION_SCALE).set_color(INK))
        outbid_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(gain_line)
        self.play(FadeOut(thread), FadeOut(deal_tag), FadeOut(tick), FadeOut(tick_tag),
                  FadeOut(ps_fill), FadeOut(cs_fill),
                  MoveAlongPath(bodies['B1'], ArcBetweenPoints(
                      bodies['B1'].get_center(),
                      bodies['S1'].get_center() + LEFT * (QUEUE + 0.9) + DOWN * 0.28,
                      angle=PI / 2)),
                  bars['B1'].animate.set_opacity(DIM_BAR),
                  twins['B1'].animate.set_opacity(DIM_TWIN).put_start_and_end_on(
                      pair_ax.c2p(1, PAIR_MB), pair_ax.c2p(2, PAIR_MB)),
                  MoveAlongPath(bodies['B2'], ArcBetweenPoints(
                      bodies['B2'].get_center(), meet_at, angle=PI / 2)),
                  bars['B2'].animate.set_opacity(LIT_BAR),
                  twins['B2'].animate.set_opacity(LIT_TWIN),
                  FadeIn(outbid_line), run_time=1.4)
        tent.clear_updaters()
        self.play(FadeOut(tent), FadeIn(thread2),
                  FadeIn(ps_fill2), FadeIn(cs_fill2),
                  FadeIn(deal_tag2), FadeIn(tick2), FadeIn(tick2_tag), run_time=0.4)
        self.bring_to_front(tick2, tick2_tag)
        self.wait(0.5)

        # Displaced, B1 starts over: S1 now asks $9, so the fresh MC 8 wins.
        tent = VGroup(
            DashedLine([*bodies['B1'].get_center()[:2], 0.03],
                       [*bodies['S2'].get_center()[:2], 0.03],
                       color=TRADE, stroke_width=2.5),
            Dot([*bodies['B1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.55)
        tent.follow = bodies['B1']
        tent.end_pt = [*bodies['S2'].get_center()[:2], 0.03]
        tent.add_updater(lambda m: (
            m[0].become(DashedLine([*m.follow.get_center()[:2], 0.03], m.end_pt,
                                   color=TRADE, stroke_width=2.5).set_opacity(0.55)),
            m[1].move_to([*m.follow.get_center()[:2], 0.03])))
        self.add(tent)
        self.play(bodies['B1'].animate.move_to(
            bodies['S2'].get_center() + LEFT * QUEUE), run_time=1.5)
        self.wait(0.6)
        price = (PAIR_MB + RERUN_MC) / 2
        meet_at = bodies['S2'].get_center() + LEFT * MEET
        thread = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S2'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag.apply_matrix(BILLBOARD).move_to(
            (meet_at + bodies['S2'].get_center()) / 2 + OUT * 0.3)
        tick = fixed(Line(pair_ax.c2p(1.1, price), pair_ax.c2p(1.9, price),
                          color=GUIDE, stroke_width=3.5))
        tick_tag = fixed(Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
                         .next_to(tick, UP, buff=0.1))
        restart_line = fixed(Tex(r'Displaced, the first buyer starts over --- and settles at \$9.')
                             .scale(DEFINITION_SCALE).set_color(INK))
        restart_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        ps_fill3 = fixed(Polygon(pair_ax.c2p(1, RERUN_MC), pair_ax.c2p(2, RERUN_MC),
                                 pair_ax.c2p(2, price), pair_ax.c2p(1, price),
                                 stroke_width=0).set_fill(SUPPLY, AREA_OPACITY))
        cs_fill3 = fixed(Polygon(pair_ax.c2p(1, price), pair_ax.c2p(2, price),
                                 pair_ax.c2p(2, PAIR_MB), pair_ax.c2p(1, PAIR_MB),
                                 stroke_width=0).set_fill(DEMAND, AREA_OPACITY))
        self.remove(outbid_line)
        self.play(bodies['B1'].animate.move_to(meet_at), run_time=1)
        tent.clear_updaters()
        self.play(FadeOut(tent), FadeIn(thread),
                  FadeIn(ps_fill3), FadeIn(cs_fill3), FadeIn(tick), FadeIn(tick_tag),
                  FadeIn(deal_tag),
                  bars['B1'].animate.set_opacity(LIT_BAR),
                  bars['S2'].animate.set_opacity(LIT_BAR),
                  twins['B1'].animate.set_opacity(LIT_TWIN),
                  twins['S2'].animate.set_opacity(LIT_TWIN),
                  FadeIn(restart_line))
        self.bring_to_front(tick, tick_tag)
        self.pause('2.b')

        # ---- Strip to the full market.
        for key in bars:
            bars[key].clear_updaters()
            values[key].clear_updaters()
        self.play(*[FadeOut(m) for m in self.mobjects if m is not head and m is not floor])

        # ---- 3.a · Ten and ten | The full cast walks in entry order.
        # The mechanics, inline (market_model.py rules pending): a walker takes
        # the lowest feasible ask; both fresh split (MB + MC)/2; outbidding a
        # taken seller splits (standing + MB)/2 and must beat the standing deal;
        # nobody deals at a loss; a displaced buyer starts over immediately.
        events = []
        deal_b, deal_s = {}, {}         # buyer -> (seller, price), seller -> (buyer, price)
        for entrant in range(10):
            stack = [entrant]
            while stack:
                b = stack.pop()
                mb = TEN_MB[b]
                asks = {s: (deal_s[s][1] if s in deal_s else TEN_MC[s])
                        for s in range(10)}
                workable = {s: (mb > asks[s] if s in deal_s else asks[s] <= mb)
                            for s in range(10)}
                chosen = next((s for s in sorted(range(10), key=lambda s: (asks[s], s))
                               if workable[s]), None)
                # The walker's view from the lookout: one verdict per seller.
                view = [(s, asks[s], 'best' if s == chosen else
                         ('ok' if workable[s] else 'no')) for s in range(10)]
                if chosen is None:
                    events.append(('fail', b, view))
                    continue
                price = (mb + asks[chosen]) / 2
                if chosen in deal_s:
                    old = deal_s[chosen][0]
                    del deal_b[old]
                    stack.append(old)
                    events.append(('displace', b, chosen, price, old, view))
                else:
                    events.append(('match', b, chosen, price, view))
                deal_b[b] = (chosen, price)
                deal_s[chosen] = (b, price)
        last_action = max(i for i, e in enumerate(events) if e[0] != 'fail')

        # Rebuild the 0.a world, panel already sorted; then let the run play out.
        crowd_bodies, crowd_bars, crowd_twins = {}, {}, {}
        for side, xs, vals, color in [('B', BUYER_X, TEN_MB, DEMAND),
                                      ('S', SELLER_X, TEN_MC, SUPPLY)]:
            for i, value in enumerate(vals):
                base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                              opacity=0.5).set_color(color)
                base.move_to([xs, TEN_ROWS[i], 0.02])
                ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
                ball.move_to([xs, TEN_ROWS[i], HOVER])
                body = Group(base, ball)
                bar_h = value * TEN_BAR_SCALE
                bar = Rectangle3D(width=TEN_BAR_W, height=bar_h, resolution=(2, 2),
                                  opacity=DIM_BAR).set_color(color)
                bar.rotate(90 * DEGREES, RIGHT)
                bar.anchor = body
                bar.z_center = BAR_LIFT + bar_h / 2
                bar.add_updater(lambda m: m.move_to(
                    [m.anchor.get_center()[0], m.anchor.get_center()[1], m.z_center]))
                bar.update()
                slot = d_slot[i] if side == 'B' else s_slot[i]
                twin = fixed(Line(ten_ax.c2p(slot, value), ten_ax.c2p(slot + 1, value),
                                  color=color, stroke_width=5).set_opacity(DIM_TWIN))
                crowd_bodies[side, i] = body
                crowd_bars[side, i] = bar
                crowd_twins[side, i] = twin
        ten_panel = fixed(VGroup(ten_ax, ten_caps, ten_ticks).copy())
        d_lab = fixed(Tex('D').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, min(TEN_MB)), RIGHT, buff=0.15))
        s_lab = fixed(Tex('S').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, max(TEN_MC)), RIGHT, buff=0.15))
        lookout = Circle(radius=0.3, color=MUTED, stroke_width=2).move_to(
            [VIEW_AT[0], VIEW_AT[1], 0.02]).set_stroke(opacity=0.6)
        home = {i: crowd_bodies['B', i].get_center().copy() for i in range(10)}
        self.play(*[FadeIn(b) for b in crowd_bodies.values()],
                  *[FadeIn(b) for b in crowd_bars.values()], FadeIn(lookout),
                  FadeIn(ten_panel), *[FadeIn(t) for t in crowd_twins.values()],
                  FadeIn(d_lab), FadeIn(s_lab))

        threads, deal_tags, ticks, areas = {}, {}, {}, {}   # keyed by seller index
        for step, event in enumerate(events[:last_action + 1], start=1):
            b, view = event[1], event[-1]
            # Every walk starts at the lookout: a ray to each seller (best
            # workable ask dashed in TRADE pink with its price, the rest grey),
            # and the same choices marked on the graph — a stub at every
            # seller's column at their effective ask. Each survey is its own
            # pausepoint, so the choice can be talked through.
            self.play(crowd_bodies['B', b].animate.move_to(
                [VIEW_AT[0], VIEW_AT[1], crowd_bodies['B', b].get_center()[2]]),
                run_time=0.6)
            rays, marks, ask_tag, best_check = VGroup(), VGroup(), None, None
            best_end = None
            for s, ask, verdict in view:
                seller_ground = crowd_bodies['S', s].get_center()
                ray_a = [VIEW_AT[0], VIEW_AT[1], 0.03]
                ray_b = [seller_ground[0], seller_ground[1], 0.03]
                sj = s_slot[s]
                mark = fixed(Dot(ten_ax.c2p(sj + 0.5, ask), radius=0.06))
                if verdict == 'best':
                    mark.set_color(TRADE).set_opacity(1)
                    marks.add(mark)
                    best_end = ray_b
                    best_check = VGroup(
                        DashedLine(ray_a, ray_b, color=TRADE, stroke_width=2.5),
                        Dot(ray_a, radius=0.05, color=TRADE),
                        Dot(ray_b, radius=0.05, color=TRADE)).set_opacity(0.9)
                    ask_tag = Tex(rf'\${ask:g}').scale(
                        SCALE_TICK * 0.68).set_color(GUIDE)
                    ask_tag.apply_matrix(BILLBOARD).move_to(
                        (np.array(ray_a) + np.array(ray_b)) / 2 + OUT * 0.3)
                    continue
                if verdict == 'ok':
                    mark.set_color(INK).set_opacity(0.85)
                else:
                    mark.set_color(MUTED).set_opacity(0.35)
                marks.add(mark)
                ray = Line(ray_a, ray_b)
                if verdict == 'ok':
                    ray.set_stroke(MUTED, width=2, opacity=0.5)
                else:
                    ray.set_stroke(MUTED, width=1.5, opacity=0.2)
                rays.add(ray)
            if best_check is not None:
                best_check.follow = crowd_bodies['B', b]
                best_check.end_pt = best_end
                best_check.add_updater(lambda m: (
                    m[0].become(DashedLine(
                        [*m.follow.get_center()[:2], 0.03], m.end_pt,
                        color=TRADE, stroke_width=2.5).set_opacity(0.9)),
                    m[1].move_to([*m.follow.get_center()[:2], 0.03])))
            looked = [FadeIn(r) for r in rays]
            if best_check is not None:
                looked.append(FadeIn(best_check))
            self.play(LaggedStart(*looked, lag_ratio=0.03), FadeIn(marks),
                      *([FadeIn(ask_tag)] if ask_tag else []), run_time=0.6)
            self.pause(f'3.a.{step}')
            if event[0] == 'match':
                _, b, s, price, _ = event
                seller_at = crowd_bodies['S', s].get_center()
                meet3 = seller_at + LEFT * MEET
                new_thread = VGroup(
                    Line([*meet3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*meet3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                self.play(FadeOut(rays), FadeOut(ask_tag), FadeOut(marks),
                          crowd_bodies['B', b].animate.move_to(meet3), run_time=0.7)
                best_check.clear_updaters()
                threads[s] = new_thread
                deal_tags[s] = Tex(rf'\${price:g}').scale(
                    SCALE_TICK * 0.68).set_color(GUIDE)
                deal_tags[s].apply_matrix(BILLBOARD).move_to(
                    seller_at + LEFT * MEET / 2 + OUT * 0.3)
                sj = s_slot[s]
                ticks[s] = fixed(Line(ten_ax.c2p(sj + 0.1, price),
                                      ten_ax.c2p(sj + 0.9, price),
                                      color=GUIDE, stroke_width=3))
                areas[s] = fixed(VGroup(
                    Polygon(ten_ax.c2p(sj, TEN_MC[s]), ten_ax.c2p(sj + 1, TEN_MC[s]),
                            ten_ax.c2p(sj + 1, price), ten_ax.c2p(sj, price),
                            stroke_width=0).set_fill(SUPPLY, AREA_OPACITY),
                    Polygon(ten_ax.c2p(sj, price), ten_ax.c2p(sj + 1, price),
                            ten_ax.c2p(sj + 1, TEN_MB[b]), ten_ax.c2p(sj, TEN_MB[b]),
                            stroke_width=0).set_fill(DEMAND, AREA_OPACITY)))
                self.play(FadeOut(best_check), FadeIn(new_thread),
                          FadeIn(areas[s]), FadeIn(deal_tags[s]), FadeIn(ticks[s]),
                          crowd_bars['B', b].animate.set_opacity(LIT_BAR),
                          crowd_bars['S', s].animate.set_opacity(LIT_BAR),
                          crowd_twins['B', b].animate.set_opacity(LIT_TWIN)
                          .put_start_and_end_on(ten_ax.c2p(sj, TEN_MB[b]),
                                                ten_ax.c2p(sj + 1, TEN_MB[b])),
                          crowd_twins['S', s].animate.set_opacity(LIT_TWIN),
                          run_time=0.5)
                self.bring_to_front(*ticks.values())
            elif event[0] == 'displace':
                _, b, s, price, old, _ = event
                seller_at = crowd_bodies['S', s].get_center()
                center3 = seller_at + LEFT * MEET
                beside3 = center3 + UP * SIDE + LEFT * 0.2
                nudged3 = center3 + DOWN * SIDE
                nudged_thread = VGroup(
                    Line([*nudged3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*nudged3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                self.play(FadeOut(rays), FadeOut(ask_tag), FadeOut(marks),
                          crowd_bodies['B', b].animate.move_to(beside3),
                          crowd_bodies['B', old].animate.move_to(nudged3),
                          ReplacementTransform(threads[s], nudged_thread),
                          deal_tags[s].animate.shift(DOWN * (SIDE / 2)),
                          run_time=0.7)
                threads[s] = nudged_thread
                self.wait(0.3)
                new_thread = VGroup(
                    Line([*center3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*center3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                new_tag = Tex(rf'\${price:g}').scale(
                    SCALE_TICK * 0.68).set_color(GUIDE)
                new_tag.apply_matrix(BILLBOARD).move_to(
                    seller_at + LEFT * MEET / 2 + OUT * 0.3)
                sj = s_slot[s]
                new_tick = fixed(Line(ten_ax.c2p(sj + 0.1, price),
                                      ten_ax.c2p(sj + 0.9, price),
                                      color=GUIDE, stroke_width=3))
                new_areas = fixed(VGroup(
                    Polygon(ten_ax.c2p(sj, TEN_MC[s]), ten_ax.c2p(sj + 1, TEN_MC[s]),
                            ten_ax.c2p(sj + 1, price), ten_ax.c2p(sj, price),
                            stroke_width=0).set_fill(SUPPLY, AREA_OPACITY),
                    Polygon(ten_ax.c2p(sj, price), ten_ax.c2p(sj + 1, price),
                            ten_ax.c2p(sj + 1, TEN_MB[b]), ten_ax.c2p(sj, TEN_MB[b]),
                            stroke_width=0).set_fill(DEMAND, AREA_OPACITY)))
                # The two buyers circle around each other: the loser swings out
                # the near side while the winner slides into the vacated spot.
                self.play(FadeOut(threads[s]), FadeOut(deal_tags[s]), FadeOut(ticks[s]),
                          FadeOut(areas[s]),
                          MoveAlongPath(crowd_bodies['B', old], ArcBetweenPoints(
                              crowd_bodies['B', old].get_center(),
                              seller_at + LEFT * (QUEUE + 0.9) + DOWN * 0.28,
                              angle=PI / 2)),
                          crowd_bars['B', old].animate.set_opacity(DIM_BAR),
                          crowd_twins['B', old].animate.set_opacity(DIM_TWIN)
                          .put_start_and_end_on(
                              ten_ax.c2p(d_slot[old], TEN_MB[old]),
                              ten_ax.c2p(d_slot[old] + 1, TEN_MB[old])),
                          MoveAlongPath(crowd_bodies['B', b], ArcBetweenPoints(
                              crowd_bodies['B', b].get_center(), center3,
                              angle=PI / 2)),
                          crowd_bars['B', b].animate.set_opacity(LIT_BAR),
                          crowd_twins['B', b].animate.set_opacity(LIT_TWIN)
                          .put_start_and_end_on(ten_ax.c2p(sj, TEN_MB[b]),
                                                ten_ax.c2p(sj + 1, TEN_MB[b])),
                          run_time=0.8)
                best_check.clear_updaters()
                self.play(FadeOut(best_check), FadeIn(new_thread),
                          FadeIn(new_areas), FadeIn(new_tag), FadeIn(new_tick),
                          run_time=0.4)
                threads[s], deal_tags[s], ticks[s], areas[s] = (
                    new_thread, new_tag, new_tick, new_areas)
                self.bring_to_front(*ticks.values())
            else:
                self.play(FadeOut(rays), FadeOut(marks),
                          crowd_bodies['B', b].animate.move_to(home[b]), run_time=0.8)
        self.pause('3.a')

        # ---- 3.b · Settling | The last walkers survey the market from the
        # lookout, find nothing workable, and go home. Everything after the
        # final match or displacement is a fail by construction.
        for step, event in enumerate(events[last_action + 1:], start=1):
            b, view = event[1], event[-1]
            self.play(crowd_bodies['B', b].animate.move_to(
                [VIEW_AT[0], VIEW_AT[1], crowd_bodies['B', b].get_center()[2]]),
                run_time=0.9)
            rays, marks = VGroup(), VGroup()
            for s, ask, verdict in view:
                seller_ground = crowd_bodies['S', s].get_center()
                ray = Line([VIEW_AT[0], VIEW_AT[1], 0.03],
                           [seller_ground[0], seller_ground[1], 0.03])
                ray.set_stroke(MUTED, width=2 if verdict == 'ok' else 1.5,
                               opacity=0.5 if verdict == 'ok' else 0.2)
                rays.add(ray)
                sj = s_slot[s]
                marks.add(fixed(Dot(ten_ax.c2p(sj + 0.5, ask), radius=0.06)
                                .set_color(MUTED).set_opacity(0.35)))
            self.play(LaggedStart(*[FadeIn(r) for r in rays], lag_ratio=0.03),
                      FadeIn(marks), run_time=0.7)
            self.pause(f'3.b.{step}')
            self.play(FadeOut(rays), FadeOut(marks),
                      crowd_bodies['B', b].animate.move_to(home[b]), run_time=0.9)
        self.wait(0.8)
        settle_def = fixed(Tex(r'\mbox{ This settling down, where no one wants to'
                               r' change, is {{equilibrium}}.}',
                               tex_to_color_map={'equilibrium': DEFINITION}))
        settle_def.scale(DEFINITION_SCALE)
        settle_def.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.play(FadeIn(settle_def))
        self.pause('3.b')

        # ---- 4.a · The graph knew | Hold the panel; the ticks sit at the crossing.
        for bar in crowd_bars.values():
            bar.clear_updaters()
        prices = [p for _, p in deal_b.values()]
        band = fixed(Polygon(ten_ax.c2p(0, min(prices) - 0.35),
                             ten_ax.c2p(10, min(prices) - 0.35),
                             ten_ax.c2p(10, max(prices) + 0.35),
                             ten_ax.c2p(0, max(prices) + 0.35),
                             stroke_color=FOCUS, stroke_width=2)
                     .set_fill(FOCUS, opacity=0.08))
        knew_line = fixed(Tex(r'The band the prices found is where the'
                              r' staircases cross.')
                          .scale(DEFINITION_SCALE).set_color(INK))
        knew_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(settle_def)
        self.play(FadeOut(floor), FadeOut(lookout),
                  *[FadeOut(b) for b in crowd_bodies.values()],
                  *[FadeOut(b) for b in crowd_bars.values()],
                  *[FadeOut(t) for t in threads.values()],
                  *[FadeOut(t) for t in deal_tags.values()],
                  run_time=1.2)
        self.play(FadeIn(band), FadeIn(knew_line))
        self.bring_to_front(*ticks.values())
        self.pause('4.a')

        # ---- 5.a · Caveats | The dim twins linger. Wording placeholder until the
        # notes' Companion prose is written; phrases follow the storyboard.
        caveats = fixed(VGroup(
            Tex('Not everyone trades.'),
            Tex('A bigger MB can outbid a bigger need.'),
            Tex('Every buyer saw every ask --- information matters.'))
            .arrange(DOWN, buff=0.45, aligned_edge=LEFT)
            .scale(SCALE_CAPTION).set_color(INK)
            .move_to([-7.2, -0.1, 0], aligned_edge=LEFT))
        self.remove(knew_line)
        for line in caveats:
            self.play(FadeIn(line))
        self.pause('5.a')
