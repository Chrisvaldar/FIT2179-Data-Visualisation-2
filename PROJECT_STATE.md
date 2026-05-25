# FIT2179 Data Visualisation 2, Internal Project State

## Assignment Context

FIT2179 Data Visualisation 2, Semester 1 2026. Tutor is Bruno, applied group Tuesday 12 to 2.
The assignment requires a substantial number of different idioms, two data sources, at least one map, and a coherent narrative. Submission is due Friday Week 12, 29 May 2026, 11:55 PM.
Tutor feedback on file: use more map types, choropleth is good, more is better.

---

## Plan and Reference Documents

- **Plan document:** `shark_attack_plan.md` (sections 1.x through 5.x, sixteen candidate charts).
- **Assignment brief:** `references/assignment_brief_and_examples/(Version 1.2) FIT2179 Data Visualisation 2 (2).pdf`.
- **Unit material:** `references/unit_material/`. Most relevant for this project are Week 8 Map Idioms, Week 9 Studio (interactivity, bubble plot, sliders, tooltips, legend selection), Week 10 Studio (vconcat brushing, multiple coordinated views, zoomable choropleth with time slider, small multiples via repeat or facet), Week 11 Typography, and the Storytelling course notes.
- **Vega-Lite docs:** `references/vegalite-docs/` mirrors the official documentation for composition, encoding, mark, parameter, transform, types, and view.
- **Inspiration:** `references/unit_material/The Data Visualisation Catalogue.html` for idiom selection when filling chart slots.

---

## Topic

Shark incidents in Australia (1791 to 2022), with a secondary comparison against California (USA), 1950 to 2022.

---

## Data Sources

### Primary, Australian Shark Incident Database (ASID)
- **Files:** `data/base_data/locdat2.txt`, `injurydat.txt`, `timedb2.txt` (overlapping subsets of the same incidents).
- **URL:** https://github.com/cjabradshaw/AustralianSharkIncidentDatabase/tree/main/data
- **Coverage:** 1,203 Australian incidents, 1791 to 2022.
- **Key fields:** Latitude, Longitude, State, Location, Shark.common.name, Shark.length.m, Provoked.unprovoked, Victim.activity, Injury.location, Injury.severity, Victim.gender, Victim.age, Time.of.incident, Incident.year, Incident.month, Incident.day, Victim.injury.

### Secondary, California White Shark Incidents
- **File:** `data/base_data/SharkIncidents_1950_2022_220302.xlsx`.
- **Coverage:** 220 California incidents, 1950 to 2022.
- **Key fields:** Latitude, Longitude, County, Activity, Injury, Species, Date.

---

## Processed CSV Files (all in `data/wrangled_data/`)

| File | Description |
|------|-------------|
| `dot_map.csv` | 1,196 rows. Fields: Incident.year, Latitude, Longitude, Victim.injury, Species.clean, Activity.clean, State, Location, Provoked.unprovoked, Decade |
| `state_choropleth.csv` | 7 rows. Fields: State, total, fatal, fatal_rate |
| `decade_timeline.csv` | 23 rows. Fields: Decade, total, fatal, injured, uninjured, population_m, rate_per_million |
| `species_bubble.csv` | 12 rows. Fields: Species.clean, count, fatal, provoked, median_length, mean_length, length_count, fatal_rate, provoked_rate |
| `activity_risk.csv` | 8 rows. Fields: Activity.clean, count, fatal, injured, fatal_rate, risk_score |
| `seasonal_heatmap.csv` | 79 rows. Fields: State, Incident.month, Month.name, count, normalised |
| `radial_time.csv` | 24 rows. Fields: Hour, total, fatal |
| `body_region.csv` | 9 rows. Fields: Body.region, Victim.injury, count, total, pct |
| `age_histogram.csv` | 40 rows. Fields: age_bin, Victim.injury, count |
| `gender_outcome.csv` | 6 rows. Fields: Victim.gender, Victim.injury, count |
| `provoked_outcome.csv` | 6 rows. Fields: Provoked.unprovoked, Victim.injury, count, total, pct |
| `wobbegong_activity.csv` | 13 rows. Fields: Activity.clean, Victim.injury, count |
| `length_injury.csv` | 32 rows. Fields: length_bin, length_label, Victim.injury, count |
| `ca_dot_map.csv` | 202 rows. Fields: Incident.year, Latitude, Longitude, Victim.injury, Activity.clean, County, Decade |
| `decade_fatality_comparison.csv` | 8 rows. Fields: Decade, AU_fatal_rate, CA_fatal_rate |
| `activity_comparison.csv` | 8 rows. Fields: Activity.clean, AU_count, AU_pct, CA_count, CA_pct |

