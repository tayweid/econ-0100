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
#   - Staging (per Taylor's viewer notes, 2026-09-16/17): the platform is
#     a round plaza — one soft disk with a rim line and a small hub ring
#     marking the center lookout. Sellers hold an even crescent facing the
#     hub (stalls); buyers gather on the facing crescent at jittered radii
#     (a crowd, not a formation). Approaches are radial: a walker stands
#     MEET in front of a seller along the seller-to-hub line, a challenger
#     pulls up beside the incumbent tangentially (SIDE), and every walk
#     routes through the hub. No ID labels; each person is a faint ground
#     shadow with the orb hovering low above it; a displacement swap
#     circles the two buyers around each other; a survey is a ray to every
#     seller from the hub. 2.b zooms in on the switch decision (pause
#     2.b.i): camera push, the rest dims, comparison chips carry the two
#     choices — the seller's $9 > $7, the buyer's $9 < $11 — before the
#     snap. Check lines are dashed with dots under both shadows; they
#     FOLLOW the walking buyer (become-updater, B2's idiom) and solidify
#     into the match thread by a crossfade at contact — in the run, the
#     chosen ray is that dashed line. The panel draws every match as its
#     PS/CS split — SUPPLY fill below the red price tick, DEMAND above —
#     on the SELLER's quantity column, and every run survey is its own
#     pausepoint (3.a.N, 3.b.N) with each seller's effective ask marked on
#     the graph (best pink, workable grey, unaffordable faint).
#   - The camera narrates the decisions (Taylor, 2026-09-17): whatever
#     is being considered swings to the TOP of the plaza, nearest the
#     title — the whole seller crescent for a survey (theta -90), the
#     one seller for a match or a challenge, held a little off vertical
#     so the radial pair never stacks on screen (run: seller angle - 72;
#     pair beats with $ value tags: seller angle - 55).
#     0.a keeps the establishing drift (-26 to -8) and the 3.b settle
#     sweeps home to -8. orbit_center() pivots every theta move about
#     the plaza's own axis so the plaza holds its place on screen; phi
#     never changes. Backward seeks restore camera orientation too as of
#     maniml cffb0010 (2026-09-16, on main), so stepping back is safe.
#   - The spotlight rule (Taylor, 2026-09-17): light exactly the players
#     in the decision being made. A survey lights the walker and every
#     seller; a challenge lights challenger, incumbent, and seller; once
#     a deal is struck only the chooser and the chosen stay lit — every
#     bystander (and their standing threads and price tags) fades back.
#     The 3.b settle restores the whole tableau. The plaza also SORTS
#     with the panel in 0.a — sellers take crescent spots in ask order,
#     buyers re-slot by MB (the jitter stays with the spot) — and the
#     hub ring is dashed.
#   - Dollar tags and price labels are world text kept flat to the screen
#     by face_camera(), an idempotent updater: it rewrites points only
#     when the camera's orientation actually changed, so it costs nothing
#     while the camera is still (no checkpoint churn), follows any orbit
#     live, and re-faces itself after a seek (updaters run during display
#     restore). This replaces the earlier one-time billboard matrix.

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

        # The two camera companions (the only helpers in the file).
        # face_camera keeps a piece of world text flat to the screen. It is
        # idempotent — nothing is rewritten while the camera holds still —
        # and it re-faces the text after any seek. New labels start with
        # face_mat = identity and call .update() once, so they face the
        # camera before their first play (an animation suspends its own
        # target's updaters).
        def face_camera(m):
            cur = self.camera.frame.get_orientation().as_matrix()
            if np.allclose(cur, m.face_mat, atol=1e-6):
                return
            # Always rebuild from the flat geometry captured on first call
            # (float64 on a fixed base). Rotating the stored float32 points
            # incrementally lets them drift off their plane, and ~40 ticks
            # of drift trips the renderer's planar-fill tolerance.
            if not hasattr(m, 'face_base'):
                m.face_base = [sub.get_points().astype(float).copy()
                               for sub in m.get_family()]
            center = m.get_center().astype(float)
            for sub, base in zip(m.get_family(), m.face_base):
                if len(base):
                    sub.set_points(base @ cur.T)
            m.move_to(center)
            m.face_mat = cur

        # orbit_center gives the frame center that pivots a theta move about
        # the plaza's own vertical axis (home: theta -8, center ORIGIN), so
        # the plaza keeps its place on screen while the view swings.
        def orbit_center(theta_deg):
            a = np.radians(theta_deg + 8)
            rz = np.array([[np.cos(a), -np.sin(a), 0.0],
                           [np.sin(a), np.cos(a), 0.0], [0.0, 0.0, 1.0]])
            return PLAZA_AT - rz @ PLAZA_AT

        # spotlight fades everyone but the decision's cast (Taylor's rule:
        # highlight exactly who is part of the decision being made). It
        # emits animations for one play. `still` names bodies that play
        # already moves (one animation per mobject per play) — their look
        # is handled in a neighbouring play. `skip_threads` leaves a deal's
        # thread and tag alone for the same reason. Threads and tags light
        # with their seller: a standing deal is that seller's ask.
        def spotlight(lit, bodies_d, bars_d, threads_d, tags_d,
                      still=(), skip_threads=()):
            anims = []
            for key, body in bodies_d.items():
                if key in still:
                    continue
                on = key in lit
                anims += [body[0].animate.set_opacity(SHADOW if on else FADE),
                          body[1].animate.set_opacity(1.0 if on else FADE_BALL),
                          bars_d[key].animate.set_opacity(
                              LIT_BAR if on else FADE)]
            for s_, th in threads_d.items():
                if s_ in skip_threads:
                    continue
                on = ('S', s_) in lit
                anims += [th.animate.set_opacity(0.9 if on else FADE_BALL),
                          tags_d[s_].animate.set_opacity(
                              1.0 if on else FADE_TAG)]
            return anims

        # ---- The cast. Values are dollars for one unit; positions only stage the view.
        PAIR_MB, PAIR_MC = 10, 4        # 1.a — OneTrade's numbers, so the scenes rhyme
        JOIN_MB, JOIN_MC = 12, 2        # 2.a — the newcomers who still meet at $7
        RERUN_MB, RERUN_MC = 11, 8      # 2.b — the newcomers who make displacement pay
        TEN_MB = [12, 7, 11, 5, 10, 6, 8, 9, 4, 3]      # B1..B10, entry order
        TEN_MC = [3, 6, 9, 8, 7, 2, 5, 10, 11, 4]       # S1..S10

        # ---- Layout and treatment constants.
        PLAZA_AT = np.array([-4.3, -0.5, 0])    # plaza center — and the lookout
        PLAZA_R = 3.55
        SELLER_R, BUYER_R = 2.75, 2.95  # crescent radii: sellers inside, buyers a step out
        HOVER = 0.30                    # orb float height; the ground shadow stays on the plane
        SHADOW = 0.32                   # ground-shadow opacity
        VIEW_AT = PLAZA_AT              # where a walker surveys the asks
        MEET = 0.85                     # stand-off in front of a seller, along the radial
        SIDE = 0.3                      # tangential step when a challenger pulls up beside a matched buyer
        RETREAT = 3.3                   # how far past the seller a displaced buyer backs off
        # Index 0 is the top of each crescent; buyers get per-person radial
        # jog so the waiting side reads as a crowd, not a formation.
        BUYER_JOG = [0.10, -0.22, 0.16, -0.12, 0.24, -0.18, 0.08, -0.26, 0.20, -0.08]
        SELLER_SPOT = {i: PLAZA_AT + SELLER_R * np.array([np.cos(a), np.sin(a), 0])
                       for i, a in enumerate(np.radians(np.linspace(72, -72, 10)))}
        BUYER_SPOT = {i: PLAZA_AT + (BUYER_R + BUYER_JOG[i])
                      * np.array([np.cos(a), np.sin(a), 0])
                      for i, a in enumerate(np.radians(np.linspace(108, 252, 10)))}
        PAIR_SPOT = {key: PLAZA_AT + r * np.array([np.cos(np.radians(deg)),
                                                   np.sin(np.radians(deg)), 0])
                     for key, r, deg in [('S1', SELLER_R, 24), ('S2', SELLER_R, -32),
                                         ('B1', BUYER_R, 156), ('B2', BUYER_R, 212)]}
        # Head-bars and dollar tags are world objects (they magnify under a
        # camera zoom, like the people); only the panel and captions stay
        # screen-fixed.
        BAR_SCALE, BAR_W = 0.13, 0.12               # world units per dollar, pair beats
        TEN_BAR_SCALE, TEN_BAR_W = 0.10, 0.06       # world units per dollar, ten-a-side
        BAR_LIFT = 0.58                 # world height of a bar's base, above the orb
        DIM_BAR, LIT_BAR = 0.4, 0.95    # world bars: unmatched vs matched
        FADE, FADE_BALL, FADE_TAG = 0.10, 0.25, 0.35    # spotlight bystanders
        DIM_TWIN, LIT_TWIN = 0.45, 1.0  # panel twins: unmatched vs matched
        PANEL_AT = RIGHT * 4.5 + DOWN * 0.2
        DEFINITION_SCALE = 0.7443       # B2's fixed bottom-line size
        DEFINITION_BOTTOM = 0.05
        # Open off-axis; 0.a drifts the view home while the market assembles.
        self.camera.frame.reorient(-26, center=orbit_center(-26))

        # ---- 0.a · Platform | The whole market assembles; the panel sorts it.
        head = fixed(title('Where do prices come from?'))
        plane = Disk3D(radius=PLAZA_R, shading=(0, 0, 0),
                       opacity=0.18).set_color(MUTED).move_to(PLAZA_AT)
        rim = Circle(radius=PLAZA_R, color=MUTED, stroke_width=1.5).move_to(
            PLAZA_AT + OUT * 0.01)
        hub = DashedVMobject(Circle(radius=0.35, color=MUTED, stroke_width=2),
                             num_dashes=12).set_stroke(
            opacity=0.6).move_to(PLAZA_AT + OUT * 0.01)
        floor = Group(plane, rim, hub)
        self.play(FadeIn(head), FadeIn(floor),
                  self.camera.frame.animate.reorient(
                      -22, center=orbit_center(-22)))

        crowd_bodies, crowd_bars = {}, {}
        for side, spots, vals, color in [('B', BUYER_SPOT, TEN_MB, DEMAND),
                                         ('S', SELLER_SPOT, TEN_MC, SUPPLY)]:
            for i, value in enumerate(vals):
                base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                              opacity=SHADOW).set_color(color)
                base.move_to([spots[i][0], spots[i][1], 0.02])
                ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
                ball.move_to([spots[i][0], spots[i][1], HOVER])
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
        for side, mid_theta, end_theta in [('B', -18, -14), ('S', -11, -8)]:
            self.play(*[FadeIn(crowd_bodies[side, i]) for i in range(10)],
                      self.camera.frame.animate.reorient(
                          mid_theta, center=orbit_center(mid_theta)), run_time=0.8)
            self.play(LaggedStart(*[GrowFromEdge(crowd_bars[side, i], IN)
                                    for i in range(10)], lag_ratio=0.06),
                      self.camera.frame.animate.reorient(
                          end_theta, center=orbit_center(end_theta)), run_time=1.4)

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
        # The plaza sorts WITH the panel: sellers take their crescent spots
        # in ask order, buyers re-slot by MB (the jitter stays with the spot,
        # so the crowd keeps its shape); head-bars ride their owners.
        self.play(*[crowd_twins['B', i].animate.shift(
                        ten_ax.c2p(d_slot[i], 0) - ten_ax.c2p(i, 0)) for i in range(10)],
                  *[crowd_twins['S', j].animate.shift(
                        ten_ax.c2p(s_slot[j], 0) - ten_ax.c2p(j, 0)) for j in range(10)],
                  *[crowd_bodies['B', i].animate.move_to(
                        [BUYER_SPOT[d_slot[i]][0], BUYER_SPOT[d_slot[i]][1],
                         crowd_bodies['B', i].get_center()[2]]) for i in range(10)],
                  *[crowd_bodies['S', j].animate.move_to(
                        [SELLER_SPOT[s_slot[j]][0], SELLER_SPOT[s_slot[j]][1],
                         crowd_bodies['S', j].get_center()[2]]) for j in range(10)],
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
        for key, value, color in [('B1', PAIR_MB, DEMAND),
                                  ('S1', PAIR_MC, SUPPLY)]:
            at = PAIR_SPOT[key]
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=SHADOW).set_color(color)
            base.move_to([at[0], at[1], 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([at[0], at[1], HOVER])
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
            tag.face_mat = np.eye(3)
            tag.add_updater(face_camera)
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

        # B1 walks out to look — one seller today, and that seller's spot
        # swings to the top of the plaza, closest to the title. The dashed
        # check line, dotted under both shadows, morphs into the solid match
        # thread as he closes the distance.
        self.play(bodies['B1'].animate.move_to(
                      [VIEW_AT[0], VIEW_AT[1], bodies['B1'].get_center()[2]]),
                  self.camera.frame.animate.reorient(
                      -31, center=orbit_center(-31)), run_time=2)
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
        u1 = VIEW_AT - bodies['S1'].get_center()
        u1 = np.array([u1[0], u1[1], 0.0])
        u1 /= np.linalg.norm(u1)                # S1 -> hub: the approach radial
        t1 = np.array([-u1[1], u1[0], 0.0])     # tangential: side-by-side stands
        meet_at = bodies['S1'].get_center() + u1 * MEET
        thread = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag.face_mat = np.eye(3)
        deal_tag.add_updater(face_camera)
        deal_tag.update()
        deal_tag.move_to((meet_at + bodies['S1'].get_center()) / 2 + OUT * 0.3)
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
        for key, value, color in [('B2', JOIN_MB, DEMAND),
                                  ('S2', JOIN_MC, SUPPLY)]:
            at = PAIR_SPOT[key]
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=SHADOW).set_color(color)
            base.move_to([at[0], at[1], 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([at[0], at[1], HOVER])
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
            tag.face_mat = np.eye(3)
            tag.add_updater(face_camera)
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
        center_at = bodies['S1'].get_center() + u1 * MEET
        beside_at = center_at - t1 * SIDE + u1 * 0.2
        nudged_at = center_at + t1 * SIDE + u1 * 0.45   # yields a full step back
        thread_nudged = VGroup(
            Line([*nudged_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*nudged_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        self.play(bodies['B2'].animate.move_to(beside_at),
                  bodies['B1'].animate.move_to(nudged_at),
                  ReplacementTransform(thread, thread_nudged),
                  deal_tag.animate.shift(t1 * (SIDE / 2)), run_time=1.5)
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
        ).set_opacity(FADE_BALL)
        self.play(bodies['B2'].animate.move_to(
                      [VIEW_AT[0], VIEW_AT[1], bodies['B2'].get_center()[2]]),
                  bodies['B1'].animate.move_to(center_at),
                  ReplacementTransform(thread, thread_back),
                  deal_tag.animate.shift(-t1 * (SIDE / 2)).set_opacity(FADE_TAG),
                  self.camera.frame.animate.reorient(
                      -87, center=orbit_center(-87)),
                  bodies['S1'][0].animate.set_opacity(FADE),
                  bodies['S1'][1].animate.set_opacity(FADE_BALL),
                  bars['S1'].animate.set_opacity(FADE),
                  values['S1'].animate.set_opacity(FADE_BALL),
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
        u2 = VIEW_AT - bodies['S2'].get_center()
        u2 = np.array([u2[0], u2[1], 0.0])
        u2 /= np.linalg.norm(u2)                # S2 -> hub radial
        meet_at = bodies['S2'].get_center() + u2 * MEET
        thread2 = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S2'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag2 = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag2.face_mat = np.eye(3)
        deal_tag2.add_updater(face_camera)
        deal_tag2.update()
        deal_tag2.move_to((meet_at + bodies['S2'].get_center()) / 2 + OUT * 0.3)
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
        self.play(bodies['B2'].animate.move_to(meet_at),
                  bodies['B1'][0].animate.set_opacity(FADE),
                  bodies['B1'][1].animate.set_opacity(FADE_BALL),
                  bars['B1'].animate.set_opacity(FADE),
                  values['B1'].animate.set_opacity(FADE_BALL), run_time=1)
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
                  FadeOut(ps_fill2), FadeOut(cs_fill2),
                  bodies['B1'][0].animate.set_opacity(SHADOW),
                  bodies['B1'][1].animate.set_opacity(1.0),
                  bars['B1'].animate.set_opacity(LIT_BAR),
                  values['B1'].animate.set_opacity(1.0),
                  bodies['S1'][0].animate.set_opacity(SHADOW),
                  bodies['S1'][1].animate.set_opacity(1.0),
                  bars['S1'].animate.set_opacity(LIT_BAR),
                  values['S1'].animate.set_opacity(1.0),
                  thread.animate.set_opacity(0.9),
                  deal_tag.animate.set_opacity(1.0),
                  self.camera.frame.animate.reorient(
                      -31, center=orbit_center(-31)),
                  FadeIn(rerun_line))
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
        for key, value, color in [('B2', RERUN_MB, DEMAND),
                                  ('S2', RERUN_MC, SUPPLY)]:
            at = PAIR_SPOT[key]
            base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                          opacity=SHADOW).set_color(color)
            base.move_to([at[0], at[1], 0.02])
            ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
            ball.move_to([at[0], at[1], HOVER])
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
            tag.face_mat = np.eye(3)
            tag.add_updater(face_camera)
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
        center_at = bodies['S1'].get_center() + u1 * MEET
        beside_at = center_at - t1 * SIDE + u1 * 0.2
        nudged_at = center_at + t1 * SIDE + u1 * 0.45   # yields a full step back
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
        # Re-matching: challenger, incumbent, and seller are the cast —
        # the bystander S2 fades back while the challenge forms.
        self.play(bodies['B2'].animate.move_to(beside_at),
                  bodies['B1'].animate.move_to(nudged_at),
                  ReplacementTransform(thread, thread_nudged),
                  deal_tag.animate.shift(t1 * (SIDE / 2)),
                  bodies['S2'][0].animate.set_opacity(FADE),
                  bodies['S2'][1].animate.set_opacity(FADE_BALL),
                  bars['S2'].animate.set_opacity(FADE),
                  values['S2'].animate.set_opacity(FADE_BALL), run_time=1.5)
        thread = thread_nudged
        self.wait(0.3)

        # ---- 2.b.i · The decision, up close | The cast of three stays lit
        # (S2 already faded), the camera pushes in on the pair, and chips
        # weigh the $9 offer from both sides; the standing $7 tag stays —
        # it is one side of the comparison. Never bind self.camera.frame to
        # a variable across a pause — animate it inline and pull back to the
        # explicit -66 pose.
        gain_line = fixed(Tex(r'Both sides of the switch gain.')
                          .scale(DEFINITION_SCALE).set_color(INK))
        gain_line.set_x(0).to_edge(DOWN, buff=DEFINITION_BOTTOM)
        self.remove(rerun_line)
        self.play(FadeIn(gain_line), run_time=0.5)
        self.play(self.camera.frame.animate.scale(0.62).move_to(
            (bodies['B2'].get_center() + bodies['S1'].get_center()) / 2
            + OUT * 0.7), run_time=1.3)
        focus_mid = screen_point(self.camera.frame,
                                 (bodies['B2'].get_center()
                                  + bodies['S1'].get_center()) / 2)
        offer_tag = Tex(r'\$9?').scale(0.65).set_color(GUIDE)
        offer_tag.face_mat = np.eye(3)
        offer_tag.add_updater(face_camera)
        offer_tag.update()
        offer_tag.move_to(
            bodies['S1'].get_center() - u1 * 0.62 + OUT * 0.35)
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

        self.play(self.camera.frame.animate.set_height(FRAME_HEIGHT).move_to(
                      orbit_center(-31)),
                  FadeOut(chip_b), FadeOut(chip_s), FadeOut(offer_tag),
                  run_time=1.2)

        # The snap: the outbid at $9 breaks B1's thread; S1 takes the better
        # offer, and the two buyers circle around each other instead of crossing.
        price = (7 + RERUN_MB) / 2
        meet_at = bodies['S1'].get_center() + u1 * MEET
        thread2 = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S1'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S1'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag2 = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag2.face_mat = np.eye(3)
        deal_tag2.add_updater(face_camera)
        deal_tag2.update()
        deal_tag2.move_to((meet_at + bodies['S1'].get_center()) / 2 + OUT * 0.3)
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
                      bodies['S1'].get_center() + u1 * RETREAT + t1 * 0.28,
                      angle=PI / 2)),
                  bars['B1'].animate.set_opacity(FADE),
                  values['B1'].animate.set_opacity(FADE_BALL),
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
                  FadeIn(deal_tag2), FadeIn(tick2), FadeIn(tick2_tag),
                  bodies['B1'][0].animate.set_opacity(FADE),
                  bodies['B1'][1].animate.set_opacity(FADE_BALL), run_time=0.4)
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
        # B1's turn to decide: back to the lookout, both sellers to the top,
        # the menu lit — B2, no longer deciding anything, fades back.
        self.play(bodies['B1'].animate.move_to(
                      [VIEW_AT[0], VIEW_AT[1], bodies['B1'].get_center()[2]]),
                  self.camera.frame.animate.reorient(
                      -59, center=orbit_center(-59)),
                  bars['B1'].animate.set_opacity(LIT_BAR),
                  values['B1'].animate.set_opacity(1.0),
                  bodies['S2'][0].animate.set_opacity(SHADOW),
                  bodies['S2'][1].animate.set_opacity(1.0),
                  bars['S2'].animate.set_opacity(LIT_BAR),
                  values['S2'].animate.set_opacity(1.0),
                  bodies['B2'][0].animate.set_opacity(FADE),
                  bodies['B2'][1].animate.set_opacity(FADE_BALL),
                  bars['B2'].animate.set_opacity(FADE),
                  values['B2'].animate.set_opacity(FADE_BALL), run_time=1.5)
        self.play(bodies['B1'][0].animate.set_opacity(SHADOW),
                  bodies['B1'][1].animate.set_opacity(1.0), run_time=0.25)
        self.wait(0.35)
        price = (PAIR_MB + RERUN_MC) / 2
        meet_at = bodies['S2'].get_center() + u2 * MEET
        thread = VGroup(
            Line([*meet_at[:2], 0.03], [*bodies['S2'].get_center()[:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*meet_at[:2], 0.03], radius=0.055, color=TRADE),
            Dot([*bodies['S2'].get_center()[:2], 0.03], radius=0.055, color=TRADE),
        ).set_opacity(0.9)
        deal_tag = Tex(rf'\${price:g}').scale(SCALE_TICK * 0.85).set_color(GUIDE)
        deal_tag.face_mat = np.eye(3)
        deal_tag.add_updater(face_camera)
        deal_tag.update()
        deal_tag.move_to((meet_at + bodies['S2'].get_center()) / 2 + OUT * 0.3)
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
        self.play(bodies['B1'].animate.move_to(meet_at),
                  self.camera.frame.animate.reorient(
                      -87, center=orbit_center(-87)),
                  bodies['S1'][0].animate.set_opacity(FADE),
                  bodies['S1'][1].animate.set_opacity(FADE_BALL),
                  bars['S1'].animate.set_opacity(FADE),
                  values['S1'].animate.set_opacity(FADE_BALL),
                  thread2.animate.set_opacity(FADE_BALL),
                  deal_tag2.animate.set_opacity(FADE_TAG), run_time=1)
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

        # Rebuild the 0.a world exactly as it ended — sorted on the plaza,
        # sorted on the panel; then let the run play out.
        crowd_bodies, crowd_bars, crowd_twins = {}, {}, {}
        for side, spots, vals, color in [('B', BUYER_SPOT, TEN_MB, DEMAND),
                                         ('S', SELLER_SPOT, TEN_MC, SUPPLY)]:
            for i, value in enumerate(vals):
                slot = d_slot[i] if side == 'B' else s_slot[i]
                base = Disk3D(radius=0.21, resolution=(2, 24), shading=(0, 0, 0),
                              opacity=SHADOW).set_color(color)
                base.move_to([spots[slot][0], spots[slot][1], 0.02])
                ball = Sphere(radius=0.16, color=color, resolution=(16, 9))
                ball.move_to([spots[slot][0], spots[slot][1], HOVER])
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
        home = {i: crowd_bodies['B', i].get_center().copy() for i in range(10)}
        # The run plays from behind the crowd: the seller crescent swings to
        # the top — a sorted menu of stalls under the title.
        self.play(*[FadeIn(b) for b in crowd_bodies.values()],
                  *[FadeIn(b) for b in crowd_bars.values()],
                  FadeIn(ten_panel), *[FadeIn(t) for t in crowd_twins.values()],
                  FadeIn(d_lab), FadeIn(s_lab),
                  self.camera.frame.animate.reorient(
                      -90, center=orbit_center(-90)),
                  run_time=2.2)

        threads, deal_tags, ticks, areas = {}, {}, {}, {}   # keyed by seller index
        for step, event in enumerate(events[:last_action + 1], start=1):
            b, view = event[1], event[-1]
            # Every walk starts at the lookout: a ray to each seller (best
            # workable ask dashed in TRADE pink with its price, the rest grey),
            # and the same choices marked on the graph — a stub at every
            # seller's column at their effective ask. Each survey is its own
            # pausepoint, so the choice can be talked through.
            self.play(crowd_bodies['B', b].animate.move_to(
                          [VIEW_AT[0], VIEW_AT[1],
                           crowd_bodies['B', b].get_center()[2]]),
                      self.camera.frame.animate.reorient(
                          -90, center=orbit_center(-90)),
                      *spotlight({('S', s) for s in range(10)},
                                 crowd_bodies, crowd_bars, threads, deal_tags,
                                 still={('B', b)}),
                      run_time=0.8)
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
                    ask_tag.face_mat = np.eye(3)
                    ask_tag.add_updater(face_camera)
                    ask_tag.update()
                    ask_tag.move_to(
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
                      *([FadeIn(ask_tag)] if ask_tag else []),
                      crowd_bodies['B', b][0].animate.set_opacity(SHADOW),
                      crowd_bodies['B', b][1].animate.set_opacity(1.0),
                      crowd_bars['B', b].animate.set_opacity(LIT_BAR),
                      run_time=0.6)
            self.pause(f'3.a.{step}')
            if event[0] == 'match':
                _, b, s, price, _ = event
                seller_at = crowd_bodies['S', s].get_center()
                u = VIEW_AT - seller_at
                u = np.array([u[0], u[1], 0.0])
                u /= np.linalg.norm(u)          # seller -> hub radial
                meet3 = seller_at + u * MEET
                new_thread = VGroup(
                    Line([*meet3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*meet3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                th_deg = np.degrees(np.arctan2(seller_at[1] - PLAZA_AT[1],
                                               seller_at[0] - PLAZA_AT[0])) - 72
                self.play(FadeOut(rays), FadeOut(ask_tag), FadeOut(marks),
                          crowd_bodies['B', b].animate.move_to(meet3),
                          self.camera.frame.animate.reorient(
                              th_deg, center=orbit_center(th_deg)),
                          *spotlight({('B', b), ('S', s)},
                                     crowd_bodies, crowd_bars, threads, deal_tags,
                                     still={('B', b)}),
                          run_time=0.8)
                best_check.clear_updaters()
                threads[s] = new_thread
                deal_tags[s] = Tex(rf'\${price:g}').scale(
                    SCALE_TICK * 0.68).set_color(GUIDE)
                deal_tags[s].face_mat = np.eye(3)
                deal_tags[s].add_updater(face_camera)
                deal_tags[s].update()
                deal_tags[s].move_to(seller_at + u * (MEET / 2) + OUT * 0.3)
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
                u = VIEW_AT - seller_at
                u = np.array([u[0], u[1], 0.0])
                u /= np.linalg.norm(u)          # seller -> hub radial
                t = np.array([-u[1], u[0], 0.0])
                center3 = seller_at + u * MEET
                beside3 = center3 - t * SIDE + u * 0.2
                nudged3 = center3 + t * SIDE
                nudged_thread = VGroup(
                    Line([*nudged3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*nudged3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                th_deg = np.degrees(np.arctan2(seller_at[1] - PLAZA_AT[1],
                                               seller_at[0] - PLAZA_AT[0])) - 72
                self.play(FadeOut(rays), FadeOut(ask_tag), FadeOut(marks),
                          crowd_bodies['B', b].animate.move_to(beside3),
                          crowd_bodies['B', old].animate.move_to(nudged3),
                          ReplacementTransform(threads[s], nudged_thread),
                          deal_tags[s].animate.shift(t * (SIDE / 2)),
                          self.camera.frame.animate.reorient(
                              th_deg, center=orbit_center(th_deg)),
                          *spotlight({('B', b), ('B', old), ('S', s)},
                                     crowd_bodies, crowd_bars, threads, deal_tags,
                                     still={('B', b), ('B', old)},
                                     skip_threads={s}),
                          run_time=0.8)
                threads[s] = nudged_thread
                self.play(crowd_bodies['B', old][0].animate.set_opacity(SHADOW),
                          crowd_bodies['B', old][1].animate.set_opacity(1.0),
                          crowd_bars['B', old].animate.set_opacity(LIT_BAR),
                          run_time=0.25)
                self.wait(0.3)
                new_thread = VGroup(
                    Line([*center3[:2], 0.03], [*seller_at[:2], 0.03],
                         color=TRADE, stroke_width=3.5),
                    Dot([*center3[:2], 0.03], radius=0.05, color=TRADE),
                    Dot([*seller_at[:2], 0.03], radius=0.05, color=TRADE),
                ).set_opacity(0.9)
                new_tag = Tex(rf'\${price:g}').scale(
                    SCALE_TICK * 0.68).set_color(GUIDE)
                new_tag.face_mat = np.eye(3)
                new_tag.add_updater(face_camera)
                new_tag.update()
                new_tag.move_to(seller_at + u * (MEET / 2) + OUT * 0.3)
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
                              seller_at + u * RETREAT + t * 0.28,
                              angle=PI / 2)),
                          crowd_bars['B', old].animate.set_opacity(FADE),
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
                threads[s], deal_tags[s], ticks[s], areas[s] = (
                    new_thread, new_tag, new_tick, new_areas)
                self.play(FadeOut(best_check), FadeIn(new_thread),
                          FadeIn(new_areas), FadeIn(new_tag), FadeIn(new_tick),
                          crowd_bodies['B', old][0].animate.set_opacity(FADE),
                          crowd_bodies['B', old][1].animate.set_opacity(FADE_BALL),
                          run_time=0.4)
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
                          [VIEW_AT[0], VIEW_AT[1],
                           crowd_bodies['B', b].get_center()[2]]),
                      self.camera.frame.animate.reorient(
                          -90, center=orbit_center(-90)),
                      *spotlight({('S', s) for s in range(10)},
                                 crowd_bodies, crowd_bars, threads, deal_tags,
                                 still={('B', b)}),
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
                      FadeIn(marks),
                      crowd_bodies['B', b][0].animate.set_opacity(SHADOW),
                      crowd_bodies['B', b][1].animate.set_opacity(1.0),
                      crowd_bars['B', b].animate.set_opacity(LIT_BAR),
                      run_time=0.7)
            self.pause(f'3.b.{step}')
            self.play(FadeOut(rays), FadeOut(marks),
                      crowd_bodies['B', b].animate.move_to(home[b]), run_time=0.9)
        # The market settles: the view eases home and every deal re-lights —
        # the whole tableau at once, nobody spotlit, nobody hidden.
        self.play(self.camera.frame.animate.reorient(-8, center=ORIGIN),
                  *[crowd_bodies[k][0].animate.set_opacity(SHADOW)
                    for k in crowd_bodies],
                  *[crowd_bodies[k][1].animate.set_opacity(1.0)
                    for k in crowd_bodies],
                  *[crowd_bars['B', i].animate.set_opacity(
                        LIT_BAR if i in deal_b else DIM_BAR) for i in range(10)],
                  *[crowd_bars['S', j].animate.set_opacity(
                        LIT_BAR if j in deal_s else DIM_BAR) for j in range(10)],
                  *[th.animate.set_opacity(0.9) for th in threads.values()],
                  *[t.animate.set_opacity(1.0) for t in deal_tags.values()],
                  run_time=2.5)
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
        self.play(FadeOut(floor),
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
