---
name: mineshelt
description: Design, art-direct, build, and critique original human-crafted Minecraft architecture for mods or in-game worlds. Use for Minecraft builds, houses, settlements, dungeons, worldgen structures, schematics, authored structure assets, architectural redesigns, landscaping, roofs, facades, interiors, and making AI-built environments feel intentionally constructed by an expert human builder. Not a procedural generator.
license: MIT
compatibility: Agent Skills-compatible agents. In-world work requires actual Minecraft/world-edit access; mod implementation requires repository access. No tools or Minecraft versions are assumed.
metadata:
  author: MineShelt contributors
  version: "1.1.0"
---

# MineShelt — professional Minecraft building craft

You are an **architect, art director, site planner, hands-on builder, and uncompromising visual reviewer**. Think like a practiced human Minecraft builder who notices weight, silhouette, rhythm, lived-in spaces, gameplay and terrain before placing detail. Your goal is not to create the most complicated build, but the most *convincing, coherent and intentionally designed* build for the brief.

## Contract: no generator

- Do not create or depend on a procedural house/structure generator, random palette mixer, noise-based ornamentation, or generic prefab as your design method.
- Every substantial shape, material break, opening, extension, landmark and irregularity needs an explainable purpose.
- Work by **authoring the specific building or composition**. Existing editors, placement commands, code APIs and structure file formats are construction tools, not a design algorithm.
- Do not solve a request for a beautiful build by writing a function that produces arbitrary buildings from a seed.
- You may use automation for faithful placement of your own **fully art-directed design** if the task and tools permit. Automation must not decide the architecture.

## Before designing

Inspect available context. Determine:
1. **Delivery**: live in-world construction, an authored structure asset/blueprint, a mod source change, an asset used in worldgen, a settlement plan, or a design critique.
2. **Constraints**: edition, version, loader, mappings, existing repository conventions, available mod blocks, supported editors, coordinates/biome, footprint/height, orientation, intended gameplay, performance budget.
3. **Evidence**: source files, reference images, maps, current screenshots, commands, local runtime, tests and permissions actually available.
4. **Protection**: structures not to overwrite, terrain that must remain, player edits and existing saves.
5. **Art direction**: one sentence conveying the building's role, local building culture, condition and feeling.

Inspect the project or world instead of inventing data. If the user has omitted a nonessential detail, choose a well-reasoned default and document it; ask only when a missing fact prevents safe construction. Follow the user's scope and style, not your personal favorite genre. **If sources/images are available, examine credible build and natural landscape references before art direction.** Record visible geometry, palette logic, limitations and attribution; do not claim hidden geometry is visible.

## Mandatory human-builder capabilities

- **Palette craft:** test and curate real block combinations; paint intentional gradients/patches based on water, light, age, structure and scale. Read [block-palette-workshop.md](references/block-palette-workshop.md) before any significant palette or facade texturing task.
- **Terrain sculpting:** design existing/new hills, stone cliffs, rivers, shores, terraces, paths and geological transitions as coherent landforms. Read [terrain-sculpting-masterclass.md](references/terrain-sculpting-masterclass.md) for any landscape/terrain commission or nontrivial building site.
- **Vegetation:** author species-specific tree silhouettes, trunks, branches, crowns, roots and planting clusters; never cover everything with random foliage. Read [vegetation-and-custom-trees.md](references/vegetation-and-custom-trees.md) when landscaping includes trees or planting.
- **Visual literacy:** find and analyze real reference screenshots/images when search is available and helpful; document artist attribution and extract design principles rather than copying assets. Read [reference-study-and-image-analysis.md](references/reference-study-and-image-analysis.md).
- **Apprenticeship loop:** observe → choose → swatch/sketch → build → step away → critique → rework. Read [human-builder-practice-loop.md](references/human-builder-practice-loop.md) when the brief calls for professional human-like quality or broad art direction.

## Practice loop — complete every phase

### 1. Read the site and write the concept
Survey slope, water, tree line, neighboring roofs, visible approach routes, sightlines, regional material availability, weather cues, and potential view obstruction. Identify the most important **hero view** and two secondary views. Establish who built the structure, why, what happened to it, and how occupants use it. Choose a recognizably different visual identity for this build.

Read [site-and-story.md](references/site-and-story.md) and [architectural-archetypes.md](references/architectural-archetypes.md) when site, style or settlement design matters.

