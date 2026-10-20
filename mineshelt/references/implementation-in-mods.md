# Implementing authored Minecraft buildings in mods and worlds

MineShelt does **not** provide a generator. The agent's design is made once, authored deliberately, and realized using whichever **existing construction pipeline** the project supports. Source code, block placements and structure files are delivery mechanisms for a specific architectural composition; they must not decide style, proportions or detail through random assembly.

## Select the actual delivery mode

### A. Live world build

When an agent has authorized access to a running world, block editor, commands or WorldEdit-like operations:
1. Verify edition/version, mod list, world/site, coordinates, protected bounds and permissions.
2. Snapshot or back up the affected region using the project's existing safe practice.
3. Establish a local coordinate frame and direction markers.
4. Place foundational and large structural elements in small visible phases.
5. Observe the result, repair block orientation and collisions, then continue.
6. Check all sides, approach, interior and nighttime conditions.
7. Report the final world name, dimension, origin and extent. If not actually placed, explicitly say so.

A command that reports success is **not** proof of good architecture or proof that Minecraft rendered all blocks as intended.

### B. Authored structure asset

When a mod/world uses a version-appropriate structure asset (for example a structure template or schematic supported by its tools):
1. Determine which structure format the actual target runtime/importer accepts; inspect existing files and conventions.
2. Hand-author the intended composition in an editor/world or through deterministic exact positions from a reviewed block plan. Do not replace this step with a procedural layout algorithm.
3. Preserve orientation, palette/block IDs and states, air/void semantics, structure block entity data, size, origin and bounding volume as required by that **specific format**.
4. Verify that it imports or loads in the intended version. Binary NBT or schematic extensions alone do not prove compatibility.
5. Inspect the placed asset at all allowed rotations/mirrors. Directional stairs, doors, beds, logs, banners and waterlogged states may require special care.
6. Store it in the actual mod data/resource path required by the loader and project layout. Infer nothing from another version's tutorials.

An authored structure can be integrated into worldgen **without creating a structure generator**. World placement selection is separate from architectural authorship.

### C. Existing mod repository

Inspect before modifying:
- build system, loader, Minecraft target version, mappings, data/resource layout;
- registries and dependency mods providing blocks;
- existing classes controlling structure loading or placement;
- data packs, structure templates, biome configuration and worldgen hooks;
- CI, unit/game tests, integration tests and available client development launch tasks.

Then:
1. Identify the minimally invasive integration path in **this** repo: an authored structure asset, explicit placement of handcrafted geometry, an existing editor/export pipeline or a data-driven worldgen structure.
2. State the structure's footprint, origin and height; establish coordinate transforms and bounds. Verify the rotation/mirror semantics of the target API.
3. Confirm every block ID and state exists in the configured registry. Use real mod IDs, not guessed identifiers.
4. Keep block entities only where necessary; preserve or initialize required data. Avoid inventing unknown NBT schemas.
5. Guard world writes: protect existing blocks or follow user-specified replacement policy; handle air, terrain and fluid transitions deliberately.
6. Consider chunk boundaries, required loaded chunks, block update flags, main-thread constraints, worldgen context, and failure rollback as appropriate to the actual APIs.
7. Validate behavior with the project's build and test commands, then launch a client or test world when possible.
8. Inspect visual fidelity in the game. Rebuild or replace any authored asset after architectural changes so source and output agree.

Do not fabricate methods from NeoForge, Fabric, Forge, Mojang mappings or WorldEdit. Version-specific calls should be grounded in the target source and current docs. API migration can affect registry, serialization, placement and worldgen behavior.

## Worldgen integration is not design generation

A handcrafted, designed building may appear in worldgen through a placement system, but architectural content must remain intentionally authored. Keep distinct:
- **Design**: form, materials, rooms, facade, detail, terrain joins.
- **Authored artifact**: exact human-curated structure or build.
- **Placement**: choosing world positions/rotations compatible with the target framework.

If the user requests varied villages, design a coherent family of **individually art-directed structures** with distinct roles instead of a single procedural shape with randomized roofs.

## Rotation, state and connectivity

Always test directional and connected states:
- stairs, slabs, trapdoors and doors (facing, half, hinge, open, shape);
- log axes, glazed terracotta orientation, barrels/furnaces/chests;
- walls, fences, panes and redstone connectivity;
- beds and multi-block combinations;
- fluid states, leaves and waterlogging;
- modded custom blocks with unusual neighbor updates;
- block entities and signs with content or inventory.

Rotation bugs can visually destroy otherwise strong architecture. Verify actual world state after transformations instead of assuming all state types rotate identically.

## Structure placement safety

Treat worlds and saves as user data:
- prefer a disposable test world during development;
- never silently overwrite player creations or protected blocks;
- understand target block replacement policy and limits;
- avoid uncontrolled fill/replace over huge areas;
- prevent large one-tick placement loads when the game/runtime can't tolerate them;
- monitor unwanted block updates, lighting or fluid cascades where relevant;
- keep construction reproducible with explicit inputs and safe restoration paths.

Do not advertise crash-free or lag-free behavior without measurement.

## Deliver the right artifacts

For source modifications, include real files changed, test commands and their outcomes. For live builds, include world/coordinates/dimension/screenshots. For a text-only session, deliver a **construction-ready authored plan** with exact decisions and clear implementation boundaries; do not present that plan as an NBT file.

## Mod-release verification matrix

| Check | Evidence |
| --- | --- |
| Target version and loader | version properties, build metadata |
| Existing structural integration path | inspected source paths |
| Blocks and states valid | registry/config and game checks |
| Placed building actually looks as designed | screenshots across required views |
| Rotation and mirroring | placed and compared variants, if supported |
| Entry, floors, light, collisions | in-game walkthrough |
| Existing saves/world protected | tests or explicit safe procedure |
| Performance acceptable | measured test or clearly noted as not measured |
| Tests/build | actual commands and output |

A passing Gradle build covers none of the visual rows by itself.
