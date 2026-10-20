# Architectural depth and relief — buildings must be modeled, not painted

**Scope:** the *relief of the building itself*: three-dimensional massing, depth of walls and openings, structural frames, transitions between volumes, profile of roofs and foundations, projections, recesses, shadows and inside/outside relationships. This is distinct from terrain relief and distinct from surface texturing.

The goal is **real authored architectural geometry**, not a flat cuboid with trapdoors and stairs pasted on. Read with [form-and-proportion.md](form-and-proportion.md), [roofs-and-facades.md](roofs-and-facades.md), [interiors-and-gameplay.md](interiors-and-gameplay.md) and [block-palette-workshop.md](block-palette-workshop.md).

## 0. Four different kinds of depth

Distinguish these before choosing blocks.

1. **Primary volume (macro):** portions of the building that truly occupy different world-space masses: main hall, taller stair tower, kitchen wing, recessed courtyard, porch, split floor levels, roof planes, side annex, balcony or arcaded gallery. At distance these control the silhouette and the readable program.
2. **Architectural relief (meso):** structural frame forward of infill, deep door/window reveals, recessed bays, buttresses, pilasters, arcades, cornices, gable projections, corbels, bay windows, roof dormers, projecting fireplace stack. These control shadow, rhythm and perceived weight from medium distance.
3. **Block-scale modeling (micro):** stairs, slabs, walls, fences and carefully placed narrow blocks completing ledges, chamfers, brackets, sills and transitions. They must reinforce geometry, not cover defects.
4. **Material/lighting relief (optical):** warm/cool/value contrasts, shadow on the underside of eaves, darker recess interiors and sunlight across returns. Texture cannot replace real changes of geometry.

A build can be intentionally smooth and planar (modern minimalist or formal masonry). “Flat” is a problem when its form is **unintentionally featureless**, not when the chosen architectural style relies on clean planes.

## 1. Design *depth budget* before decorating

Set project dimensions, front/back/right/left orientation, usable interior volume and bounds including eaves, balconies, exterior stairs and trim. A single extra block of facade thickness can consume a small interior or trespass on a protected street.

For each elevation label:
- **Datum / main wall plane**, for example local Z=0 on a south-facing elevation;
- **negative relief**: inset window glazing, door threshold, portico, ground-floor arcade, courtyard;
- **positive relief**: frame/post, bay window, balcony, buttress, cornice, eave;
- **dominant projecting masses**, with footprint and height;
- **circulation/clearances**, both inside and outside;
- **shadow hierarchy**: broad deep shadow under eaves, medium shadow in the entry, small sill shadows.

Use **relative** depth steps (often single blocks at village scale, more at monument scale) as a visual tool, not a mandatory “three layers” recipe. Depth must be proportionate to wall height, architectural style and target viewing distance. Don't attach a giant 3-block-deep cornice to a 6-block-high hut.

A useful wall assembly *when it fits the plan*:

| Plane (illustrative, south elevation) | Elements | Role |
| --- | --- | --- |
| Z=-1 (behind datum) | glass, door recess, sheltered alcove | primary dark recess |
| Z=0 (datum) | wall infill, opening returns | quiet field |
| Z=+1 (projecting) | structural posts, corner pilasters, lintel/sill edges | middle-depth rhythm |
| Z=+2 only where earned | porch edge, large bay, supported balcony or projecting eave | local emphasis, not constant fuzz |

Here +Z is **toward the viewer**, not a global map convention. Reorient all values to the real target. The two-block projection is not a quota: a one-plane clean modern facade may be stronger than artificial protrusions.

**Depth must be allocated by design**, never generated through periodic “push every Nth column out” rules.

## 2. Start with real 3D masses — the front-view trap

If the main hall and all rooms share exactly one wall plane and one roof silhouette, you cannot rescue the building merely with window boxes.

Make a small physical/mapped massing study:

1. Draw top-down footprint with main use spaces.
2. Draw at least front and side elevations plus one vertical section.
3. Mark height differences and roof ridges.
4. Choose a lead element that affects the *real silhouette*: recessed public porch, taller chimney block, low side workshop, stair bay, tower or stepped second storey.
5. Test **three-quarter view** and rear view. Does the composition still make sense if the ornamental front is hidden?
6. Reject unusable fake masses: balconies without doors, towers without stair/service room where that purpose is implied, giant roof forms with no plausible connection.

At village scale, **one dominant volume and one purpose-driven subordinate volume** usually reads better than many busy boxes. A fort, palace, town hall or cathedral may need a more complex hierarchy; increase complexity only to support function and site.

## 3. Wall relief is constructed in section

Design a real wall section rather than a sticker sheet. Resolve these in order:

