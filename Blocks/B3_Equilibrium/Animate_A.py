# maniml Animate_A.py PostedPrice
# Episode B3 | Posted price in 3D (Track B).
# Beat IDs match 02_Episode_Storyboard.md. Read construct() top to bottom.
# Same world as Animate.py's PriceDiscovery (plaza, crescents, head-bars,
# threads, screen-fixed panel) with one mechanic swapped: per-seller posted
# tags instead of bilateral midpoint deals. Every market state is computed
# by the pure rules in Sim/posted_price.py (tests in Sim/test_posted_price.py)
# before anything moves; the world only stages what the model decided.
#
# Animator decisions, all swappable constants below:
#   - Cast order is arrival order, values scrambled so the panel has a sort
#     to do and the story lands on the right people: Gary is B0 (served by
#     Molly, S0, at $3 because the lowest IDs pair first), Amanda-Grace is
#     B4 (first in the $3 queue, so "jumping the line" is stepping out of
#     it). Molly S0 (MC 2), Andrew S4 (MC 4). The $6 choice lists are
#     story-cast per the storyboard: Gary buys from Andrew; Amanda-Grace
#     from S5, the other MC-2 seller, so Molly is left holding crates.
#   - The going price (the panel's line) is the cheapest tag a buyer could
#     take right now: the lowest crated tag while crates exist, else the
#     lowest posted tag. Qd/Qs read off the staircases at that price.
#   - Cascades run as rounds: a shortage round lets every queued buyer
#     (ID order) overbid the cheapest serving seller by a tick; an excess
#     round has every crated seller cut a tick (or pull the tag at MC), then
#     buyers switch to strictly cheaper crated tags and willing newcomers
#     step in. From $3: 7 rounds to $4; from $6: 18 rounds to $4. No
#     sub-pausepoints inside the cascades; UP/DOWN still step the plays.
#   - Price tags, gauges, readouts and offers are attached labels (screen
#     projected via scene_layers.screen_point, so DecimalNumbers can roll on
#     trackers); head-bars stay world objects. The camera holds home until
#     the 4.b flatten, the one orientation change in the scene (backward
#     seeks across it keep the flat view; known maniml gap).
#   - The bumper is rebuilt inline with fixed() squares: the shared helpers
#     add world geometry, which the 3D camera would tilt.
#   - 4.a stages the perturbation with Andrew and his MB-4 buyer: a raised
#     tag loses the marginal buyer under the no-loss rule; the buyer's
#     lowball is refused because his seller already sells at the tag.
#   - 5.b draws the exchange-rate line at A3's worked rate (1 C = 3 S); the
#     notes give no carrot price. See ANIMATOR-Q there.

from manim import *
import numpy as np
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
sys.path.append(os.path.join(os.path.dirname(__file__), '../Sim'))
from style import *
from style import axes as style_axes
from scene_layers import fixed, add_market_objects, camera_home, screen_point
from posted_price import (TICK, crates, going, overbid, post, quantities, queue,
                          run_excess, run_shortage, settled, undercut)
from Video import PPF_Molly, PPF_Andrew