---

## TopoJSON Files (in `data/topojson/`)

| File | Object name | Notes |
|------|-------------|-------|
| `australia.json` | `australia` | Country outline only, used for base map layer |
| `australia_states.json` | `australia_states` | State boundaries from Natural Earth via Mapshaper. Join key: `iso_3166_2` property (e.g. `AU-NSW`). Strip `AU-` prefix with `slice(datum.properties.iso_3166_2, 3)` to match CSV abbreviations |

---

## Charts: Current Status

The plan in `shark_attack_plan.md` lists sixteen candidate charts (sections 1.1 through 5.3). The agreed final deliverable is **at least ten polished charts**, not all sixteen. The rule of thumb: prefer custom or impressive idioms (custom SVG, polar, paired views, small multiples, brushed multi-view) over basic bar or line where there is overlap. Final ten-chart scope is deferred until the existing six are polished to top-notch.

### Done, polish pass complete

All callout-box annotations were stripped from the six built charts on 25 May 2026; the annotation approach for the assignment is being rethought from scratch. Inline map labels and data-point labels (state names, state totals/rates at lat/lon, end-of-bar totals, lollipop count and rate labels, inside-bubble species names) were kept because they are data labels, not callouts.

| File | Section | Idiom | Polish notes |
|------|---------|-------|----------------|
| `dot_map.vg.json` | 1.1 | Filterable dot map | Sand-fill base, white state outlines, ocean-blue background rect, embedded ghosted state labels at centroids, decade dropdown plus outcome radio (all/fatal/injured/uninjured) |
| `state_choropleth.vg.json` | 1.2 | Two side-by-side choropleths (volume + fatal rate) | hconcat of two 480x520 maps, projection `center: [120, -27]` `scale: 540` (extra height fixes the previous Tasmania clipping). Left blues for total, right reds for fatal rate. Five large states get inline halo labels stacked vertically (state name above, value below, on neighbouring latitudes). Small states VIC and TAS currently have no inline label, they fit inside their cell tightly and the previous callouts were removed. Lord Howe Island and Macquarie Island filtered from the topojson |
| `decade_timeline.vg.json` | 1.3 | Stacked area + rate-per-million line | Radio toggle between count and rate. Y-axis title switches per metric mode. Stacked area for count by outcome, single navy line + soft area for rate per million (1880 onward where population data is reliable) |
| `species_bubble.vg.json` | 2.1 | hconcat overview + zoom inset, inside-bubble labels | Left panel shows true positions for all twelve species. Right panel zooms into the seven small or rare species at 0% fatal so each can be read. Click-to-highlight via `select: point` shared across both panels. Colour ramp switched from `oranges` to `purples` to avoid clashing with the injured outcome colour. Species names sit **inside** the bubbles for the four headline species (Tiger, White, Bull, Whaler) using bold white text with a dark halo |
| `wobbegong_activity.vg.json` | 2.2 | Stacked bar | Bars sorted by total via joinaggregate then sort op:max. Inline activity totals at end of each bar. Legend includes a fatal swatch labelled "Fatal (never observed)" to make the absence visible |
| `activity_risk.vg.json` | 3.1 | Paired (butterfly) lollipop | Hardcoded sort array fixes the cross-layer y-axis union issue. Count labels at left of each circle, rate labels at right (now shown on every row) |