### Load path: corners, piers and bays

- Corner columns, masonry buttresses or timber posts visually receive load from lintels, arches, floor beams or roof members.
- Structural members continue logically through stories and rest on plinths. A corner log that stops in mid-air is not a convincing column.
- Bay spacing reflects spans, room functions and openings. Uniform rhythm is acceptable when a frame system calls for it; arbitrary jitter is not.
- A deep structure can have **quiet bays** framed by legible posts. Do not fill every quiet bay with another independent relief motif.

### Windows and reveals

A strong inset window has:
- window opening tied to the plan, interior light and upper floor;
- wall thickness giving an actual reveal, not only a dark-colored frame;
- lintel or arch transferring perceived load to adjacent solid material;
- sill/drip/projection whose scale matches opening size;
- shutters, lattice or balcony only where function and clearance make sense.

A **bay window** is different from a recessed window: glazing projects, usually creating interior space and requiring a support, brackets or coherent cantilever. Don't paste a glass cube on the side and call it a bay.

### Doors and entries

Treat entrance depth as **an actual spatial sequence**: public approach → porch/portico/arched gateway → sheltered landing → door plane → interior. A proud frame creates visual hierarchy; a recessed door creates shadow and weather protection. Verify that the threshold doesn't consume required accessibility/collision space.

### Arcades, pilasters, arches

- An arcade is repeated *negative volume* under arches/columns. Its bays should provide traversable routes where required.
- A pilaster changes the visible wall plane; its base and capital, if any, should support the elevation's structural story.
- A buttress should connect meaningful foundations to the part of the wall resisting apparent loads; a decorative 1-block stick beside a huge tower fails the weight test.
- Arch shapes have consistent centers/spans across supporting blocks. Side elevations and under-arch view matter.

### Cornices and horizontal lines

Use a foundation/plinth break, floor beam or cornice where it coincides with real story divisions, roof/wall junction or a compositionally important threshold. Repeating giant horizontal stripes every few blocks can produce a layered cake instead of architecture.

## 4. Roof relief is *geometry*, not a stair outline

Before roof texture, author:
- span, ridge axis, pitch and height relative to walls;
- one consistent construction logic for each principal roof plane;
- eave thickness and depth (and where returns close at corners);
- real fascia/soffit/shadow under overhangs when suitable;
- roof intersections, valleys, joints and drainage;
- dormers, vents and chimneys only with an interior/exterior reason;
- visible supports/brackets for larger porches/overhangs.

Roof depth is visible from below and three-quarter views. A layered stair trim **cannot hide** an inaccessible attic, intersecting roof holes, or a roof which ends in the middle of a secondary volume.

Some roofs should be simple and thin. A flat modern cantilever can be elegant with a clean underside and rational support, not five stair/slab bands added for “depth”.

## 5. Foundations, floors and ground interface

Relief starts at the bottom:
- a plinth may extend outward and cast a narrow base shadow;
- pillars or piers must connect to the actual grade or foundation;
- stepped foundations follow terrain; long downhill cantilevers need a clear support/intent;
- visible sill courses tie stone/timber changes to actual wall thickness;
- porches, terraces, ramps, exterior stairs and galleries sit on structurally readable supports;
- avoid arbitrarily covering every foundation in stairs; make meaningful transitions and steps.

Review under porches and balconies: decorative floating undersides and hidden holes are common.

## 6. Relief must survive rotation and block constraints

When implementing in a Minecraft mod:
- Every stair's facing, half and shape, slab top/bottom, log axis, door hinge, trapdoor open state, wall/fence connection and waterlogged state matters.
- Check block variants in the **actual registry**. A texture family might not include a matching stair, corner stair, fence or wall in the target game.
- Deep reveals, projecting bays and cornices alter bounds, collision, mob navigation, lighting, fluid behavior and structure rotation; include these in origin/bounding-box calculations.
- Placed authored structures must be inspected at rotated/mirrored orientations if the game can place them that way.
- Apply only the author's permitted changes to user worlds; preview footprint/clearances before writing.

## 7. Five archetypes of *legitimate* relief

| Architecture | Dominant depth mechanism | Secondary mechanism | What to avoid |
| --- | --- | --- | --- |
| Timber-framed cottage | frame forward of plaster/infill and a real sheltered entry | restrained deep reveals, sill/roof eave | identical 1-block wooden strips across every wall |
| Stone fortress gate | massive inset passageway, thick walls and buttresses | arches, slit reveals, guard walkway | “castle” created by tacking a few stone stairs onto a thin wall |
| Modern hillside villa | interlocking volumes and controlled cantilevers | glazing behind overhang; terrace/retaining wall transition | decorative posts on smooth facades solely to break flatness |
| Gothic shrine | legible bays, deep pointed openings and buttresses | traceried/recessed windows, strong cornice/rib silhouette | every pillar decorated at equal visual intensity |
| Working village smithy | projecting covered forge/loading bay and external chimney mass | useful recessed working windows, porch bracket | a huge fake chimney disconnected from hearth and a flat back wall |

