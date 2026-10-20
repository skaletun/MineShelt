# Professional hand-authored terraforming and landform design

**Terraforming is sculpting geography, not scattering grass and moss.** A professional Minecraft landscape should make geographic sense at all scales while framing gameplay routes and architecture. Landscape is a series of authored spatial decisions. Large brushes are permissible as *labor-saving tools*, but never let noise choose the actual landform.

Read [site-and-story.md](site-and-story.md), [block-palette-workshop.md](block-palette-workshop.md), [vegetation-and-custom-trees.md](vegetation-and-custom-trees.md), [reference-study-and-image-analysis.md](reference-study-and-image-analysis.md).

## 1. Reconnaissance: read existing land before touching it

Capture or inspect:
- current topographic edges and approximate elevations;
- ridges, valleys, local drainage, river/water table, outcrops;
- soil and rock already visible and present biome colors;
- structure footprint and foundation datum;
- user-protected blocks, nearby builds and underground features;
- where visitors will walk and what distant silhouettes they will see.

Record a **before** height sketch or screenshot plus editable bounds. Preserve the original terrain in a reversible way when modifying user data.

### Topographic notes

Use real coordinates where available. For each critical cross-section record X/Z location, the current surface Y, desired Y and cause for change. Identify where cut material goes and where fill requires support. Do not simply say “smooth the terrain”.

A useful three-section set:
1. main public approach;
2. cross-slope through the building;
3. route between landform and water or second landmark.

## 2. Shape first: big, medium, small

### Macro — readable from the horizon

Identify the ridgeline, valley shape, cliff face, terrace, bay, headland or crater. Make a silhouette that has a direction and focal point. Broad mountains aren't piles of equally sized ball brushes.

Establish:
- one primary high/low organizing landform;
- significant secondary spurs/benches;
- drainage path and watershed;
- route network and view corridors;
- background/foreground separation.

If no one can identify the proposed landform at distance, **don't paint more textures**.

### Meso — land behaves under gravity

Introduce ledges, changes in slope, buttresses, gullies, shelves and small berms. Keep them related to the macro landform. Natural features use *families* of similar forms, not an even distribution of random humps.

Transition the building site with stepped footings, retaining walls or terrain terraces. Avoid sudden super-flat circles around a house.

### Micro — finish only after shape passes

Loose stones, erosion steps, shallow roots, small ground-color variation, tufts and broken gravel edges belong to the final pass. Tiny details must support the underlying terrain shape, not disguise flat topography.

## 3. Rock cliffs: design geological character

Choose a geology story (sedimentary layered, massive igneous, fractured basaltic, metamorphic/tilted strata or stylized fantasy stone). Minecraft blocks are a representation; literal geologic fidelity is subordinate to a **clear coherent visual rule**.

### Cliff authoring workflow

1. Trace **a non-uniform crest** with major direction changes and a few strong points.
2. Define vertical and overhanging/undercut zones intentionally, preserving accessible/structural stability as needed.
3. Carve or model **2–4 dominant rock spines/ribs**, rather than equal repeated spikes.
4. Introduce shelves and fractures that connect to those spines.
5. Create a talus apron *below* areas that plausibly shed rock.
6. Arrange rock faces using materials by exposed strata, fracture type, erosion and wetness.
7. Root shrubs or trees in soil pockets/ledges, not randomly glued to vertical stone.
8. Check the cliff as an **outline** from distant vantage points; it should not resemble a serrated vertical wall or repeating cylindrical brush stamps.

### Stratification

Sedimentary cliffs can use broad roughly consistent strata running through neighboring rock faces; displaced strata can indicate faults. Massive volcanic rock can prioritize fractured columns and joint lines instead of horizontal color stripes. Every cliff should *not* receive the same stone-to-andesite gradient.

### Talus and scree

Rockfall collects near the base, especially below visible fractures/erosion chutes. Use larger blocks/boulders near likely fall sources or slope breaks; smaller gravel-like texture extends downslope as an apron. Avoid perfect cones, identical boulder sizes or a gravel outline around every cliff.

### Special treatment

When the cliff lies behind an important tower, control contrast so rock does not camouflage the building. Reserve a silhouette gap if possible. A dramatic cliff can deliberately exaggerate ridges for Minecraft viewing distance; realism is not an excuse for unreadable shape.

## 4. Hills, slopes and terrace transitions

Sketch the desired profile from side and top:
- convex upper slopes where a hill rolls over;
- concave lower slopes where material accumulates;
- alternating gentler shelves and steeper zones;
- one or two walkable contour-following approaches.

Avoid a perfect staircase of equal-height, equal-run steps. Individual full Minecraft blocks are inevitable; plan an **irregular coherent contour flow**. Keep enough flat/level land where a road, farm, foundation or plaza requires it.

On cut-and-fill sites:
- minimize terrain disturbance where possible;
- hide or intentionally expose retaining structures;
- integrate the fill with adjacent contours rather than leaving a square shoulder;
- ensure the underside/edges do not become hollow one-block skins where block updates/mobs could cause problems.