### Candidate, not yet built (final selection deferred, must total ten or more once decided)

| Section | Chart | CSV ready | Idiom note |
|---------|-------|-----------|------------|
| 2.3 | Shark length vs injury severity | `length_injury.csv` | Beeswarm or strip plot |
| 3.2 | Seasonal heatmap (state x month) | `seasonal_heatmap.csv` | Heatmap, normalised within state |
| 3.3 | Radial time-of-day clock | `radial_time.csv` | Radial bar, custom polar, HD differentiator |
| 3.4 | Body region silhouette heatmap | `body_region.csv` | Custom SVG body diagram, HD differentiator |
| 4.1 | Gender isotype/unit chart | `gender_outcome.csv` | Pictogram, Week 11 alignment with iconography |
| 4.2 | Age histogram (fatal vs non-fatal) | `age_histogram.csv` | Mirrored histogram |
| 4.3 | Provoked vs unprovoked | `provoked_outcome.csv` | Stacked proportional bar |
| 5.1 | AU vs CA activity comparison | `activity_comparison.csv` | Grouped or mirrored bar |
| 5.2 | AU vs CA fatality rate by decade | `decade_fatality_comparison.csv` | Dual line |
| 5.3 | CA dot map | `ca_dot_map.csv` | Dot map, candidate for `repeat` small multiples paired with AU |

---

## Formatting and Technical Conventions

### Field name escaping
Vega-Lite parses dots in field names as property path separators. All field names containing dots MUST be escaped with double backslash in the spec:

```json
{ "field": "Victim\\.injury" }
{ "field": "Incident\\.year" }
{ "field": "Species\\.clean" }
{ "field": "Activity\\.clean" }
{ "field": "Provoked\\.unprovoked" }
{ "field": "Shark\\.common\\.name" }
{ "field": "Body\\.region" }
{ "field": "Month\\.name" }
{ "field": "Victim\\.gender" }
```

Applies in encoding, tooltip, transform filter, calculate, lookup, sort, every reference.

### Colour conventions
- Fatal: `#c0392b` (red)
- Injured: `#e67e22` (orange)
- Uninjured: `#7f8c8d` (grey)

For sequential ramps where outcome is not the encoded variable, prefer single-hue ramps that do NOT collide with the outcome triad: `blues` for volume, `purples` or `viridis` for percent-derived metrics, `greens` for normalised intensity. Avoid the `oranges` ramp because it collides with the injured outcome colour.

For the AU vs CA comparison, AU uses a deep ocean navy `#1a4a63`, CA uses a sand `#c8a96e`. These match the page palette in `index.html`.

### Map projection (locked)
Every map uses:
```json
"projection": {
  "type": "mercator",
  "center": [133, -27],
  "scale": 850
}
```
For Section 5 California-only maps the projection becomes:
```json
"projection": {
  "type": "mercator",
  "center": [-120, 36],
  "scale": 850
}
```
For AU vs CA small multiples via `repeat`, both panels share the same `scale` (850) so the geographic spread is honestly comparable.

### Map dimensions
- Choropleth: 700 by 600.
- Dot map: 700 by 700.
- Small-multiple maps inside `repeat`: 460 by 380 each.

### Map projection quirk worth knowing
At full canvas size (~720x640) the AU mercator with `center: [133, -27]` and `scale: 850` fits the country exactly as expected. When the canvas shrinks (such as side-by-side panels at 480x520) the headless renderer sometimes places the centre too far east and clips Western Australia. The `state_choropleth.vg.json` workaround uses `center: [120, -27]` with `scale: 540` and `height: 520` (extra height keeps Tasmania from being cut off at the bottom). Side-effect: VIC and TAS labels become tight inside the cell, so they are pulled out as pixel-positioned callout boxes anchored in the Bass Strait and Tasman Sea respectively. If a future map is clipped, push the centre west before reaching for `fit`, and prefer extra `height` over a smaller `scale` because reducing scale also shrinks state labels.