class PostedPrice(ThreeDScene):
    default_camera_config = {'fps': 15}
    add = add_market_objects

    def construct(self):
        self.camera.fps = 15
        camera_home(self)

        # ---- The cast. Values are dollars for one unit; IDs are arrival order.
        TEN_MB = [6, 5, 4, 3, 6, 5, 4, 3, 2, 2]      # B0..B9
        TEN_MC = [2, 4, 3, 5, 4, 2, 6, 3, 5, 6]      # S0..S9
        B_GARY, B_AMANDA_GRACE, S_MOLLY, S_ANDREW = 0, 4, 0, 4
        SHORTAGE_AT, EXCESS_AT = 3, 6
        JUMP_OFFER, MOLLY_CUT = 3.25, 5              # the notes' own numbers
        EXCESS_CHOICE = {B_GARY: [S_ANDREW], B_AMANDA_GRACE: [5]}
        RAISE_TRY, LOWBALL_TRY = 4.25, 3.75          # 4.a's perturbation
        RATE_S_PER_C = 3                             # 5.b, A3's worked rate

        # ---- Layout and treatment constants (world half shared with Animate.py).
        PLAZA_AT = np.array([-4.3, -0.5, 0])
        PLAZA_R = 3.55
        SELLER_R, BUYER_R = 2.75, 2.95
        HOVER, SHADOW = 0.30, 0.32
        MEET, SIDE = 0.85, 0.3
        BUYER_JOG = [0.10, -0.22, 0.16, -0.12, 0.24, -0.18, 0.08, -0.26, 0.20, -0.08]
        SELLER_SPOT = {i: PLAZA_AT + SELLER_R * np.array([np.cos(a), np.sin(a), 0])
                       for i, a in enumerate(np.radians(np.linspace(72, -72, 10)))}
        BUYER_SPOT = {i: PLAZA_AT + (BUYER_R + BUYER_JOG[i])
                      * np.array([np.cos(a), np.sin(a), 0])
                      for i, a in enumerate(np.radians(np.linspace(108, 252, 10)))}
        QUEUE_SPOT = {k: PLAZA_AT + LEFT * (0.8 + 0.45 * k) for k in range(4)}
        TEN_BAR_SCALE, TEN_BAR_W = 0.10, 0.06
        BAR_LIFT = 0.58
        DIM_BAR, LIT_BAR = 0.4, 0.95
        DIM_TWIN, LIT_TWIN = 0.45, 1.0
        CRATE_SIDE, CRATE_OUT = 0.22, 0.42       # crate size; tangential step from the stall
        TAG_OUT, TAG_Z, TAG_SCALE = 0.72, 0.3, 0.62   # tag: outward of the stall, low
        PANEL_AT = RIGHT * 4.5 + DOWN * 0.2
        GAUGE_RIGHT, GAUGE_Y = 7.5, (3.05, 2.6)      # top-right corner, clear of the panel
        GRAPH_AT = np.array([-2.6, 0.15, 0])         # 4.b+: B2's graph position
        # Per-seller geometry: u is the stall-to-hub radial (a buyer stands
        # MEET along it), t the tangent; crates sit a step along t, tags a
        # step outward.
        U, T, MEET_AT, BESIDE_AT, CRATE_AT, TAG_AT = {}, {}, {}, {}, {}, {}
        for s in range(10):
            u = PLAZA_AT - SELLER_SPOT[s]
            u = np.array([u[0], u[1], 0.0]) / np.linalg.norm(u[:2])
            U[s], T[s] = u, np.array([-u[1], u[0], 0.0])
            MEET_AT[s] = SELLER_SPOT[s] + u * MEET
            BESIDE_AT[s] = MEET_AT[s] + T[s] * SIDE + u * 0.2
            CRATE_AT[s] = SELLER_SPOT[s] + T[s] * CRATE_OUT + OUT * (CRATE_SIDE / 2)
            TAG_AT[s] = SELLER_SPOT[s] - u * TAG_OUT + OUT * TAG_Z

        # ---- 0.a · Title | MICROECONOMICS raster, "Part B | Episode 3".
        # Rebuilt from the bumper helpers' pieces so the squares are flat.
        squares = fixed(VGroup(*Raster_Font('MICROECONOMICS')))
        self.play(FadeIn(squares))
        flicker(self, squares)
        episode = fixed(part_label('B', 3).move_to(DOWN * 0.9))
        self.play(AddTextWordByWord(episode), squares.animate.move_to(UP * 0.9))
        flicker(self, squares)
        thesis = fixed(Tex(r'\textit{Equilibrium: when no one wants to change}',
                           color=CAPTION).scale(1.1).next_to(episode, DOWN, buff=0.5))
        self.play(FadeIn(thesis))
        self.pause('0.a')
        self.play(FadeOut(squares), FadeOut(episode), FadeOut(thesis))

        # ---- 1.a · Recap, two curves | The crowd files in; the panel sorts it.
        head = fixed(title('What happens to the price of spinach?'))
        plane = Disk3D(radius=PLAZA_R, shading=(0, 0, 0),
                       opacity=0.18).set_color(MUTED).move_to(PLAZA_AT)
        rim = Circle(radius=PLAZA_R, color=MUTED, stroke_width=1.5).move_to(
            PLAZA_AT + OUT * 0.01)
        hub = Circle(radius=0.35, color=MUTED, stroke_width=2).set_stroke(
            opacity=0.6).move_to(PLAZA_AT + OUT * 0.01)
        floor = Group(plane, rim, hub)
        self.play(FadeIn(head), FadeIn(floor))

        bodies, bars = {}, {}
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
                bodies[side, i] = body
                bars[side, i] = bar
        BODY_Z = bodies['B', 0].get_center()[2]   # walks keep this height
        home = {b: np.array([*BUYER_SPOT[b][:2], BODY_Z]) for b in range(10)}
        for s in range(10):
            MEET_AT[s][2] = BESIDE_AT[s][2] = BODY_Z
        for k in QUEUE_SPOT:
            QUEUE_SPOT[k][2] = BODY_Z
        for side in ['B', 'S']:
            self.play(LaggedStart(*[FadeIn(bodies[side, i]) for i in range(10)],
                                  lag_ratio=0.1), run_time=1.2)
            self.play(LaggedStart(*[GrowFromEdge(bars[side, i], IN) for i in range(10)],
                                  lag_ratio=0.06), run_time=1.4)

        ten_ax = style_axes(x_range=[0, 10, 1], y_range=[0, 8, 2],
                            x_length=4.6, y_length=4.1).move_to(PANEL_AT)
        ten_caps = VGroup(
            Tex(narration('Dollars / unit')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(ten_ax.y_axis, UP, buff=0.2),
            Tex(narration('Units')).scale(SCALE_TICK).set_color(CAPTION)
                .next_to(ten_ax.c2p(10, 0), RIGHT, buff=0.18))
        ten_ticks = VGroup(*[Tex(str(p)).scale(SCALE_TICK).set_color(MUTED)
                             .next_to(ten_ax.c2p(0, p), LEFT, buff=0.13) for p in [0, 2, 4, 6, 8]],
                           *[Tex(str(q)).scale(SCALE_TICK).set_color(MUTED)
                             .next_to(ten_ax.c2p(q, 0), DOWN, buff=0.1) for q in [2, 4, 6, 8, 10]])
        ten_panel = fixed(VGroup(ten_ax, ten_caps, ten_ticks))
        self.play(FadeIn(ten_panel))
        # Each head-bar's twin flies up from the bar to an entry-order slot,
        # then the twins sort: descending MB for demand, ascending MC for supply.
        d_slot = {i: rank for rank, i in
                  enumerate(sorted(range(10), key=lambda i: -TEN_MB[i]))}
        s_slot = {j: rank for rank, j in
                  enumerate(sorted(range(10), key=lambda j: TEN_MC[j]))}
        twins = {}
        for side, vals, slots, color in [('B', TEN_MB, d_slot, DEMAND),
                                         ('S', TEN_MC, s_slot, SUPPLY)]:
            for i, value in enumerate(vals):
                twin = fixed(Line(ten_ax.c2p(i, value), ten_ax.c2p(i + 1, value),
                                  color=color, stroke_width=5).set_opacity(DIM_TWIN))
                twin.slot_at = twin.get_center().copy()
                top = bars[side, i].get_center() + OUT * (value * TEN_BAR_SCALE / 2)
                twin.move_to(screen_point(self.camera.frame, top))
                twins[side, i] = twin
            self.play(*[FadeIn(twins[side, i]) for i in range(10)], run_time=0.4)
            self.play(*[twins[side, i].animate.move_to(twins[side, i].slot_at)
                        for i in range(10)], run_time=1.2)
            self.play(*[twins[side, i].animate.shift(
                            ten_ax.c2p(slots[i], 0) - ten_ax.c2p(i, 0)) for i in range(10)],
                      run_time=1.5)
        # The many-farmers limit: the smooth lines the staircases gesture at.
        ghost_d = fixed(Line(ten_ax.c2p(0, 6.5), ten_ax.c2p(10, 1.5), color=MUTED,
                             stroke_width=2).set_opacity(0.5))
        ghost_s = fixed(Line(ten_ax.c2p(0, 1.5), ten_ax.c2p(10, 6.5), color=MUTED,
                             stroke_width=2).set_opacity(0.5))
        d_lab = fixed(Tex('D').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, min(TEN_MB)), RIGHT, buff=0.15))
        s_lab = fixed(Tex('S').scale(SCALE_TICK).set_color(INK)
                      .next_to(ten_ax.c2p(10, max(TEN_MC)), RIGHT, buff=0.15))
        self.play(FadeIn(ghost_d), FadeIn(ghost_s), FadeIn(d_lab), FadeIn(s_lab))
        self.pause('1.a')

        # ---- 1.b · The floating price | A blank tag hovers; the line drifts with a "?".
        p_tr = ValueTracker(4.5)
        price_line = fixed(Line(ten_ax.c2p(0, 4.5), ten_ax.c2p(10, 4.5),
                                color=GUIDE, stroke_width=2.5).set_opacity(0.85))
        price_line.add_updater(lambda m: m.put_start_and_end_on(
            ten_ax.c2p(0, p_tr.get_value()), ten_ax.c2p(10, p_tr.get_value())))
        p_query = fixed(Tex('?').scale(SCALE_TICK).set_color(GUIDE))
        p_query.add_updater(lambda m: m.next_to(
            ten_ax.c2p(0, p_tr.get_value()), LEFT, buff=0.55))
        p_query.update()
        blank_box = RoundedRectangle(width=0.62, height=0.4, corner_radius=0.06,
                                     color=MUTED, stroke_width=1.5).set_fill(BG, 0.85)
        blank_tag = fixed(VGroup(blank_box, Tex('?').scale(TAG_SCALE).set_color(INK)))
        blank_tag.add_updater(lambda m: m.move_to(screen_point(
            self.camera.frame,
            PLAZA_AT + RIGHT * SELLER_R * 0.55 + OUT * (0.9 + 0.15 * (p_tr.get_value() - 4)))))
        blank_tag.update()
        self.play(FadeIn(price_line), FadeIn(p_query), FadeIn(blank_tag))
        self.play(p_tr.animate.set_value(3), run_time=1.6)
        self.play(p_tr.animate.set_value(6), run_time=2.2)
        self.play(p_tr.animate.set_value(4.5), run_time=1.6)
        self.pause('1.b')

        # ---- 2.a · Shortage at $3 | Tags post; four serve, eight cross, a queue forms.
        # Everything the panel reads comes from the model state (tags, served).
        tags, served = post(TEN_MB, TEN_MC, SHORTAGE_AT)
        tag_tr = {s: ValueTracker(SHORTAGE_AT) for s in range(10)}
        tag_objs = {}
        for s in range(10):
            box = RoundedRectangle(width=0.78, height=0.36, corner_radius=0.06,
                                   color=MUTED, stroke_width=1.5).set_fill(BG, 0.85)
            num = VGroup(Tex(r'\$').scale(TAG_SCALE),
                         DecimalNumber(SHORTAGE_AT, num_decimal_places=2).scale(TAG_SCALE))
            num.arrange(RIGHT, buff=0.03).set_color(INK)
            num[1].tracker = tag_tr[s]
            num[1].add_updater(lambda m: m.set_value(m.tracker.get_value())
                               if m.get_value() != m.tracker.get_value() else None)
            tag = fixed(VGroup(box, num))
            tag.move_to(screen_point(self.camera.frame, TAG_AT[s]))
            tag_objs[s] = tag
        crate_tpl = {s: Cube(side_length=CRATE_SIDE, color=SUPPLY, opacity=0.75,
                             shading=(0.2, 0.4, 0.1)).move_to(CRATE_AT[s])
                     for s in range(10)}
        crate_objs = {}
        thread_tpl = {s: VGroup(
            Line([*MEET_AT[s][:2], 0.03], [*SELLER_SPOT[s][:2], 0.03],
                 color=TRADE, stroke_width=3.5),
            Dot([*MEET_AT[s][:2], 0.03], radius=0.05, color=TRADE),
            Dot([*SELLER_SPOT[s][:2], 0.03], radius=0.05, color=TRADE),
        ).set_opacity(0.9) for s in range(10)}
        threads = {}
        c_tr, q_tr = ValueTracker(0), ValueTracker(0)
        crate_gauge = fixed(VGroup(Tex('crates').scale(SCALE_CAPTION).set_color(SUPPLY),
                                   Integer(0).scale(SCALE_CAPTION).set_color(INK))
                            .arrange(RIGHT, buff=0.18))
        crate_gauge.move_to([GAUGE_RIGHT, GAUGE_Y[1], 0], aligned_edge=RIGHT)
        crate_gauge[1].add_updater(lambda m: m.set_value(int(round(c_tr.get_value())))
                                   if m.get_value() != int(round(c_tr.get_value())) else None)
        queue_gauge = fixed(VGroup(Tex('queue').scale(SCALE_CAPTION).set_color(DEMAND),
                                   Integer(0).scale(SCALE_CAPTION).set_color(INK))
                            .arrange(RIGHT, buff=0.18))
        queue_gauge.move_to([GAUGE_RIGHT, GAUGE_Y[0], 0], aligned_edge=RIGHT)
        queue_gauge[1].add_updater(lambda m: m.set_value(int(round(q_tr.get_value())))
                                   if m.get_value() != int(round(q_tr.get_value())) else None)
        # Price readout, Qd/Qs drops with readouts, and the gap on the axis,
        # all driven by the one price tracker.
        p_read = fixed(VGroup(Tex(r'\$').scale(SCALE_TICK),
                              DecimalNumber(SHORTAGE_AT, num_decimal_places=2).scale(SCALE_TICK))
                       .arrange(RIGHT, buff=0.03).set_color(GUIDE))
        p_read[1].add_updater(lambda m: m.set_value(p_tr.get_value())
                              if m.get_value() != p_tr.get_value() else None)
        p_read.add_updater(lambda m: m.next_to(
            ten_ax.c2p(0, p_tr.get_value()), LEFT, buff=0.55))
        qd_drop = fixed(Line(ten_ax.c2p(8, 0), ten_ax.c2p(8, 3), color=GUIDE,
                             stroke_width=2).set_opacity(0.5))
        qd_drop.add_updater(lambda m: m.put_start_and_end_on(
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[0], 0),
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[0], p_tr.get_value())))
        qs_drop = fixed(Line(ten_ax.c2p(4, 0), ten_ax.c2p(4, 3), color=GUIDE,
                             stroke_width=2).set_opacity(0.5))
        qs_drop.add_updater(lambda m: m.put_start_and_end_on(
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[1], 0),
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[1], p_tr.get_value())))
        qd_read = fixed(Tex('$Q_d$').scale(SCALE_TICK).set_color(GUIDE))
        qd_read.add_updater(lambda m: m.next_to(
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[0], 0),
            DOWN, buff=0.5).shift(LEFT * 0.32))
        qs_read = fixed(Tex('$Q_s$').scale(SCALE_TICK).set_color(GUIDE))
        qs_read.add_updater(lambda m: m.next_to(
            ten_ax.c2p(quantities(TEN_MB, TEN_MC, p_tr.get_value())[1], 0),
            DOWN, buff=0.5).shift(RIGHT * 0.32))
        gap = fixed(Line(ten_ax.c2p(4, 0), ten_ax.c2p(8, 0), color=TRADE, stroke_width=6))

        def gap_follow(m):
            lo, hi = sorted(quantities(TEN_MB, TEN_MC, p_tr.get_value()))
            m.put_start_and_end_on(ten_ax.c2p(lo, 0), ten_ax.c2p(hi + (1e-3 if hi == lo else 0), 0))
            m.set_opacity(0 if hi == lo else 0.9)
        gap.add_updater(gap_follow)
        for m in [p_read, qd_drop, qs_drop, qd_read, qs_read, gap]:
            m.update()
        for s in tags:
            if tags[s] is not None:
                crate_objs[s] = crate_tpl[s].copy()
        self.play(FadeOut(blank_tag), FadeOut(p_query),
                  p_tr.animate.set_value(SHORTAGE_AT),
                  *[twins['B', i].animate.set_opacity(
                      LIT_TWIN if TEN_MB[i] >= SHORTAGE_AT else DIM_TWIN) for i in range(10)],
                  *[twins['S', j].animate.set_opacity(
                      LIT_TWIN if TEN_MC[j] <= SHORTAGE_AT else DIM_TWIN) for j in range(10)],
                  run_time=1.2)
        p_read.update()
        self.play(FadeIn(p_read),
                  *[FadeIn(tag_objs[s]) for s in tags if tags[s] is not None],
                  *[FadeIn(crate_objs[s]) for s in crate_objs],
                  FadeIn(crate_gauge), FadeIn(queue_gauge), run_time=1.0)
        self.add(gap)
        self.play(FadeIn(qd_drop), FadeIn(qd_read), FadeIn(qs_drop), FadeIn(qs_read),
                  c_tr.animate.set_value(len(crate_objs)))
        # The served buyers cross to their stalls; the crates go with the sale.
        self.play(*[bodies['B', b].animate.move_to(MEET_AT[s]) for b, s in served.items()],
                  run_time=1.6)
        for b, s in served.items():
            threads[s] = thread_tpl[s].copy()
        self.play(*[FadeIn(threads[s]) for s in served.values()],
                  *[FadeOut(crate_objs.pop(s)) for s in list(served.values())],
                  *[bars['B', b].animate.set_opacity(LIT_BAR) for b in served],
                  *[bars['S', s].animate.set_opacity(LIT_BAR) for s in served.values()],
                  c_tr.animate.set_value(0), run_time=0.7)
        # The rest who would buy at $3 line up from the hub; the markers mark the line.
        queue_marks = Group(*[Dot([*QUEUE_SPOT[k][:2], 0.03], radius=0.07, color=MUTED)
                              .set_opacity(0.45) for k in QUEUE_SPOT])
        q_now = queue(TEN_MB, tags, served)
        self.play(FadeIn(queue_marks),
                  *[bodies['B', b].animate.move_to(QUEUE_SPOT[k]) for k, b in enumerate(q_now)],
                  q_tr.animate.set_value(len(q_now)), run_time=1.4)
        self.pause('2.a')

        # ---- 2.b · Amanda-Grace jumps the line | She offers Molly $3.25; Gary's thread snaps.
        gap_word = fixed(Tex('shortage').scale(SCALE_TICK).set_color(CAPTION))
        gap_word.gap = gap
        gap_word.add_updater(lambda m: m.next_to(m.gap, UP, buff=0.1))
        gap_word.update()
        self.play(FadeIn(gap_word))
        ag = bodies['B', B_AMANDA_GRACE]
        self.play(ag.animate.move_to([PLAZA_AT[0], PLAZA_AT[1], BODY_Z]), run_time=0.8)
        self.play(ag.animate.move_to(BESIDE_AT[S_MOLLY]), run_time=1.0)
        offer = fixed(VGroup(Tex(r'\$').scale(SCALE_TICK),
                             DecimalNumber(JUMP_OFFER, num_decimal_places=2).scale(SCALE_TICK),
                             Tex('?').scale(SCALE_TICK))
                      .arrange(RIGHT, buff=0.03).set_color(GUIDE))
        offer.move_to(screen_point(self.camera.frame, BESIDE_AT[S_MOLLY] + OUT * 1.15))
        self.play(FadeIn(offer), run_time=0.5)
        tags, served, displaced = overbid(TEN_MB, tags, served, B_AMANDA_GRACE, S_MOLLY, JUMP_OFFER)
        q_now = queue(TEN_MB, tags, served)
        new_thread = thread_tpl[S_MOLLY].copy()
        self.play(FadeOut(threads[S_MOLLY]), FadeOut(offer),
                  tag_tr[S_MOLLY].animate.set_value(JUMP_OFFER),
                  MoveAlongPath(bodies['B', displaced], ArcBetweenPoints(
                      bodies['B', displaced].get_center(), QUEUE_SPOT[q_now.index(displaced)],
                      angle=PI / 2)),
                  MoveAlongPath(ag, ArcBetweenPoints(ag.get_center(), MEET_AT[S_MOLLY],
                                                     angle=PI / 2)),
                  bars['B', displaced].animate.set_opacity(DIM_BAR),
                  bars['B', B_AMANDA_GRACE].animate.set_opacity(LIT_BAR),
                  *[bodies['B', b].animate.move_to(QUEUE_SPOT[k])
                    for k, b in enumerate(q_now) if b != displaced],
                  run_time=1.4)
        threads[S_MOLLY] = new_thread
        self.play(FadeIn(new_thread), run_time=0.4)
        self.pause('2.b')

        # ---- 2.c · Shortage lesson | Gary rebids; tags ratchet up by ticks; the queue drains.
        up_d = fixed(Arrow(d_lab.get_center() + DOWN * 0.22, d_lab.get_center() + UP * 0.22,
                           buff=0).set_color(FOCUS).next_to(d_lab, RIGHT, buff=0.15))
        up_s = fixed(Arrow(s_lab.get_center() + DOWN * 0.22, s_lab.get_center() + UP * 0.22,
                           buff=0).set_color(FOCUS).next_to(s_lab, RIGHT, buff=0.15))
        self.play(FadeIn(up_d), FadeIn(up_s), run_time=0.5)
        # maniml keeps the namespace as of each play: nothing written after
        # a round's last play survives, so each round assigns the model state
        # first and ends on a play.
        for new_tags, new_served, moves in run_shortage(TEN_MB, TEN_MC, tags, served):
            old_tags, old_served = tags, served
            tags, served = new_tags, new_served
            # Challengers step up beside the buyer they are about to outbid.
            self.play(*[bodies['B', b].animate.move_to(BESIDE_AT[s]) for b, s, _ in moves],
                      run_time=0.6)
            # The snap: tags tick, displaced buyers fall back to the queue,
            # challengers take the stall; the queue closes up in ID order.
            q_after = queue(TEN_MB, new_tags, new_served)
            displaced_now = [d for _, _, d in moves if d is not None]
            still_queued = [b for b in queue(TEN_MB, old_tags, old_served)
                            if b not in {m[0] for m in moves}]
            q_mid = sorted(set(displaced_now) | set(still_queued))
            q_mid = [b for b in q_mid if TEN_MB[b] >= going(new_tags, new_served)]
            new_threads = {s: thread_tpl[s].copy() for _, s, _ in moves}
            p_next = going(new_tags, new_served)
            self.play(*[tag_tr[s].animate.set_value(new_tags[s]) for _, s, _ in moves],
                      *[FadeOut(threads[s]) for _, s, _ in moves],
                      *[bodies['B', d].animate.move_to(QUEUE_SPOT[q_mid.index(d)])
                        for d in displaced_now if d in q_mid],
                      *[bodies['B', b].animate.move_to(home[b])
                        for b in queue(TEN_MB, old_tags, old_served) + displaced_now
                        if b not in q_mid and b not in {m[0] for m in moves}],
                      *[bodies['B', b].animate.move_to(QUEUE_SPOT[q_mid.index(b)])
                        for b in still_queued if b in q_mid],
                      *[bodies['B', b].animate.move_to(MEET_AT[s]) for b, s, _ in moves],
                      *[bars['B', d].animate.set_opacity(DIM_BAR) for d in displaced_now],
                      *[bars['B', b].animate.set_opacity(LIT_BAR) for b, _, _ in moves],
                      p_tr.animate.set_value(p_next),
                      *[twins['B', i].animate.set_opacity(
                          LIT_TWIN if TEN_MB[i] >= p_next else DIM_TWIN) for i in range(10)],
                      *[twins['S', j].animate.set_opacity(
                          LIT_TWIN if TEN_MC[j] <= p_next else DIM_TWIN) for j in range(10)],
                      run_time=0.9)
            threads.update(new_threads)
            entrants = [s for s in range(10) if old_tags[s] is None and new_tags[s] is not None]
            newly_served = [b for b in new_served if (b not in old_served or b in displaced_now)
                            and b not in {m[0] for m in moves}]
            self.play(*[FadeIn(new_threads[s]) for s in new_threads],
                      q_tr.animate.set_value(len(q_after) + len(newly_served)), run_time=0.3)
            # Sellers whose MC the line has reached post a tag and crate up;
            # the queue buys from them.
            if entrants:
                for s in entrants:
                    tag_tr[s].set_value(new_tags[s])
                    tag_objs[s][1][1].update()
                    crate_objs[s] = crate_tpl[s].copy()
                self.play(*[FadeIn(tag_objs[s]) for s in entrants],
                          *[FadeIn(crate_objs[s]) for s in entrants],
                          c_tr.animate.set_value(len(entrants)), run_time=0.6)
            if newly_served:
                self.play(*[bodies['B', b].animate.move_to(MEET_AT[new_served[b]])
                            for b in newly_served], run_time=1.0)
                for b in newly_served:
                    threads[new_served[b]] = thread_tpl[new_served[b]].copy()
                self.play(*[FadeIn(threads[new_served[b]]) for b in newly_served],
                          *[FadeOut(crate_objs.pop(new_served[b])) for b in newly_served
                            if new_served[b] in crate_objs],
                          *[bars['B', b].animate.set_opacity(LIT_BAR) for b in newly_served],
                          *[bars['S', new_served[b]].animate.set_opacity(LIT_BAR)
                            for b in newly_served],
                          *[bodies['B', b].animate.move_to(QUEUE_SPOT[k])
                            for k, b in enumerate(q_after)],
                          c_tr.animate.set_value(len(crates(new_tags, new_served))),
                          q_tr.animate.set_value(len(q_after)), run_time=0.6)
        self.play(FadeOut(up_d), FadeOut(up_s), FadeOut(gap_word), run_time=0.6)
        self.pause('2.c')

        # ---- 3.a · Excess at $6 | Reset: every tag posts $6; only two buy; eight crates.
        self.play(*[FadeOut(t) for t in threads.values()],
                  *[FadeOut(tag_objs[s]) for s in tags if tags[s] is not None],
                  *[bodies['B', b].animate.move_to(home[b]) for b in range(10)],
                  *[bars['B', b].animate.set_opacity(DIM_BAR) for b in range(10)],
                  *[bars['S', s].animate.set_opacity(DIM_BAR) for s in range(10)],
                  FadeOut(queue_marks), run_time=1.4)
        threads.clear()
        tags, served = post(TEN_MB, TEN_MC, EXCESS_AT, choice=EXCESS_CHOICE)
        for s in range(10):
            tag_tr[s].set_value(EXCESS_AT)
            tag_objs[s][1][1].update()
            crate_objs[s] = crate_tpl[s].copy()
        self.play(*[FadeIn(tag_objs[s]) for s in range(10)],
                  *[FadeIn(crate_objs[s]) for s in range(10)],
                  p_tr.animate.set_value(EXCESS_AT), c_tr.animate.set_value(10),
                  *[twins['B', i].animate.set_opacity(
                      LIT_TWIN if TEN_MB[i] >= EXCESS_AT else DIM_TWIN) for i in range(10)],
                  *[twins['S', j].animate.set_opacity(
                      LIT_TWIN if TEN_MC[j] <= EXCESS_AT else DIM_TWIN) for j in range(10)],
                  run_time=1.2)
        self.play(*[bodies['B', b].animate.move_to(MEET_AT[s]) for b, s in served.items()],
                  run_time=1.6)
        for b, s in served.items():
            threads[s] = thread_tpl[s].copy()
        self.play(*[FadeIn(threads[s]) for s in served.values()],
                  *[FadeOut(crate_objs.pop(s)) for s in list(served.values())],
                  *[bars['B', b].animate.set_opacity(LIT_BAR) for b in served],
                  *[bars['S', s].animate.set_opacity(LIT_BAR) for s in served.values()],
                  c_tr.animate.set_value(len(crates(tags, served))), run_time=0.7)
        self.pause('3.a')

        # ---- 3.b · Excess, not surplus | The textbook word appears, is struck, and replaced.
        surplus_word = fixed(Tex('surplus').scale(SCALE_TICK).set_color(CAPTION)
                             .next_to(gap, UP, buff=0.1))
        self.play(FadeIn(surplus_word))
        strike = fixed(Line(surplus_word.get_left() + LEFT * 0.05,
                            surplus_word.get_right() + RIGHT * 0.05,
                            color=CAPTION, stroke_width=2.5))
        self.play(Create(strike), run_time=0.8)
        gap_word = fixed(Tex('excess').scale(SCALE_TICK).set_color(CAPTION))
        gap_word.gap = gap
        gap_word.add_updater(lambda m: m.next_to(m.gap, UP, buff=0.1))
        gap_word.update()
        self.play(FadeOut(surplus_word), FadeOut(strike))
        self.play(FadeIn(gap_word))
        self.pause('3.b')

        # ---- 3.c · Molly undercuts | $6 to $5; Gary swings from Andrew; Andrew cuts too.
        before = dict(served)
        tags, served = undercut(TEN_MB, TEN_MC, tags, served, S_MOLLY, MOLLY_CUT)
        self.play(tag_tr[S_MOLLY].animate.set_value(MOLLY_CUT), run_time=0.8)
        movers = [b for b in served if before.get(b) != served[b]]
        self.play(*[FadeOut(threads.pop(before[b])) for b in movers if b in before],
                  *[bodies['B', b].animate.move_to(MEET_AT[served[b]]) for b in movers],
                  *[FadeOut(crate_objs.pop(served[b])) for b in movers if served[b] in crate_objs],
                  run_time=1.2)
        for b in movers:
            threads[served[b]] = thread_tpl[served[b]].copy()
            if before.get(b) is not None:
                crate_objs[before[b]] = crate_tpl[before[b]].copy()
        self.play(*[FadeIn(threads[served[b]]) for b in movers],
                  *[FadeIn(crate_objs[before[b]]) for b in movers if before.get(b) is not None],
                  *[bars['S', before[b]].animate.set_opacity(DIM_BAR) for b in movers
                    if before.get(b) is not None],
                  *[bars['S', served[b]].animate.set_opacity(LIT_BAR) for b in movers],
                  run_time=0.5)
        # Andrew, holding crates, lowers his price too.
        before = dict(served)
        tags, served = undercut(TEN_MB, TEN_MC, tags, served, S_ANDREW, EXCESS_AT - TICK)
        self.play(tag_tr[S_ANDREW].animate.set_value(EXCESS_AT - TICK), run_time=0.8)
        movers = [b for b in served if before.get(b) != served[b]]
        self.play(*[FadeOut(threads.pop(before[b])) for b in movers if b in before],
                  *[bodies['B', b].animate.move_to(MEET_AT[served[b]]) for b in movers],
                  *[FadeOut(crate_objs.pop(served[b])) for b in movers if served[b] in crate_objs],
                  run_time=1.2)
        for b in movers:
            threads[served[b]] = thread_tpl[served[b]].copy()
            if before.get(b) is not None:
                crate_objs[before[b]] = crate_tpl[before[b]].copy()
        self.play(*[FadeIn(threads[served[b]]) for b in movers],
                  *[FadeIn(crate_objs[before[b]]) for b in movers if before.get(b) is not None],
                  *[bars['S', before[b]].animate.set_opacity(DIM_BAR) for b in movers
                    if before.get(b) is not None],
                  *[bars['S', served[b]].animate.set_opacity(LIT_BAR) for b in movers],
                  run_time=0.5)
        self.pause('3.c')

        # ---- 3.d · Excess lesson | The cascade: crated tags tick down, high-MC sellers
        # pull out, buyers switch and step in, until the crates are gone.
        down_d = fixed(Arrow(d_lab.get_center() + UP * 0.22, d_lab.get_center() + DOWN * 0.22,
                             buff=0).set_color(FOCUS).next_to(d_lab, RIGHT, buff=0.15))
        down_s = fixed(Arrow(s_lab.get_center() + UP * 0.22, s_lab.get_center() + DOWN * 0.22,
                             buff=0).set_color(FOCUS).next_to(s_lab, RIGHT, buff=0.15))
        self.play(FadeIn(down_d), FadeIn(down_s), run_time=0.5)
        for new_tags, new_served, cut, pulled in run_excess(TEN_MB, TEN_MC, tags, served):
            old_served = served
            tags, served = new_tags, new_served
            p_next = going(new_tags, new_served)
            self.play(*[tag_tr[s].animate.set_value(new_tags[s]) for s in cut],
                      c_tr.animate.set_value(len(crates(new_tags, new_served))),
                      *[FadeOut(tag_objs[s]) for s in pulled],
                      *[FadeOut(crate_objs.pop(s)) for s in pulled],
                      *[bars['S', s].animate.set_opacity(DIM_BAR) for s in pulled],
                      p_tr.animate.set_value(p_next),
                      *[twins['B', i].animate.set_opacity(
                          LIT_TWIN if TEN_MB[i] >= p_next else DIM_TWIN) for i in range(10)],
                      *[twins['S', j].animate.set_opacity(
                          LIT_TWIN if TEN_MC[j] <= p_next else DIM_TWIN) for j in range(10)],
                      run_time=0.5)
            movers = [b for b in new_served if old_served.get(b) != new_served[b]]
            if movers:
                self.play(*[FadeOut(threads.pop(old_served[b])) for b in movers if b in old_served],
                          *[bodies['B', b].animate.move_to(MEET_AT[new_served[b]]) for b in movers],
                          *[FadeOut(crate_objs.pop(new_served[b])) for b in movers
                            if new_served[b] in crate_objs],
                          *[bars['B', b].animate.set_opacity(LIT_BAR) for b in movers],
                          run_time=0.7)
                for b in movers:
                    threads[new_served[b]] = thread_tpl[new_served[b]].copy()
                    if b in old_served and old_served[b] not in new_served.values():
                        crate_objs[old_served[b]] = crate_tpl[old_served[b]].copy()
                self.play(*[FadeIn(threads[new_served[b]]) for b in movers],
                          *[FadeIn(crate_objs[old_served[b]]) for b in movers
                            if b in old_served and old_served[b] not in new_served.values()],
                          *[bars['S', old_served[b]].animate.set_opacity(DIM_BAR) for b in movers
                            if b in old_served and old_served[b] not in new_served.values()],
                          *[bars['S', new_served[b]].animate.set_opacity(LIT_BAR) for b in movers],
                          run_time=0.35)
        self.play(FadeOut(down_d), FadeOut(down_s), FadeOut(gap_word), run_time=0.6)
        self.pause('3.d')

        # ---- 4.a · The price that doesn't move | Andrew tries $4.25 and loses his buyer;
        # Gary tries $3.75 and is refused; the tags settle back at $4.
        self.remove(head)
        head = fixed(title("Can there ever be a price that doesn't change?"))
        self.play(FadeIn(head))
        buyer_a = next(b for b, s in served.items() if s == S_ANDREW)
        crate_objs[S_ANDREW] = crate_tpl[S_ANDREW].copy()
        raised = dict(tags)
        raised[S_ANDREW] = RAISE_TRY
        walked = {b: s for b, s in served.items() if b != buyer_a}
        self.play(tag_tr[S_ANDREW].animate.set_value(RAISE_TRY), run_time=0.7)
        self.play(FadeOut(threads.pop(S_ANDREW)), FadeIn(crate_objs[S_ANDREW]),
                  bodies['B', buyer_a].animate.move_to(MEET_AT[S_ANDREW] + U[S_ANDREW] * 0.7),
                  bars['B', buyer_a].animate.set_opacity(DIM_BAR),
                  bars['S', S_ANDREW].animate.set_opacity(DIM_BAR),
                  p_tr.animate.set_value(going(raised, walked)),
                  c_tr.animate.set_value(len(crates(raised, walked))),
                  *[twins['B', i].animate.set_opacity(
                      LIT_TWIN if TEN_MB[i] >= RAISE_TRY else DIM_TWIN) for i in range(10)],
                  *[twins['S', j].animate.set_opacity(
                      LIT_TWIN if TEN_MC[j] <= RAISE_TRY else DIM_TWIN) for j in range(10)],
                  run_time=0.9)
        threads[S_ANDREW] = thread_tpl[S_ANDREW].copy()
        self.play(tag_tr[S_ANDREW].animate.set_value(tags[S_ANDREW]),
                  bodies['B', buyer_a].animate.move_to(MEET_AT[S_ANDREW]),
                  p_tr.animate.set_value(going(tags, served)),
                  *[twins['B', i].animate.set_opacity(
                      LIT_TWIN if TEN_MB[i] >= going(tags, served) else DIM_TWIN)
                    for i in range(10)],
                  *[twins['S', j].animate.set_opacity(
                      LIT_TWIN if TEN_MC[j] <= going(tags, served) else DIM_TWIN)
                    for j in range(10)],
                  run_time=0.9)
        self.play(FadeIn(threads[S_ANDREW]), FadeOut(crate_objs.pop(S_ANDREW)),
                  bars['B', buyer_a].animate.set_opacity(LIT_BAR),
                  bars['S', S_ANDREW].animate.set_opacity(LIT_BAR),
                  c_tr.animate.set_value(0), run_time=0.5)
        lowball = fixed(VGroup(Tex(r'\$').scale(SCALE_TICK),
                               DecimalNumber(LOWBALL_TRY, num_decimal_places=2).scale(SCALE_TICK),
                               Tex('?').scale(SCALE_TICK))
                        .arrange(RIGHT, buff=0.03).set_color(GUIDE))
        lowball.move_to(screen_point(self.camera.frame, MEET_AT[served[B_GARY]] + OUT * 1.05))
        self.play(FadeIn(lowball), run_time=0.5)
        refused = fixed(Line(lowball.get_left() + LEFT * 0.05, lowball.get_right() + RIGHT * 0.05,
                             color=CAPTION, stroke_width=2.5))
        self.play(Create(refused), run_time=0.6)
        self.play(FadeOut(lowball), FadeOut(refused), run_time=0.6)
        if not settled(TEN_MB, TEN_MC, tags, served):
            print('PostedPrice 4.a: not settled', tags, served, file=sys.stderr)
        self.pause('4.a')

        # ---- 4.b · The algebra | The world fades under the panel; the camera flattens;
        # the staircases dissolve into the smooth market curves; equations write out.
        for bar in bars.values():
            bar.clear_updaters()
        self.play(FadeOut(floor),
                  *[FadeOut(b) for b in bodies.values()],
                  *[FadeOut(b) for b in bars.values()],
                  *[FadeOut(t) for t in threads.values()],
                  *[FadeOut(tag_objs[s]) for s in tags if tags[s] is not None],
                  *[FadeOut(c) for c in crate_objs.values()],
                  FadeOut(crate_gauge), FadeOut(queue_gauge),
                  self.camera.frame.animate.reorient(0, 0),
                  run_time=1.6)
        ax = style_axes(
            [0, 55, 10], [0, 13, 2], x_length=7, y_length=6, ticks=True,
            x_axis_config={'numbers_to_include': [10, 20, 30, 40, 50],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [2, 4, 6, 8, 10, 12],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}}).scale(0.8)
        ax.shift(GRAPH_AT - (ax.c2p(0, 0) + ax.c2p(55, 13)) / 2)
        p_lab = Tex('P', color=INK).next_to(ax.c2p(0, 13), LEFT, buff=0.25)
        q_lab = Tex('Q', color=INK).next_to(ax.c2p(55, 0), DOWN, buff=0.35)
        p_units = Tex(narration('dollars per pound'), color=CAPTION).scale(0.7)
        p_units.next_to(p_lab, RIGHT, buff=0.35)
        q_units = Tex(narration('thousands of pounds'), color=CAPTION).scale(0.7)
        q_units.next_to(q_lab, RIGHT, buff=0.3)
        demand = Line(ax.c2p(0, 12), ax.c2p(50, 2), color=DEMAND, stroke_width=4)
        supply = Line(ax.c2p(0, 2), ax.c2p(50, 4.5), color=SUPPLY, stroke_width=4)
        d_end = Tex('D').set_color(INK).next_to(ax.c2p(50, 2), RIGHT, buff=0.15)
        s_end = Tex('S').set_color(INK).next_to(ax.c2p(50, 4.5), RIGHT, buff=0.15)
        graph = fixed(VGroup(ax, p_lab, q_lab, p_units, q_units, demand, supply, d_end, s_end))
        self.play(FadeOut(ten_panel), *[FadeOut(t) for t in twins.values()],
                  FadeOut(ghost_d), FadeOut(ghost_s), FadeOut(d_lab), FadeOut(s_lab),
                  FadeOut(price_line), FadeOut(p_read), FadeOut(qd_drop), FadeOut(qs_drop),
                  FadeOut(qd_read), FadeOut(qs_read), FadeOut(gap),
                  FadeIn(graph), run_time=1.4)
        eq_s = fixed(Tex(r'$P = 2 + \frac{Q}{20}$').scale(0.8).move_to(ax.c2p(40, 6.6)))
        eq_d = fixed(Tex(r'$P = 12 - \frac{Q}{5}$').scale(0.8).move_to(ax.c2p(20, 9.8)))
        self.play(FadeIn(eq_s))
        self.play(FadeIn(eq_d))
        self.pause('4.b')

        # ---- 4.c · Solving | Supply equals demand; solve for Q*, substitute for P*.
        divider_x = q_units.get_right()[0] + 0.35
        MATH_AT = np.array([(divider_x + FRAME_W / 2 - 0.6) / 2, 0.55, 0])
        math_divider = fixed(Line([divider_x, -3, 0], [divider_x, 3, 0],
                                  color=MUTED, stroke_width=1).set_opacity(0.5))
        work = VGroup(
            Tex(r'$2 + \frac{Q}{20} = 12 - \frac{Q}{5}$'),
            Tex(r'$\frac{Q}{20} + \frac{Q}{5} = 10$'),
            Tex(r'$\frac{Q}{4} = 10$'),
            Tex(r'$Q^* = 40$', color=GUIDE),
            Tex(r'$P^* = 2 + \frac{40}{20}$'),
            Tex(r'$P^* = \$4$', color=GUIDE)).scale(0.8)
        work.arrange(DOWN, buff=0.32, aligned_edge=LEFT).move_to(MATH_AT)
        work = fixed(work)
        self.play(FadeIn(math_divider), FadeIn(work[0]))
        self.play(FadeIn(work[1]))
        self.play(FadeIn(work[2]))
        self.play(FadeIn(work[3]))
        self.play(FadeIn(work[4]))
        self.play(FadeIn(work[5]))
        self.pause('4.c')

        # ---- 4.d · One graph | The pair carries back to the axes with a star.
        marker = fixed(equilibrium_marker(ax, 40, 4))
        p_star = fixed(Tex(r'$P^* = \$4$', color=GUIDE).scale(0.7)
                       .next_to(ax.c2p(0, 4), LEFT, buff=0.6))
        q_star = fixed(Tex(r'$Q^* = 40$', color=GUIDE).scale(0.7)
                       .next_to(ax.c2p(40, 0), DOWN, buff=0.6))
        ax.x_axis.numbers[3].set_opacity(0)
        ax.y_axis.numbers[1].set_opacity(0)
        self.play(FadeIn(marker))
        self.play(TransformFromCopy(work[3], q_star), TransformFromCopy(work[5], p_star))
        self.bring_to_front(marker[0])
        self.pause('4.d')

        # ---- 5.a · Stable | Push the price off the star; it returns both times.
        self.play(FadeOut(work), FadeOut(math_divider))
        p2 = ValueTracker(4)
        push_line = fixed(DashedLine(ax.c2p(0, 4), ax.c2p(50, 4), color=GUIDE).set_opacity(0.6))
        push_line.add_updater(lambda m: m.move_to(
            (ax.c2p(0, p2.get_value()) + ax.c2p(50, p2.get_value())) / 2))
        dot_d = fixed(Dot(ax.c2p(40, 4), color=DEMAND, radius=0.08))
        dot_d.add_updater(lambda m: m.move_to(ax.c2p(5 * (12 - p2.get_value()), p2.get_value())))
        dot_s = fixed(Dot(ax.c2p(40, 4), color=SUPPLY, radius=0.08))
        dot_s.add_updater(lambda m: m.move_to(ax.c2p(20 * (p2.get_value() - 2), p2.get_value())))
        push_gap = fixed(Line(ax.c2p(40, 0), ax.c2p(40.001, 0), color=TRADE, stroke_width=6))

        def push_gap_follow(m):
            qd, qs = 5 * (12 - p2.get_value()), 20 * (p2.get_value() - 2)
            lo, hi = sorted([qd, qs])
            m.put_start_and_end_on(ax.c2p(lo, 0), ax.c2p(hi + (1e-3 if hi == lo else 0), 0))
            m.set_opacity(0 if abs(hi - lo) < 0.5 else 0.9)
        push_gap.add_updater(push_gap_follow)
        excess_word = fixed(Tex('excess').scale(SCALE_TICK).set_color(CAPTION))
        excess_word.add_updater(lambda m: m.next_to(push_gap, UP, buff=0.1).set_opacity(
            1 if p2.get_value() > 4.05 else 0))
        shortage_word = fixed(Tex('shortage').scale(SCALE_TICK).set_color(CAPTION))
        shortage_word.add_updater(lambda m: m.next_to(push_gap, UP, buff=0.1).set_opacity(
            1 if p2.get_value() < 3.95 else 0))
        for m in [push_line, dot_d, dot_s, push_gap, excess_word, shortage_word]:
            m.update()
        self.play(FadeIn(push_line), FadeIn(dot_d), FadeIn(dot_s))
        self.add(push_gap, excess_word, shortage_word)
        self.play(p2.animate.set_value(4.5), run_time=1.2)
        self.play(p2.animate.set_value(4), run_time=1.4)
        self.play(p2.animate.set_value(3.5), run_time=1.2)
        self.play(p2.animate.set_value(4), run_time=1.4)
        self.bring_to_front(marker[0])
        self.pause('5.a')

        # ---- 5.b · Tieback | The market graph to a corner; the two-farmer PPF returns;
        # the prices form the exchange-rate line.
        for m in [push_line, dot_d, dot_s, push_gap, excess_word, shortage_word]:
            m.clear_updaters()
        self.remove(head)
        head = fixed(title('Where on the PPF?'))
        market = fixed(VGroup(graph, marker, p_star, q_star))
        self.play(FadeIn(head), FadeOut(push_line), FadeOut(dot_d), FadeOut(dot_s),
                  FadeOut(push_gap), FadeOut(excess_word), FadeOut(shortage_word),
                  FadeOut(eq_s), FadeOut(eq_d))
        self.play(market.animate.scale(0.5).move_to([5.0, 1.3, 0]), run_time=1.6)
        axc = style_axes(
            x_range=[0, 12, 1], y_range=[0, 44, 4], x_length=6.2, y_length=5.2, ticks=True,
            x_axis_config={'numbers_to_include': [8, 10],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
            y_axis_config={'numbers_to_include': [16, 40],
                           'decimal_number_config': {'num_decimal_places': 0, 'color': MUTED}},
        ).scale(0.9).move_to(LEFT * 2.5 + DOWN * 0.5)
        cap_c = Tex('Carrots').scale(SCALE_CAPTION).set_color(CARROTS).next_to(axc.c2p(12, 0), RIGHT, buff=0.25)
        cap_s = Tex('Spinach').scale(SCALE_CAPTION).set_color(SPINACH).next_to(axc.c2p(0, 44), UP, buff=0.15)
        ppf_m = axc.plot(PPF_Molly, color=MOLLY, x_range=(0, 10))
        ppf_a = axc.plot(PPF_Andrew, color=ANDREW, x_range=(0, 8))
        lab_m = Tex('Molly').scale(SCALE_CAPTION).next_to(axc.c2p(0, 40), LEFT, buff=0.9)
        lab_a = Tex('Andrew').scale(SCALE_CAPTION).next_to(axc.c2p(0, 16), LEFT, buff=0.9)
        glow_m = Dot(axc.c2p(0, 40), radius=0.14, color=MOLLY).set_opacity(0.5)
        glow_a = Dot(axc.c2p(8, 0), radius=0.14, color=ANDREW).set_opacity(0.5)
        ppf_stage = fixed(VGroup(axc, cap_c, cap_s, ppf_m, ppf_a, lab_m, lab_a, glow_m, glow_a))
        self.play(FadeIn(ppf_stage))
        # ANIMATOR-Q: the notes name no carrot price, only "the two equilibrium
        # prices form the exchange-rate line". Drawn at A3's worked rate,
        # 1 C = 3 S, through each farmer's specialization point; a carrot
        # price (and whether one line or two) is Taylor's call.
        rate_m = DashedLine(axc.c2p(0, 40), axc.c2p(12, 40 - RATE_S_PER_C * 12),
                            color=TRADE, stroke_width=3)
        rate_a = DashedLine(axc.c2p(8, 0), axc.c2p(0, RATE_S_PER_C * 8),
                            color=TRADE, stroke_width=3)
        rate_lab = Tex('{{1}} {{C}} $=$ {{3}} {{S}}').scale(0.9).set_color_by_tex_to_color_map({
            'C': CARROTS, 'S': SPINACH}).next_to(axc.c2p(6, 22), UR, buff=0.2)
        fixed(VGroup(rate_m, rate_a, rate_lab))
        self.play(FadeIn(rate_m), FadeIn(rate_a))
        self.play(FadeIn(rate_lab))
        self.pause('5.b')
