# Palette critique exercise — when blocks become noise

This exercise trains *selection*, not random mixing. Ideally construct both sample walls in the exact target version, compare from 6 and 35 blocks away, and then inspect them inside the full facade. Without world access, treat outcomes as hypotheses.

## Commission

A 12-block-high craftsman's workshop wall, 15 blocks long, situated under a dark timber roof on a damp riverbank.

### Version A — an avoidable failure

Candidates tossed together over the entire wall:
- stone
- cobblestone
- mossy_cobblestone
- stone_bricks
- cracked_stone_bricks
- tuff
- calcite
- polished_andesite
- andesite
- gravel
- deepslate
- oak_planks

All blocks appear in similarly sized equal-frequency clusters. The wall appears spotty and loses any primary support rhythm. It is impossible to tell where dampness, age and masonry repair are meant to be located.

**Do not implement Version A as an actual randomized pattern.** It is an error diagnosis.

### Version B — authored fix

Design role-by-role:
1. Foundation: stone_bricks as the dominant worked stone at grade.
2. Secondary rough variation: limited andesite/cobblestone clusters where the wall abuts exposed rock or is damaged.
3. Dampness: mossy_cobblestone only near persistent splash/runoff zones.
4. Structural frame: spruce_log or stripped_spruce_wood spaced around actual openings and load-bearing bays.
5. Quiet upper fields: one stable lighter wall material chosen after swatching; don't invent a plaster-like mod ID.
6. Accent: worn entry sill where the public route meets the facade.

Keep the central wall legible in large areas. A damp patch near river splash should have clear spatial continuity but irregular soft edges, rather than even diagonal stripes. An older wall can include localized stone repairs; preserve coherent course patterns.

### Discussion

Version B is not “better” because it has fewer different IDs mathematically. It is stronger because each material **performs a visible architectural job**. The same number of blocks could work in a large cathedral or cliff if broken into distinct large-scale zones. The right answer depends on scale, view distance and reference.

## Revision exercise

For the actual user's project, document:
- Why this palette direction exists;
- Which original blocks were rejected and why;
- Swatch screenshots in neutral light and at target view distance (if accessible);
- Which visual hierarchy was recovered;
- Whether the adjacent roof, ground and vegetation now compete less.

**Do not claim a specific screenshot was seen without seeing it.**
