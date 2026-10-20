# Block palette workshop — paint with blocks as an expert builder

**This is a hands-on palette lab, not a palette generator.** You must choose and inspect blocks as a human build artist would. Good palettes have a legible value structure, coherent hue relationships, controlled texture frequency and spatial reasons for transitions. Gradients are optional; flat architectural surfaces can be excellent.

Load alongside [materials-and-color.md](materials-and-color.md), [architectural-archetypes.md](architectural-archetypes.md) and [reference-study-and-image-analysis.md](reference-study-and-image-analysis.md).

## 0. Verify your actual materials

Read the Minecraft edition/version, active resource packs, shader assumptions and **actual modded block registry**. This reference names familiar Java vanilla blocks as possible choices, not as a claim that every modpack contains them.

Never invent IDs, states, stair/slab variants, tile entities or interaction behavior. Verify each block against the target game. Evaluate the actual texture in the target resource pack, not only its display name. A block that looks smooth in vanilla can be noisy under another pack.

## 1. Construct a real palette board before building

Make an actual physical in-world swatch board (or a legible, explicitly labeled digital board if no world access):
- Place each candidate block in adjacent **3×3 surfaces**, not just isolated single cubes.
- Compare six to ten candidates, narrow them to a few meaningful roles.
- Show samples in sun, shade and indoor light at both close and medium distance.
- Check side/top texture variation and whether stairs/slabs/walls exist in the same family.
- Make a **5–9-block-wide test wall**, a corner, a test window and a miniature roof/ground transition.
- Make two competing versions: a quiet one and a textured one. Pick the stronger after seeing them, not by assuming more variation wins.
- Capture screenshots without shaders first (for reliable base comparison); assess shaders separately if target users will have them.

If physical samples cannot be placed, propose and label *untested candidates*. Do not claim colors or blends were verified.

## 2. Set roles and perceptual hierarchy

An intentional small-to-medium building may have:
- **Anchor (largest)**: the background wall or main stone/timber surface.
- **Frame**: beams, corner supports and joinery.
- **Roof field**: one dominant roof color/texture.
- **Transition**: block colors/textures that bridge foundation to wall, dry to wet or exposed to sheltered surfaces.
- **Accent**: one or two visual notes at the entry, hearth, shop sign or focal element.
- **Landscape**: ground materials *outside* the building that visually join it to the terrain.

These are functions, not mandatory six distinct blocks. Several roles can share a family. The approximate share of material is a visual composition decision, not a random distribution instruction.

Examine the thumbnail/squint test: **can the viewer distinguish roof, walls, base and entry before noticing block textures?** If not, change the palette hierarchy.

## 3. Choose a color argument

A valid argument specifies:
1. dominant value (light/medium/dark);
2. hue family (warm stone, cool basalt, earthy browns);
3. contrast location (dark undercroft, pale threshold, roof against sky);
4. texture frequency (quiet plaster vs rugged cliff);
5. story (new wall, repaired corner, wet base, oxidized roof).

Inspect adjacent blocks, not isolated hex codes. Minecraft textures contain multiple colored pixels, light/shadow, connected-block appearances and animated or biome-tinted behavior. Avoid a false precision promise that an RGB number will directly predict their appearance.

### Gradient concepts

A gradient is a **directional arrangement along a physical explanation**:

- **Vertical weathering**: water splash and dampness near the base; lighter, cleaner upper wall when plausible.
- **Vertical strata**: geology or quarry layers caused by a consistent rock history.
- **Load/weight**: dark massive plinth, lighter framed upper stories.
- **Age/repair patch**: localized material change with a visible boundary and construction story.
- **Roof exposure**: runoff below ridges/eaves, accumulated moss in sheltered damp pockets (direction depends on climate and roof form).
- **Atmospheric depth**: an intentional art-directed optical gradient for distant mountains or monuments; clearly distinguish stylistic illusion from geological realism.

Reject arbitrary alternating/checkerboard block patterns unless the wall is explicitly tiled or patterned.

### Keep gradients readable

For a near-viewed cottage, prefer a compact set of compatible textures with **unequal zones and soft, hand-curated boundaries**. For a giant cliff, additional steps may be necessary to avoid color banding over long distances.

Do not prescribe mandatory percentages or random noise. A transition may be:
- low heavy region;
- irregular overlapping middle region;
- clean dominant upper region;
- occasional material islands justified by eroded projections or repairs.

Break straight boundaries where geology/weather demands it, yet keep overall direction recognizable. A gradient without a stable direction turns to visual static. A facade can legitimately be untextured if plaster, paint or formal masonry requires it.

## 4. Authored palette candidates — choose, test and adapt

These **ten study palettes** are starting arguments, not mandatory recipes, randomized mixes or fixed templates. Select exact blocks and their geometry after reviewing the site and game registry.