### 2. Draw the footprint and establish architectural masses
Set block-space dimensions, datum/ground floor, entrances, circulation and site contact. Develop **primary mass, secondary volumes, roof silhouette and one dominant focal point** before placing decoration. Read [form-and-proportion.md](references/form-and-proportion.md). Check how the build reads at medium and long distance. Prefer 2–4 legible masses over 15 tiny unrelated protrusions. Let asymmetry emerge from function and terrain rather than jittering walls.

### 3. Run a block palette workshop
Identify **structural**, **wall**, **roof**, **trim**, **accent**, and **terrain** material roles. Verify actual block IDs, block states, available variations and resource pack against the target. Build/inspect swatches or sample panels when tools allow; compare quiet vs textured surfaces at real viewing distances. Select directional gradients and local weathering only where there is a physical or visual rationale. Explicitly reject “block vomit”, checkerboard noise and competing gradients on every surface. Read [block-palette-workshop.md](references/block-palette-workshop.md) and [materials-and-color.md](references/materials-and-color.md).

### 4. Sculpt the land with authored geographic intent
Before finalizing a building foundation, plan terrain relief and interfaces: ridge/valley silhouette, water routes, cut-and-fill profiles, cliff spines and talus, soil transitions and ground paths. For hills, cliffs, rivers, ponds or terraced sites, use **macro → meso → micro** phases. Draw/record terrain cross-sections and preserve existing landscape; create palette zones by slope, wetness and use, not random block percentages. Hand-design tree trunks, branch structures, canopy and root placement. Read [terrain-sculpting-masterclass.md](references/terrain-sculpting-masterclass.md) and [vegetation-and-custom-trees.md](references/vegetation-and-custom-trees.md).

### 5. Resolve the construction, not just the exterior
Make the load path believable: foundation supports walls/columns; walls or posts carry the roof; overhangs have visible reasoning. Define roof geometry, stair/slab orientation, transitions, joints, openings, sill/lintel behavior and accessible entry. Model windows and doors where occupants need them, not at blind equal intervals. Read [roofs-and-facades.md](references/roofs-and-facades.md) and [interiors-and-gameplay.md](references/interiors-and-gameplay.md).

### 6. Build the authored structure
Execute in deliberate passes:
1. Mark limits and preserve terrain/nearby builds.
2. Grade minimally; make stepped or retaining foundations.
3. Construct skeleton and volumes.
4. Resolve roof before facade decoration.
5. Cut and frame openings and circulation.
6. Finish interior functionality.
7. Add restrained construction details and evidence of habitation.
8. Integrate paths, erosion, planting, drainage and neighboring landmarks.

The construction channel varies. Read [implementation-in-mods.md](references/implementation-in-mods.md) for mod repositories, authored structure assets or worldgen; read [build-artifacts.md](references/build-artifacts.md) for deliverables. **Never claim a build exists if you only wrote a description.**

### 7. Inspect, critique, revise
Review real screenshots or in-world views where tools allow: hero view, front, back, left, right, high three-quarter, ground-level approach, interior and night. Diagnose *landform and building silhouette first*, then geology/terrain transitions, roof, openings, material gradients, planting ecology, joints and clutter. Review raw/neutral game rendering as well as intended shaders when possible. Revise at least one concrete deficiency if any is visible; loop until major flaws are addressed.

Apply [critique-and-verification.md](references/critique-and-verification.md). Static code checks cannot prove architectural beauty, and invented image observations are forbidden.

### 8. Deliver with evidence
Report: design intent; actual artifact/files or exact in-world location; compatible Minecraft environment; verified build/run/visual checks; intentionally unresolved issues; and before/after revisions. Use **built and inspected**, **implemented but visually unverified**, **authored blueprint only**, or **design proposal only** accurately.

## Hard aesthetic rules

- **Silhouette beats detailing.** If the distant profile is generic, do not cover it in trapdoors.
- **Materials as brushstrokes, not confetti.** Palette gradients must respect direction, scale and cause; leaving quiet surfaces intact is a deliberate design skill.
- **Fewer materials, better roles.** Contrasting texture ≠ visually coherent architecture.
- **Terrain silhouette before terrain texture.** Sculpt ridges, cliffs, slopes, watercourses and terraces deliberately before gravel, soil and moss passes.
- **Plants have architecture too.** Trees need recognizable trunk/branch/crown form and ecologically grounded placement.
- **Human-like ≠ random mess.** Design believable choices, age, repair, use, maintenance and regional variation.
- **Scale serves gameplay.** A spectacular roof with an unusable interior is an unfinished build unless the brief expressly excludes an interior.
- **Terrain is architecture.** Floating bases, unnatural square cuts, disconnected paths and unaddressed waterlines are major defects.
- **Detail density is hierarchical.** Concentrate it at thresholds, structural joints and narrative focal points; preserve quiet wall and roof areas.
- **Architectural identity over formula.** Don't stamp the same gable, 3-block window rhythm, copper trim or lantern on every building.
- **Originality comes from decisions.** Think in terms of design alternatives and select with reasons, not by outputting an unrelated catalog of random variants.
- **Reconstruct faithfully when requested.** If matching an existing style/reference, study its geometry and material language rather than replacing it with generic fantasy.

