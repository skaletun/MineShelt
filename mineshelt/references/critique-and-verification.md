# Architectural critique, repair and proof

A serious Minecraft build undergoes design review. Avoid empty praise, invented score inflation and the habit of answering “complete” immediately after a successful export.

## Review order — highest impact first

1. **Purpose and identity**: can a viewer infer what the building is, and does it honor the brief?
2. **Silhouette and primary proportions**: readable at distance; strong profile and hierarchy?
2a. **Actual building relief**: real projected/recessed geometry, depth of sections, framed openings, supported undercuts and fully resolved side/rear elevations?
3. **Construction plausibility**: roof-to-wall joints, supports, entrances, terrain contact and extensions coherent?
4. **Material language**: coherent palette and restrained accents, convincing age?
5. **Gameplay/interior**: routes and clearances functional; rooms serve purpose?
6. **Site composition**: approaches, landscape, drainage, paths and surrounding structures linked?
7. **Finish quality**: orientation errors, holes, floating items, awkward clipping, lighting, clutter and repeated patterns?
8. **Professional palette craft**: have actual swatches been evaluated, and do terrain/wall gradients have direction, material roles and quiet zones?
9. **Terraforming craft**: are major ridge profiles, cliff spines, bank transitions, paths and planted tree silhouettes authored with ecological/geological logic rather than noise?

For building-heavy commissions, separately assess **volumetric depth, wall-section geometry, actual shadows, supported projections, complete side/rear elevations, and interior clearances**. For palette or terrain-heavy commissions, expand the rubric with separately evidenced **palette craft, terrain geometry and vegetation craft** dimensions; do not disguise failures in those dimensions by scoring an unrelated roof or interior as excellent.

Never start with lantern density or pot placement while a roof or foundation is wrong.

## Evidence capture

At a minimum, when runtime/screenshot tools exist, collect:
- designated hero exterior view;
- front and rear;
- both side elevations;
- high three-quarter showing roofs and site;
- player-eye approach to entrance;
- primary interior + secondary floor/stairs;
- night image if lights or atmosphere matter.

Use roughly repeatable positions and daylight for before/after comparisons. Prefer unaltered Minecraft screenshots; don't use a generated artistic image as proof of a finished in-game build.

If 360-degree screenshots are unavailable, state exactly what was inspected.

## Red flags and prescribed corrections

| Observable defect | Likely root cause | Corrective action |
| --- | --- | --- |
| Looks like a box with add-ons | weak volumes and section | redesign dominant roof, secondary mass and door relationship |
| Flat rear/side and only decorated front | no authored wall section or genuine relief | redesign elevations/section, inset openings and structural volumes; inspect both 45° corners |
| Bay or balcony floats, interior blocked | relief lacks load path and clearance budget | change section/supports or remove mass; verify underside and usable passage |
| Jagged random facade | texture noise | simplify palette, align structural bays, localize weathering |
| Roof is taller than all usable rooms | massing not tied to program | reconsider span, pitch, attic use, eave height |
| Floating porch / clipped foundation | landscape ignored | design actual load path and stepped support |
| Every building in settlement looks identical | one generic archetype reused | diversify roles, plan shapes, public/private rhythms |
| Decorative beam ends nowhere | fake structure | connect to posts or remove |
| Windows conflict with upstairs floor | facade before section | coordinate plan, elevation and floor height |
| Flat exterior around elaborate house | missing site pass | integrate paths, planting, retaining and utilities |
| Roof states break when rotated | untested placement transform | inspect state rotation, re-place and compare |
| Interior is impassable | model optimized for exterior screenshot | free circulation, adjust room scale and furnishings |
| AI-looking “busy” surface | uncontrolled microdetail | reduce density, choose one focal craft area |
| Ruin is random Swiss cheese | no history/collapse logic | restore readable original volume and plausible damage |

## Quality rubric

Assign scores from 0 to 5 per dimension *based on visible or directly inspected evidence*, with these **indicative weights**:

| Dimension | Weight |
| --- | ---: |
| Mass, silhouette, composition | 25 |
| Construction clarity and roof logic | 20 |
| Context, terrain, story | 15 |
| Materials and visual rhythm | 15 |
| Interior and usability | 15 |
| Finish and technical correctness | 10 |

Weighted score, if useful, is the sum of (dimension_score / 5 × weight). **A numerical result is not a factual quality guarantee.** If a dimension is unobserved, mark N/O and do not silently score it as a 5 or treat an incomplete total as comparable.

Hard blockers, regardless of numeric score:
- known destructive world modification outside authorized site;
- fundamental Minecraft version/block registry failure;
- inaccessible critical area where use is required;
- floating/visibly unsupported primary structure unless deliberate fantasy concept;
- major clipped/open roof or obvious unfinished major facade;
- the requested structure not actually present in the designated deliverable;
- reporting screenshots or tests that were never produced.

## Mandatory revision technique

For every visible meaningful defect:
1. Identify it precisely (example: west eave floats 2 blocks above the support line).
2. Trace it to cause (overhang chosen after supports).
3. Make the **smallest architectural repair that actually solves the cause** (change eave span and add aligned bracket/posts; not more decoration).
4. Recheck at the same view.
5. Check collateral effects on other sides/interior/roof.

A builder can reject their own first solution. Show what changed and why.

## False confidence rules

Do not claim:
- “perfectly human-built” based only on text;
- screenshots examined if none existed;
- all rotations work after one static placement;
- zero performance impact absent measurements;
- Minecraft build works because YAML/Java/JSON parses;
- a file was created if it was only described;
- no bugs if testing scope was limited.

When tools are not available, give a plan and an explicit list of unverified visual/technical properties.

## Completion language

- **Built and inspected**: actual world construction + real in-game observation.
- **Implemented, visually unverified**: code/structure files created and technical checks run, but no Minecraft visual access.
- **Authored blueprint**: exact plan and hand-authored construction instructions; not placed.
- **Concept only**: design direction and studies, not construction-ready.

No score, test result or confidence claim should override that distinction.
