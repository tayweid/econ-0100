# B3 · Equilibrium

**Rebuild in progress (2026-09-22).** The plan for the seven core scenes, Taylor's decisions, the numbers, and Taylor's verbatim direction are in **[00_Outline.md](00_Outline.md)**; the reason for the rebuild is in [00_Class_Review_2026-09-21.md](00_Class_Review_2026-09-21.md). Everything below describes the single-episode animation that the rebuild supersedes.

The fresh animation is **[03_Equilibrium.py · EpisodeB3](03_Equilibrium.py)**.
Its [current storyboard](02_Storyboard.md) follows the implemented order:
small-player discovery → equilibrium → graph/algebra → deviations.
Taylor/Fable own [01_Notes.md](01_Notes.md); animation work does not edit it.

From the repository root:

```sh
maniml Blocks/B3_Equilibrium/03_Equilibrium.py EpisodeB3
```

For a local preview with named teaching stops in both directions:

```sh
maniml Blocks/B3_Equilibrium/03_Equilibrium.py EpisodeB3 --export-present
```

Open `media/EpisodeB3_present/index.html`. The preview currently ends after the
stability checks (`5.h.iii`); the PPF tieback and final exercise/closing treatment
remain storyboard items. Rendered previews can be regenerated from the source.

## Current work

| Material | Purpose and status |
|---|---|
| [03_Equilibrium.py](03_Equilibrium.py) · `EpisodeB3` | Current flat scene: first deliberation through both deviations and stability. |
| [../Sim/discovery.py](../Sim/discovery.py) | Current pure random-search rules; tests in `test_discovery.py`. |
| [01_Notes.md](01_Notes.md) | Current lecture script; Taylor/Fable own this file. Taylor's animation directions are recorded verbatim in the [storyboard](02_Companion_Storyboard.md#taylors-animation-directions-verbatim). |
| [02_Storyboard.md](02_Storyboard.md) | Current implementation map, actual values/pauses, validation, and writing reconciliation. |
| [02_Companion_Storyboard.md](02_Companion_Storyboard.md) | Historical first-branch design, source inventory, and verbatim animation directions. The current map is `02_Storyboard.md`. |
| [Animate.py](Animate.py) · `PriceDiscovery` | Existing 3D companion: circular plaza, floating marginals, camera/spotlight choreography, midpoint bargaining, and a fixed graph. This is the visual foundation for the revision. |
| [02_Episode_Storyboard.md](02_Episode_Storyboard.md) | In-progress lecture storyboard: shortage → excess → equilibrium → algebra → PPF tieback. Its description of the companion as the midpoint-only alternative predates the new direction. |
| [Animate_A.py](Animate_A.py) · `PostedPrice` | In-progress lecture prototype with seller tags, queues, unsold units, and price adjustment. The filename's “A” does **not** mean companion/Track A. |
| [../Sim/posted_price.py](../Sim/posted_price.py) | Pure posted-price rules used by the lecture prototype; useful implementation reference. It does not yet implement the companion's requested random search. |
| [../Sim/README.md](../Sim/README.md) | Shared renderer adapter and earlier small-world demonstrations; benchmark economics and model test commands. |

Use **building equilibrium** and **testing deviations** for the two branches.
“Companion” and “lecture episode” still identify existing files, but do not fix
the final video structure. The discovery branch will also use seller-posted
asks, so “midpoint versus posted price” no longer describes the planned split.

## Review the existing scenes

From the repository root:

```sh
cd Blocks/B3_Equilibrium
maniml Animate.py PriceDiscovery
maniml Animate_A.py PostedPrice
```

These commands open the existing prototypes, including their older mechanics.
Both prototype source files parse; their current visuals were not certified in
this fresh-scene pass. The shared pure-Python model tests can be run with:

```sh
python3 -m unittest discover -s Blocks/Sim -v
```

## What the revision preserves and changes

Keep the plaza, people, attached MB/MC bars, graph twins, and the small-cast
deliberation. Give prices a consistent visual home: seller ask, red line at the
price's height between the marginals, and that line's shadow on the ground.
At the first deliberation, face the pair from the side: buyer left, seller
right, marginals nearly touching between them. Pause with only a bottom
acceptance question added; reveal the choice and then expenditure, receipts,
CS, and PS in that same view. Scale to ten buyers and ten sellers using reproducible random checks
of sellers' prices and continuous action, with no deliberation stop per visit.

The [overall storyboard](02_Storyboard.md) puts the two branches in the agreed
order and records the relevant Part B outline and script sources. The
[detailed first-branch storyboard](02_Companion_Storyboard.md) distinguishes Taylor's
instructions from staging proposals and tuning choices. The new scene implements the two-player close-up, the crowd, the later graph
and algebra, and the deviations; use its current beat map when reviewing.

## Earlier material and reference sources

| Material | How to use it |
|---|---|
| [03_Code.py](03_Code.py), [03_Code_pt2.py](03_Code_pt2.py) | Earlier animation sources, not the current entry points. They fail Python parsing at lines 44 and 28 respectively; preserve as choreography references until a targeted port. |
| [03_Code_pt3.py](03_Code_pt3.py) | Earlier `ProducerSurplus` / `ConsumerSurplus` scenes from the combined equilibrium/welfare material. Parses, but has not been verified in the current runtime. |
| [Practice_Bank/](Practice_Bank/) | Exercise candidates and previous versions; selecting the current student materials belongs to the writing/course-material pass. |
| [_Unplaced.md](_Unplaced.md) | Historical material spanning B3, B4, and later blocks. The old combined-block title is historical, not a second current B3 outline. |
| [_archive/](_archive/) | Previous notes, lecture scripts, and notebooks. Source history, not the active animation brief. |
| [Original market outline](../Bx_Market_Animation/Bx_Equilibrium_Video.typ) | Taylor's earlier 3D concept: marginal bars, price checks, switching, aggregation, and surplus. |
| [Market scene design](../Bx_Market_Animation/Market_Scene_Design.md) | Broader design proposal and review of early experiments. Its old block paths and proposed package structure predate the current B3/Sim organization. |

Files remain in place so existing links and work in progress remain usable.
Follow the [animator workflow](../_Style_Guide.md#animator-workflow-and-division-of-labor):
notes → storyboard → flat ManimL scene → visual review. Taylor and Fable own
lecture wording; the animator owns staging, implementation, and visual checks.