Do **not** copy a single depth recipe across unrelated building styles.

## 8. A complete authored facade exercise (scale-aware)

**Brief:** a workshop's south facade is 15 blocks wide, 8 blocks high to eaves. The existing interior must remain traversable. The wall currently reads as one flat rectangle.

An authored solution could:
1. Confirm room divisions, foundation support, wall face and exact protected plot.
2. Move the **actual doorway** back one block only if there is sufficient passage and entry clearance; build a 3-block-ish protected porch in front connected to foundation, not to a dangling slab.
3. Articulate load-bearing corners and the central working bay with timber piers one block proud of a quiet wall plane.
4. Position the workshop window to illuminate the real bench. Recess the glass by one block into an intentional reveal; make lintel and sill actually frame its opening.
5. Distinguish roof volume and wall by a coherent eave projecting where rain protection is needed. Finish underside, corners and joints.
6. Add an asymmetric lower service awning **only if** the storage/work route needs it; attach its roof and supports coherently.
7. Keep at least one broad calm wall field. No unnecessary trapdoor grid.
8. Recheck both side corners, porch underside, roof drainage, interior bench light, passage and remaining footprint.

**Plan-specific questions before selecting exact blocks:** Which direction is south in local axes? Which side already has the hearth/chimney? How large is the internal usable room? Can the porch occupy the public path? Are stairs/slabs for this palette available?

Without these, the above is an architectural study, **not a truthful block-by-block completed schematic**.

## 9. Visual inspection — the shadow/silhouette test

Require real views when tools exist:

| View | Diagnose |
| --- | --- |
| Front, daylight | Is depth organized around architectural hierarchy, or scattered everywhere? |
| 45° front-left and front-right | Do recesses have real side returns and do projections terminate convincingly? |
| Rear and both sides | Is the building a 3D composition or only a dressed-up front? |
| Low angle beneath eaves/porch | Are roofs, balconies and beams finished/supported from underneath? |
| High three-quarter | Do wings, ridge intersections, dormers and roofs connect? |
| Interior beside windows and doors | Has relief stolen usability, clearance, furniture and light? |
| Neutral light and nighttime | Are broad, medium and fine shadow planes legible without shader tricks? |
| Far view with terrain | Is depth at the right scale for a village/landmark, or just unreadable block speckles? |

If visually flat:
1. fix program/primary massing;
2. author a real projecting or recessed **architectural** element;
3. revise structural wall planes;
4. refine roof/base transitions;
5. only then add stairs/slabs and limited detail.

If visually overbuilt:
1. remove repetitive tiny projections;
2. keep one or two depth focal points;
3. simplify layers over quiet bays;
4. recheck clearance and side elevations.

Do not “fix” a flat facade by covering it with 50 trapdoors.

## 10. Evidence packet

For any serious build include:
- a footprint with depth/overhang bounds;
- one elevation with labeled datum, projections and recesses;
- at least one vertical wall/roof section with usable interior depth;
- the purpose of each major mass and protrusion;
- before/after comparable exterior views when editable world tools exist;
- side/rear/underside visual findings and fixes;
- version-specific block states, collision and rotation results if implemented;
- honest status **built and inspected / implemented but unverified / plan only**.

No text score proves the building has real depth. Physical placement and multi-angle observation are the authority.

## Source studies (attributed; no imported third-party builds)

- [Mojang / Kate Gray: Make Your Houses Better (2022)](https://www.minecraft.net/en-us/article/make-your-houses-better). Official Minecraft guidance emphasizes roof overhangs, recessed entries, glass panes and ground/base articulation rather than featureless flat exterior planes. Consult actual examples; do not assume any mandatory universal overhang.
- [legokid222: Depth in Building! (Minecraft Forum, 2014)](https://www.minecraftforum.net/forums/minecraft-java-edition/creative-mode/369294-depth-in-building-a-simple-way-to-improve-all). Historical community explanation of background wall, structural foreground and small finish layer. Apply *as one useful model*, not an invariant three-layer requirement.
- [Minecraft Wiki: Adding beauty to constructions](https://minecraft.wiki/w/Tutorial:Adding_beauty_to_constructions). Community reference for bay/recessed windows and architectural scale. Check links/images and game-version differences.

Referenced works are inspirational/educational; respect attribution and creator licenses. Don't mirror third-party schematics or screenshots into MineShelt.
