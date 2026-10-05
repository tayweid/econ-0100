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
# 1.b gains; 2.a trading; 2.b reporting; 3.a debrief.

from manim import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../_Assets'))
from style import *


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
