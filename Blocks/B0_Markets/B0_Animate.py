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
# Storyboard: 0.a simulation card (B0 demand convention); 1.a roles;
# 1.b gains; 2.a trading; 2.b reporting; 3.a debrief;
# 4.a Round 3 price distribution; 4.b average.
# Pending: full card deck (including non-traders) for the model prediction.

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



class PitMarket(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        self.camera.frame.set(width=FRAME_W).move_to(ORIGIN)
        BODY_MID = -0.1
        COLUMN_X = 3.65

        # ---- 0.a · Use the same exercise card as B0's demand simulation.
        exercise_card(self, 'Simulation B $|$ Pit Market',
                      ['What prices emerge when buyers and sellers negotiate?'])
        self.wait(1 / 2)
        self.pause('0.a')
        FadeAll(self)

        # ---- 1.a · Your card assigns your role and your private limit.
        head = title('Pit Market $|$ Your Role')
        buyer = Tex('Buyers: black cards', color=DEMAND).scale(1.1)
        buyer_rules = VGroup(
            Tex('Your number is your value for one unit.'),
            Tex('Buy at or below that number.'),
        ).arrange(DOWN, buff=0.35).scale(0.85)
        buyer_rules.next_to(buyer, DOWN, buff=0.55)
        buyer_group = VGroup(buyer, buyer_rules).move_to(
            LEFT * COLUMN_X + UP * BODY_MID)

        seller = Tex('Sellers: red cards', color=SUPPLY).scale(1.1)
        seller_rules = VGroup(
            Tex('Your number is your cost for one unit.'),
            Tex('Sell at or above that number.'),
        ).arrange(DOWN, buff=0.35).scale(0.85)
        seller_rules.next_to(seller, DOWN, buff=0.55)
        seller_group = VGroup(seller, seller_rules).move_to(
            RIGHT * COLUMN_X + UP * BODY_MID)

        reminder = Tex('Keep your card number private.', color=DEFINITION)
        reminder.to_edge(DOWN, buff=0.55)
        self.play(FadeIn(head), FadeIn(buyer_group), FadeIn(seller_group),
                  FadeIn(reminder))
        self.pause('1.a')

        # ---- 1.b · Gain is the difference between the card and the price.
        buyer_gain = Tex(r'Your gain $=$ value $-$ price', color=DEMAND).scale(0.85)
        buyer_gain.next_to(buyer_rules, DOWN, buff=0.65)
        seller_gain = Tex(r'Your gain $=$ price $-$ cost', color=SUPPLY).scale(0.85)
        seller_gain.next_to(seller_rules, DOWN, buff=0.65)
        self.play(FadeIn(buyer_gain), FadeIn(seller_gain))
        self.pause('1.b')

        # ---- 2.a · Negotiate; leave this screen up while explaining the market.
        self.play(FadeOut(buyer_group), FadeOut(seller_group),
                  FadeOut(buyer_gain), FadeOut(seller_gain), FadeOut(reminder),
                  Transform(head, title('Pit Market $|$ How to Trade')))
        rules = VGroup(
            Tex('Find someone on the other side of the market.'),
            Tex('Negotiate a price that works for both of you.'),
            Tex('Shop around: you do not have to accept an offer.'),
            Tex('Each card can be used for one trade only.'),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        rules.move_to(UP * BODY_MID)
        self.play(FadeIn(rules))
        self.pause('2.a')

        # ---- 2.b · This complete reminder stays up during the trading round.
        self.play(FadeOut(rules),
                  Transform(head, title('Pit Market $|$ When You Agree')))
        reporting = VGroup(
            Tex('Come together to report your agreed price.'),
            Tex('Hand in both cards face down; the price goes on the board.'),
            Tex('Wait for the next round after your trade.'),
        ).arrange(DOWN, buff=0.5, aligned_edge=LEFT)
        reporting.move_to(UP * BODY_MID)
        limits = VGroup(
            Tex(r'Buyers: price $\leq$ card value', color=DEMAND),
            Tex(r'Sellers: price $\geq$ card cost', color=SUPPLY),
        ).arrange(RIGHT, buff=1.2).scale(0.8).to_edge(DOWN, buff=0.55)
        self.play(FadeIn(reporting), FadeIn(limits))
        self.pause('2.b')

        # ---- 3.a · Advance here after trading; return to 2.b for round two.
        self.play(FadeOut(reporting), FadeOut(limits),
                  Transform(head, title('Pit Market $|$ What Happened?')))
        questions = VGroup(
            Tex('Where did transaction prices cluster?'),
            Tex('What price and quantity do the cards predict?'),
            Tex('How does the second round compare with the first?'),
        ).arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        questions.move_to(UP * BODY_MID)
        self.play(FadeIn(questions))
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
