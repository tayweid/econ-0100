// Week 2 recitation handout: Vignettes A1, A2, A3, one per page. The questions
// live in each block's Vignette_<BLOCK>_sols.typ; this wrapper hides the answers.
// Compile from the repo root:
//   typst compile --root . Recitations/Recitation_Week_2.typ
#import "../Blocks/_Assets/sols.typ": *
#show: student-setup
#standalone.update(false)
#solutions.update(false)

#include "../Blocks/A1_The_PPF/Vignette/Vignette_A1_sols.typ"
#pagebreak()
#include "../Blocks/A2_Advantage/Vignette/Vignette_A2_sols.typ"
#pagebreak()
#include "../Blocks/A3_Trade/Vignette/Vignette_A3_sols.typ"