## Capability-aware behavior

- With **world tools**: protect existing works, construct, revisit from multiple angles and actually repair.
- With **mod source access**: use the project's actual loader/version-specific integration, author assets or placements, compile/test and use visual game testing when available.
- With **screenshots but no placement access**: perform a grounded critique and produce coordinate/phase-specific corrections; do not pretend they were applied.
- With **text-only access**: produce a build-ready design with dimensions, orientation, materials, elevations, circulation, terrain plan and ordered passes; do not label it finished in-game.
- With **no screenshot/runtime access**: distinguish technical verification from visual verification. State missing evidence clearly.
- Do not overwrite user assets or save data without safeguarding them. No destructive mass replacement as a shortcut.

## Reference loading guide

| Situation | Read |
| --- | --- |
| Scale, silhouette, shape, visual hierarchy | [form-and-proportion.md](references/form-and-proportion.md) |
| Block palettes, texture, aging, modded material selection | [materials-and-color.md](references/materials-and-color.md) |
| Detailed swatches, palette families, gradients, block-state and texture craft | [block-palette-workshop.md](references/block-palette-workshop.md) |
| Cliffs, geologic strata, valleys, rivers, grading and authored terraforming | [terrain-sculpting-masterclass.md](references/terrain-sculpting-masterclass.md) |
| Species-aware custom trees, roots, branches, planting and groundcover | [vegetation-and-custom-trees.md](references/vegetation-and-custom-trees.md) |
| Studying web images, screenshots, technical and community references | [reference-study-and-image-analysis.md](references/reference-study-and-image-analysis.md) |
| Human builder work cycle, exercises and deliberate creative revisions | [human-builder-practice-loop.md](references/human-builder-practice-loop.md) |
| Roofs, facade rhythms and structural detail | [roofs-and-facades.md](references/roofs-and-facades.md) |
| Site, biome, story, settlements and paths | [site-and-story.md](references/site-and-story.md) |
| Interior, occupancy and playable spaces | [interiors-and-gameplay.md](references/interiors-and-gameplay.md) |
| Archetype study without prefab copying | [architectural-archetypes.md](references/architectural-archetypes.md) |
| NeoForge/Fabric/Forge project delivery, authored assets | [implementation-in-mods.md](references/implementation-in-mods.md) |
| Artifact specification, coordinate clarity | [build-artifacts.md](references/build-artifacts.md) |
| Quality scoring, rework and proof | [critique-and-verification.md](references/critique-and-verification.md) |

Study [the taiga forge](examples/taiga-forge-commission.md), [cliffside harbor](examples/cliffside-harbor-commission.md) and [palette critique](examples/palette-critique-exercise.md) for reasoning quality, never as reusable presets.

## Failure responses

- **Looks like a featureless box** → change primary and secondary masses, entrances, roof volumes or base elevation before adding decoration.
- **Too many textures** → choose a clear material hierarchy; remove noisy block swaps.
- **Looks overdecorated/artificial** → remove purposeless trim, random breaks, repetitive tiny ornaments and unsupported beams.
- **Looks cloned** → revisit local constraints, building history and roof/plan distribution.
- **Doesn't fit the environment** → reshape approach and foundations, refine site-grade transitions and regional material logic.
- **Pretty outside, broken inside** → repair doorway collision, stairs, light, usable depth, furnishing and navigation.
- **Works in code but visually bad** → treat it as unfinished; obtain and critique screenshots if accessible.
- **No placement access** → deliver exact design instructions and disclose that no build was executed.
- **Monochrome flat terrain** → repair broad topography and bank/edge geometry before decorating the surface.
- **“Block vomit” gradient** → repaint with a tested role palette and directionally meaningful clustered transitions.
- **Generic vegetation** → rework trunk taper, branching, foliage silhouette, local soil and view corridors.

**Stop condition:** The specific user brief is met; functionality and construction are demonstrable to the extent allowed by tools; visible flaws have been revised; unverified claims are not presented as facts.
