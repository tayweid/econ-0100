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
        context = subtitle(head, 'One dot = 1,000 fish.')
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

        # Calculate graph and matrix data without animating the other runs.
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
        compact_center = np.array([-4.0,1.1,0])
        POND_POSITIONS = [(pos-POND_CENTER)*0.8+compact_center for pos in POND_POSITIONS]
        self.play(VGroup(pond,fish).animate.scale(0.8,about_point=POND_CENTER).move_to(compact_center),
                  stock_label.animate.move_to([-4,-0.3,0]))
        chart = axes([1,3,1],[0,10,5],x_length=5.8,y_length=3.4).move_to([3.5,0.2,0])
        chart_heading = Tex("Firm 1's catch (thousands)",color=CAPTION).scale(0.65).move_to([3.5,2.35,0])
        x_labels = VGroup(*[Tex(str(m),color=CAPTION).scale(0.6).next_to(chart.c2p(m,0),DOWN,buff=0.16) for m in (1,2,3)])
        y_labels = VGroup(*[Tex(str(q),color=CAPTION).scale(0.6).next_to(chart.c2p(1,q),LEFT,buff=0.16) for q in (0,5,10)])
        x_title = Tex('Month',color=INK).scale(0.65).next_to(chart,DOWN,buff=0.6)
        hl_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['H,L'][0])])
        point_values = VGroup(*[Tex(f'{q:g}',color=ROW_PLAYER).scale(0.65).next_to(dot,UP,buff=0.13)
                               for dot,q in zip(hl_dots,paths_data['H,L'][0])])
        names = VGroup(Tex('Firm 1: High',color=ROW_PLAYER),Tex('Firm 2: Low',color=COL_PLAYER))
        names[0].scale(0.65).move_to([-5.45,-0.65,0])
        names[1].scale(0.65).move_to([-2.55,-0.65,0])
        trays = VGroup(*[RoundedRectangle(width=2.3,height=0.8,corner_radius=0.2,color=MUTED,stroke_width=1)
                         .move_to([x,-1.3,0]) for x in (-5.45,-2.55)])
        choices = VGroup(Tex(r'$\frac12\times20=$',color=ROW_PLAYER),Tex(r'$\frac14\times20=$',color=COL_PLAYER))
        choices[0].scale(0.65).move_to([-5.7,-2.05,0])
        choices[1].scale(0.65).move_to([-2.8,-2.05,0])
        catch_values = VGroup(Tex('10',color=ROW_PLAYER),Tex('5',color=COL_PLAYER))
        for i in range(2):
            catch_values[i].scale(0.65).next_to(choices[i],RIGHT,buff=0.1)
        teaching = Tex('High takes twice as many fish as Low this month.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(names),FadeIn(trays),FadeIn(choices),FadeIn(catch_values),FadeIn(teaching),
                  Create(chart),FadeIn(chart_heading),FadeIn(x_labels),FadeIn(y_labels),FadeIn(x_title))
        self.pause('3.b.choices')

        # ---- 3.b.harvest · The actual dots supply the subtraction.
        caught_1, caught_2, survivors = VGroup(*fish[:10]), VGroup(*fish[10:15]), VGroup(*fish[15:])
        survivor_homes = [dot.get_center().copy() for dot in survivors]
        moves = []
        for firm,caught in enumerate((caught_1,caught_2)):
            for i,dot in enumerate(caught):
                moves.append(dot.animate.scale(0.8).set_color(FIRM_COLORS[firm])
                             .move_to([-6.15+firm*2.9+(i%5)*0.35,-1.12-(i//5)*0.36,0]))
        self.play(*moves,FadeOut(teaching),run_time=1.2)
        harvest_math = VGroup(*[Tex(t,color=c) for t,c in zip(
            ('20','$-$','10','$-$','5','=','5'),(INK,INK,ROW_PLAYER,INK,COL_PLAYER,INK,INK))])
        harvest_math.arrange(RIGHT,buff=0.15).scale(0.8).move_to([-4,-2.75,0])
        self.play(TransformFromCopy(stock_label[1],harvest_math[0]),
                  TransformFromCopy(catch_values[0],harvest_math[2]),TransformFromCopy(catch_values[1],harvest_math[4]),
                  *[FadeIn(harvest_math[i]) for i in (1,3,5,6)],
                  Transform(stock_label[1],Tex('5',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)))
        teaching = Tex('Five thousand survive. How many fish next month?',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(hl_dots[0]),TransformFromCopy(catch_values[0],point_values[0]),FadeIn(teaching))
        self.pause('3.b.harvest')

        # ---- 3.b.growth · Only offspring move; no second pond run.
        growth_math = VGroup(Tex(r'$\min\{20,\,2\times$',color=INK),Tex('5',color=INK),
                            Tex(r'$\}=$',color=INK),Tex('10',color=INK))
        growth_math.arrange(RIGHT,buff=0.1).scale(0.8).move_to([-4,-2.75,0])
        self.play(FadeOut(teaching),FadeIn(growth_math[0]),ReplacementTransform(harvest_math[6],growth_math[1]),FadeIn(growth_math[2]),
                  *[FadeOut(harvest_math[i]) for i in range(6)])
        babies = VGroup(*[dot.copy() for dot in survivors])
        self.add(babies)
        self.play(*[dot.animate.move_to(POND_POSITIONS[i]) for i,dot in enumerate(babies)],run_time=1.2)
        self.play(FadeIn(growth_math[3]),Transform(stock_label[1],
                  Tex('10',color=INK).scale(0.8).move_to(stock_label[1],aligned_edge=LEFT)))
        assert all(np.allclose(dot.get_center(),pos) for dot,pos in zip(survivors,survivor_homes))
        teaching = Tex('A smaller stock means a smaller catch next month.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.b.growth')

        # ---- 3.e.first · Predict the next catch on the same graph.
        forecast = VGroup(Tex(r'$\frac12\times$',color=ROW_PLAYER),Tex('10',color=INK),
                          Tex('=',color=ROW_PLAYER),Tex('5',color=ROW_PLAYER))
        forecast.arrange(RIGHT,buff=0.12).scale(0.75).move_to([3.5,-2.85,0])
        self.play(FadeOut(teaching),FadeIn(forecast[0]),TransformFromCopy(stock_label[1],forecast[1]),
                  FadeIn(forecast[2]),FadeIn(forecast[3]))
        hl_segments = VGroup(DashedLine(hl_dots[0].get_center(),hl_dots[1].get_center(),
                                       color=ROW_PLAYER,stroke_width=3,dash_length=0.16))
        teaching = Tex('Next month: half of 10 is 5.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(hl_dots[1]),TransformFromCopy(forecast[3],point_values[1]),
                  Create(hl_segments[0]),FadeIn(teaching))
        self.pause('3.e.first')

        # ---- 3.e.path · Expand the existing graph and complete the trend.
        chart_target = axes([1,3,1],[0,10,5],x_length=7,y_length=3.5).move_to([-2.3,-0.2,0])
        x_labels_target = VGroup(*[Tex(str(m),color=CAPTION).scale(0.7).next_to(chart_target.c2p(m,0),DOWN,buff=0.16) for m in (1,2,3)])
        y_labels_target = VGroup(*[Tex(str(q),color=CAPTION).scale(0.7).next_to(chart_target.c2p(1,q),LEFT,buff=0.16) for q in (0,5,10)])
        x_title_target = Tex('Month',color=INK).scale(0.75).next_to(chart_target,DOWN,buff=0.6)
        dots_target = VGroup(*[dot.copy().move_to(chart_target.c2p(m+1,q))
                              for m,(dot,q) in enumerate(zip(hl_dots,paths_data['H,L'][0]))])
        values_target = VGroup(*[value.copy().next_to(dot,UP,buff=0.13) for value,dot in zip(point_values,dots_target)])
        segment_target = DashedLine(dots_target[0].get_center(),dots_target[1].get_center(),
                                   color=ROW_PLAYER,stroke_width=3,dash_length=0.16)
        self.play(FadeOut(pond),FadeOut(fish),FadeOut(babies),FadeOut(stock_label),FadeOut(names),
                  FadeOut(trays),FadeOut(choices),FadeOut(catch_values),FadeOut(growth_math),FadeOut(forecast),
                  FadeOut(chart_heading),FadeOut(teaching),run_time=0.6)
        self.play(Transform(head,title('Catch Over Time')),
                  Transform(context,subtitle(head,"Firm 1's monthly catch, in thousands of fish.")),
                  Transform(chart,chart_target),Transform(x_labels,x_labels_target),Transform(y_labels,y_labels_target),
                  Transform(x_title,x_title_target),Transform(hl_segments[0],segment_target),
                  *[Transform(hl_dots[i],dots_target[i]) for i in (0,1)],
                  *[Transform(point_values[i],values_target[i]) for i in (0,1)])
        hl_dots[2].move_to(dots_target[2])
        point_values[2].move_to(values_target[2])
        hl_segments.add(DashedLine(hl_dots[1].get_center(),hl_dots[2].get_center(),
                                  color=ROW_PLAYER,stroke_width=3,dash_length=0.16))
        hl_label = Tex('H,L',color=CAPTION).scale(0.7).next_to(hl_dots[2],RIGHT,buff=0.25)
        teaching = Tex('High against Low: the stock halves, so the catch halves.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(hl_segments[1]),FadeIn(hl_dots[2]),FadeIn(point_values[2]),FadeIn(hl_label),FadeIn(teaching))
        self.pause('3.e.path')

        # ---- 3.e.total · Turn the three observations into one payoff.
        sum_rows = VGroup()
        for firm,values in enumerate(paths_data['H,L']):
            row = VGroup(*[Tex(t,color=FIRM_COLORS[firm]) for t in
                          (f'{values[0]:g}','+',f'{values[1]:g}','+',f'{values[2]:g}','=',f'{sum(values):g}')])
            row.arrange(RIGHT,buff=0.08).scale(0.65).move_to([4.9,0.8-firm*0.9,0])
            sum_rows.add(row)
        sum_heading = Tex('Total catch: H,L',color=INK).scale(0.8).move_to([4.9,1.8,0])
        result_cards = VGroup()
        for profile in ('L,L','H,L','H,H'):
            a,b = payoff_by_profile[profile]
            pair = VGroup(Tex(f'{a:g}',color=ROW_PLAYER),Tex(r'$\mid$',color=MUTED),Tex(f'{b:g}',color=COL_PLAYER))
            pair.arrange(RIGHT,buff=0.14).scale(0.8)
            card = VGroup(Tex(profile,color=CAPTION).scale(0.7),pair).arrange(DOWN,buff=0.2)
            result_cards.add(card)
        result_cards[0].move_to([4.9,1.4,0])
        result_cards[1].move_to([4.9,0,0])
        result_cards[2].move_to([4.9,-1.4,0])
        self.play(FadeIn(sum_heading),*[TransformFromCopy(point_values[i],sum_rows[0][2*i]) for i in range(3)],
                  *[FadeIn(sum_rows[0][i]) for i in (1,3,5,6)],FadeIn(sum_rows[1]),FadeOut(teaching))
        teaching = Tex('Add the three catches to get each firm\'s payoff.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.e.total')

        # ---- 3.e.low · Sustainable catch: one curve, one result pair.
        self.play(TransformFromCopy(sum_rows[0][6],result_cards[1][1][0]),
                  TransformFromCopy(sum_rows[1][6],result_cards[1][1][2]),
                  FadeIn(result_cards[1][0]),FadeIn(result_cards[1][1][1]),
                  FadeOut(sum_heading),FadeOut(sum_rows),FadeOut(point_values),FadeOut(teaching))
        self.add(result_cards[1])
        totals_heading = Tex('Three-month totals',color=INK).scale(0.8).move_to([4.9,2.3,0])
        ll_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['L,L'][0])])
        ll_line = Line(ll_dots[0].get_center(),ll_dots[2].get_center(),color=ROW_PLAYER,stroke_width=3)
        ll_label = Tex('L,L',color=CAPTION).scale(0.7).next_to(ll_dots[2],RIGHT,buff=0.25)
        teaching = Tex('Both Low: 5 each month, 15 each in total.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(totals_heading),Create(ll_line),FadeIn(ll_dots),FadeIn(ll_label),
                  FadeIn(result_cards[0]),FadeIn(teaching))
        self.pause('3.e.low')

        # ---- 3.e.high · Restore the earlier three-path figure.
        hh_dots = VGroup(*[Dot(chart.c2p(m+1,q),radius=0.065,color=ROW_PLAYER) for m,q in enumerate(paths_data['H,H'][0])])
        hh_segments = VGroup(*[DashedLine(hh_dots[i].get_center(),hh_dots[i+1].get_center(),color=ROW_PLAYER,
                                stroke_width=3,dash_length=0.045,dashed_ratio=0.3) for i in range(2)])
        hh_label = Tex('H,H',color=CAPTION).scale(0.7).next_to(hh_dots[2],RIGHT,buff=0.25)
        self.play(Create(hh_segments),FadeIn(hh_dots),FadeIn(hh_label),FadeIn(result_cards[2]),FadeOut(teaching))
        teaching = Tex('Both High: 10 now, then no fish left to catch.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.e.high')

        # Keep the calculated results as the graph gives way to the matrix.
        self.play(*[FadeOut(mob) for mob in self.mobjects if mob not in list(result_cards)])
        head = title('The Fishing Game')
        self.play(FadeIn(head),*[card.animate.move_to([-4.8+i*4.8,2.3,0]) for i,card in enumerate(result_cards)])

        # ---- 4.a · Carry actual totals into D1's diamond matrix.
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
        self.play(FadeIn(matrix.get_horizontal_lines()),FadeIn(matrix.get_vertical_lines()),
                  FadeIn(row_labels),FadeIn(col_labels),FadeIn(player_1),FadeIn(player_2),FadeIn(teaching))
        for card_index, (r,c) in enumerate(((0,0),(1,0),(1,1))):
            self.play(TransformFromCopy(result_cards[card_index][1],payoffs[r][c]),run_time=0.8)
            if card_index==1:
                self.play(TransformFromCopy(payoffs[1][0],payoffs[0][1]),run_time=0.8)
        self.play(FadeOut(result_cards))
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
        teaching = Tex('Tragedy of the commons: both would do better with Low.',color=DEFINITION)
        teaching.scale(TEACHING_SCALE).to_edge(DOWN,buff=TEACHING_BOTTOM).set_x(0)
        self.play(Create(efficient_box),FadeIn(comparison),FadeIn(teaching))
        self.pause('4.k')