### Writing conventions
- **No em dashes**, no double dashes anywhere. Use commas, colons, semicolons, or start a new sentence.
- **Sentence case** for titles.
- **Insight-first subtitles**: subtitles state the key takeaway, not the chart structure. Bad: "Shark incidents per state". Good: "NSW leads in raw numbers, but QLD and SA are the most dangerous".
- **No jargon**: assume the average Australian audience without statistical training.

### Narration convention (mandatory for every chart in `index.html`)
Every chart appears in `index.html` accompanied by:
1. The chart itself inside `.vis-wrap`.
2. An editorial lede paragraph (`<p class="chart-lede">`) **immediately below** the chart that delivers the headline insight in human prose with specific values from the data.
3. A figure caption (`<p class="chart-caption">`) under the lede that documents the chart construction (idiom used, encoding rationale, interactivity).
4. Section intros at the top of each major section that set up the next two or three figures.

The lede and caption are both **below** the chart. Editorial framing above each chart was tried and rejected: readers process the visual first, then want the takeaway and the construction notes underneath. Lede has a 2 px ocean-navy top border and the caption has a thin neutral top border so the two stack visually.

All narration is sentence-case prose, no em dashes, no jargon, and follows the storytelling principles in the unit's Storytelling with Data course notes.

### Interactivity philosophy
The page must demonstrate a substantial range of meaningful interactivity (not interactivity for its own sake). Drawn from Week 9 and Week 10 studios:
- **Filtering controls:** binding select, binding radio, binding range. Already used on the dot map and choropleth.
- **Cross-view brushing (Week 10 Studio idiom):** an interval brush on a small chart filters a larger chart. Plan to add between the decade timeline and the dot map.
- **Legend selections:** `select: "point"` on a colour or shape encoding allows click-to-highlight. Plan for the species bubble.
- **Click-to-filter drilldown:** click a body region in the silhouette to filter another chart. Plan for the body region heatmap.
- **Small multiples via `repeat`:** for the AU vs CA comparison.

Interactivity that adds zero analytical value (pan/zoom on a static dataset, redundant tooltips that just repeat axis labels) is not used.

### Vega-Lite version (locked, v6)
- All specs declare `"$schema": "https://vega.github.io/schema/vega-lite/v6.json"`.
- `index.html` loads matching CDN versions:
  ```html
  <script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-lite@6"></script>
  <script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>
  ```
- The schema URL and the loaded library version must always agree. If a future spec needs a v5 only feature, downgrade both, do not mix.

### v6 idioms learned during the polish pass

- **`dy` and `dx` are mark properties, not encoding channels in v6.** Setting `encoding.dy` is silently dropped. Use `mark.dy` and `mark.yOffset` instead.
- **`fontWeight` and `fontStyle` are not encoding channels either.** To conditionally style text, split into multiple text marks with different mark properties rather than using `encoding.fontWeight: { condition: ... }`.
- **`groupby` in transforms uses literal field names, not the encoding-channel escape.** A field called `Activity.clean` in the data must be referenced via `datum['Activity.clean']` inside `calculate`, then groupby uses the renamed flat field. Do not write `groupby: ["Activity\\.clean"]`, that fails because the runtime tries to access `datum.Activity.clean` as a nested path.
- **Cross-layer y-axis sort arrays get dropped when domains are unioned.** When a layered chart has the same y nominal field across layers, the only sort ops vega-lite is willing to union-merge are `count`, `min`, and `max`. Use `sort: { field: "<col>", op: "max", order: "descending" }` rather than the array form, or keep all secondary layers free of an explicit sort and let them inherit.
- **`hconcat` children with a top-level `params` selection collide.** A selection declared at the parent level is copied into both children's signal namespaces, producing a duplicate-signal-name error. Declare the selection inside one specific child mark's `params` and reference it elsewhere by name, or use `resolve: { legend: shared }` to keep shared scales clean.
- **Mark-only specs (no encoding) crash the v6 normaliser.** A spec with `mark: { ... }` and no `encoding` block triggers `Cannot read properties of undefined (reading 'shape')` in v6. Always include an `encoding` block, even if it just maps to `field` references in a single inline data row. For pixel-positioned annotations (rect, text, rule with no projection), set `scale: null` and `axis: null` on the encoded x and y so vega-lite uses the raw pixel value as-is.
- **Vega-Lite `rect` does not accept `latitude`/`longitude`.** Geographic callout boxes must be positioned via pixel x/y with `scale: null` on both encoding channels. The accompanying leader rule and label can use either pixel coordinates (consistent with the rect) or projection coordinates (better for moving with the map). Pixel coordinates are simpler when the projection is fixed.
- **Inline state labels overlap when stacked via `yOffset` in geographic projection.** The fix is to give each text layer a slightly different `latitude` (1 to 1.5 degrees apart) instead of one shared lat with `yOffset` per layer. Mercator y-spacing of one degree at typical AU choropleth scales (540) is roughly 9.5 px, enough room for a 12 px label and an 11 px value to sit cleanly stacked.

