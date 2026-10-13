# Raw material for B5_Changes, not runnable as written.
#
# These two chunks came out of B1_Demand's fall-2024 animation script
# (animation_1) on 2026-09-13, when B1 was ported to the Graphite house
# style. Shifters and elasticity belong to B5's story, not B1's, so they
# were lifted out verbatim -- old style, old colors, old triple-quoted
# section markers and all -- and parked here for B5's own pass.
# The B1 original in full: ../../B1_Demand/_archive/03_Code_fall2024.py.

    """ Elasticity """
        
        #new_title = Tex("{{Elasticity}} of Demand: how $Q_d$ changes with a change in $P$.").set_color_by_tex_to_color_map(
        #    {"Elasticity": YELLOW,}
        #).to_edge(UP)
        
        #elasticity_equation = Tex("$\\frac{Q_1 - Q_2}{\\bar{Q}} \\Big/ \\frac{P_1 - P_2}{\\bar{P}}$")
        
        #self.play(FadeIn(elasticity_equation), Transform(title, new_title))
        #self.wait()
        
        # show another graph with elasticity
        
    """ Shifters """
        
        new_title = Tex("A {{Demand Shifter}} changes the demand curve.").set_color_by_tex_to_color_map(
            {"Demand Shifter": YELLOW,}
        ).to_edge(UP)
        self.play(Transform(title, new_title), axes.animate.shift(RIGHT*3), demand.animate.shift(RIGHT*3), grid_labels.animate.shift(RIGHT*3))
        
        shifter_list = [
            "- Preferences", 
            "- Prices of related goods", 
            "- Income", 
            "- Buyer expectations",
        ]
        for i, shifter in enumerate(shifter_list):
            self.play(FadeIn(Tex(shifter).set_color(BLUE).to_edge(UP + LEFT).shift(DOWN*(1 + i*2/3))))
            self.wait()
