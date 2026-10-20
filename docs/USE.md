# How to make MineShelt build like an expert

This guide is for the user commissioning an AI agent. MineShelt is a **craft skill**. Without Minecraft/world and/or mod tooling, it can produce informed plans but cannot place blocks or verify aesthetics.

## Best possible inputs

Tell the agent:
- Minecraft edition/version and loader where relevant;
- location, biome and screenshots or an existing world/save/test instance;
- whether the agent may modify real terrain and neighboring buildings;
- approximate footprint/scale and stylistic goal;
- critical gameplay requirements: access, storage, NPC pathing, worldgen placement;
- allowed block families and resource packs;
- what the agent can actually use to place blocks;
- what visual evidence you expect.

Allow the agent to inspect the project instead of listing all existing block IDs by hand.

## A professional site commission (copyable)

~~~text
Use MineShelt as your professional Minecraft architecture and terraforming
workflow. Inspect the world/site and existing project first.

Design and actually build an original small riverside village hall. Before
construction, study credible Minecraft builder references with artist links,
survey the terrain and plan the hero view. Select real block palette options,
test sample walls and material gradients in the target Minecraft version, and
reject noisy block mixing. Sculpt the riverbanks, paths and slope transitions
with deliberate geology and erosion. Hand-design the trees and foliage.

Work in reviewable stages: massing, terrain profile, foundation, roof,
materials/gradients, interiors, planted environment and final visual review.
Inspect front, rear, both sides, aerial and player-eye views, plus night if
relevant. Correct visually weak parts instead of hiding them in decoration.

Do not create a structure generator. Do not overwrite protected world areas.
Confirm what was truly built, tested and visually inspected, with coordinates,
files, screenshots and a list of unverified items.
~~~

## A block palette-only commission

~~~text
Use MineShelt's block palette workshop. I want a believable abandoned
mountain library, not a randomized wall. Inspect the installed Minecraft
blocks and build palette swatches first. Compare two intentionally different
palettes in neutral and target lighting. Choose material roles, gradients and
real weathering directions. Produce a physical sample wall and correct it
after inspecting distance and near views. Do not apply changes destructively
outside the approved region.
~~~

## A terraforming-only commission

~~~text
Use MineShelt's professional terraforming workflow. Survey the mountain
slope, water, paths, elevations and all protected blocks. Hand-art-direct
a cliffside trail with convincing ridge silhouette, connected rock spines,
realistic talus, drainage and rooted vegetation. Sculpt macro form before
painting textures. Use editing tools only to realize intentional shapes.
Walk the route, compare before/after cross sections and screen views, and
repair brush artifacts.
~~~

## A custom forest commission

~~~text
Use MineShelt to build a small hand-authored taiga forest around an existing
tower without blocking its skyline. Study custom tree references. Design
distinct mature and juvenile spruce silhouettes and one weather-bent pine,
with traceable branches, rooted bases, canopy gaps and ecologically justified
undergrowth. Inspect from ground and elevated approaches. Do not scatter
identical trees or foliage randomly.
~~~

## How to review the answer

A great response has concrete design reasoning **and actual execution evidence**. Ask:
1. Did it survey or faithfully receive the site context?
2. Did it test real palette blocks in a relevant resource pack?
3. Did it solve the silhouette/landform before adding microdetail?
4. Do rock strata, water and planting have spatial causes?
5. Is gameplay circulation functional?
6. Can it show raw-game front/back/side/site screenshots?
7. Did it revise real visual defects rather than only praise the result?
8. Is its completion status honest about what was not tested?

Use [the review sheet](../tests/review-sheet.md) for repeatable critique.

## Skill invocation is not gameplay connectivity

Do not assume the agent can run Minecraft, launch a client or edit a world merely because MineShelt was installed. This skill is intentionally independent of NeoForge/Fabric/Forge/WorldEdit. Connect the actual tools for the chosen environment.