**No universal “never more than N blocks in a line” law.** Organic edges generally benefit from variation, but geological strata, formal canals, roads and terraces can correctly be straight. Treat tutorial heuristics as prompts for visual inspection, not an algorithm.

## 5. Rivers, shorelines and water

A believable waterway has source/destination and changes character with slope and space.

### Author a small river

1. Locate a plausible upstream connection and downstream exit.
2. Trace a route following the land, not randomly wriggling on a flat plane.
3. Widen channels where gradient softens, narrow where it steepens; maintain a navigable or aesthetic objective if specified.
4. Establish channel bottom, bank shelves and adjacent flood/planting zone.
5. On bends, represent **erosion on outer banks** and deposition/shallower bars on inner banks when appropriate.
6. Expose stone where currents cut into rock; use gravel/sand where sediment settles.
7. Plan bridges, paths and building entrances around the actual water height.
8. Test water flow/source states and the interface to chunk borders if modifying world data.

Do not claim perfect hydraulics: Minecraft water mechanics differ from real rivers. A stylized visual representation should still have plausible continuity.

### Pond/lake

Identify basin shape, depth, incoming/outgoing drainage or a plausible isolated setting, shallow perimeter shelves and vegetation along protected margins. Avoid a symmetrical one-depth swimming pool unless human-made.

### Coast

Use coves, headlands and erosion shelves where appropriate. Mix beaches and rocky walls according to wave exposure rather than tracing the entire coast with one band of sand. Create believable harbor quays and cargo movement where settlement requires them.

## 6. Terrain palettes are spatial maps

Define visible zones rather than randomized percentages:

| Terrain zone | Strong candidate materials | Placement logic |
| --- | --- | --- |
| intact exposed rock | stone, andesite, tuff, deepslate as context allows | coherent geological mass, local fractures |
| talus/rubble | cobblestone, gravel, coarse_dirt | below unstable faces, not across mountaintop |
| forest floor | grass_block, podzol, coarse_dirt, rooted_dirt | tree shade/root systems, paths, bare depressions |
| alpine transition | stone, gravel, grass_block | exposure, altitude and gentler ledges |
| marsh margin | mud, packed_mud, clay, dirt and vegetation | wet low points rather than evenly spread |
| arid wash | sand, sandstone, terracotta, gravel | flow paths, sediment deposition and cliff strata |
| built footpath | dirt_path, coarse_dirt, gravel, cobblestone | intensity of traffic, drainage, slope |

These are **candidate blocks**: validate game edition/version/mod availability. Block variants should follow structural and site logic.

### Surface painting: two axes

Most landscapes need both:
- **height-linked transition**: rock on steep face → broken rock → soil → vegetated flat;
- **context-linked transition**: wet concavity vs dry exposed ridge, high-traffic path vs sheltered shrub pocket.

Random placement without these two maps leads to synthetic “noise”.

## 7. What skilled builders use editing tools for

Hand placement and editor tools can coexist. A brush may place a rough mountain mass or cut a trench; the agent must **inspect and hand-direct the shape afterward**.

If WorldEdit is actually installed:
- discover supported version-specific commands;
- bound the active region and set a safe mask before large edits;
- prefer narrow protected selections around the terrain being edited;
- check undo/snapshot limits and store backups for irreplaceable worlds;
- use sculpt/raise/lower/smooth operations for roughing form, **not as the final aesthetic judgment**;
- manually rebuild unnatural balls, repeated brush outlines, ragged cliffs and damaged undercuts;
- only then paint palette zones and vegetation.

Official WorldEdit documentation distinguishes brushes from masks (masks limit affected blocks). Be precise about edition and command syntax. A random weighted pattern cannot replace authored erosion or drainage.

## 8. Before/after terrain review

Review at least:
- bird's-eye / 3:4 topological view;
- horizon-level silhouette;
- path approach and building-footing join;
- side section for cliffs/slope;
- water entry/exit if present;
- close terrain seam and vegetation distribution.

Look for:
- unnatural level circular platforms;
- visible giant brush spheres and evenly stepped terraces;
- perfect straight biome boundaries;
- floating or hollow grass surfaces;
- uniform cobble everywhere;
- isolated shrubs on bare vertical walls;
- disconnected streams and impassable paths.

Use [critique-and-verification.md](critique-and-verification.md) for the repair loop.

## 9. Deliverables

Report **actual modified bounds**, original vs final elevation profile where measured, earthwork decisions, palette zones, hydrology/route decisions, vegetation placement, and screenshots with the same before/after vantage.

If you could not inspect or modify the world, provide an *authored cross-section and elevation map with coordinate conventions* and mark it unexecuted.

## Source-informed principles

Mojang's [landscaping and terraforming tutorial](https://www.minecraft.net/en-us/article/tutorial--tips-for-landscaping-and-terraforming) highlights winding paths, layered terrain and riverbank erosion; the [Terraforming in Minecraft](https://www.minecraft.net/en-us/article/terraforming-minecraft) article emphasizes artists shaping illusion at Minecraft scale. The [WorldEdit brush and mask guides](https://worldedit.enginehub.org/en/latest/usage/) describe editing mechanisms; they do not substitute for artistic review. Read these as references, not as source material to copy.