### Embed alignment in `index.html`
Each chart sits inside a `.chart-block` card with this structure:
```html
<div class="chart-block full-width">
  <div class="vis-wrap"><div id="vis-foo"></div></div>
  <p class="chart-lede">...editorial paragraph with concrete values...</p>
  <p class="chart-caption">...figure caption documenting construction...</p>
</div>
```
The `.vis-wrap` div is `display: flex; justify-content: center;`. The Vega-Embed override CSS centres the embed canvas, the bindings form, and the SVG horizontally inside it. The lede has a 2 px ocean-navy `border-top`, the caption has a thin neutral `border-top`, and both sit left-aligned at a 820 px reading width below the chart.

### Data paths
All data files referenced as `"url": "data/wrangled_data/filename.csv"` or `"url": "data/topojson/filename.json"`. The local server runs from the project root with `python -m http.server 8000`.

### No Node.js / npm
This project does **not** use `node_modules`, `package.json`, or npm. Vega, Vega-Lite, and Vega-Embed load from jsDelivr in `index.html`. Data wrangling uses Python scripts in `scripts/`. Do not run `npm install` in this repo.

---

## HTML File

`index.html` embeds charts using `vegaEmbed`. Page palette (locked):
- Ocean navy `#0d2b3e`, ocean mid `#1a4a63`, ocean light `#2c6e8a`.
- Sand `#c8a96e`, sand light `#e8d9b8`, sand pale `#f5f0e6`.
- Blood `#9b2226`, blood light `#c0392b` (matches the fatal outcome).
- Foam `#fafaf7`, slate `#4a6274`.

Type pairing (locked): Playfair Display (serif, display weights 700 and 900) for hero title, section titles, and stat-pill numerals. Source Sans 3 (sans, weights 300, 400, 600) for everything else. Both loaded from Google Fonts.

Layout: single-column, max width 1160 px, fits a small laptop without horizontal scrolling. Section dividers are thin rules, not full bars. Each chart sits in a `.chart-block` with a top editorial paragraph, the chart, and a figure caption.

---

## Submission Checklist

- [ ] Ten or more polished charts on the page.
- [ ] At least one geographic map (currently two, dot map and choropleth).
- [ ] Two data sources visibly compared (Section 5).
- [ ] Hand-drawn sketch (PDF) linked from the repo. Digital sketches score zero.
- [ ] All Vega-Lite JSON specs human readable and committed to the same GitHub repo as the page.
- [ ] Page hosted on GitHub Pages, publicly accessible.
- [ ] Page metadata: author name, date, data sources cited.
- [ ] 500 word write-up submitted on Moodle covering domain, who/what/why, and how (idioms and rationale).
- [ ] No em dashes, no jargon, all narration grammatically correct.
