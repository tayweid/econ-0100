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
        TOKEN_RADIUS = 0.16
        LEDGER_SCALE = 0.65
        POND_CENTER = np.array([-4.0, 0.85, 0.0])
        # A fixed, gently scattered population: no jitter or rearrangement on birth.
        POND_POSITIONS = [POND_CENTER + np.array([x,y,0]) for x,y in (
            (0.10,0.66),(2.07,-0.45),(1.20,0.44),(0.73,-0.84),(-2.13,-0.25),
            (0.01,-0.39),(1.56,0.96),(-0.44,1.08),(-1.97,0.68),(-0.56,0.59),
            (-1.38,0.22),(0.25,0.12),(-0.68,-0.07),(1.03,-0.41),(1.85,-1.04),
            (2.07,0.19),(-0.49,-0.66),(-1.12,-0.75),(-1.75,-0.62),(1.54,0.08))]
        FIRM_COLORS = (ROW_PLAYER, COL_PLAYER)
        CELL_SIDE = 1.5
        DIAMOND_ANGLE = -PI / 4
        GAME_CENTER = DOWN * 0.5
        TABLE_RIGHT = (RIGHT + DOWN) / 2**0.5
        TABLE_UP = (RIGHT + UP) / 2**0.5

        # ---- sim.a–sim.e · Original D0 simulation instructions, before the model.
        # Copy of D0_Strategic_Interaction/03_Code.py's final rules card.
        # Only integration changes: standalone heading (no D0 bumper dependency),
        # named ManimLive holds instead of waits, then clear before the D2 model.
        simulation_label = Tex('{{Part D}} $|$ Common Resources Simulation').set_color(GREY).set_color_by_tex_to_color_map(
            {"Part D": RED,}
        ).scale(1.5).to_edge(UP, buff=1)
        self.play(FadeIn(simulation_label))

        rule_label = Tex('{{Rules}}').set_color(YELLOW).scale(1.5).to_edge(UP+LEFT, buff=1).shift(DOWN*3 + RIGHT*2)

        rules = [
            Tex('- One lake, five firms').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*4 + RIGHT*2),
            Tex('- Each round, choose your harvest').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*4.5 + RIGHT*2),
            Tex('- Fish population doubles each round').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*5 + RIGHT*2),
            Tex('- Carrying capacity is 20,000 fish').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*5.5 + RIGHT*2),
            Tex('- Maximize harvest after 4 rounds').set_color(GREY).to_edge(UP+LEFT, buff=1).shift(DOWN*6 + RIGHT*2),
        ]

        self.play(FadeIn(rule_label))
        self.play(FadeIn(rules[0]))
        self.pause('sim.a')
        self.play(FadeIn(rules[1]))
        self.pause('sim.b')
        self.play(FadeIn(rules[2]))
        self.pause('sim.c')
        self.play(FadeIn(rules[3]))
        self.pause('sim.d')
        self.play(FadeIn(rules[4]))
        self.pause('sim.e')
        self.play(FadeOut(simulation_label), FadeOut(rule_label), *[FadeOut(rule) for rule in rules])
        self.clear()

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

        # ---- 1.b · The shared stock stays put; a caught unit moves to its owner.
        self.play(FadeOut(taxonomy), FadeOut(box), FadeOut(teaching))
        pond = RoundedRectangle(width=5.4, height=2.8, corner_radius=0.8, color=INK, stroke_width=2).move_to(POND_CENTER)
        capacity = Tex(r'Shared pond: capacity $20$', color=CAPTION).scale(0.8).move_to([-4, 2.5, 0])
        units = Tex(r'\textsf{One full dot = 1,000 fish}', color=CAPTION).scale(0.6).move_to([-4, -1.45, 0])
        stock_label = VGroup(Tex('Stock:', color=INK), Tex('20', color=INK)).arrange(RIGHT, buff=0.15).scale(0.8).move_to([-4, -0.9, 0])
        trays = VGroup(*[RoundedRectangle(width=2.3, height=0.8, corner_radius=0.12, color=MUTED, stroke_width=1.5)
                        .move_to([x, -2.55, 0]) for x in (-5.5, -2.5)])
        firm_names = VGroup(*[Tex(f'Firm {i+1}', color=FIRM_COLORS[i]).scale(0.75)
                             .move_to([x, -1.95, 0]) for i, x in enumerate((-5.5, -2.5))])
        fish = VGroup(*[Dot(radius=TOKEN_RADIUS, color=INK)
                       .move_to(pos) for pos in POND_POSITIONS])
        teaching = Tex('A fish I catch is no longer available for you to catch.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(pond), FadeIn(fish), FadeIn(units), FadeIn(trays), FadeIn(firm_names), FadeIn(teaching))
        self.play(fish[-1].animate.move_to(trays[0]).set_color(ROW_PLAYER), run_time=1.2)
        self.pause('1.b')
        self.play(fish[-1].animate.move_to(POND_POSITIONS[-1]).set_color(INK))

        # ---- 1.c · Capacity is the fixed boundary; stock is the population inside.
        self.remove(teaching)
        teaching = Tex('Carrying capacity limits the stock, not the monthly catch.', color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN, buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(capacity), FadeIn(stock_label), FadeIn(teaching))
        self.pause('1.c')

        # ---- 2.a–2.d · Same pond and trays; only catches and births move.
        self.play(Transform(head, title('Population And Harvest')), FadeOut(teaching))
        divider = Line([0, -3.05, 0], [0, 2.5, 0], color=MUTED, stroke_width=1)
        self.play(Create(divider))
        example_objects = VGroup()
        for example, per_firm in enumerate((5, 6, 2)):
            if example:
                # An explicit fresh example, not a jump during population growth.
                self.play(FadeOut(fish), FadeOut(catches[0]), FadeOut(catches[1]),
                          FadeOut(catch_values), FadeOut(example_objects), FadeOut(teaching))
                fish = VGroup(*[Dot(radius=TOKEN_RADIUS, color=INK)
                               .move_to(pos) for pos in POND_POSITIONS])
                self.play(FadeIn(fish), Transform(stock_label,
                    VGroup(Tex('Stock:', color=INK), Tex('20', color=INK)).arrange(RIGHT, buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
            remaining = K - 2*per_firm
            next_stock = min(K, 2*remaining)
            month_label = Tex('Month 1', color=CAPTION).scale(0.8).move_to([4,2.35,0])
            phase = Tex('Harvest', color=INK).scale(0.8).move_to([4,1.65,0])
            equation = VGroup(*[Tex(t, color=c) for t,c in zip(
                ('20', '$-$', str(per_firm), '$-$', str(per_firm), '$=$', '?'),
                (INK, INK, ROW_PLAYER, INK, COL_PLAYER, INK, INK))]).arrange(RIGHT,buff=0.15).scale(0.9).move_to([4,0.75,0])
            catches = [VGroup(*fish[:per_firm]), VGroup(*fish[per_firm:2*per_firm])]
            survivors = VGroup(*fish[2*per_firm:])
            survivor_homes = [token.get_center().copy() for token in survivors]
            self.play(Transform(stock_label[0],Tex('Start:',color=INK).scale(0.8).move_to(stock_label[0])))
            self.play(FadeIn(month_label), FadeIn(phase), TransformFromCopy(stock_label[1], equation[0]))
            # Every caught dot retains its size. Neutral survivors never move.
            self.play(*[token.animate.move_to([-6.34+(i%5)*0.42+firm*3,-2.35-(i//5)*0.4,0]).set_color(FIRM_COLORS[firm])
                        for firm, group in enumerate(catches) for i,token in enumerate(group)], run_time=1.4)
            catch_values = VGroup(*[Tex(f'${per_firm}$',color=c).scale(0.75).move_to([x,-3.15,0])
                                   for c,x in zip(FIRM_COLORS,(-5.5,-2.5))])
            self.play(FadeIn(catch_values))
            self.play(TransformFromCopy(catch_values[0],equation[2]), TransformFromCopy(catch_values[1],equation[4]),
                      *[FadeIn(equation[i]) for i in (1,3,5,6)], run_time=0.9)
            teaching = Tex('How many fish remain to reproduce?',color=DEFINITION)
            teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
            self.play(FadeIn(teaching))
            if example == 0:
                self.pause('2.a')
            answer = Tex(f'${remaining:g}$',color=INK).scale(0.9).move_to(equation[6])
            self.play(Transform(equation[6],answer), Transform(stock_label,
                VGroup(Tex('Survivors:',color=INK),Tex(f'{remaining:g}',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
            if example == 1:
                self.pause('2.c.survivors')
            elif example == 2:
                self.pause('2.d.survivors')
            growth_heading = Tex('Reproduction',color=INK).scale(0.8).move_to([4,-0.35,0])
            growth = VGroup(Tex(r'$\min\{20,\,2\times$',color=INK), Tex(f'${remaining:g}$',color=INK),
                            Tex(r'$\}=$',color=INK), Tex(f'${next_stock:g}$',color=INK))
            growth.arrange(RIGHT,buff=0.12).scale(0.9).move_to([4,-1.25,0])
            self.play(FadeIn(growth_heading),FadeIn(growth[0]),TransformFromCopy(equation[6],growth[1]),FadeIn(growth[2]),FadeOut(teaching))
            # Births alone fill vacated slots. Parents retain both identity and position.
            babies = VGroup(*[survivors[i].copy() for i in range(int(next_stock-remaining))])
            self.add(babies)
            self.play(*[baby.animate.move_to(POND_POSITIONS[i]) for i,baby in enumerate(babies)],run_time=1.4)
            assert all(np.allclose(t.get_center(),p) for t,p in zip(survivors,survivor_homes))
            fish = VGroup(*survivors,*babies)
            self.play(FadeIn(growth[3]), Transform(stock_label,
                VGroup(Tex('Stock:',color=INK),Tex(f'{next_stock:g}',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])),
                Transform(month_label,Tex('Month 2',color=CAPTION).scale(0.8).move_to(month_label)))
            line = ('Catch 10; the surviving 10 restore the stock to 20.',
                    'Catch 12; the surviving 8 restore only 16.',
                    'The population grows only as far as the pond can support.')[example]
            teaching = Tex(line,color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
            self.play(FadeIn(teaching))
            example_objects = VGroup(month_label,phase,equation,growth_heading,growth)
            if example == 0:
                self.pause('2.b')
            elif example == 1:
                self.pause('2.c')
            else:
                capacity_focus = SurroundingRectangle(capacity,color=FOCUS,buff=0.12)
                self.play(Create(capacity_focus),Indicate(growth[0],color=FOCUS))
                self.pause('2.d')
                self.play(FadeOut(capacity_focus))

        # ---- 2.e · Replace concrete arithmetic with its general rule, term by term.
        self.play(FadeOut(month_label),FadeOut(phase),FadeOut(growth_heading),FadeOut(teaching))
        survivor_rule = VGroup(*[MathTex(t,color=c) for t,c in zip(
            ('N_t','-','h_{1t}','-','h_{2t}','=','S_t'),
            (INK,INK,ROW_PLAYER,INK,COL_PLAYER,INK,INK))]).arrange(RIGHT,buff=0.15).scale(0.9).move_to([4,0.75,0])
        self.play(*[ReplacementTransform(equation[i],survivor_rule[i]) for i in range(7)])
        self.pause('2.e.survivors')
        growth_rule = MathTex(r'N_{t+1}=\min\{20,\;2S_t\}',color=INK).scale(0.9).move_to([4,-1.25,0])
        feasible = MathTex(r'0\leq h_{1t}+h_{2t}\leq N_t',color=CAPTION).scale(0.7).move_to([4,-2.3,0])
        teaching = Tex("Next month's stock depends on what survives this month's catch.",color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(ReplacementTransform(growth,growth_rule),FadeIn(feasible),FadeIn(teaching))
        self.pause('2.e')

        # ---- 2.f · Show each recovery step while it happens; no hidden new stock.
        self.play(FadeOut(fish),FadeOut(catches[0]),FadeOut(catches[1]),FadeOut(catch_values),
                  FadeOut(survivor_rule),FadeOut(growth_rule),FadeOut(feasible),FadeOut(teaching),
                  FadeOut(trays),FadeOut(firm_names))
        fish = VGroup(*[Dot(radius=TOKEN_RADIUS,color=INK)
                       .move_to(pos) for pos in POND_POSITIONS[:8]])
        recovery = VGroup(*[Tex(t,color=INK) for t in ('8',r'$\longrightarrow$','16',r'$\longrightarrow$','20')])
        recovery.arrange(RIGHT,buff=0.2).scale(0.9).move_to([4,0.75,0])
        no_catch = Tex('No further harvest',color=CAPTION).scale(0.8).move_to([4,1.65,0])
        self.play(FadeIn(fish),FadeIn(no_catch),FadeIn(recovery[0]),Transform(stock_label,
            VGroup(Tex('Stock:',color=INK),Tex('8',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
        for step,stock in enumerate((16,20)):
            babies = VGroup(*[fish[i].copy() for i in range(stock-len(fish))])
            self.add(babies)
            self.play(*[t.animate.move_to(POND_POSITIONS[len(fish)+i]) for i,t in enumerate(babies)],FadeIn(recovery[1+step*2]),run_time=1.2)
            fish.add(*babies)
            self.play(FadeIn(recovery[2+step*2]),Transform(stock_label,
                VGroup(Tex('Stock:',color=INK),Tex(str(stock),color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
        self.pause('2.f.recovery')
        self.play(FadeOut(fish),Transform(stock_label,
            VGroup(Tex('Stock:',color=INK),Tex('0',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
        zero = MathTex(r'0\longrightarrow0',color=INK).scale(0.9).move_to([4,-0.8,0])
        teaching = Tex('Depletion can be reversed; an empty pond cannot reproduce.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(zero),FadeIn(teaching))
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

        # ---- 3.b–3.d · One persistent pond, one ledger, three fresh strategy runs.
        pond = RoundedRectangle(width=5.4,height=2.8,corner_radius=0.8,color=INK,stroke_width=2).move_to(POND_CENTER)
        capacity = Tex(r'Shared pond: capacity $20$',color=CAPTION).scale(0.8).move_to([-4,2.5,0])
        ledger_head = Tex('Catch by month',color=INK).scale(0.8).move_to([4.2,2.5,0])
        ledger_columns = VGroup(*[Tex(str(m+1),color=CAPTION).scale(0.75).move_to([2.3+m*2,1.8,0]) for m in range(MONTHS)])
        ledger_boxes = VGroup(*[RoundedRectangle(width=1.65,height=0.85,corner_radius=0.12,color=MUTED,stroke_width=1)
                               .move_to([2.3+m*2,0.9-firm*1.65,0]) for firm in range(2) for m in range(MONTHS)])
        divider = Line([0,-3.1,0],[0,2.5,0],color=MUTED,stroke_width=1)
        self.play(Create(pond),FadeIn(capacity),FadeIn(ledger_head),FadeIn(ledger_columns),FadeIn(ledger_boxes),Create(divider))
        result_cards = VGroup()
        profiles = [('L,L',LOW,LOW),('H,L',HIGH,LOW),('H,H',HIGH,HIGH)]
        payoff_by_profile = {}
        harvest_paths = []
        for profile_index,(profile,share_1,share_2) in enumerate(profiles):
            if profile_index:
                # Clear a completed trial; keep the physical pond and ledger fixed.
                self.play(FadeOut(fish),FadeOut(captured),FadeOut(ledger_numbers),FadeOut(ledger_names),
                          FadeOut(stock_label),FadeOut(phase),FadeOut(harvest_math),FadeOut(growth_math),FadeOut(sums),FadeOut(teaching))
            ledger_names = VGroup(*[VGroup(Tex(f'Firm {firm+1}',color=color),Tex('Low' if share==LOW else 'High',color=color))
                .arrange(DOWN,buff=0.12).scale(0.65).move_to([0.75,0.9-firm*1.65,0])
                for firm,(color,share) in enumerate(zip(FIRM_COLORS,(share_1,share_2)))])
            stock_label = VGroup(Tex('Stock:',color=INK),Tex('20',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])
            fish = VGroup(*[Dot(radius=TOKEN_RADIUS,color=INK).move_to(pos) for pos in POND_POSITIONS])
            for slot,token in enumerate(fish):
                token.fish_units = 1.0
                token.pond_slot = slot
                token.fish_angle = 0.0
            self.play(FadeIn(fish),FadeIn(stock_label),FadeIn(ledger_names))
            n = K
            catches_by_firm = [[],[]]
            captured = VGroup()
            ledger_numbers = VGroup()
            phase = Tex('Month 1',color=CAPTION).scale(0.65).move_to([-4,-1.4,0])
            harvest_math = VGroup()
            growth_math = VGroup()
            self.play(FadeIn(phase))
            for month in range(MONTHS):
                h_1,h_2 = share_1*n,share_2*n
                survivor_count = n-h_1-h_2
                next_stock = min(K,2*survivor_count)
                assert 0 <= h_1+h_2 <= n and 0 <= next_stock <= K
                if month:
                    self.play(FadeOut(harvest_math),FadeOut(growth_math),
                              Transform(phase,Tex(f'Month {month+1}',color=CAPTION).scale(0.65).move_to(phase)))
                self.play(Transform(stock_label,
                    VGroup(Tex('Start:',color=INK),Tex(f'{n:g}',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
                catches_by_firm[0].append(h_1)
                catches_by_firm[1].append(h_2)
                # Reuse every whole dot. Split only the token at a catch boundary,
                # in place, with the pieces' combined area equal to the original.
                available = list(fish)
                partitions = [VGroup(),VGroup()]
                for owner,quantity in enumerate((h_1,h_2)):
                    need = quantity
                    while need > 1e-8:
                        token = available.pop(0)
                        if token.fish_units <= need+1e-8:
                            partitions[owner].add(token)
                            need -= token.fish_units
                        else:
                            remainder = token.copy()
                            remainder.fish_units = token.fish_units-need
                            remainder.fish_angle = token.fish_angle+TAU*need
                            # Divide the circular area in place. The two sectors
                            # together look exactly like the original dot.
                            remainder.become(Sector(radius=TOKEN_RADIUS,angle=TAU*remainder.fish_units,
                                start_angle=remainder.fish_angle,arc_center=POND_POSITIONS[token.pond_slot],color=INK))
                            token.fish_units = need
                            token.become(Sector(radius=TOKEN_RADIUS,angle=TAU*need,
                                start_angle=token.fish_angle,arc_center=POND_POSITIONS[token.pond_slot],color=INK))
                            self.add(remainder)
                            partitions[owner].add(token)
                            available.insert(0,remainder)
                            need = 0
                survivors = VGroup(*available)
                survivor_homes = [token.get_center().copy() for token in survivors]
                survivor_ids = [id(token) for token in survivors]
                month_values = VGroup(*[Tex(f'${quantity:g}$',color=FIRM_COLORS[firm]).scale(0.75)
                    .move_to([2.3+month*2,0.23-firm*1.65,0]) for firm,quantity in enumerate((h_1,h_2))])
                moves = []
                for firm in range(2):
                    for i,token in enumerate(partitions[firm]):
                        target = [1.76+month*2+(i%5)*0.27,1.1-firm*1.65-(i//5)*0.36,0]
                        moves.append(token.animate.scale(LEDGER_SCALE).move_to(target).set_color(FIRM_COLORS[firm]))
                if moves:
                    self.play(*moves,run_time=1.4)
                captured.add(*partitions[0],*partitions[1])
                self.play(FadeIn(month_values),run_time=0.5)
                ledger_numbers.add(month_values)
                harvest_math = VGroup(*[Tex(t,color=c) for t,c in zip(
                    (f'${n:g}$','$-$',f'${h_1:g}$','$-$',f'${h_2:g}$','$=$',f'${survivor_count:g}$'),
                    (INK,INK,ROW_PLAYER,INK,COL_PLAYER,INK,INK))]).arrange(RIGHT,buff=0.12).scale(0.8).move_to([-4,-2.05,0])
                self.play(TransformFromCopy(stock_label[1],harvest_math[0]),
                          TransformFromCopy(month_values[0],harvest_math[2]),TransformFromCopy(month_values[1],harvest_math[4]),
                          *[FadeIn(harvest_math[i]) for i in (1,3,5)],run_time=0.9)
                self.play(FadeIn(harvest_math[6]),Transform(stock_label,
                    VGroup(Tex('Survivors:',color=INK),Tex(f'{survivor_count:g}',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
                if month == 0:
                    teaching = Tex('What stock will these survivors produce?',color=DEFINITION)
                    teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
                    self.play(FadeIn(teaching))
                    if profile_index == 0:
                        self.pause('3.b.harvest')
                    elif profile_index == 1:
                        self.pause('3.c.harvest')
                    else:
                        self.pause('3.d.harvest')
                    self.play(FadeOut(teaching))
                growth_math = VGroup(Tex(r'$\min\{20,\,2\times$',color=INK),Tex(f'${survivor_count:g}$',color=INK),
                                    Tex(r'$\}=$',color=INK),Tex(f'${next_stock:g}$',color=INK))
                growth_math.arrange(RIGHT,buff=0.1).scale(0.8).move_to([-4,-2.85,0])
                self.play(FadeIn(growth_math[0]),TransformFromCopy(harvest_math[6],growth_math[1]),FadeIn(growth_math[2]))
                # Parents stay exactly where they survived. Only newborn copies move.
                vacant = [slot for slot in range(20) if slot not in {t.pond_slot for t in survivors}]
                births_needed = next_stock-survivor_count
                babies = VGroup()
                for parent in survivors:
                    if births_needed <= 1e-8:
                        break
                    amount = min(parent.fish_units,births_needed)
                    baby = parent.copy()
                    baby.fish_units = amount
                    baby.pond_slot = vacant[len(babies)]
                    baby.birth_shift = POND_POSITIONS[baby.pond_slot]-POND_POSITIONS[parent.pond_slot]
                    if amount < parent.fish_units-1e-8:
                        baby.become(Sector(radius=TOKEN_RADIUS,angle=TAU*amount,start_angle=parent.fish_angle,
                            arc_center=POND_POSITIONS[parent.pond_slot],color=INK))
                    babies.add(baby)
                    births_needed -= amount
                assert abs(births_needed)<1e-8
                if len(babies):
                    self.add(babies)
                    self.play(*[baby.animate.shift(baby.birth_shift) for baby in babies],run_time=1.4)
                assert [id(t) for t in survivors] == survivor_ids
                assert all(np.allclose(t.get_center(),p) for t,p in zip(survivors,survivor_homes))
                fish = VGroup(*survivors,*babies)
                assert np.isclose(sum(t.fish_units for t in fish),next_stock)
                self.play(FadeIn(growth_math[3]),Transform(stock_label,
                    VGroup(Tex('Next stock:',color=INK),Tex(f'{next_stock:g}',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-0.9,0])))
                n = next_stock
                if month == 0:
                    teaching = Tex('What will each firm catch next month?',color=DEFINITION)
                    teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
                    self.play(FadeIn(teaching))
                    if profile_index == 0:
                        self.pause('3.b.first')
                    elif profile_index == 1:
                        self.pause('3.c.first')
                    else:
                        self.pause('3.d.first')
                    self.play(FadeOut(teaching))
            total_1,total_2 = map(sum,catches_by_firm)
            payoff_by_profile[profile] = (total_1,total_2)
            harvest_paths.append(catches_by_firm[0])
            sums = VGroup()
            for firm,total in enumerate((total_1,total_2)):
                terms = [Tex(f'${v:g}$',color=FIRM_COLORS[firm]) for v in catches_by_firm[firm]]
                row = VGroup(terms[0],Tex('$+$',color=FIRM_COLORS[firm]),terms[1],Tex('$+$',color=FIRM_COLORS[firm]),
                             terms[2],Tex('$=$',color=FIRM_COLORS[firm]),Tex(f'${total:g}$',color=FIRM_COLORS[firm]))
                row.arrange(RIGHT,buff=0.1).scale(0.8).move_to([4.2,-2.3-firm*0.65,0])
                self.play(*[TransformFromCopy(ledger_numbers[m][firm],row[m*2]) for m in range(MONTHS)],
                          *[FadeIn(row[i]) for i in (1,3,5)],run_time=0.8)
                self.play(FadeIn(row[6]))
                sums.add(row)
            line = ('Low harvests maintain the stock.',
                    'A larger share today can leave fewer fish tomorrow.',
                    'Both firms empty the pond in the first month.')[profile_index]
            teaching = Tex(line,color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
            self.play(FadeIn(teaching))
            if profile_index == 0:
                self.pause('3.b')
            elif profile_index == 1:
                self.pause('3.c')
            else:
                self.pause('3.d')
            card = VGroup(Tex(profile,color=CAPTION),sums[0][6].copy(),Tex(r'$\mid$',color=MUTED),sums[1][6].copy())
            card.arrange(RIGHT,buff=0.16)
            card.set_height(0.28)
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
