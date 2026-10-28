# maniml D3_Animation.py EpisodeD3
# First classroom draft: NPR -> Dobby -> voting. See 02_Storyboard.md.
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


class EpisodeD3(Scene):
    default_camera_config = {'fps': 15}

    def construct(self):
        self.camera.fps = 15
        BODY_TOP, BODY_BOTTOM = 2.5, -2.8
        BODY_MID = (BODY_TOP + BODY_BOTTOM) / 2
        TEACHING_SCALE = 0.7443
        CELL_SIDE = 1.5
        GAME_CENTER = np.array([3.9, -0.2, 0])
        TABLE_RIGHT, TABLE_UP = (RIGHT+DOWN)/2**0.5, (RIGHT+UP)/2**0.5
        ENDOWMENT, RETURN = 15, 2/3
        npr_payoffs = [[(20,20),(10,25)],[(25,10),(15,15)]]
        residents = ('Harry','Ron','Hermione','Ginny','Neville')  # Oct. 30 PDF names.
        benefits = (34,29,24,19,14)
        cost = 100

        # 1 · NPR. The same two players, same diamond, and same response colors as D2.
        head = title('The NPR Game')
        context = subtitle(head, 'Public goods are non-rival and non-excludable.')
        trays = VGroup(*[RoundedRectangle(width=2.1,height=0.85,corner_radius=0.18,
                     color=MUTED,stroke_width=2).move_to([x,1.25,0]) for x in (-5.6,-2.5)])
        names = VGroup(*[Tex(f'Player {i+1}',color=c).scale(0.75).next_to(tray,DOWN,buff=0.2)
                     for i,(c,tray) in enumerate(zip((ROW_PLAYER,COL_PLAYER),trays))])
        money = VGroup(*[Tex('15',color=c).scale(0.85).move_to(tray)
                     for c,tray in zip((ROW_PLAYER,COL_PLAYER),trays)])
        kept_heading = Tex('Money kept',color=CAPTION).scale(0.65).move_to([-4.05,2.15,0])
        fund = RoundedRectangle(width=3.2,height=0.85,corner_radius=0.18,color=MUTED,stroke_width=2).move_to([-4.05,-1.6,0])
        fund_name = Tex('Broadcast fund',color=INK).scale(0.75).next_to(fund,DOWN,buff=0.2)
        fund_value = Tex('0',color=INK).scale(0.85).move_to(fund)
        rules = VGroup(Tex('Two Strategies:',color=INK).scale(0.85),
            VGroup(Tex('Contribute (C):'),Tex('15',color=CAPTION)).arrange(RIGHT,buff=0.18).scale(0.75),
            VGroup(Tex('Do not contribute (DC):'),Tex('0',color=CAPTION)).arrange(RIGHT,buff=0.18).scale(0.75)
        ).arrange(DOWN,buff=0.5,aligned_edge=LEFT).move_to([3.65,BODY_MID,0])
        teaching = Tex('Everyone can listen, whether or not they contribute.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(trays),FadeIn(names),FadeIn(money),FadeIn(kept_heading),FadeIn(fund),FadeIn(fund_name),FadeIn(fund_value),FadeIn(rules),FadeIn(teaching))
        self.pause('1.a.rules')

        self.play(FadeOut(teaching))
        teaching = Tex('Each 15 contributed creates a benefit of 10 for each player.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        gift = money[0].copy()
        self.add(gift)
        self.play(gift.animate.move_to(fund),Transform(money[0],Tex('0',color=ROW_PLAYER).scale(0.85).move_to(trays[0])),FadeOut(fund_value),FadeIn(teaching))
        self.remove(gift)
        fund_value = Tex('15',color=INK).scale(0.85).move_to(fund)
        self.add(fund_value)
        benefit_labels = VGroup(*[VGroup(Tex('Benefit:',color=CAPTION),Tex('10',color=c)).arrange(RIGHT,buff=0.15).scale(0.65).move_to([x,-0.15,0])
                                  for x,c in zip((-5.6,-2.5),(ROW_PLAYER,COL_PLAYER))])
        self.play(TransformFromCopy(fund_value,benefit_labels[0]),TransformFromCopy(fund_value,benefit_labels[1]))
        self.pause('1.b.benefits')

        self.play(FadeOut(rules),FadeOut(teaching))
        ledger = VGroup(
            Tex('Payoff = money kept + benefit',color=CAPTION).scale(0.65).move_to([3.8,1.4,0]),
            VGroup(MathTex('0+10=',color=ROW_PLAYER),Tex('10',color=ROW_PLAYER)).arrange(RIGHT,buff=0.1).scale(0.85).move_to([3.8,0.4,0]),
            VGroup(MathTex('15+10=',color=COL_PLAYER),Tex('25',color=COL_PLAYER)).arrange(RIGHT,buff=0.1).scale(0.85).move_to([3.8,-0.55,0]))
        teaching = Tex('What does each player receive?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.c.question')
        self.play(FadeIn(ledger))
        self.pause('1.d.payoffs')

        payoffs = [[VGroup(Tex(str(a),color=ROW_PLAYER),Tex(r'$\mid$',color=MUTED),Tex(str(b),color=COL_PLAYER)).arrange(RIGHT,buff=0.12).scale(0.7)
                    for a,b in row] for row in npr_payoffs]
        entries = [cell for row in payoffs for cell in row]
        matrix = Table(payoffs,h_buff=CELL_SIDE-max(c.width for c in entries),v_buff=CELL_SIDE-max(c.height for c in entries),include_outer_lines=True,
                       line_config={'color':MUTED,'stroke_width':2}).rotate(-PI/4).move_to(GAME_CENTER)
        for cell in entries:
            cell.rotate(PI/4,about_point=cell.get_center())
        row_labels = VGroup(*[Tex(s,color=CAPTION).scale(0.7) for s in ('C','DC')])
        col_labels = VGroup(*[Tex(s,color=CAPTION).scale(0.7) for s in ('C','DC')])
        for i in range(2):
            offset = (0.5-i)*CELL_SIDE
            row_labels[i].move_to(GAME_CENTER-CELL_SIDE*TABLE_RIGHT+offset*TABLE_UP+LEFT*0.3,aligned_edge=RIGHT)
            col_labels[i].move_to(GAME_CENTER-offset*TABLE_RIGHT+CELL_SIDE*TABLE_UP+RIGHT*0.3,aligned_edge=LEFT)
        player_labels = VGroup(Tex('Player 1',color=ROW_PLAYER).scale(0.8).move_to([1.9,2.15,0]),Tex('Player 2',color=COL_PLAYER).scale(0.8).move_to([5.9,2.15,0]))
        divider = Line([0,2.5,0],[0,-2.7,0],color=MUTED,stroke_width=1)
        self.play(FadeOut(teaching),FadeOut(ledger[0]),FadeIn(matrix.get_horizontal_lines()),FadeIn(matrix.get_vertical_lines()),FadeIn(row_labels),FadeIn(col_labels),FadeIn(player_labels),Create(divider),
                  FadeOut(ledger[1][0]),FadeOut(ledger[2][0]),ReplacementTransform(ledger[1][1],payoffs[0][1][0]),ReplacementTransform(ledger[2][1],payoffs[0][1][2]),FadeIn(payoffs[0][1][1]))
        self.add(payoffs[0][1])
        teaching = Tex('Contribute, do not contribute: 10 and 25.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.e.matrix')

        # Change only the numbers; the fund, players, and benefit labels persist.
        self.play(FadeOut(teaching),Transform(money[0],Tex('15',color=ROW_PLAYER).scale(0.85).move_to(trays[0])),
                  Transform(fund_value,Tex('0').scale(0.85).move_to(fund)),
                  *[Transform(label[1],Tex('0',color=c).scale(0.65).move_to(label[1])) for label,c in zip(benefit_labels,(ROW_PLAYER,COL_PLAYER))])
        teaching = Tex('Nobody contributes: each keeps 15.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(TransformFromCopy(money[0],payoffs[1][1][0]),TransformFromCopy(money[1],payoffs[1][1][2]),FadeIn(payoffs[1][1][1]),FadeIn(teaching))
        self.add(payoffs[1][1])
        self.pause('1.f.neither')

        self.play(FadeOut(teaching),*[Transform(m,Tex('0',color=c).scale(0.85).move_to(tray)) for m,c,tray in zip(money,(ROW_PLAYER,COL_PLAYER),trays)],
                  Transform(fund_value,Tex('30').scale(0.85).move_to(fund)),
                  *[Transform(label[1],Tex('20',color=c).scale(0.65).move_to(label[1])) for label,c in zip(benefit_labels,(ROW_PLAYER,COL_PLAYER))])
        teaching = Tex('Both contribute: each receives 20.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(*[TransformFromCopy(benefit_labels[i][1],payoffs[0][0][2*i]) for i in (0,1)],FadeIn(payoffs[0][0][1]),FadeIn(teaching))
        self.add(payoffs[0][0])
        self.pause('1.g.both')
        self.play(FadeOut(teaching),Transform(money[0],Tex('15',color=ROW_PLAYER).scale(0.85).move_to(trays[0])),
                  Transform(fund_value,Tex('15').scale(0.85).move_to(fund)),
                  *[Transform(label[1],Tex('10',color=c).scale(0.65).move_to(label[1])) for label,c in zip(benefit_labels,(ROW_PLAYER,COL_PLAYER))],
                  TransformFromCopy(payoffs[0][1][2],payoffs[1][0][0]),TransformFromCopy(payoffs[0][1][0],payoffs[1][0][2]),FadeIn(payoffs[1][0][1]))
        self.add(payoffs[1][0])
        teaching = Tex('Switch the contributor; switch the payoffs.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.h.symmetry')

        # Remove the now-unused fund; keep a simple incentive statement on the left.
        self.play(*[FadeOut(o) for o in (trays,names,money,kept_heading,fund,fund_name,fund_value,benefit_labels,teaching)])
        incentive = VGroup(Tex('Contributing 15',color=INK).scale(0.85),Tex('Own benefit: 10',color=ROW_PLAYER).scale(0.8),Tex('Benefit to the other player: 10',color=COL_PLAYER).scale(0.7)).arrange(DOWN,buff=0.5).move_to([-4,BODY_MID,0])
        shade = Rectangle(width=CELL_SIDE,height=2*CELL_SIDE,stroke_width=0,fill_color=COL_PLAYER,fill_opacity=0.12).rotate(-PI/4).move_to(GAME_CENTER-0.5*CELL_SIDE*TABLE_RIGHT).set_z_index(-1)
        teaching = Tex('If Player 2 contributes, what is Player 1\'s best response?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(incentive),FadeIn(shade),FadeIn(teaching))
        self.pause('1.i.response-c')
        br1 = SurroundingRectangle(payoffs[1][0][0],buff=0.08,color=ROW_PLAYER)
        self.play(FadeOut(teaching),Create(br1))
        teaching = Tex(r'Do not contribute: $25>20$.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.j.answer-c')
        self.play(FadeOut(teaching),shade.animate.shift(CELL_SIDE*TABLE_RIGHT))
        teaching = Tex('If Player 2 does not contribute, what is the best response?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.k.response-dc')
        br2 = SurroundingRectangle(payoffs[1][1][0],buff=0.08,color=ROW_PLAYER)
        self.play(FadeOut(teaching),Create(br2))
        teaching = Tex(r'Do not contribute: $15>10$.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.l.answer-dc')
        other_responses = VGroup(*[SurroundingRectangle(payoffs[r][1][2],buff=0.08,color=COL_PLAYER) for r in (0,1)])
        nash = Square(side_length=1.35,color=NASH,stroke_width=3).rotate(-PI/4).move_to(payoffs[1][1])
        efficient = Square(side_length=1.35,color=EFFICIENT,stroke_width=3).rotate(-PI/4).move_to(payoffs[0][0])
        self.play(FadeOut(shade),FadeOut(teaching),Create(other_responses),Create(nash))
        teaching = Tex('Neither contributes. Neither gains by changing alone.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.m.nash')
        self.play(FadeOut(teaching),Create(efficient))
        teaching = VGroup(Tex('The free rider problem',color=DEFINITION).scale(TEACHING_SCALE),
             Tex('People can benefit without contributing, so individual incentives',color=INK).scale(0.65),
             Tex('can leave a non-rival, non-excludable good underprovided.',color=INK).scale(0.65)).arrange(DOWN,buff=0.12).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('1.n.free-rider')

        # 2 · The PDF's three-player extension: one short calculation, no extra matrix.
        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title('Three Contributors')
        context = subtitle(head,'Each player still has 15. Each contribution of 15 benefits everyone by 10.')
        formula = MathTex(r'u_i=15-c_i+\frac{2}{3}(c_1+c_2+c_3)').scale(0.9).move_to([0,1.7,0])
        three_names = VGroup(*[Tex(f'Player {i+1}',color=c).scale(0.8).move_to([x,0.65,0]) for i,(x,c) in enumerate(zip((-4,0,4),(ROW_PLAYER,COL_PLAYER,PURPLE)))])
        choices = VGroup(*[Tex(s,color=CAPTION).scale(0.75).move_to([x,-0.25,0]) for x,s in zip((-4,0,4),('C: 15','DC: 0','DC: 0'))])
        three_values = VGroup(*[Tex(str(v),color=c).scale(1.1).move_to([x,-1.2,0]) for x,v,c in zip((-4,0,4),(10,25,25),(ROW_PLAYER,COL_PLAYER,PURPLE))])
        teaching = Tex('One contributor: 10 for them, 25 for each of the others.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(formula),FadeIn(three_names),FadeIn(choices),FadeIn(three_values),FadeIn(teaching))
        self.pause('2.a.one')
        self.play(FadeOut(teaching),Transform(choices[0],Tex('DC: 0',color=CAPTION).scale(0.75).move_to(choices[0])),
                  *[Transform(v,Tex('15',color=c).scale(1.1).move_to(v)) for v,c in zip(three_values,(ROW_PLAYER,COL_PLAYER,PURPLE))])
        teaching = Tex('Nobody contributes: 15 each. Total payoff: 45.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('2.b.none')
        self.play(FadeOut(teaching),*[Transform(ch,Tex('C: 15',color=CAPTION).scale(0.75).move_to(ch)) for ch in choices],
                  *[Transform(v,Tex('30',color=c).scale(1.1).move_to(v)) for v,c in zip(three_values,(ROW_PLAYER,COL_PLAYER,PURPLE))])
        teaching = Tex('Everybody contributes: 30 each. Total payoff: 90.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('2.c.all')

        # 3 · Dobby. The same benefit bars remain through votes, efficiency, and fees.
        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title('A Memorial To Dobby')
        context = subtitle(head,'Annual benefits and costs, in galleons. Everyone can enjoy the memorial.')
        chart = axes([0,6,1],[0,40,10],x_length=6.2,y_length=3.3).move_to([-3.75,-0.1,0])
        ticks = VGroup(*[Tex(str(v),color=CAPTION).scale(0.6).next_to(chart.c2p(0,v),LEFT,buff=0.15) for v in (0,20,40)])
        bars = VGroup(*[Rectangle(width=0.62,height=3.3*v/40,color=DEMAND,fill_color=DEMAND,fill_opacity=0.3,stroke_width=2).move_to(chart.c2p(i+1,v/2)) for i,v in enumerate(benefits)])
        bar_values = VGroup(*[Tex(str(v),color=DEMAND).scale(0.7).next_to(bar,UP,buff=0.12) for v,bar in zip(benefits,bars)])
        bar_names = VGroup(*[Tex(name,color=CAPTION).scale(0.51).next_to(chart.c2p(i+1,0),DOWN,buff=0.2) for i,name in enumerate(residents)])
        chart_heading = Tex('Individual benefit',color=CAPTION).scale(0.7).move_to([-3.75,2.2,0])
        divider = Line([0,2.5,0],[0,-2.7,0],color=MUTED,stroke_width=1)
        cost_label = Tex('Annual cost: 100',color=SUPPLY).scale(0.9).move_to([3.8,1.4,0])
        teaching = Tex('If it is built, how many people will visit?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(chart),FadeIn(ticks),FadeIn(bars),FadeIn(bar_values),FadeIn(bar_names),FadeIn(chart_heading),Create(divider),FadeIn(cost_label),FadeIn(teaching))
        self.pause('3.a.visits')
        visitors = Tex('All five',color=INK).scale(1).move_to([3.8,-0.1,0])
        self.play(FadeIn(visitors))
        self.pause('3.b.all-five')

        self.play(FadeOut(visitors),FadeOut(teaching))
        tax_line = DashedLine(chart.c2p(0,20),chart.c2p(6,20),color=GUIDE,stroke_width=2)
        tax_label = Tex('Tax: 20 each',color=GUIDE).scale(0.8).move_to([3.8,0.3,0])
        teaching = Tex('Would an equal tax of 20 pass a majority vote?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(Create(tax_line),FadeIn(tax_label),FadeIn(teaching))
        self.pause('3.c.vote')
        votes = VGroup(*[Tex('Yes' if v>20 else 'No',color=EFFICIENT if v>20 else NASH).scale(0.65).next_to(name,DOWN,buff=0.24) for v,name in zip(benefits,bar_names)])
        vote_result = Tex('3 Yes, 2 No',color=INK).scale(0.9).move_to([3.8,-0.8,0])
        tax_total = Tex(r'$5\times20=100$',color=GOV).scale(0.75).move_to([3.8,-1.7,0])
        self.play(FadeOut(teaching),FadeIn(votes),FadeIn(vote_result),FadeIn(tax_total))
        teaching = Tex('It passes, and the tax pays for the memorial.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.d.passes')

        self.play(FadeOut(teaching),FadeOut(tax_label),FadeOut(tax_total),FadeOut(vote_result),FadeOut(votes),FadeOut(tax_line),FadeOut(cost_label))
        teaching = Tex('Is building the memorial socially efficient?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.e.efficiency')
        # Add benefits vertically: five people enjoy the same one memorial.
        total_bar = VGroup()
        running = 0
        for v in benefits:
            segment = Rectangle(width=0.9,height=v*0.025,color=DEMAND,fill_color=DEMAND,fill_opacity=0.3,stroke_width=2).move_to([3.3,-1.65+(running+v/2)*0.025,0])
            total_bar.add(segment)
            running += v
        total_name = Tex('Social benefit',color=CAPTION).scale(0.7).move_to([3.3,-2.15,0])
        total_value = Tex('120',color=DEMAND).scale(0.85).next_to(total_bar,UP,buff=0.16)
        cost_line = DashedLine([1.8,0.85,0],[5.4,0.85,0],color=SUPPLY,stroke_width=2)
        cost_value = Tex('Cost: 100',color=SUPPLY).scale(0.7).next_to(cost_line,RIGHT,buff=0.16)
        self.play(*[TransformFromCopy(bar,segment) for bar,segment in zip(bars,total_bar)],FadeIn(total_name))
        self.play(TransformFromCopy(bar_values,total_value),Create(cost_line),FadeIn(cost_value),FadeOut(teaching))
        teaching = Tex(r'$MSB=120>MSC=100$: a net gain of 20.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.f.efficient')

        # The vignette's higher-tax question. Project cost is still 100.
        self.play(*[FadeOut(o) for o in (total_bar,total_name,total_value,cost_line,cost_value,teaching)])
        tax_line = DashedLine(chart.c2p(0,25),chart.c2p(6,25),color=GUIDE,stroke_width=2)
        tax_label = Tex('Tax: 25 each',color=GUIDE).scale(0.9).move_to([3.8,1.4,0])
        teaching = Tex('What if the proposed tax were 25 each?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(Create(tax_line),FadeIn(tax_label),FadeIn(teaching))
        self.pause('3.g.tax25')
        votes = VGroup(*[Tex('Yes' if v>25 else 'No',color=EFFICIENT if v>25 else NASH).scale(0.65).next_to(name,DOWN,buff=0.24) for v,name in zip(benefits,bar_names)])
        vote_result = Tex('2 Yes, 3 No',color=INK).scale(0.9).move_to([3.8,0.15,0])
        tax_total = VGroup(Tex('Revenue if passed: 125',color=CAPTION),Tex('Project cost: still 100',color=CAPTION)).arrange(DOWN,buff=0.3).scale(0.65).move_to([3.8,-1.3,0])
        self.play(FadeIn(votes),FadeIn(vote_result),FadeIn(tax_total),FadeOut(teaching))
        teaching = Tex('It fails. Support depends on the proposed payment.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.h.fails')

        # Admission is a counterfactual: exclusion is now possible, one uniform fee.
        self.play(*[FadeOut(o) for o in (votes,vote_result,tax_total,tax_label,tax_line,teaching,context)])
        context = subtitle(head,'Suppose access can be restricted. One annual admission fee.')
        admission_heading = Tex('Admission revenue',color=CAPTION).scale(0.8).move_to([3.8,2.1,0])
        fee_line = DashedLine(chart.c2p(0,20),chart.c2p(6,20),color=GUIDE,stroke_width=2)
        fee_label = Tex('Fee: 20',color=GUIDE).scale(0.75).move_to([3.8,1.25,0])
        teaching = Tex('Can a private operator cover the cost of 100?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(context),FadeIn(admission_heading),FadeIn(fee_label),Create(fee_line),FadeIn(teaching))
        self.pause('3.i.admission')
        revenue20 = Tex(r'$3\times20=60$',color=INK).scale(0.85).move_to([3.8,0.15,0])
        self.play(FadeIn(revenue20),bars[3].animate.set_fill(opacity=0.06).set_stroke(opacity=0.2),bars[4].animate.set_fill(opacity=0.06).set_stroke(opacity=0.2))
        self.pause('3.j.fee20')
        self.play(FadeOut(teaching),Transform(fee_line,DashedLine(chart.c2p(0,24),chart.c2p(6,24),color=GUIDE,stroke_width=2)),Transform(fee_label,Tex('Fee: 24',color=GUIDE).scale(0.75).move_to(fee_label)),
                  revenue20.animate.scale(0.8).move_to([3.8,-1,0]).set_color(CAPTION))
        revenue24 = Tex(r'$3\times24=72$',color=INK).scale(0.85).move_to([3.8,0.15,0])
        self.play(FadeIn(revenue24))
        self.pause('3.k.fee24')
        self.play(Transform(fee_line,DashedLine(chart.c2p(0,19),chart.c2p(6,19),color=GUIDE,stroke_width=2)),Transform(fee_label,Tex('Fee: 19',color=GUIDE).scale(0.75).move_to(fee_label)),
                  revenue20.animate.move_to([3.8,-1.8,0]),revenue24.animate.scale(0.8).move_to([3.8,-1,0]).set_color(CAPTION),bars[3].animate.set_fill(opacity=0.3).set_stroke(opacity=1))
        revenue19 = Tex(r'$4\times19=76$',color=INK).scale(0.85).move_to([3.8,0.15,0])
        self.play(FadeIn(revenue19))
        teaching = Tex(r'Even the best uniform fee raises only $76<100$.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.l.fee19')

        # A brief Lindahl-inspired bridge; this discrete cost split is not a formal equilibrium.
        self.play(*[FadeOut(o) for o in (admission_heading,fee_line,fee_label,revenue20,revenue24,revenue19,teaching,context)],*[bar.animate.set_fill(opacity=0.3).set_stroke(opacity=1) for bar in bars])
        context = subtitle(head,'Personalized taxes: an alternative to equal payments.')
        payments = (30,25,20,15,10)
        tax_marks = VGroup(*[Line(chart.c2p(i+1,p)+LEFT*0.42,chart.c2p(i+1,p)+RIGHT*0.42,color=GUIDE,stroke_width=3) for i,p in enumerate(payments)])
        payment_values = VGroup(*[Tex(str(p),color=GUIDE).scale(0.6).next_to(name,DOWN,buff=0.24) for p,name in zip(payments,bar_names)])
        split_total = VGroup(Tex('Total tax: 100',color=GOV),Tex('Each benefit exceeds its tax',color=INK)).arrange(DOWN,buff=0.55).scale(0.75).move_to([3.8,BODY_MID,0])
        teaching = Tex('Could different payments make everyone willing to fund it?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(context),FadeIn(teaching))
        self.pause('3.m.personalized-question')
        self.play(FadeIn(tax_marks),FadeIn(payment_values),FadeIn(split_total),FadeOut(teaching))
        teaching = Tex('The difficulty: learning how much each person really values it.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('3.n.personalized')

        # 4 · The exercise supplies a counterexample: majority does not maximize total gains.
        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title('Does A Majority Choose Efficiently?')
        context = subtitle(head,'The Dumbledore memorial: annual cost 90; equal tax 30.')
        small_chart = axes([0,4,1],[0,90,30],x_length=5.8,y_length=3.5).move_to([-3.7,-0.1,0])
        small_benefits = (75,10,20)
        small_bars = VGroup(*[Rectangle(width=0.85,height=3.5*v/90,color=DEMAND,fill_color=DEMAND,fill_opacity=0.3).move_to(small_chart.c2p(i+1,v/2)) for i,v in enumerate(small_benefits)])
        small_values = VGroup(*[Tex(str(v),color=DEMAND).scale(0.8).next_to(b,UP,buff=0.15) for v,b in zip(small_benefits,small_bars)])
        small_names = VGroup(*[Tex(s,color=CAPTION).scale(0.6).next_to(small_chart.c2p(i+1,0),DOWN,buff=0.2) for i,s in enumerate(('Aurelius','Aberforth','Ariana'))])
        small_tax = DashedLine(small_chart.c2p(0,30),small_chart.c2p(4,30),color=GUIDE)
        small_tax_value = Tex('30',color=GUIDE).scale(0.65).next_to(small_tax,LEFT,buff=0.15)
        divider = Line([0,2.5,0],[0,-2.7,0],color=MUTED,stroke_width=1)
        teaching = Tex('Does it pass? Should it be built?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(small_chart),FadeIn(small_bars),FadeIn(small_values),FadeIn(small_names),Create(small_tax),FadeIn(small_tax_value),Create(divider),FadeIn(teaching))
        self.pause('4.a.counterexample')
        rejection = VGroup(Tex('1 Yes, 2 No',color=NASH),Tex(r'$MSB=105>90=MSC$',color=INK),Tex('Efficient, but rejected',color=INK)).arrange(DOWN,buff=0.6).scale(0.8).move_to([3.9,BODY_MID,0])
        self.play(FadeIn(rejection),FadeOut(teaching))
        teaching = Tex('Votes count people, not the size of their gains and losses.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('4.b.rejected')

        # 5 · A short new illustration for the old schedule's three-ballot topic.
        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title('Three Voters, Three Alternatives')
        context = subtitle(head,'Each voter has a consistent ranking. Read from least to most preferred.')
        rankings = (('C','B','A'),('A','C','B'),('B','A','C'))
        ranking_rows = VGroup(*[VGroup(Tex(f'Voter {i+1}',color=CAPTION).scale(0.75),MathTex(r' \prec '.join(rank)).scale(0.9)).arrange(RIGHT,buff=0.55)
                               for i,rank in enumerate(rankings)]).arrange(DOWN,buff=0.65,aligned_edge=LEFT).move_to([-3.9,BODY_MID,0])
        divider = Line([0,2.5,0],[0,-2.7,0],color=MUTED,stroke_width=1)
        teaching = Tex('Which alternative wins a pairwise majority vote?',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(ranking_rows),Create(divider),FadeIn(teaching))
        self.pause('5.a.rankings')
        pair_results = VGroup(*[Tex(s,color=INK).scale(0.9).move_to([3.8,y,0]) for s,y in zip(('A beats B: 2 to 1','B beats C: 2 to 1','C beats A: 2 to 1'),(1.25,0,-1.25))])
        self.play(FadeIn(pair_results[0]))
        self.pause('5.b.ab')
        self.play(FadeIn(pair_results[1]))
        self.pause('5.c.bc')
        self.play(FadeIn(pair_results[2]),FadeOut(teaching))
        teaching = Tex('A Condorcet cycle: no alternative beats every other one.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(teaching))
        self.pause('5.d.cycle')
        self.play(FadeOut(teaching))
        agenda = Tex('A vs. B, then C: C wins',color=CAPTION).scale(0.7).move_to([3.8,-2.45,0])
        teaching = Tex('The order of the votes can change the winner.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(agenda),FadeIn(teaching))
        self.pause('5.e.agenda')

        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title("Arrow's Impossibility Theorem")
        context = subtitle(head,'With three or more alternatives, aggregating rankings involves a tradeoff.')
        conditions = VGroup(Tex('Any individual rankings',color=INK),Tex('Respect unanimous preferences',color=INK),
            Tex('Compare A and B using only rankings of A and B',color=INK),Tex('No single voter always decides',color=INK)).arrange(DOWN,buff=0.4,aligned_edge=LEFT).scale(0.72).move_to([0,0.4,0])
        arrow_result = Tex('No rule satisfies all four and always gives a complete, transitive social ranking.',color=INK).scale(0.65).move_to([0,-2,0])
        teaching = Tex('This is a limit on ranking rules, not a reason to abandon voting.',color=DEFINITION).scale(TEACHING_SCALE).to_edge(DOWN,buff=0.05).set_x(0)
        self.play(FadeIn(head),FadeIn(context),FadeIn(conditions),FadeIn(arrow_result),FadeIn(teaching))
        self.pause('5.f.arrow')

        # 6 · One sparse closing comparison with D2.
        self.play(*[FadeOut(o) for o in list(self.mobjects)])
        self.clear()
        head = title('Public Goods And Collective Choice')
        recap = VGroup(
            VGroup(Tex('Common resources',color=DEFINITION),Tex('Rival: take too much',color=INK)).arrange(RIGHT,buff=0.6),
            VGroup(Tex('Public goods',color=DEFINITION),Tex('Non-rival: contribute too little',color=INK)).arrange(RIGHT,buff=0.6),
            VGroup(Tex('Voting',color=DEFINITION),Tex('Can fund a good; need not choose efficiently',color=INK)).arrange(RIGHT,buff=0.6)
        ).arrange(DOWN,buff=0.7,aligned_edge=LEFT).scale(0.7).move_to([0,BODY_MID,0])
        for row in recap:
            row[0].align_to(np.array([-5.8,0,0]),LEFT)
            row[1].align_to(np.array([-1.3,0,0]),LEFT)
        context = subtitle(head,'Both common resources and public goods are non-excludable.')
        self.play(FadeIn(head),FadeIn(context),FadeIn(recap))
        self.pause('6.a.recap')
