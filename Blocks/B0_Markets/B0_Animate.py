# maniml B0_Animate.py PitMarket
# /// script
# dependencies = ["seaborn==0.13.2"]
# ///
# Pit market instructions for the live class simulation after Checkpoint B.
# New scene reconstructed from B3_Equilibrium/B3_Notes.typ, "Pit Market",
# and https://en.wikiversity.org/wiki/Economic_Classroom_Experiments/Pit_Market
# (the earlier instruction animation could not be located).
# Run: maniml B0_Animate.py PitMarket
# One numbered card = one unit; use the instructor's prepared card decks.
# Storyboard: 0.a complete simulation setup on one screen; 3.a debrief;
# 4.a Round 3 price distribution; 4.b average; 5.a full-deck card curves;
# 5.b predicted price ($6), compared with the historical average.

from manim import *
from decimal import Decimal, ROUND_HALF_UP
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *
from style import axes as style_axes


# Snapshot: Equilibrium_Simulation_preF24.xlsx, Sheet1!H3:H23 (Round 3).
# x4 / H6 is blank and is omitted, not counted as a zero price.
# These are participant reports, not 20 distinct transactions; retain each
# source observation rather than guessing a deduplication from repeated prices.
ROUND3_PRICES = (
    5, 5, 5, 4.15, 6, 5.25, 6, 5, 6, 5.25,
    6, 5, 5, 4.15, 4.1, 6.25, 5, 5, 6.25, 4.1,
)


# Full deck supplied by Taylor on 2026-10-05, independently of the old
# workbook: three of each black card 5–10; three of each red card 2–7.
BUYER_VALUES = tuple(value for value in range(10, 4, -1) for _ in range(3))
SELLER_COSTS = tuple(cost for cost in range(2, 8) for _ in range(3))


