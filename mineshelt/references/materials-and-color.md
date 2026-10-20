# Materials, colors and weathering

For **hands-on palette board construction, annotated candidate block families, directional gradients and hard material critiques**, read [block-palette-workshop.md](block-palette-workshop.md). Palette selection is a major building phase, not a final decoration step.

A credible palette is an architectural system: blocks are chosen because of **local availability, building technology, weather, hierarchy and age**. Texture noise is not equivalent to visual complexity.

## The five material roles

For each structure name:
1. **Foundation/load-bearing**: compressive stone, plinth, heavy column, pier, timber post with plausible footing.
2. **Main envelope**: dominant wall surface that occupies broad, readable areas.
3. **Roof**: weathering surface with visible mass and a consistent structural intent.
4. **Joinery/trim**: sparse corner, sill, lintel, eave and joint articulation.
5. **Special-use accents**: hearth, signage, colored glazing, ritual mark, repair or trade symbol.

Some roles can reuse the same block family. That is good. Contrast should be earned.

## Practical palette method

Before placing blocks, identify:
- overall value structure: predominantly light, medium or dark;
- warm/cool relationship; biome vegetation and sky color;
- one dominant surface and no more than a few supporting families;
- readable contrast between structural frame, infill and roof;
- known block states: axis, facing, half, shape, waterlogged, stairs and slabs;
- availability of all blocks in the **actual version and installed mod set**.

Write palette notes as *roles*, not a randomized percentage recipe. For example: “Weathered local stone lower course, dark spruce posts on the load-bearing corners, desaturated plank infill in sheltered bays, darker spruce roof, thin pale sandstone highlight only at the public entrance.”

### Example palettes to reason from, not copy

| Context | Structural reasoning | Proposed direction | Avoid |
| --- | --- | --- | --- |
| Wet taiga workshop | rot and snow; sturdy stone footings | cobbled stone plinth, spruce frame, weather-dark roof | pure white concrete, arbitrary moss everywhere |
| Dry mesa outpost | high sun, dust, thermal mass | terracotta/stone main walls, deeply shaded openings, restrained timber | snow-climate steep roofs by default |
| River merchant town | flood level and loading activity | elevated stone quays, timber upper stories, varied shopfront infill | buildings with disconnected entrances |
| Mountain sanctuary | wind exposure, limited access | heavy rock anchoring, sheltered courts, clear vertical beacon | delicate unsupported huge eaves |
| Ruined observatory | original geometry + chronology | sound old core, missing roof zones, collapsed edges oriented downhill | random holes on every surface |

If a style references a modded block family, query/check registries before relying on it. Do not hallucinate block IDs or expected variants.

## Where weathering belongs

Think of water flow, dirt deposition, human touch and maintenance:
- near grade: splash, mud, dampness and foot traffic;
- near roofline: runoff, dark staining and repair at gutters;
- behind chimneys: soot in a plausible plume path;
- around thresholds: polished or replaced contact surfaces;
- sun/wind-exposed faces: differing exposure; sheltered areas stay comparatively intact.

Weathering should have gradients and patches caused by the environment, not even percentages sprinkled across every wall. It may be absent on new, ceremonial or magically maintained buildings.

For abandoned structures, infer the sequence: abandonment → roof leaks → exposed frame → vegetation → interior collapse. Ruins preserve readable remnants of once-complete architecture. Random deletion fails.

## Color hierarchy

Before looking at specific textures, squint at the build or review a thumbnail. The value blocks should separate roof, walls, foundation and focal point. If all surfaces have identical value and granularity, simplify or increase structural contrast.

Use bright accent colors only where the narrative demands notice: bell, shrine, painted tavern sign, copper dome. A rich environment can contain quiet buildings. Not every wall needs a colored stripe.

## Texture hierarchy

Large quiet regions make crafted focal areas legible. Cluster small components at meaningful places: eaves, entrance, chimney base, shop awning, handrail terminus. Do not blanket every exterior surface with stairs, buttons, signs and open trapdoors.

Texture changes at wall junctions can suggest building phases. They should not read as a block roulette game.

## Vanilla/modded discipline

The word “spruce” is not a guarantee that every requested facing, slab or stair exists in the target mod/version. Check actual block registries and state definitions.

When using modded blocks:
- choose them for design semantics, not mere novelty;
- know whether they have tile/block entities or dynamic rendering cost;
- respect placement orientation and waterlogging behavior;
- define how the build degrades or falls back if the mod is absent, or make the dependency explicit;
- test collisions and light emission in the live game when they matter.

## Final palette audit

Ask: can you point to the reason for every family of blocks? Does wear correspond to physics and occupancy? Are high-contrast accents restricted to a few important areas? Would the silhouette and mass still work in a greyscale view? If not, palette work cannot rescue weak architecture.
