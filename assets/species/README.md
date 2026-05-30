# Species size icon

Section 2.2 uses a **single shared silhouette** for every species row (six sankey-aligned categories).

| File | Purpose |
|------|---------|
| `shark-icon.svg` | Source artwork; the live chart embeds an equivalent path in `charts/section-2/species_size_icons.vg.json` |

To swap the artwork, update the path in the Vega spec (or replace this SVG and re-export the path). Width scales to each species' median recorded length on the metre axis.