class PitMarket(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        self.camera.frame.set(width=FRAME_W).move_to(ORIGIN)
        BODY_MID = -0.1

        # ---- 0.a · One complete setup screen stays up during trading.
        head = title('Simulation B $|$ The Market')
        question = subtitle(head, 'What prices emerge when buyers and sellers negotiate?')

        buyer = Tex('Black cards: buyers', color=DEMAND).scale(1.0)
        buyer.move_to([-7.4, 1.7, 0], aligned_edge=LEFT)
        buyer_rules = VGroup(
            Tex(r'Face value $=$ MB'),
            Tex(r'CS $=$ MB $-$ price'),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).scale(0.85)
        buyer_rules.next_to(buyer, DOWN, buff=0.3).align_to(buyer, LEFT)

        seller = Tex('Red cards: sellers', color=SUPPLY).scale(1.0)
        seller.move_to([0.4, 1.7, 0], aligned_edge=LEFT)
        seller_rules = VGroup(
            Tex(r'Face value $=$ MC'),
            Tex(r'PS $=$ price $-$ MC'),
        ).arrange(DOWN, buff=0.22, aligned_edge=LEFT).scale(0.85)
        seller_rules.next_to(seller, DOWN, buff=0.3).align_to(seller, LEFT)

        rules = VGroup(
            Tex('1. Find a trading partner. Negotiate; no losses.'),
            Tex('2. One trade per card. You may turn down any offer.'),
            Tex('3. Report your price together. Turn in both cards face down.'),
            Tex('4. Wait for the next round.'),
        ).arrange(DOWN, buff=0.32, aligned_edge=LEFT).scale(0.85)
        rules.move_to([-7.4, -1.1, 0], aligned_edge=UL)
        reminder = Tex('Keep your card number private.', color=DEFINITION).scale(0.9)
        reminder.move_to([-7.4, -0.4, 0], aligned_edge=LEFT)
        self.play(FadeIn(head), FadeIn(question), FadeIn(buyer), FadeIn(buyer_rules),
                  FadeIn(seller), FadeIn(seller_rules), FadeIn(rules), FadeIn(reminder))
        self.pause('0.a')

        # ---- 3.a · Advance after trading; return to 0.a for another round.
        FadeAll(self)
        head = title('Pit Market $|$ What Happened?')
        questions = VGroup(
            Tex('Where did transaction prices cluster?'),
            Tex('What price and quantity do the cards predict?'),
            Tex('How does the second round compare with the first?'),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        questions.move_to(UP * BODY_MID)
        self.play(FadeIn(head), FadeIn(questions))
        self.pause('3.a')

        # ---- 4.a · Prior-class observations, with price vertical so the
        # model can later use the same price scale. Horizontal spacing only
        # separates dots; it does not imply transaction order or quantity.
        FadeAll(self)
        head = title('Pit Market $|$ Earlier Results')
        data_head = Tex('Earlier class: Round 3', color=INK).scale(0.85)
        data_head.move_to([-4.2, 2.8, 0])
        data_ax = style_axes([0, 4.5, 1], [0, 10, 2],
                             x_length=4.5, y_length=4.8, ticks=True)
        data_ax.shift([-6.5, -2.45, 0] - data_ax.c2p(0, 0))
        data_ax.x_axis.set_opacity(0)
        data_ticks = VGroup(*[
            Tex(str(p), color=CAPTION).scale(0.7)
            .next_to(data_ax.c2p(0, p), LEFT, buff=0.15)
            for p in range(0, 11, 2)
        ])
        data_units = Tex(r'Price (\$)', color=CAPTION).scale(0.7)
        data_units.rotate(PI / 2).move_to([-7.4, -0.05, 0])
        data_note = Tex('One dot per participant report', color=CAPTION).scale(0.7)
        data_note.move_to([-4.2, -2.95, 0])

        price_dots, lanes = VGroup(), []
        for price in sorted(ROUND3_PRICES):
            lane = 0
            while lane < len(lanes) and abs(price - lanes[lane]) * 0.48 < 0.2:
                lane += 1
            if lane == len(lanes):
                lanes.append(price)
            else:
                lanes[lane] = price
            price_dots.add(Dot(data_ax.c2p(0.45 + 0.4 * lane, price),
                               radius=0.07, color=INK, z_index=5))
        self.play(FadeIn(head), FadeIn(data_head), FadeIn(data_ax),
                  FadeIn(data_ticks), FadeIn(data_units), FadeIn(data_note))
        self.play(LaggedStart(*[FadeIn(dot) for dot in price_dots],
                              lag_ratio=0.08), run_time=1.5)
        self.pause('4.a')

        # ---- 4.b · The observed mean, independently calculated from prices.
        average = sum(Decimal(str(p)) for p in ROUND3_PRICES) / len(ROUND3_PRICES)
        average_text = average.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
        mean_line = DashedLine(data_ax.c2p(0, float(average)),
                               data_ax.c2p(4.35, float(average)),
                               color=DEFINITION, stroke_width=2, z_index=3)
        mean_label = Tex(rf'Average: \${average_text}', color=DEFINITION).scale(0.9)
        mean_label.move_to([-4.2, -3.55, 0])
        self.play(Create(mean_line), FadeIn(mean_label))
        self.pause('4.b')

        # ---- 5.a · Build the model from sorted card values. Retain the
        # observed distribution and mean, but withhold the equilibrium marker.
        model_head = Tex('The card model', color=INK).scale(0.85)
        model_head.move_to([3.45, 2.8, 0])
        model_ax = style_axes([0, 21, 3], [0, 10, 2],
                              x_length=7.2, y_length=4.8, ticks=True)
        model_ax.shift([-0.4, -2.45, 0] - model_ax.c2p(0, 0))
        model_ticks = VGroup(*[
            Tex(str(p), color=CAPTION).scale(0.7)
            .next_to(model_ax.c2p(0, p), LEFT, buff=0.15)
            for p in range(0, 11, 2)
        ], *[
            Tex(str(q), color=CAPTION).scale(0.7)
            .next_to(model_ax.c2p(q, 0), DOWN, buff=0.15)
            for q in (0, 3, 6, 9, 12, 15, 18, 21)
        ])
        model_units = Tex(r'Price (\$)', color=CAPTION).scale(0.7)
        model_units.rotate(PI / 2).move_to([-1.3, -0.05, 0])
        quantity_label = Tex('Quantity', color=CAPTION).scale(0.7)
        quantity_label.next_to(model_ax.c2p(21, 0), DOWN, buff=0.55)
        model_note = Tex('18 buyers, 18 sellers; 3 of each card', color=CAPTION).scale(0.7)
        model_note.move_to([3.05, -3.1, 0])

        demand_points, supply_points = [], []
        for q, value in enumerate(BUYER_VALUES):
            demand_points.extend([model_ax.c2p(q, value), model_ax.c2p(q + 1, value)])
        for q, cost in enumerate(SELLER_COSTS):
            supply_points.extend([model_ax.c2p(q, cost), model_ax.c2p(q + 1, cost)])
        demand = polyline(demand_points, color=DEMAND, width=4)
        supply = polyline(supply_points, color=SUPPLY, width=4)
        demand_label = Tex('Demand', color=DEMAND).scale(0.8)
        demand_label.next_to(model_ax.c2p(6, 9), UP, buff=0.2)
        supply_label = Tex('Supply', color=SUPPLY).scale(0.8)
        supply_label.next_to(model_ax.c2p(18, 7), UP, buff=0.3)
        self.play(FadeIn(model_head), FadeIn(model_ax), FadeIn(model_ticks),
                  FadeIn(model_units), FadeIn(quantity_label), FadeIn(model_note))
        self.play(Create(demand), FadeIn(demand_label), run_time=1.2)
        self.play(Create(supply), FadeIn(supply_label), run_time=1.2)
        self.pause('5.a')

        # ---- 5.b · Punchline: P=6. Twelve trades have strictly positive
        # gains, and three more have MB=MC=6. Hence Q can be 12–15, with
        # the same total surplus; do not pretend the model pins down one Q.
        positive_trades = sum(v > c for v, c in zip(BUYER_VALUES, SELLER_COSTS))
        possible_trades = sum(v >= c for v, c in zip(BUYER_VALUES, SELLER_COSTS))
        price_low = max(SELLER_COSTS[possible_trades - 1],
                        BUYER_VALUES[possible_trades])
        price_high = min(BUYER_VALUES[possible_trades - 1],
                         SELLER_COSTS[possible_trades])
        assert price_low == price_high
        predicted_price = price_low
        equilibrium = Line(model_ax.c2p(positive_trades, predicted_price),
                           model_ax.c2p(possible_trades, predicted_price),
                           color=GUIDE, stroke_width=7)
        guides = VGroup(
            DashedLine(model_ax.c2p(0, predicted_price),
                       model_ax.c2p(positive_trades, predicted_price),
                       color=GUIDE, stroke_width=2),
            *[DashedLine(model_ax.c2p(q, 0), model_ax.c2p(q, predicted_price),
                         color=GUIDE, stroke_width=2)
              for q in (positive_trades, possible_trades)],
        )
        prediction = Tex(rf'Predicted: \${predicted_price}', color=DEFINITION).scale(0.9)
        prediction.move_to([3.45, -3.55, 0])
        model_result = Tex(f'{positive_trades}--{possible_trades} trades at this price',
                           color=CAPTION).scale(0.7).move_to(model_note)
        data_prediction = DashedLine(data_ax.c2p(0, predicted_price),
                                     data_ax.c2p(4.35, predicted_price),
                                     color=GUIDE, stroke_width=2, z_index=3)
        self.play(Create(guides), Create(equilibrium), FadeIn(prediction),
                  Transform(model_note, model_result))
        self.play(Create(data_prediction))
        self.pause('5.b')