| Situation / readable result | Main masses | Frame / support | Transition and touchpoints | Risks and checks |
| --- | --- | --- | --- | --- |
| Taiga craftsman's home | stripped_spruce_wood, spruce_planks | spruce_log, cobblestone | mossy_cobblestone only in damp lower areas; stone_bricks at worked entry | dark-on-dark can lose silhouette; test light |
| Damp forge / stonemason | stone_bricks, andesite | spruce_log, cobblestone | cracked_stone_bricks near stress/age; tuff near rubble or soot | large clashing textures; avoid “all blocks everywhere” |
| Alpine slate lodge | stone, tuff or polished_tuff | spruce_log, deepslate_bricks | cobbled_deepslate at lower exposed rock; light trim at threshold | coal-black roof and wall merging |
| Red mesa caravan house | terracotta, red_sandstone | stripped_acacia_log or matching dry timber | smooth_red_sandstone around carefully built openings; coarse_dirt on approach | excessive contrasting orange/red bands |
| Pale desert observatory | sandstone, smooth_sandstone | cut_sandstone or chiseled_sandstone at focal joints | terracotta recesses; deliberately shadowed loggia | featureless flat block or random temple glyphs |
| Riverside market | oak_planks or spruce_planks | oak_log / stone_bricks at quay | cobblestone by water, gravel on unloading ground | wood appearing below permanent floodline |
| Foggy marsh hut | mangrove_planks or spruce_planks | mangrove_log/spruce_log, stone/wood footings | mud, packed_mud, rooted_dirt at wet-ground transitions | floating stilts; muddy material invading clean interior |
| Gothic memorial | stone_bricks, deepslate_tiles | polished_deepslate, stone_brick_wall | tuff, cracked_stone_bricks and local moss in plausible damage | ornamental spires without support |
| Woodland cottage with light infill | calcite, white_terracotta or accessible plaster-like block | stripped_oak_log, oak_planks | stone / cobblestone at base and small worn step | whites blown out in shaders; unrelated stone noise |
| Volcanic watchpost | blackstone, polished_blackstone_bricks | basalt, smooth_basalt | tuff and gravel on ashward slopes; controlled lava-safe accents | texture muddiness, accessibility and lava safety |

**Exact block registry names may vary by edition or mod.** Tuff variants expanded in Minecraft 1.21; check 1.21.1 against the actual target. A palette must be rejected if a required stair, slab, wall or facing block doesn't exist. Replace with a real alternative and reevaluate the silhouette.

## 5. Hand-painted surface plans

Do not say merely “texture the base”; specify *where*.

### Forge south wall

- **Structural beam rhythm** is the dominant dark pattern. Posts occur at supporting corners and the opening, never as floating braces.
- **Central wall** remains mostly quiet and lighter than the roof.
- **Ground contact** changes toward stone and damp patching within a visually limited lower zone.
- **Soot** is localized around the actual flue/vent, not sprayed across all elevations.
- **Window area** is clean enough to focus the eye on work inside.

### Old monastery ruin

- Readable original masonry courses remain.
- Darker rubble gathers **beneath** genuine collapse.
- New moss grows where water would run or pool.
- Broken edges follow gravity and load paths. Do not randomly replace every fifth stone.

### Pine forest trail cut

- Hard stone core on steep inside edge.
- Rubble transition beneath exposed cliff, soil on gentler lower slope.
- Podzol/coarse dirt appears as ground cover beneath conifers and in high-traffic or bare patches.
- Adjacent upper path is compressed earth/gravel, with transition to foliage away from footfall.
- Avoid parallel perfect “stripes” of biome blocks.

## 6. Special handling: slabs, stairs, walls and directional material

Texture continuity isn't only about cube colors. A roof gradient made of full cubes but mismatched stairs may look jagged; a stone foundation gradient can lose weight if a wall block shrinks the silhouette at random. For each chosen family ask:
- Full cube, stair, slab, wall, button, door, fence variant availability?
- Placement state: facing, half, axis, waterlogged, stair shape?
- Texture orientation across adjoining pieces?
- Cross-version stability and compatibility with resource packs?

Do not use “stairs everywhere” to artificially introduce detail.

## 7. Review against anti-patterns

- **Block vomit**: too many materials at equal scale; repair by eliminating competitors and reassigning roles.
- **Checkerboard noise**: regular alternating patches unintentionally become a pattern; repaint with directional clusters.
- **All-over gradients**: every roof, wall, floor and cliff competes; select a hero textured surface and quiet complements.
- **Wrong scale**: a ten-step palette compressed into a five-block-high wall cannot blend smoothly; simplify.
- **Misleading material**: wet moss everywhere in an arid biome or unsupported glass wall in a fort; restore context.
- **Vanilla-only assumption**: modded pack changes color and behavior; reswatch.

Expert judgment includes knowing **when not to texture**. Community critique notes that “more gradient” is not universally better and distance changes whether texture works; see [reference notes](reference-study-and-image-analysis.md).

## 8. Palette acceptance record

For each reviewed build, state:
- Tested game version and resource pack;
- chosen 3–7-ish meaningful material families **or a justified different count**;
- anchor, frame, roof, focal accents and transition direction;
- swatch/test-wall outcome and screenshot paths, or N/O if not observable;
- one rejected material and the reason;
- one verified visible improvement after palette revision.

Do not mark a palette visually verified without actual images/game view.
