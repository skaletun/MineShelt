# Worked commission — make a workshop volumetric, not decorated

**Status:** authored design critique and repair plan. This is not a screenshot of a built Minecraft world, nor a stored Minecraft structure. It demonstrates reasoning. Use [architectural-depth-and-relief.md](../references/architectural-depth-and-relief.md) to adapt it.

## The failure

A small two-story river workshop has a strong color palette but still looks like a painted shoebox:
- rectangular 17×11 external block footprint;
- both stories' walls flush in one plane;
- flat vertical facade with glass directly on the outer surface;
- simple gable roof meeting the wall without eave shadow;
- central exposed door and uniform identical windows;
- a row of decorative trapdoors has been attached to “add detail”;
- the back and side elevations are almost blank.

The site's actual coordinates, wall thickness and modded blocks are **not provided**. Do not fabricate a completed implementation.

## Structural diagnosis

The problem is not insufficient number of block IDs: it is absence of **depth hierarchy**. The building must acquire some purposeful volumes. Plan first:
- river-facing work/loading function;
- dry upstairs storage or living area;
- customer entry off the road;
- protection from weather;
- usable 2nd-floor route;
- safe clearance on narrow side plot.

Propose two distinct solutions, choose the one fitting the actual site.

### Option A: low loading gallery (working riverfront)

Preserve the main gable, but attach a **real narrow covered loading gallery** facing the river, supported on grounded posts or pier structure. Make its entrance/loading opening genuinely usable. Move the glazed workshop window slightly back behind a robust frame. Integrate waterline and platform support.

### Option B: modest urban shopfront (narrow street)

Keep river wall simple but recess the road-facing customer entrance to form a vestibule with an external canopy. At second-floor level, create one narrow projected bay window **connected to the room**, plus carefully aligned load-bearing supports. Relieve the side with the real stairwell's slit window, not random decorations.

If the plot is cramped and street clearance prohibits the bay, choose Option A if riverfront rights allow; otherwise scale back projections and use a strong recessed threshold.

## Selected commission if water access is free

Choose **Option A** because it directly supports the workshop's river trade and avoids a fake second-storey balcony.

### Macro
- Dominant mass remains the two-story workshop.
- The river gallery creates a **distinct lower secondary volume**, not another ornamental strip.
- Chimney is aligned with an actual heating/work hearth and has its own continuous mass.
- The main roof meets a lower gallery roof with an intentionally resolved eave/junction.

### Meso
- A stone plinth stands slightly proud of upper timber wall.
- Timber posts sit in front of a quiet infill plane, connected to a meaningful eave load path.
- A working window is set back behind the post/lintel rhythm.
- A sliding/cargo door opening faces the gallery and is reachable from inside.
- Loading awning posts meet proper foundation/piers.

### Micro
- Stairs/slabs finish sills, eave edges and gallery steps.
- Avoid decorative fence strips every two blocks.
- Favor a calm broad wall behind legible beams.

## Relative facade plan example

For an **illustrative south-facing** gallery, local +Z faces the river, and the main wall at Z=0:
- Z=-1: glazing in framed opening; only after confirming the interior clearance;
- Z=0: structural infill and actual door opening;
- Z=+1: meaningful posts and window sill;
- Z=+2 or more: limited gallery projection supported by grounded piers, *after verifying plot bounds*.

Those are possible layer positions, not final coordinates or a forced block generator. Real portal/window coordinates come from the measured room layout and player interaction requirements.

## Visual repair procedure

1. Remove purposeless surface trapdoors and photograph neutral front view.
2. Check plan and floor section for walkable interior and real gallery loading.
3. Add actual secondary gallery volume, base and supports.
4. Complete secondary roof and underside; do not let it slice the main wall.
5. Align post/beam rhythm to usable windows and floor spans.
6. Recess one working window and rebuild lintel/sill depth.
7. Test entry and route from public road to goods counter to gallery.
8. Compare front, both corners, rear, riverside path and under-gallery views.
9. Fix any unsupported underside, collision, blank side or overdone trim.
10. Capture before/after screenshots in actual Minecraft if access exists.

## Review checklist

- **Distant:** does a clear main workshop plus lower river gallery read without any trim?
- **Mid-range:** can the viewer understand supports, eaves, window recess, approach?
- **Close:** are half-block choices and block states aligned?
- **Back:** is the chimney/roof connection complete?
- **Low-angle:** are projected elements supported beneath?
- **Inside:** can the player interact with working block and walk to the gallery?
- **Site:** do landing elevations connect to water and terrain?

If only a front render looks good and the gallery has no usable access, **reject**. If no runtime exists, mark the result as a design proposal; do not say it was built.

## Lesson

The repaired facade becomes interesting because it actually **does something in 3D**. Surface detailing supports that program instead of manufacturing fake complexity.
