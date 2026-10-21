# maniml D2_Animation.py EpisodeD2
# Common resources only. NPR/public goods now live in D3_Notes.md.
# Choreography and narration: D2_Notes.md. All scene code is flat and editable.
# /// script
# requires-python = ">=3.11"
# dependencies = ["seaborn==0.13.2"]
# ///

from manim import *
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '../../_Assets'))
from style import *

config.frame_rate = 15


class EpisodeD2(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.5, -2.8
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        TEACHING_SCALE, TEACHING_BOTTOM = 0.7443, 0.05
        K = 20.0                    # Thousands of fish; stock before harvest.
        LOW, HIGH = 0.25, 0.5       # Simultaneous shares of that same stock.
        MONTHS = 3                  # Commitment horizon; no terminal-stock payoff.
        TOKEN_WIDTH, TOKEN_HEIGHT = 0.42, 0.18
        POND_CENTER = np.array([-4.0, 0.55, 0.0])
        POND_POSITIONS = [np.array([-5.5 + (i % 5) * 0.75,
                                   1.25 - (i // 5) * 0.47, 0.0]) for i in range(20)]
        FIRM_COLORS = (ROW_PLAYER, COL_PLAYER)
        CELL_SIDE = 1.5
        DIAMOND_ANGLE = -PI / 4
        GAME_CENTER = DOWN * 0.5
        TABLE_RIGHT = (RIGHT + DOWN) / 2**0.5
        TABLE_UP = (RIGHT + UP) / 2**0.5

        # ---- 1.a · D1's taxonomy, with the common-resource cell selected.
        head = title('Common Resources')
        taxonomy = Table(
            [[r'Private\\Goods', r'Club\\Goods'],
             [r'Common\\Resources', r'Public\\Goods']],
            row_labels=[Tex('Excludable', color=GUIDE), Tex('Non-Excludable', color=GUIDE)],
            col_labels=[Tex('Rival', color=GUIDE), Tex('Non-Rival', color=GUIDE)],
            element_to_mobject=Tex,
            line_config={'color': MUTED, 'stroke_width': 2},
        ).scale(0.7).move_to([0.4, BODY_MID, 0])
        selected = taxonomy.get_entries_without_labels((2, 1))
        box = SurroundingRectangle(selected, buff=0.22, color=NASH)
        teaching = Tex('What changes when we cannot exclude other users?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(taxonomy), FadeIn(teaching))
        self.play(Create(box))
        self.pause('1.a')

        # ---- 1.b · A caught fish leaves the shared stock.
        self.play(FadeOut(taxonomy), FadeOut(box))
        self.remove(teaching)
        pond = Ellipse(width=5.4, height=2.65, color=INK, stroke_width=2).move_to(POND_CENTER)
        capacity = Tex(r'Carrying capacity: $K = 20$', color=CAPTION).scale(0.7).move_to([-4, 2.25, 0])
        units = Tex(r'\textsf{Thousands of fish}', color=CAPTION).scale(0.6).move_to([-4, 1.95, 0])
        stock_label = Tex(r'Stock: $20$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
        trays = VGroup(*[Rectangle(width=2.4, height=0.65, color=MUTED, stroke_width=1.5)
                        .move_to([x, -2.25, 0]) for x in (-5.5, -2.5)])
        firm_names = VGroup(*[Tex(f'Firm {i+1}', color=FIRM_COLORS[i]).scale(0.8)
                             .move_to([x, -1.65, 0]) for i, x in enumerate((-5.5, -2.5))])
        fish = VGroup(*[Rectangle(width=TOKEN_WIDTH, height=TOKEN_HEIGHT, stroke_width=0,
                                  fill_color=INK, fill_opacity=1).move_to(pos) for pos in POND_POSITIONS])
        teaching = Tex('A fish I catch is no longer available for you to catch.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(pond), FadeIn(trays), FadeIn(firm_names), FadeIn(fish), FadeIn(teaching))
        self.play(fish[-1].animate.move_to([-5.5, -2.25, 0]).set_color(ROW_PLAYER))
        self.pause('1.b')
        self.play(fish[-1].animate.move_to(POND_POSITIONS[-1]).set_color(INK))

        # ---- 1.c · Fixed pond boundary, stock and capacity are different quantities.
        self.remove(teaching)
        teaching = Tex('Carrying capacity is a stock, not a monthly catch.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(capacity), FadeIn(units), FadeIn(stock_label), FadeIn(teaching))
        self.pause('1.c')

        # ---- 2.a · Take ten; pause before revealing the survivor calculation.
        self.remove(head, teaching)
        head = title('Population And Harvest')
        divider = Line([0, -2.85, 0], [0, 2.5, 0], color=MUTED, stroke_width=1)
        month_label = Tex('Month 1', color=CAPTION).scale(0.8).move_to([4, 2.15, 0])
        phase = Tex(r'\textsf{Harvest}', color=CAPTION).scale(0.7).move_to([4, 1.55, 0])
        equation = MathTex('20 - 10 = ?', color=INK).move_to([4, 0.5, 0])
        start_catch = Tex(r'Start: $20$\qquad Catch: $10$', color=CAPTION).scale(0.8).move_to([4, -0.35, 0])
        teaching = Tex('How many fish remain to reproduce?', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(divider), FadeIn(month_label), FadeIn(phase), FadeIn(teaching))
        catches = [VGroup(*fish[0:5]), VGroup(*fish[5:10])]
        survivors = VGroup(*fish[10:])
        self.remove(stock_label)
        self.play(*[token.animate.move_to([-6.42 + i * 0.46 + firm * 3, -2.25, 0]).set_color(FIRM_COLORS[firm])
                    for firm, group in enumerate(catches) for i, token in enumerate(group)], run_time=1.2)
        catch_values = VGroup(*[Tex('$5$', color=color).scale(0.75).move_to([x, -2.85, 0])
                               for color, x in zip(FIRM_COLORS, (-5.5, -2.5))])
        self.play(FadeIn(start_catch), FadeIn(equation), FadeIn(catch_values))
        self.pause('2.a')

        # ---- 2.b · Only the ten surviving tokens reproduce.
        self.remove(equation, teaching, phase)
        equation = MathTex('20 - 10 = 10', color=INK).move_to([4, 0.5, 0])
        phase = Tex(r'\textsf{Reproduction}', color=CAPTION).scale(0.7).move_to([4, 1.55, 0])
        stock_label = Tex(r'Survivors: $10$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
        self.play(FadeIn(equation), FadeIn(phase), FadeIn(stock_label))
        babies = VGroup(*[token.copy() for token in survivors])
        self.add(babies)
        self.play(*[token.animate.move_to(POND_POSITIONS[i]) for i, token in enumerate(survivors)],
                  *[token.animate.move_to(POND_POSITIONS[i+10]) for i, token in enumerate(babies)], run_time=1.2)
        fish = VGroup(*survivors, *babies)
        self.remove(stock_label, month_label, start_catch)
        stock_label = Tex(r'Stock: $20$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
        month_label = Tex('Month 2', color=CAPTION).scale(0.8).move_to([4, 2.15, 0])
        growth = MathTex(r'2\times10=20', color=INK).move_to([4, -0.45, 0])
        teaching = Tex('Ten thousand fish caught; twenty thousand next month.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(stock_label), FadeIn(month_label), FadeIn(growth), FadeIn(teaching))
        self.pause('2.b')

        # ---- 2.c / 2.d · Reset examples; no fish ever exceed the capacity.
        for per_firm in (6, 2):
            self.remove(fish, *catches, catch_values, stock_label, month_label, phase, equation, growth, teaching)
            fish = VGroup(*[Rectangle(width=TOKEN_WIDTH, height=TOKEN_HEIGHT, stroke_width=0,
                                      fill_color=INK, fill_opacity=1).move_to(pos) for pos in POND_POSITIONS])
            stock_label = Tex(r'Stock: $20$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
            month_label = Tex('Month 1', color=CAPTION).scale(0.8).move_to([4, 2.15, 0])
            phase = Tex(r'\textsf{Harvest}', color=CAPTION).scale(0.7).move_to([4, 1.55, 0])
            self.play(FadeIn(fish), FadeIn(stock_label), FadeIn(month_label), FadeIn(phase))
            catches = [VGroup(*fish[:per_firm]), VGroup(*fish[per_firm:2*per_firm])]
            survivors = VGroup(*fish[2*per_firm:])
            self.play(*[token.animate.move_to([-6.42+(i%5)*0.46+firm*3, -2.12-(i//5)*0.26, 0])
                        .set_color(FIRM_COLORS[firm])
                        for firm, group in enumerate(catches) for i, token in enumerate(group)], run_time=1)
            remaining = K - 2*per_firm
            next_stock = min(K, 2*remaining)
            equation = MathTex(f'20 - {2*per_firm} = {remaining:g}', color=INK).move_to([4, 0.5, 0])
            catch_values = VGroup(*[Tex(f'${per_firm}$', color=color).scale(0.75).move_to([x, -2.85, 0])
                                   for color, x in zip(FIRM_COLORS, (-5.5, -2.5))])
            self.remove(stock_label)
            stock_label = Tex(f'Survivors: ${remaining:g}$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
            self.play(FadeIn(equation), FadeIn(catch_values), FadeIn(stock_label))
            if per_firm == 6:
                self.pause('2.c.survivors')
            else:
                self.pause('2.d.survivors')
            babies = VGroup(*[survivors[i % len(survivors)].copy() for i in range(int(next_stock-remaining))])
            self.add(babies)
            self.remove(phase)
            phase = Tex(r'\textsf{Reproduction}', color=CAPTION).scale(0.7).move_to([4, 1.55, 0])
            self.play(FadeIn(phase),
                      *[token.animate.move_to(POND_POSITIONS[i]) for i, token in enumerate(survivors)],
                      *[token.animate.move_to(POND_POSITIONS[int(remaining)+i]) for i, token in enumerate(babies)], run_time=1.2)
            fish = VGroup(*survivors, *babies)
            self.remove(stock_label, month_label)
            stock_label = Tex(f'Stock: ${next_stock:g}$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
            month_label = Tex('Month 2', color=CAPTION).scale(0.8).move_to([4, 2.15, 0])
            growth = MathTex(r'\min\{20,\;2\times'+f'{remaining:g}'+r'\}='+f'{next_stock:g}', color=INK).scale(0.9).move_to([4, -0.45, 0])
            line = ('The same pond now starts next month with fewer fish.' if per_firm == 6
                    else 'Reproduction is limited by carrying capacity.')
            teaching = Tex(line, color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
            self.play(FadeIn(stock_label), FadeIn(month_label), FadeIn(growth), FadeIn(teaching))
            if per_firm == 6:
                self.pause('2.c')
            else:
                cap_box = SurroundingRectangle(capacity, buff=0.12, color=FOCUS)
                self.play(Create(cap_box))
                self.pause('2.d')
                self.play(FadeOut(cap_box))

        # ---- 2.e · General equations arrive only after the concrete examples.
        self.remove(equation, growth, month_label, phase, teaching)
        clock_rule = Tex(r'\textsf{Harvest $\to$ Reproduction $\to$ Next month}', color=CAPTION).scale(0.6).move_to([4, 2.15, 0])
        survivor_rule = MathTex('S_t=N_t-h_{1t}-h_{2t}', color=INK).scale(0.9).move_to([4, 0.75, 0])
        growth_rule = MathTex(r'N_{t+1}=\min\{20,\;2S_t\}', color=INK).scale(0.9).move_to([4, -0.4, 0])
        feasible = MathTex(r'0\leq h_{1t}+h_{2t}\leq N_t', color=CAPTION).scale(0.75).move_to([4, -1.55, 0])
        self.play(Indicate(stock_label, color=FOCUS), FadeIn(clock_rule), FadeIn(survivor_rule))
        self.pause('2.e.survivors')
        teaching = Tex("Next month's stock depends on what survives this month's catch.", color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(Indicate(capacity, color=FOCUS), FadeIn(growth_rule), FadeIn(feasible), FadeIn(teaching))
        self.pause('2.e')

        # ---- 2.f · With no further harvest, a positive stock recovers; zero cannot.
        self.remove(fish, *catches, catch_values, stock_label, survivor_rule, growth_rule, feasible, teaching)
        fish = VGroup(*[Rectangle(width=TOKEN_WIDTH, height=TOKEN_HEIGHT, stroke_width=0,
                                  fill_color=INK, fill_opacity=1).move_to(pos) for pos in POND_POSITIONS[:8]])
        recovery = MathTex(r'8\ \longrightarrow\ 16\ \longrightarrow\ 20', color=INK).scale(0.9).move_to([4, 0.6, 0])
        no_catch = Tex('No further harvest', color=CAPTION).scale(0.8).move_to([4, 1.4, 0])
        self.play(FadeIn(fish), FadeIn(no_catch))
        for stock in (8, 16, 20):
            self.remove(stock_label)
            stock_label = Tex(f'Stock: ${stock}$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
            if stock > len(fish):
                babies = VGroup(*[fish[i % len(fish)].copy() for i in range(stock-len(fish))])
                self.add(babies)
                self.play(*[token.animate.move_to(POND_POSITIONS[len(fish)+i]) for i, token in enumerate(babies)], run_time=0.8)
                fish.add(*babies)
            self.play(FadeIn(stock_label), run_time=0.3)
        self.play(FadeIn(recovery))
        self.pause('2.f.recovery')
        self.play(FadeOut(fish))
        self.remove(stock_label)
        stock_label = Tex(r'Stock: $0$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
        zero = MathTex(r'0\ \longrightarrow\ 0', color=INK).move_to([4, -0.8, 0])
        teaching = Tex('Depletion can be reversed; an empty pond cannot reproduce.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(stock_label), FadeIn(zero), FadeIn(teaching))
        self.pause('2.f')
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 3.a · Commit to a share for three months; explain the score first.
        head = title('The Fishing Game')
        rules = VGroup(Tex(r'Low: catch $\frac14$ of the current stock.', color=INK),
                       Tex(r'High: catch $\frac12$ of the current stock.', color=INK),
                       Tex('Both firms choose at the same time.', color=CAPTION),
                       Tex('Keep the chosen strategy for three months.', color=CAPTION)).arrange(DOWN, buff=0.45, aligned_edge=LEFT).scale(0.8).move_to([0, 0.5, 0])
        scoring = Tex(r'Payoff $=$ catch in month 1 $+$ month 2 $+$ month 3', color=CAPTION).scale(0.75).move_to([0, -1.65, 0])
        assumptions = Tex('Equal value per fish; no costs or terminal-stock payoff.', color=CAPTION).scale(0.7).move_to([0, -2.35, 0])
        teaching = Tex('Choose a fishing strategy for all three months.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), FadeIn(rules), FadeIn(scoring), FadeIn(assumptions), FadeIn(teaching))
        self.pause('3.a')
        self.play(FadeOut(rules), FadeOut(scoring), FadeOut(assumptions))
        self.remove(teaching)

        # ---- 3.b / 3.c / 3.d · Same pond, timing, scale and ledger in all runs.
        # Rectangles are divisible fish tokens: their width measures the fraction
        # of one thousand fish. Split boundary tokens before simultaneous catches.
        result_cards = VGroup()
        profiles = [('L,L', LOW, LOW), ('H,L', HIGH, LOW), ('H,H', HIGH, HIGH)]
        payoff_by_profile = {}
        harvest_paths = []
        for profile_index, (profile, share_1, share_2) in enumerate(profiles):
            if profile_index:
                self.play(*[FadeOut(mob) for mob in self.mobjects if mob is not head and mob is not result_cards])
                self.remove(*[mob for mob in self.mobjects if mob is not head and mob is not result_cards])
            pond = Ellipse(width=5.4, height=2.65, color=INK, stroke_width=2).move_to(POND_CENTER)
            capacity = Tex(r'Carrying capacity: $K = 20$', color=CAPTION).scale(0.7).move_to([-4, 2.25, 0])
            units = Tex(r'\textsf{Thousands of fish}', color=CAPTION).scale(0.6).move_to([-4, 1.95, 0])
            stock_label = Tex(r'Stock: $20$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
            selections = VGroup(Tex(f'Firm 1: {profile[0]}', color=ROW_PLAYER),
                                Tex(f'Firm 2: {profile[2]}', color=COL_PLAYER)).arrange(RIGHT, buff=0.65).scale(0.8).move_to([-4, -1.9, 0])
            ledger_head = Tex('Catch By Month', color=INK).scale(0.8).move_to([4.3, 2.2, 0])
            ledger_columns = VGroup(*[Tex(f'{m+1}', color=CAPTION).scale(0.8).move_to([2.3+m*2, 1.55, 0]) for m in range(MONTHS)])
            ledger_names = VGroup(Tex('Firm 1', color=ROW_PLAYER).scale(0.7).move_to([0.7, 0.6, 0]),
                                  Tex('Firm 2', color=COL_PLAYER).scale(0.7).move_to([0.7, -0.9, 0]))
            ledger_boxes = VGroup(*[Rectangle(width=1.6, height=0.85, color=MUTED, stroke_width=1)
                                   .move_to([2.3+m*2, 0.6-firm*1.5, 0]) for firm in range(2) for m in range(MONTHS)])
            fish = VGroup(*[Rectangle(width=TOKEN_WIDTH, height=TOKEN_HEIGHT, stroke_width=0,
                                      fill_color=INK, fill_opacity=1).move_to(pos) for pos in POND_POSITIONS])
            self.play(FadeIn(pond), FadeIn(capacity), FadeIn(units), FadeIn(stock_label), FadeIn(selections),
                      FadeIn(ledger_head), FadeIn(ledger_columns), FadeIn(ledger_names), FadeIn(ledger_boxes), FadeIn(fish))
            n = K
            catches_by_firm = [[], []]
            captured = VGroup()
            ledger_numbers = VGroup()
            phase = VGroup()
            for month in range(MONTHS):
                h_1, h_2 = share_1*n, share_2*n
                survivor_count = n-h_1-h_2
                next_stock = min(K, 2*survivor_count)
                assert 0 <= h_1+h_2 <= n and 0 <= next_stock <= K
                catches_by_firm[0].append(h_1)
                catches_by_firm[1].append(h_2)
                self.remove(phase)
                phase = Tex(f'Month {month+1}: harvest', color=CAPTION).scale(0.75).move_to([-4, -2.55, 0])
                self.play(FadeIn(phase), run_time=0.3)
                # Partition the current token grid at the exact two catch boundaries.
                partitions = [VGroup(), VGroup(), VGroup()]
                cursor = 0.0
                for owner, quantity in enumerate((h_1, h_2, survivor_count)):
                    remaining = quantity
                    while remaining > 1e-8:
                        slot = int(cursor+1e-8)
                        fraction_start = cursor-slot
                        amount = min(remaining, 1-fraction_start)
                        piece = Rectangle(width=TOKEN_WIDTH*amount, height=TOKEN_HEIGHT,
                                          stroke_width=0, fill_color=INK, fill_opacity=1)
                        piece.move_to(POND_POSITIONS[slot] + RIGHT*TOKEN_WIDTH*(fraction_start+amount/2-0.5))
                        partitions[owner].add(piece)
                        cursor += amount
                        remaining -= amount
                self.remove(fish)
                self.add(*partitions)
                moves = []
                for firm in range(2):
                    for i, piece in enumerate(partitions[firm]):
                        target = np.array([1.76+month*2+(i%5)*0.27, 0.76-firm*1.5-(i//5)*0.3, 0])
                        moves.append(piece.animate.scale(0.5).move_to(target).set_color(FIRM_COLORS[firm]))
                if moves:
                    self.play(*moves, run_time=1.0)
                captured.add(*partitions[0], *partitions[1])
                month_values = VGroup(*[Tex(f'${quantity:g}$', color=FIRM_COLORS[firm]).scale(0.75)
                                        .move_to([2.3+month*2, -0.1-firm*1.5, 0])
                                        for firm, quantity in enumerate((h_1, h_2))])
                ledger_numbers.add(*month_values)
                self.remove(stock_label)
                stock_label = Tex(f'Survivors: ${survivor_count:g}$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
                self.play(FadeIn(month_values), FadeIn(stock_label), run_time=0.4)
                self.remove(phase)
                phase = Tex(f'Reproduce: ${survivor_count:g} \\to {next_stock:g}$', color=CAPTION).scale(0.75).move_to([-4, -2.55, 0])
                self.play(FadeIn(phase), run_time=0.3)
                # Repack survivors into unit tokens, then grow only from survivors.
                self.remove(partitions[2])
                surviving_tokens = VGroup()
                for i in range(int(np.ceil(survivor_count))):
                    amount = min(1.0, survivor_count-i)
                    token = Rectangle(width=TOKEN_WIDTH*amount, height=TOKEN_HEIGHT, stroke_width=0,
                                      fill_color=INK, fill_opacity=1).move_to(POND_POSITIONS[i]+LEFT*TOKEN_WIDTH*(1-amount)/2)
                    surviving_tokens.add(token)
                self.add(surviving_tokens)
                fish = VGroup()
                for i in range(int(np.ceil(next_stock))):
                    amount = min(1.0, next_stock-i)
                    token = Rectangle(width=TOKEN_WIDTH*amount, height=TOKEN_HEIGHT, stroke_width=0,
                                      fill_color=INK, fill_opacity=1).move_to(POND_POSITIONS[i]+LEFT*TOKEN_WIDTH*(1-amount)/2)
                    fish.add(token)
                if len(fish):
                    # Copies start inside the surviving population, not in catch trays.
                    newborn_display = fish.copy()
                    for i, token in enumerate(newborn_display):
                        token.move_to(surviving_tokens[i % len(surviving_tokens)].get_center())
                    self.remove(surviving_tokens)
                    self.add(newborn_display)
                    self.play(Transform(newborn_display, fish), run_time=1.0)
                    self.remove(newborn_display)
                    self.add(fish)
                else:
                    self.remove(surviving_tokens)
                self.remove(stock_label)
                stock_label = Tex(f'Next stock: ${next_stock:g}$', color=INK).scale(0.8).move_to([-4, -1.15, 0])
                self.play(FadeIn(stock_label), run_time=0.3)
                n = next_stock
                if month == 0:
                    teaching = Tex('What will each firm catch next month?', color=DEFINITION)
                    teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
                    self.play(FadeIn(teaching))
                    if profile_index == 0:
                        self.pause('3.b.first')
                    elif profile_index == 1:
                        self.pause('3.c.first')
                    else:
                        self.pause('3.d.first')
                    self.remove(teaching)
            total_1, total_2 = map(sum, catches_by_firm)
            payoff_by_profile[profile] = (total_1, total_2)
            harvest_paths.append(catches_by_firm[0])
            sums = VGroup(*[MathTex('+'.join(f'{h:g}' for h in catches_by_firm[firm])+f'={total:g}', color=FIRM_COLORS[firm])
                            .scale(0.8).move_to([4.3, -2.2-firm*0.55, 0]) for firm, total in enumerate((total_1,total_2))])
            self.play(FadeIn(sums))
            line = ('Low harvests maintain the stock.',
                    'A larger share today can leave fewer fish tomorrow.',
                    'Both firms take more at first, then there are no fish left.')[profile_index]
            teaching = Tex(line, color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
            self.play(FadeIn(teaching))
            if profile_index == 0:
                self.pause('3.b')
            elif profile_index == 1:
                self.pause('3.c')
            else:
                self.pause('3.d')
            card = VGroup(Tex(profile, color=CAPTION), Tex(f'{total_1:g}', color=ROW_PLAYER),
                          Tex(r'$\mid$', color=MUTED), Tex(f'{total_2:g}', color=COL_PLAYER)).arrange(RIGHT, buff=0.16).scale(0.7)
            card.move_to([-4.8+profile_index*4.8, -2.8, 0])
            # Retain result cards off-stage between runs, then bring back for the plot.
            result_cards.add(card)

        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()

        # ---- 3.e · Harvest over time (not a population plot).
        head = title('Catch Over Time')
        chart = axes([1, 3, 1], [0, 10, 5], x_length=7.5, y_length=4.0).move_to([-1.5, 0, 0])
        x_labels = VGroup(*[Tex(str(m), color=CAPTION).scale(0.7).next_to(chart.c2p(m,0), DOWN, buff=0.16) for m in (1,2,3)])
        y_labels = VGroup(*[Tex(str(q), color=CAPTION).scale(0.7).next_to(chart.c2p(1,q), LEFT, buff=0.16) for q in (0,5,10)])
        x_title = Tex('Month', color=INK).scale(0.8).next_to(chart, DOWN, buff=0.6)
        y_title = Tex("Firm 1's catch", color=INK).scale(0.8).move_to([-3.7, 2.65, 0])
        chart_units = Tex(r'\textsf{Thousands of fish per month}', color=CAPTION).scale(0.6).move_to([1.1, 2.65, 0])
        teaching = Tex('The payoff counts all three months.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head), Create(chart), FadeIn(x_labels), FadeIn(y_labels), FadeIn(x_title), FadeIn(y_title), FadeIn(chart_units), FadeIn(teaching))
        paths = VGroup()
        for index, ((profile, _, _), values) in enumerate(zip(profiles, harvest_paths)):
            if len(paths):
                self.play(paths.animate.set_opacity(0.35), run_time=0.3)
            segments = VGroup()
            for j in range(2):
                a, b = chart.c2p(j+1,values[j]), chart.c2p(j+2,values[j+1])
                if index == 0:
                    segment = Line(a,b,color=ROW_PLAYER,stroke_width=3)
                else:
                    segment = DashedLine(a,b,color=ROW_PLAYER,stroke_width=3,
                                         dash_length=0.16 if index==1 else 0.025,
                                         dashed_ratio=0.6 if index==1 else 0.22)
                segments.add(segment)
            dots = VGroup(*[Dot(chart.c2p(m+1,q), radius=0.055, color=ROW_PLAYER) for m,q in enumerate(values)])
            direct_label = Tex(profile, color=CAPTION).scale(0.7).next_to(chart.c2p(3,values[-1]), RIGHT, buff=0.2)
            path = VGroup(segments,dots,direct_label)
            paths.add(path)
            result_cards[index].move_to([5.3, 1.4-index*1.3, 0])
            self.play(Create(segments), FadeIn(dots), FadeIn(direct_label), FadeIn(result_cards[index]))
        self.play(paths.animate.set_opacity(1))
        self.pause('3.e')

        # ---- 4.a · Carry actual totals into D1's diamond matrix.
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in list(result_cards)])
        self.remove(head, teaching)
        head = title('The Fishing Game')
        # The L,H case is the H,L case with the identities exchanged.
        payoff_by_profile['L,H'] = payoff_by_profile['H,L'][::-1]
        numeric = [[payoff_by_profile['L,L'], payoff_by_profile['L,H']],
                   [payoff_by_profile['H,L'], payoff_by_profile['H,H']]]
        payoffs = [[VGroup(Tex(f'{a:g}', color=ROW_PLAYER), Tex(r'$\mid$', color=MUTED), Tex(f'{b:g}', color=COL_PLAYER))
                    .arrange(RIGHT,buff=0.12).scale(0.7) for a,b in row] for row in numeric]
        entries = [cell for row in payoffs for cell in row]
        matrix = Table(payoffs, h_buff=CELL_SIDE-max(cell.width for cell in entries),
                       v_buff=CELL_SIDE-max(cell.height for cell in entries), include_outer_lines=True,
                       line_config={'color':MUTED,'stroke_width':2}).rotate(DIAMOND_ANGLE).move_to(GAME_CENTER)
        for cell in entries:
            cell.rotate(-DIAMOND_ANGLE, about_point=cell.get_center())
        row_labels = VGroup(*[Tex(r'\textsf{'+s+'}',color=CAPTION).scale(0.7) for s in ('Low','High')])
        col_labels = VGroup(*[Tex(r'\textsf{'+s+'}',color=CAPTION).scale(0.7) for s in ('Low','High')])
        for i in range(2):
            offset=(0.5-i)*CELL_SIDE
            row_anchor=GAME_CENTER-CELL_SIDE*TABLE_RIGHT+offset*TABLE_UP
            col_anchor=GAME_CENTER-offset*TABLE_RIGHT+CELL_SIDE*TABLE_UP
            row_labels[i].move_to(row_anchor+LEFT*0.3,aligned_edge=RIGHT)
            col_labels[i].move_to(col_anchor+RIGHT*0.3,aligned_edge=LEFT)
        player_1=Tex('Firm 1',color=ROW_PLAYER).scale(0.8).move_to([-2.8,2,0])
        player_2=Tex('Firm 2',color=COL_PLAYER).scale(0.8).move_to([2.8,2,0])
        teaching=Tex("Firm 1's payoff first; Firm 2's payoff second.",color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head),FadeIn(matrix.get_horizontal_lines()),FadeIn(matrix.get_vertical_lines()),
                  FadeIn(row_labels),FadeIn(col_labels),FadeIn(player_1),FadeIn(player_2),FadeIn(teaching))
        for card_index, (r,c) in enumerate(((0,0),(1,0),(1,1))):
            self.play(TransformFromCopy(result_cards[card_index][1:],payoffs[r][c]),run_time=0.8)
            if card_index==1:
                self.play(TransformFromCopy(payoffs[1][0],payoffs[0][1]),run_time=0.8)
        self.play(FadeOut(result_cards))
        self.pause('4.a')

        # ---- 4.b–4.i · Exactly D1's fixed-strategy shading and payoff boxes.
        responses=VGroup()
        shade=VGroup()
        underline=VGroup()
        for acting_player in (0,1):
            for fixed_strategy in (0,1):
                self.remove(teaching,shade,underline)
                rival=2 if acting_player==0 else 1
                rival_color=COL_PLAYER if acting_player==0 else ROW_PLAYER
                fixed_word=('Low','High')[fixed_strategy]
                teaching=Tex(f"If Firm {rival} chooses {fixed_word}, what is Firm {acting_player+1}'s best response?",color=DEFINITION)
                teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
                if acting_player==0:
                    shade=Rectangle(width=CELL_SIDE,height=2*CELL_SIDE,stroke_width=0,fill_color=rival_color,fill_opacity=0.12)
                    shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER+(fixed_strategy-0.5)*CELL_SIDE*TABLE_RIGHT).set_z_index(-1)
                    underline=Underline(col_labels[fixed_strategy],buff=0.1,stroke_color=rival_color,stroke_width=3,stretch_factor=1)
                else:
                    shade=Rectangle(width=2*CELL_SIDE,height=CELL_SIDE,stroke_width=0,fill_color=rival_color,fill_opacity=0.12)
                    shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER+(0.5-fixed_strategy)*CELL_SIDE*TABLE_UP).set_z_index(-1)
                    underline=Underline(row_labels[fixed_strategy],buff=0.1,stroke_color=rival_color,stroke_width=3,stretch_factor=1)
                self.play(FadeIn(shade),FadeIn(underline),FadeIn(teaching))
                if acting_player==0 and fixed_strategy==0:
                    self.pause('4.b')
                elif acting_player==0:
                    self.pause('4.d')
                elif fixed_strategy==0:
                    self.pause('4.f')
                else:
                    self.pause('4.h')
                r,c=(1,fixed_strategy) if acting_player==0 else (fixed_strategy,1)
                best=payoffs[r][c][0 if acting_player==0 else 2]
                response=SurroundingRectangle(best,buff=0.08,color=FIRM_COLORS[acting_player])
                responses.add(response)
                self.remove(teaching)
                answer=r'High: $17.5 > 15$.' if fixed_strategy==0 else r'High: $10 > 8.75$.'
                teaching=Tex(answer,color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
                self.play(Create(response),FadeIn(teaching))
                if acting_player==0 and fixed_strategy==0:
                    self.pause('4.c')
                elif acting_player==0:
                    self.pause('4.e')
                elif fixed_strategy==0:
                    self.pause('4.g')
                else:
                    self.pause('4.i')

        # ---- 4.j · Unilateral-deviation test, then Nash.
        self.remove(shade,underline,teaching)
        nash_box=Square(side_length=CELL_SIDE-0.15,color=NASH,stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1])
        teaching=Tex('Neither firm gains by changing its strategy alone.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(nash_box),FadeIn(teaching))
        self.pause('4.j')

        # ---- 4.k · Compare combined catch across the four available profiles.
        self.remove(teaching)
        total_labels=VGroup()
        for (r,c),position in zip(((0,0),(0,1),(1,0),(1,1)),((4.8,1.1,0),(4.8,0.2,0),(-4.8,0.2,0),(4.8,-1.5,0))):
            profile=f"{('L','H')[r]},{('L','H')[c]}"
            value=sum(numeric[r][c])
            label=Tex(f'{profile}: total ${value:g}$',color=TOTAL).scale(0.75).move_to(position)
            total_labels.add(label)
            self.play(FadeIn(label),run_time=0.4)
        efficient_box=Square(side_length=CELL_SIDE-0.15,color=EFFICIENT,stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[0][0])
        teaching=Tex('Both firms would catch more if both chose Low.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(efficient_box),FadeIn(teaching))
        self.pause('4.k')

        # ---- 5.a · Part C's private consequence, external cost, joint result.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head=title('Private And Shared Consequences')
        before=VGroup(Tex('Low, Low',color=CAPTION),payoffs[0][0].copy()).arrange(DOWN,buff=0.3).move_to([-3.3,1.5,0])
        after=VGroup(Tex('High, Low',color=CAPTION),payoffs[1][0].copy()).arrange(DOWN,buff=0.3).move_to([3.3,1.5,0])
        arrow=Arrow([-1.4,1.3,0],[1.4,1.3,0],color=MUTED)
        private=Tex(r'Firm 1: $17.5-15=+2.5$',color=ROW_PLAYER).scale(0.9).move_to([0,0.1,0])
        external=Tex(r'Firm 2: $8.75-15=-6.25$',color=COL_PLAYER).scale(0.9).move_to([0,-0.85,0])
        combined=Tex(r'Combined catch: $2.5-6.25=-3.75$',color=TOTAL).scale(0.9).move_to([0,-1.85,0])
        self.play(FadeIn(head),FadeIn(before),FadeIn(after),GrowArrow(arrow),FadeIn(private))
        self.pause('5.a.private')
        self.play(FadeIn(external))
        self.pause('5.a.external')
        teaching=Tex("The extra catch benefits one firm and reduces the other's catch.",color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(combined),FadeIn(teaching))
        self.pause('5.a')

        # ---- 5.b · Restore the clean game; no invented enforcement payoffs.
        self.play(*[FadeOut(mob) for mob in self.mobjects])
        self.clear()
        head=title('Changing The Game')
        teaching=Tex('What would make Low a best response?',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(head),FadeIn(matrix),FadeIn(row_labels),FadeIn(col_labels),FadeIn(player_1),FadeIn(player_2),FadeIn(teaching))
        self.pause('5.b')
        institutions=VGroup(*[Tex(text,color=CAPTION).scale(0.75) for text in ('Harvest rules','Monitoring','Consequences for violations')]).arrange(DOWN,buff=0.5,aligned_edge=LEFT).move_to([4.8,-0.65,0])
        for label in institutions:
            self.play(FadeIn(label),run_time=0.5)
        self.pause('5.b.rules')
