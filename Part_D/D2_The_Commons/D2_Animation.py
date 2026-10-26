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
        # The pond plus its stock readout shares the strategy panel's body center.
        POND_CENTER = np.array([-4.0, BODY_MID + 0.3, 0.0])
        # A fixed, gently scattered population: no jitter or rearrangement on birth.
        POND_POSITIONS = [POND_CENTER + np.array([x,y,0]) for x,y in (
            (0.10,0.66),(2.07,-0.45),(1.20,0.44),(0.73,-0.84),(-2.13,-0.25),
            (0.01,-0.39),(1.56,0.96),(-0.44,1.08),(-1.97,0.68),(-0.56,0.59),
            (-1.38,0.22),(0.25,0.12),(-0.68,-0.07),(1.03,-0.41),(1.85,-1.04),
            (2.07,0.19),(-0.49,-0.66),(-1.12,-0.75),(-1.75,-0.62),(1.54,0.08))]
        FIRM_COLORS = (ROW_PLAYER, COL_PLAYER)
        PRIOR_PATH_OPACITY = 0.25
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
        context = subtitle(head, 'Goods that are rival and non-excludable.')
        self.play(FadeIn(head), FadeIn(context), FadeIn(taxonomy))
        self.play(Create(box))
        self.pause('1.a')

        # ---- 3.a · Turn the simulation into a deliberately small strategic model.
        # Keep the pond and its actual population through the rules and first run.
        self.play(FadeOut(taxonomy),FadeOut(box),FadeOut(context),Transform(head,title('The Fishing Game')))
        pond = RoundedRectangle(width=5.4,height=2.8,corner_radius=0.8,color=INK,stroke_width=2).move_to(POND_CENTER)
        context = subtitle(head, 'One full dot = 1,000 fish.')
        fish = VGroup(*[Dot(radius=TOKEN_RADIUS,color=INK).move_to(pos) for pos in POND_POSITIONS])
        stock_label = VGroup(Tex('Stock:',color=INK),Tex('20',color=INK)).arrange(RIGHT,buff=0.15).scale(0.8).next_to(pond,DOWN,buff=0.2)
        strategies_heading = Tex('Two Strategies:',color=INK).scale(0.85)
        low_rule = VGroup(Tex('- Low Catch (L):',color=INK),Tex(r'$\frac14$ of the Stock',color=CAPTION))
        high_rule = VGroup(Tex('- High Catch (H):',color=INK),Tex(r'$\frac12$ of the Stock',color=CAPTION))
        low_rule.arrange(RIGHT,buff=0.18).scale(0.75)
        high_rule.arrange(RIGHT,buff=0.18).scale(0.75)
        rules = VGroup(strategies_heading,low_rule,high_rule)
        rules.arrange(DOWN,buff=0.55,aligned_edge=LEFT).move_to([4,BODY_MID,0])
        teaching = Tex('Maximize total catch over 3 months.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(pond),FadeIn(fish),FadeIn(stock_label),FadeIn(context),FadeIn(rules),FadeIn(teaching))
        self.pause('3.a')
        self.play(FadeOut(rules),FadeOut(teaching))

        # Calculate the three short runs and their matrix payoffs.
        paths_data = {}
        payoff_by_profile = {}
        for profile,a,b in (('L,L',LOW,LOW),('H,L',HIGH,LOW),('H,H',HIGH,HIGH)):
            stock = K
            catches = [[],[]]
            for month in range(MONTHS):
                h1,h2 = a*stock,b*stock
                catches[0].append(h1)
                catches[1].append(h2)
                stock = min(K,2*(stock-h1-h2))
            paths_data[profile] = catches
            payoff_by_profile[profile] = tuple(map(sum,catches))
        payoff_by_profile['L,H'] = payoff_by_profile['H,L'][::-1]

        # ---- 3.b.choices · One worked month: High against Low.
        # Every classroom hold is top-level, so ManimLive stops at each one.
        # Put month and stock on one header row, leaving space below the pond.
        compact_center = np.array([-4.0,0.9,0])
        CATCH_TOP = -1.27
        CATCH_ROW_GAP = 0.36
        POND_POSITIONS = [(pos-POND_CENTER)*0.8+compact_center for pos in POND_POSITIONS]
        self.play(VGroup(pond,fish).animate.scale(0.8,about_point=POND_CENTER).move_to(compact_center),
                  stock_label.animate.move_to([-2.95,2.5,0]))
        chart = axes([1,3,1],[0,10,5],x_length=5.8,y_length=3.4).move_to([3.5,0.2,0])
        month_label = Tex('Month 1',color=CAPTION).scale(0.6).move_to([-5.35,2.5,0])
        chart_heading = Tex("Firm 1's catch (thousands)",color=CAPTION).scale(0.65).move_to([3.5,2.35,0])
        x_labels = VGroup(*[Tex(str(m),color=CAPTION).scale(0.6).next_to(chart.c2p(m,0),DOWN,buff=0.16) for m in (1,2,3)])
        y_labels = VGroup(*[Tex(str(q),color=CAPTION).scale(0.6).next_to(chart.c2p(1,q),LEFT,buff=0.16) for q in (0,5,10)])
        x_title = Tex('Month',color=INK).scale(0.65).next_to(chart,DOWN,buff=0.6)
        hl_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['H,L'][0])])
        point_values = VGroup(*[Tex(f'{q:g}',color=ROW_PLAYER).scale(0.65).next_to(dot,UP,buff=0.13)
                               for dot,q in zip(hl_dots,paths_data['H,L'][0])])
        names = VGroup(Tex('Firm 1: High',color=ROW_PLAYER),Tex('Firm 2: Low',color=COL_PLAYER))
        names[0].scale(0.65).move_to([-5.45,-0.75,0])
        names[1].scale(0.65).move_to([-2.55,-0.75,0])
        trays = VGroup(*[RoundedRectangle(width=2.3,height=0.8,corner_radius=0.2,color=MUTED,stroke_width=1)
                         .move_to([x,-1.45,0]) for x in (-5.45,-2.55)])
        choices = VGroup(Tex(r'$\frac12\times20=$',color=ROW_PLAYER),Tex(r'$\frac14\times20=$',color=COL_PLAYER))
        choices[0].scale(0.65).move_to([-5.7,-2.2,0])
        choices[1].scale(0.65).move_to([-2.8,-2.2,0])
        catch_values = VGroup(Tex('10',color=ROW_PLAYER),Tex('5',color=COL_PLAYER))
        for i in range(2):
            catch_values[i].scale(0.65).next_to(choices[i],RIGHT,buff=0.1)
        teaching = Tex('High takes twice as many fish as Low this month.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(names),FadeIn(trays),FadeIn(choices),FadeIn(catch_values),FadeIn(teaching),
                  Create(chart),FadeIn(chart_heading),FadeIn(x_labels),FadeIn(y_labels),FadeIn(x_title),FadeIn(month_label))
        self.pause('3.b.choices')

        # ---- 3.b.harvest · Plot the catch, then clear the trays.
        caught_1, caught_2, survivors = VGroup(*fish[:10]), VGroup(*fish[10:15]), VGroup(*fish[15:])
        survivor_homes = [dot.get_center().copy() for dot in survivors]
        moves = []
        for firm,caught in enumerate((caught_1,caught_2)):
            for i,dot in enumerate(caught):
                moves.append(dot.animate.scale(0.8).set_color(FIRM_COLORS[firm])
                             .move_to([-6.15+firm*2.9+(i%5)*0.35,CATCH_TOP-(i//5)*CATCH_ROW_GAP,0]))
        self.play(*moves,FadeOut(teaching),run_time=1.2)
        self.play(Transform(stock_label[1],Tex('5',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.4)
        teaching = Tex('Five thousand survive. How many fish next month?',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(hl_dots[0]),TransformFromCopy(catch_values[0],point_values[0]),FadeIn(teaching))
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        self.pause('3.b.harvest')

        # ---- 3.b.growth · Each survivor spawns one dashed, translucent newborn.
        self.play(FadeOut(teaching),run_time=0.3)
        babies = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = babies
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-dot.get_center())
                    for i,(dot,edge) in enumerate(zip(newborns,newborn_edges))],
                  Transform(stock_label[1],Tex('10',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=1.2)
        assert all(np.allclose(dot.get_center(),pos) for dot,pos in zip(survivors,survivor_homes))
        teaching = Tex('Each fish spawns one new fish.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.b.growth')

        # ---- 3.e.first · Month 2: repeat the rule quickly, keeping the same fish.
        self.play(*[dot.animate.set_fill(opacity=1) for dot in newborns],FadeOut(newborn_edges),
                  FadeOut(teaching),
                  Transform(month_label,Tex('Month 2',color=CAPTION).scale(0.6).move_to(month_label)),
                  Transform(choices[0],Tex(r'$\frac12\times10=$',color=ROW_PLAYER).scale(0.65).move_to(choices[0])),
                  Transform(choices[1],Tex(r'$\frac14\times10=$',color=COL_PLAYER).scale(0.65).move_to(choices[1])),
                  Transform(catch_values[0],Tex('5',color=ROW_PLAYER).scale(0.65).move_to(catch_values[0],aligned_edge=LEFT)),
                  Transform(catch_values[1],Tex('2.5',color=COL_PLAYER).scale(0.65).move_to(catch_values[1],aligned_edge=LEFT)),run_time=0.4)
        # Split one thousand-fish dot into two halves, preserving its total area.
        half_caught = Sector(radius=TOKEN_RADIUS*0.8,angle=PI,start_angle=0,color=INK,arc_center=POND_POSITIONS[2])
        half_left = Sector(radius=TOKEN_RADIUS*0.8,angle=PI,start_angle=PI,color=INK,arc_center=POND_POSITIONS[2])
        self.remove(babies[2])
        self.add(half_caught,half_left)
        caught_1 = VGroup(*survivors)
        caught_2 = VGroup(babies[0],babies[1],half_caught)
        survivors = VGroup(babies[3],babies[4],half_left)
        moves = [dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+(i%5)*0.35,CATCH_TOP-(i//5)*CATCH_ROW_GAP,0])
                 for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)]
        hl_segments = VGroup(DashedLine(hl_dots[0].get_center(),hl_dots[1].get_center(),
                                       color=ROW_PLAYER,stroke_width=3,dash_length=0.16))
        self.play(*moves,FadeIn(hl_dots[1]),Create(hl_segments[0]),TransformFromCopy(catch_values[0],point_values[1]),
                  Transform(stock_label[1],Tex('2.5',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        offspring = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = offspring
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-POND_POSITIONS[j])
                    for dot,edge,i,j in zip(newborns,newborn_edges,(5,6,7),(3,4,2))],
                  Transform(stock_label[1],Tex('5',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.8)
        teaching = Tex('Less stock, smaller catches.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.first')

        # ---- 3.e.path · Month 3 completes H,L without leaving the pond.
        self.play(*[dot.animate.set_fill(opacity=1) for dot in newborns],FadeOut(newborn_edges),
                  FadeOut(teaching),
                  Transform(month_label,Tex('Month 3',color=CAPTION).scale(0.6).move_to(month_label)),
                  Transform(choices[0],Tex(r'$\frac12\times5=$',color=ROW_PLAYER).scale(0.65).move_to(choices[0])),
                  Transform(choices[1],Tex(r'$\frac14\times5=$',color=COL_PLAYER).scale(0.65).move_to(choices[1])),
                  Transform(catch_values[0],Tex('2.5',color=ROW_PLAYER).scale(0.65).move_to(catch_values[0],aligned_edge=LEFT)),
                  Transform(catch_values[1],Tex('1.25',color=COL_PLAYER).scale(0.65).move_to(catch_values[1],aligned_edge=LEFT)),run_time=0.4)
        quarter_caught = Sector(radius=TOKEN_RADIUS*0.8,angle=PI/2,start_angle=PI,color=INK,arc_center=POND_POSITIONS[7])
        quarter_left = Sector(radius=TOKEN_RADIUS*0.8,angle=PI/2,start_angle=3*PI/2,color=INK,arc_center=POND_POSITIONS[7])
        self.remove(offspring[2])
        self.add(quarter_caught,quarter_left)
        caught_1 = VGroup(*survivors)
        caught_2 = VGroup(offspring[0],quarter_caught)
        survivors = VGroup(offspring[1],quarter_left)
        moves = [dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+(i%5)*0.35,CATCH_TOP-(i//5)*CATCH_ROW_GAP,0])
                 for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)]
        hl_segments.add(DashedLine(hl_dots[1].get_center(),hl_dots[2].get_center(),
                                  color=ROW_PLAYER,stroke_width=3,dash_length=0.16))
        hl_label = Tex('H,L',color=CAPTION).scale(0.65).next_to(hl_dots[2],RIGHT,buff=0.2)
        self.play(*moves,FadeIn(hl_dots[2]),Create(hl_segments[1]),TransformFromCopy(catch_values[0],point_values[2]),
                  Transform(stock_label[1],Tex('1.25',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        offspring = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = offspring
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-POND_POSITIONS[j])
                    for dot,edge,i,j in zip(newborns,newborn_edges,(8,9),(6,7))],
                  Transform(stock_label[1],Tex('2.5',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),FadeIn(hl_label),run_time=0.8)
        teaching = Tex('High against Low: the stock halves, so the catch halves.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.path')

        # ---- 3.e.total · Carry the plotted catches into their three-month payoff.
        sum_rows = VGroup()
        for firm,values in enumerate(paths_data['H,L']):
            row = VGroup(*[Tex(t,color=FIRM_COLORS[firm]) for t in
                          (f'{values[0]:g}','+',f'{values[1]:g}','+',f'{values[2]:g}','=',f'{sum(values):g}')])
            row.arrange(RIGHT,buff=0.08).scale(0.6).move_to([3.5,-2.65-firm*0.5,0])
            sum_rows.add(row)
        result_cards = VGroup()
        for profile in ('L,L','H,L','H,H'):
            a,b = payoff_by_profile[profile]
            pair = VGroup(Tex(f'{a:g}',color=ROW_PLAYER),Tex(r'$\mid$',color=MUTED),Tex(f'{b:g}',color=COL_PLAYER))
            pair.arrange(RIGHT,buff=0.14).scale(0.8)
            card = VGroup(Tex(profile,color=CAPTION).scale(0.7),pair).arrange(DOWN,buff=0.2)
            result_cards.add(card)
        self.play(*[TransformFromCopy(point_values[i],sum_rows[0][2*i]) for i in range(3)],
                  *[FadeIn(sum_rows[0][i]) for i in (1,3,5,6)],FadeIn(sum_rows[1]),FadeOut(teaching),run_time=0.7)
        teaching = Tex('Add the three catches to get each firm\'s payoff.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.total')
        # Save the actual sum results for the later comparison and matrix.
        result_cards[1].move_to([3.5,-2.85,0])
        self.play(TransformFromCopy(sum_rows[0][6],result_cards[1][1][0]),
                  TransformFromCopy(sum_rows[1][6],result_cards[1][1][2]),
                  FadeIn(result_cards[1][0]),FadeIn(result_cards[1][1][1]),FadeOut(sum_rows),run_time=0.5)
        self.add(result_cards[1])

        # ---- 3.e.low.first · New scenario: reset once, then run all three months.
        self.play(FadeOut(survivors),FadeOut(offspring),FadeOut(newborn_edges),
                  FadeOut(teaching),FadeOut(result_cards[1]),FadeOut(point_values),
                  VGroup(hl_dots,hl_segments,hl_label).animate.set_opacity(PRIOR_PATH_OPACITY),
                  Transform(names[0],Tex('Firm 1: Low',color=ROW_PLAYER).scale(0.65).move_to(names[0])),
                  Transform(month_label,Tex('Month 1',color=CAPTION).scale(0.6).move_to(month_label)),
                  Transform(stock_label[1],Tex('20',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.5)
        fish = VGroup(*[Dot(radius=TOKEN_RADIUS*0.8,color=INK).move_to(pos) for pos in POND_POSITIONS])
        ll_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['L,L'][0])])
        ll_segments = VGroup(*[Line(ll_dots[i].get_center(),ll_dots[i+1].get_center(),color=ROW_PLAYER,stroke_width=3) for i in range(2)])
        ll_label = Tex('L,L',color=CAPTION).scale(0.65).next_to(ll_dots[2],RIGHT,buff=0.2)
        self.play(FadeIn(fish),
                  *[Transform(choices[i],Tex(r'$\frac14\times20=$',color=FIRM_COLORS[i]).scale(0.65).move_to(choices[i])) for i in range(2)],
                  *[Transform(catch_values[i],Tex('5',color=FIRM_COLORS[i]).scale(0.65).move_to(catch_values[i],aligned_edge=LEFT)) for i in range(2)],run_time=0.4)
        caught_1, caught_2, survivors = VGroup(*fish[:5]),VGroup(*fish[5:10]),VGroup(*fish[10:])
        self.play(*[dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+i*0.35,CATCH_TOP,0])
                    for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)],
                  Transform(stock_label[1],Tex('10',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),
                  FadeIn(ll_dots[0]),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        offspring = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = offspring
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-dot.get_center())
                    for i,(dot,edge) in enumerate(zip(newborns,newborn_edges))],
                  Transform(stock_label[1],Tex('20',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.8)
        teaching = Tex('Both Low: the stock returns to 20.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.low.first')

        # ---- 3.e.low.second · Both Low, month 2.
        self.play(*[dot.animate.set_fill(opacity=1) for dot in newborns],FadeOut(newborn_edges),
                  FadeOut(teaching),
                  Transform(month_label,Tex('Month 2',color=CAPTION).scale(0.6).move_to(month_label)),run_time=0.3)
        caught_1, caught_2 = VGroup(*offspring[:5]),VGroup(*offspring[5:])
        self.play(*[dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+i*0.35,CATCH_TOP,0])
                    for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)],
                  Transform(stock_label[1],Tex('10',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),
                  FadeIn(ll_dots[1]),Create(ll_segments[0]),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        offspring = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = offspring
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-dot.get_center())
                    for i,(dot,edge) in enumerate(zip(newborns,newborn_edges))],
                  Transform(stock_label[1],Tex('20',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.8)
        teaching = Tex('The same catch, again.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.low.second')

        # ---- 3.e.low · Both Low, month 3.
        self.play(*[dot.animate.set_fill(opacity=1) for dot in newborns],FadeOut(newborn_edges),
                  FadeOut(teaching),
                  Transform(month_label,Tex('Month 3',color=CAPTION).scale(0.6).move_to(month_label)),run_time=0.3)
        caught_1, caught_2 = VGroup(*offspring[:5]),VGroup(*offspring[5:])
        self.play(*[dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+i*0.35,CATCH_TOP,0])
                    for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)],
                  Transform(stock_label[1],Tex('10',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),
                  FadeIn(ll_dots[2]),Create(ll_segments[1]),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        offspring = VGroup(*[dot.copy().set_fill(opacity=0.3) for dot in survivors])
        newborns = offspring
        newborn_edges = VGroup(*[DashedVMobject(dot.copy().set_fill(opacity=0)
                                    .set_stroke(INK,width=1.5,opacity=0.85),num_dashes=8)
                                  for dot in newborns])
        self.add(newborns,newborn_edges)
        self.play(*[VGroup(dot,edge).animate.shift(POND_POSITIONS[i]-dot.get_center())
                    for i,(dot,edge) in enumerate(zip(newborns,newborn_edges))],
                  Transform(stock_label[1],Tex('20',color=INK).scale(0.8)
                            .move_to(stock_label[1],aligned_edge=LEFT)),run_time=0.8)
        result_cards[0].move_to([3.5,-2.85,0])
        self.play(FadeIn(ll_label),FadeIn(result_cards[0]),run_time=0.3)
        teaching = Tex('Both Low: 5 each month, 15 each in total.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.low')

        # ---- 3.e.high.first · Both High removes the entire stock in month 1.
        self.play(FadeOut(survivors),FadeOut(offspring),FadeOut(newborn_edges),
                  FadeOut(teaching),FadeOut(result_cards[0]),
                  VGroup(ll_dots,ll_segments,ll_label).animate.set_opacity(PRIOR_PATH_OPACITY),
                  *[Transform(names[i],Tex(f'Firm {i+1}: High',color=FIRM_COLORS[i]).scale(0.65).move_to(names[i])) for i in range(2)],
                  Transform(month_label,Tex('Month 1',color=CAPTION).scale(0.6).move_to(month_label)),run_time=0.5)
        fish = VGroup(*[Dot(radius=TOKEN_RADIUS*0.8,color=INK).move_to(pos) for pos in POND_POSITIONS])
        hh_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['H,H'][0])])
        hh_segments = VGroup(*[DashedLine(hh_dots[i].get_center(),hh_dots[i+1].get_center(),color=ROW_PLAYER,
                                stroke_width=3,dash_length=0.045,dashed_ratio=0.3) for i in range(2)])
        hh_label = Tex('H,H',color=CAPTION).scale(0.65).next_to(hh_dots[2],RIGHT,buff=0.2)
        self.play(FadeIn(fish),
                  *[Transform(choices[i],Tex(r'$\frac12\times20=$',color=FIRM_COLORS[i]).scale(0.65).move_to(choices[i])) for i in range(2)],
                  *[Transform(catch_values[i],Tex('10',color=FIRM_COLORS[i]).scale(0.65).move_to(catch_values[i],aligned_edge=LEFT)) for i in range(2)],run_time=0.4)
        caught_1, caught_2 = VGroup(*fish[:10]),VGroup(*fish[10:])
        self.play(*[dot.animate.scale(0.8).set_color(FIRM_COLORS[firm]).move_to(
                    [-6.15+firm*2.9+(i%5)*0.35,CATCH_TOP-(i//5)*CATCH_ROW_GAP,0])
                    for firm,caught in enumerate((caught_1,caught_2)) for i,dot in enumerate(caught)],
                  Transform(stock_label[1],Tex('0',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)),FadeIn(hh_dots[0]),run_time=0.6)
        self.play(FadeOut(caught_1),FadeOut(caught_2),run_time=0.25)
        teaching = Tex('Both High: nothing left to reproduce.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.high.first')

        # ---- 3.e.high.second · Month 2: empty pond, zero catch.
        self.play(FadeOut(teaching),
                  Transform(month_label,Tex('Month 2',color=CAPTION).scale(0.6).move_to(month_label)),
                  *[Transform(choices[i],Tex(r'$\frac12\times0=$',color=FIRM_COLORS[i]).scale(0.65).move_to(choices[i])) for i in range(2)],
                  *[Transform(catch_values[i],Tex('0',color=FIRM_COLORS[i]).scale(0.65).move_to(catch_values[i],aligned_edge=LEFT)) for i in range(2)],
                  FadeIn(hh_dots[1]),Create(hh_segments[0]),run_time=0.6)
        teaching = Tex('No stock, no catch.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.high.second')

        # ---- 3.e.high · Month 3: no recovery; complete the third line.
        result_cards[2].move_to([3.5,-2.85,0])
        self.play(Transform(month_label,Tex('Month 3',color=CAPTION).scale(0.6).move_to(month_label)),
                  FadeIn(hh_dots[2]),Create(hh_segments[1]),FadeIn(hh_label),FadeIn(result_cards[2]),FadeOut(teaching),run_time=0.6)
        teaching = Tex('Both High: 10 now, then no fish left to catch.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching),run_time=0.3)
        self.pause('3.e.high')

        # ---- 3.e.compare · Expand all three existing paths; carry their totals forward.
        chart_target = axes([1,3,1],[0,10,5],x_length=7,y_length=3.5).move_to([-2.3,-0.2,0])
        x_labels_target = VGroup(*[Tex(str(m),color=CAPTION).scale(0.7).next_to(chart_target.c2p(m,0),DOWN,buff=0.16) for m in (1,2,3)])
        y_labels_target = VGroup(*[Tex(str(q),color=CAPTION).scale(0.7).next_to(chart_target.c2p(1,q),LEFT,buff=0.16) for q in (0,5,10)])
        x_title_target = Tex('Month',color=INK).scale(0.75).next_to(chart_target,DOWN,buff=0.6)
        # One affine motion keeps every point, segment, and endpoint label together.
        plot = VGroup(chart,x_labels,y_labels,x_title,hl_dots,hl_segments,hl_label,
                      ll_dots,ll_segments,ll_label,hh_dots,hh_segments,hh_label)
        plot_target = plot.copy()
        plot_target.stretch(7/5.8,0,about_point=chart.get_center()).stretch(3.5/3.4,1,about_point=chart.get_center())
        plot_target.shift(chart_target.get_center()-chart.get_center())
        # Preserve circular markers and normal letter proportions during expansion.
        for dots_index,label_index in ((4,6),(7,9),(10,12)):
            for source,target in zip(plot[dots_index],plot_target[dots_index]):
                target.become(source.copy().move_to(target.get_center()))
            plot_target[label_index].become(plot[label_index].copy().scale(0.7/0.65)
                                           .next_to(plot_target[dots_index][2],RIGHT,buff=0.25))
        # Keep axis typography undistorted at its full-graph size.
        plot_target[1].become(x_labels_target)
        plot_target[2].become(y_labels_target)
        plot_target[3].become(x_title_target)
        # Restore equal emphasis when comparing all three completed scenarios.
        for path_part in plot_target[4:]:
            path_part.set_opacity(1)
        self.play(FadeOut(pond),FadeOut(stock_label),FadeOut(names),FadeOut(trays),FadeOut(choices),
                  FadeOut(catch_values),FadeOut(month_label),FadeOut(chart_heading),FadeOut(teaching),run_time=0.4)
        self.play(Transform(head,title('Catch Over Time')),
                  Transform(context,subtitle(head,"Firm 1's monthly catch, in thousands of fish.")),Transform(plot,plot_target),
                  result_cards[2].animate.move_to([4.9,-1.4,0]),run_time=0.8)
        result_cards[0].move_to([4.9,1.4,0])
        result_cards[1].move_to([4.9,0,0])
        totals_heading = Tex('Three-month totals',color=INK).scale(0.8).move_to([4.9,2.3,0])
        teaching = Tex('Three paths, three payoff pairs.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(result_cards[0]),FadeIn(result_cards[1]),FadeIn(totals_heading),FadeIn(teaching),run_time=0.4)
        self.pause('3.e.compare')

        # ---- 4.a · Move totals straight from the graph into the completed matrix.
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
        matrix_teaching=Tex("Firm 1's payoff first; Firm 2's payoff second.",color=DEFINITION)
        matrix_teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        # Grid and values arrive together; no payoff-card row or empty-matrix stage.
        self.play(FadeOut(plot),FadeOut(context),FadeOut(totals_heading),FadeOut(teaching),
                  Transform(head,title('The Fishing Game')),
                  FadeIn(matrix.get_horizontal_lines()),FadeIn(matrix.get_vertical_lines()),
                  FadeIn(row_labels),FadeIn(col_labels),FadeIn(player_1),FadeIn(player_2),FadeIn(matrix_teaching),
                  *[FadeOut(card[0]) for card in result_cards],
                  ReplacementTransform(result_cards[0][1],payoffs[0][0]),
                  ReplacementTransform(result_cards[1][1],payoffs[1][0]),
                  ReplacementTransform(result_cards[2][1],payoffs[1][1]),
                  TransformFromCopy(result_cards[1][1][2],payoffs[0][1][0]),
                  TransformFromCopy(result_cards[1][1][0],payoffs[0][1][2]),
                  FadeIn(payoffs[0][1][1]),run_time=1.2)
        self.add(*entries)
        teaching = matrix_teaching
        self.pause('4.a')

        # ---- 4.b–4.f · Two comparisons, then symmetry.
        responses = VGroup()
        self.play(FadeOut(teaching))
        shade = Rectangle(width=CELL_SIDE,height=2*CELL_SIDE,stroke_width=0,fill_color=COL_PLAYER,fill_opacity=0.12)
        shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER+(0-0.5)*CELL_SIDE*TABLE_RIGHT).set_z_index(-1)
        underline = Underline(col_labels[0],buff=0.1,stroke_color=COL_PLAYER,stroke_width=3,stretch_factor=1)
        teaching = Tex("If Firm 2 chooses Low, what is Firm 1's best response?",color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(shade),FadeIn(underline),FadeIn(teaching))
        self.pause('4.b')
        response = SurroundingRectangle(payoffs[1][0][0],buff=0.08,color=ROW_PLAYER)
        responses.add(response)
        self.play(FadeOut(teaching),Create(response))
        teaching = Tex(r'High: $17.5 > 15$.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('4.c')
        self.play(FadeOut(shade),FadeOut(underline),FadeOut(teaching))
        shade = Rectangle(width=CELL_SIDE,height=2*CELL_SIDE,stroke_width=0,fill_color=COL_PLAYER,fill_opacity=0.12)
        shade.rotate(DIAMOND_ANGLE).move_to(GAME_CENTER+(1-0.5)*CELL_SIDE*TABLE_RIGHT).set_z_index(-1)
        underline = Underline(col_labels[1],buff=0.1,stroke_color=COL_PLAYER,stroke_width=3,stretch_factor=1)
        teaching = Tex("If Firm 2 chooses High, what is Firm 1's best response?",color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(shade),FadeIn(underline),FadeIn(teaching))
        self.pause('4.d')
        response = SurroundingRectangle(payoffs[1][1][0],buff=0.08,color=ROW_PLAYER)
        responses.add(response)
        self.play(FadeOut(teaching),Create(response))
        teaching = Tex(r'High: $10 > 8.75$.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('4.e')
        self.play(FadeOut(shade),FadeOut(underline),FadeOut(teaching))
        firm_2_responses = VGroup(*[SurroundingRectangle(payoffs[r][1][2],buff=0.08,color=COL_PLAYER) for r in (0,1)])
        teaching = Tex('The same comparisons hold for Firm 2. Both prefer High.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(firm_2_responses),FadeIn(teaching))
        self.pause('4.f')

        # ---- 4.j · Unilateral-deviation test, then Nash.
        self.remove(shade,underline,teaching)
        nash_box=Square(side_length=CELL_SIDE-0.15,color=NASH,stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[1][1])
        teaching=Tex('Neither firm gains by changing its strategy alone.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(nash_box),FadeIn(teaching))
        self.pause('4.j')

        # ---- 4.k · End on the incentive conflict.
        self.play(FadeOut(teaching))
        efficient_box = Square(side_length=CELL_SIDE-0.15,color=EFFICIENT,stroke_width=3).rotate(DIAMOND_ANGLE).move_to(payoffs[0][0])
        comparison = Tex(r'$15 > 10$ for each firm.',color=INK).scale(0.85).move_to([4.8,0,0])
        teaching = VGroup(
            Tex('Tragedy of the commons',color=DEFINITION).scale(TEACHING_SCALE),
            Tex('Individual incentives lead to overuse of a rival, non-excludable resource:',color=INK).scale(0.65),
            Tex('each user benefits from extra use but bears only part of its total cost.',color=INK).scale(0.65),
        ).arrange(DOWN,buff=0.12).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(efficient_box),FadeIn(comparison),FadeIn(teaching))
        self.pause('4.k')
