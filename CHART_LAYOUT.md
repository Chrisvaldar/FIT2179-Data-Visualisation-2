# Chart layout & alignment guide

This document captures layout, typography, and embed conventions for the dashboard. Follow it when adding or refactoring charts so every figure lines up with its title, controls, and prose below.

---

## Core principle: one vertical column

Every chart block should read as a single aligned column inside the white card:

```
┌─ chart-block (card) ─────────────────────────────┐
│  Title (left-aligned)                              │
│  Chart / controls                                │
│  ─────────── ocean separator ───────────         │
│  chart-lede (takeaway prose)                     │
└──────────────────────────────────────────────────┘
```

**Left edges must match.** The Vega title, the plot area, bound controls (dropdowns), and the text below should all start on the same vertical line. Avoid layouts where the chart is narrower and centred while the prose spans the full card—that looks broken.

**Right edges should match where possible.** Full-width charts (dot map, choropleth pair) use the full card content width. Fixed-width charts (timeline, wobbegong, activity risk) use a capped embed centred in the card, with prose still spanning the full card width (see Pattern C).

**Left alignment vs centred chart.** Block titles and prose always share the same left edge via HTML `.chart-header`. Chart embeds may be full-width, left-aligned, or centred independently.

---

## Page & card sizing

| Token | Value | Notes |
|-------|-------|-------|
| `--max-width` | `1160px` | Main page column |
| Page padding | `0 40px 80px` | Horizontal inset |
| `.chart-block` padding | `32px 36px 28px` | Inner card padding |
| Usable card width | ~1088px | Page width minus page + card padding |

Default card uses `overflow: hidden`. Charts with annotations or overflowing labels use modifier classes that set `overflow: visible` (see below).

---

## HTML structure (required pattern)

Each figure lives in a `.chart-block.full-width` with layout modifiers:

```html
<div class="chart-block full-width chart-block--split-maps chart-block--{type}">
  <div class="chart-header">
    <div class="chart-header__title">Figure title</div>
  </div>
  <div class="vis-wrap">
    <!-- single embed OR choropleth-grid -->
  </div>
  <p class="chart-lede">…</p>
</div>
```

### Layout modifier classes

| Class | Use for | Behaviour |
|-------|---------|-----------|
| `chart-block--split-maps` | All Section 1 full-width figures | Prose (`chart-lede`, `chart-caption`) uses full card width (`max-width: none`). Base `overflow: visible`. |
| `chart-block--dot-map` | Figure 1.1 dot map | Chart container stretches to **full card width**. |
| `chart-block--choropleth` | Figure 1.2 state maps | Two-column grid, each panel `width: 100%`. Tighter gap before prose (see spacing). |
| `chart-block--timeline` | Figure 1.3 decade timeline | Chart embed max **1000px** wide, centred. `overflow: visible` on embed wrappers so annotations are not clipped. |
| `chart-block--sankey` | Figure 2.1 species sankey | Vega embed max **1000px** wide, **left-aligned** with title and prose. |
| `chart-block--species-size` | Figure 2.2 species size icons | Chart embed max **1000px** wide, **left-aligned**. |
| `chart-block--activity` | Figure 3.1 activity butterfly | hconcat embed max **1000px** wide, **centred** in the card. |
| `chart-block--radial-clock` | Figure 3.2 radial time clock | Square embed max **560px** wide, **centred** in the card. |
| `chart-block--gender-isotype` | Figure 4.1 gender isotype | Chart embed max **1000px** wide, **centred** in the card. |
| `chart-block--age-ridge` | Figure 4.2 age mirror ridge | Chart embed max **1000px** wide, **centred** in the card. |
| `chart-block--comparison-maps` | Figure 5.1 NSW vs California maps | Two stacked full-width map embeds with shared HTML filters. |
| `chart-block--outcome-comparison` | Figure 5.2 outcome comparison | Chart embed max **1000px** wide, **centred** in the card. |

Legacy `chart-block--820` (820px centred column) is **not** used for Section 1 anymore. Do not use it for new charts unless you intentionally want a narrow centred column.

---

## Three layout patterns (reference implementations)

### Pattern A — Full-width single chart (Figure 1.1: dot map)

**HTML classes:** `chart-block--split-maps chart-block--dot-map`

```html
<div class="chart-header">
  <div class="chart-header__title">Every shark incident in Australia, 1791 to 2022</div>
</div>
<div class="vis-wrap"><div id="vis-dot-map"></div></div>
```

**Vega-Lite (`dot_map.vg.json`):** no block `title` in the spec.

```json
"width": "container",
"height": 640,
"autosize": { "type": "pad", "contains": "padding", "resize": true },
"padding": { "bottom": 12 }
```

**Map projection:** fixed scale — do **not** scale projection with container width. Only the ocean background rect should grow wider.

```json
"projection": {
  "type": "mercator",
  "center": [133, -27],
  "scale": 850
}
```

**Do not use** `autosize: { type: "fit" }` on geographic charts — it zooms the map and clips Tasmania.

**Controls:** `<select>` dropdowns (not radio buttons). Binds render **below** the SVG via vega-embed — use `padding.bottom: 28` for the in-chart outcome legend only, not extra space for binds.

**Legend:** In-chart at bottom with **title on its own row**, items on the row below (`titleOrient: "top"`). Outcome key also appears in the page-level legend bar (same stacked layout).

---

### Pattern B — Two equal columns (Figure 1.2: choropleth)

**Do not use Vega-Lite `hconcat` with responsive width** — it breaks easily. Use **two HTML containers** and **two separate `.vg.json` files**.

**HTML:**

```html
<div class="chart-header">
  <div class="chart-header__title">…</div>
</div>
<div class="vis-wrap">
  <div class="choropleth-grid">
    <div class="choropleth-panel"><div id="vis-choropleth-rate"></div></div>
    <div class="choropleth-panel"><div id="vis-choropleth-fatal"></div></div>
  </div>
</div>
```

**CSS grid:** `grid-template-columns: 1fr 1fr; gap: 20px; width: 100%`

**Shared block title** lives in HTML (`.chart-header`). See **Block title styling** — not the same size as narration prose.

**Each panel spec** (`state_choropleth_rate.vg.json`, `state_choropleth_fatal.vg.json`):

```json
"width": "container",
"height": 380,
"autosize": { "type": "pad", "contains": "padding", "resize": true },
"padding": { "bottom": 4 }
```

- Panel title: 12px bold, `#1a2530`, `anchor: "middle"`
- Legend: bottom, offset 4
- Embed with `renderer: "svg"`

**Spacing to prose:** `chart-lede` uses tight spacing (`margin-top: 4px`, `padding-top: 8px`) — no large gap between legends and the blue separator.

---

### Pattern C — Fixed-width single chart (Figure 1.3: timeline)

**HTML classes:** `chart-block--split-maps chart-block--timeline`

```html
<div class="chart-header">
  <div class="chart-header__title">Shark incidents per decade, 1790s to 2020s</div>
</div>
<div class="vis-wrap"><div id="vis-timeline"></div></div>
```

**Vega-Lite (`decade_timeline.vg.json`):** no block `title` in the spec.

```json
"width": 1000,
"height": 380,
"padding": { "top": 44, "right": 12, "bottom": 12 },
"config": {
  "view": { "stroke": "transparent", "clip": false }
}
```

- CSS caps embed at `max-width: 1000px` and centres it in the card
- Prose below still spans full card width
- Y-axis headroom: count mode `[0, 280]`, rate mode `[0, 235]` — leave room for labels above peaks
- X-axis domain: `[1790, 2020]` — **no fake margin years** (e.g. 2050) for annotation placement

**Controls:** one `<select>` bind (`Show:`), not radios.

**Legend:** bottom, horizontal; hidden in rate mode via legend encode opacity.

---

### Pattern C variant — Fixed-width centred chart (Figures 1.3, 3.1, 4.2, 5.2)

Use when the chart is narrower than the card. The embed is centred; prose below still spans the full card width.

**HTML classes:** `chart-block--split-maps` plus `chart-block--timeline`, `chart-block--activity`, `chart-block--age-ridge`, or `chart-block--outcome-comparison`.

**CSS:** `.vis-wrap { justify-content: center }`, embed wrapper `max-width: 1000px`, `.vega-embed { align-items: center }`.

**Vega-Lite (hconcat butterfly, `activity_risk.vg.json`):**

```json
"width": 1000,
"height": 380,
"padding": { "bottom": 4 },
"autosize": { "type": "pad", "contains": "padding", "resize": true }
```

Panel widths inside hconcat must sum to the top-level width. **Activity butterfly: 410 + 180 + 410 = 1000** — left and right wings must be equal width so the chart centres in the card.

**Axis tick spacing:** left and right wings share the same pixel width and the same number of tick intervals (10 × 50 incidents on the left, 10 × 5 percentage points on the right) so gridline spacing matches visually even though the units differ.

```json
"scale": { "domain": [-500, 0], "nice": false },
"axis": { "values": [-500, -450, …, -50, 0], "labelExpr": "abs(datum.value)" }
```

Right wing:

```json
"scale": { "domain": [0, 50], "nice": false },
"axis": { "values": [0, 5, 10, …, 45, 50] }
```

Do not use a wider right domain (e.g. 0–70) with fewer ticks — it leaves dead space and throws off centre balance.

**Radial time clock (Figure 3.2):** square **centred** chart, **left-aligned** filter.

```json
"width": 560,
"height": 560,
"padding": { "top": 4, "left": 4, "right": 4, "bottom": 16 },
"autosize": { "type": "pad", "contains": "padding" },
"config": {
  "view": { "stroke": "transparent", "clip": false },
  "legend": { "orient": "bottom", "offset": 4 }
}
```

- CSS: title→chart **6px**; filter→prose **8px** bind margin + **8px** lede padding-top
- Use `arc` marks with explicit `theta`/`theta2` wedge angles plus `radius` encoding (not `outerRadius`, which is dropped in v6)
- Dual rings need `"resolve": { "scale": { "radius": "independent" } }` on the layer stack
- **Must use `renderer: "svg"`** in vegaEmbed (see **Typography & vegaEmbed**)
- Clock labels use calculated pixel `x`/`y` with `scale: null`, not polar `theta`/`radius` on text
- Hour label positions: `angle = (Hour + 0.5) / 24 * 2π − π/2`, then `x = 280 + r·sin(angle)`, `y = 280 − r·cos(angle)`
- Split bold text into a separate text layer (v6 drops `encoding.fontWeight`)
- `Show:` select toggles outer (total) and inner (fatal) ring opacity

**Spacing to prose:** same tight lede spacing as all chart blocks (4px / 8px).

---

### Pattern D — Fixed-width left-aligned chart (Figure 2.1: species sankey, Figure 2.2: species size)

Use for charts where the plot should line up with the block title and prose.

**HTML classes:** `chart-block--split-maps` plus `chart-block--sankey` or `chart-block--species-size`

**CSS:** `.vis-wrap { justify-content: flex-start }`, embed wrapper `max-width: 1000px`, `.vega-embed { align-items: flex-start }`.

**Vega (`species_sankey.vg.json`, `species_size_icons.vg.json`):**

```json
"width": 1000,
"height": 380,
"padding": { "bottom": 4 },
"autosize": { "type": "pad", "contains": "padding", "resize": true }
```

Panel sub-titles inside the spec use the **panel title** tier (see below). Sankey node labels use plain `#1a2530` text, no stroke.

---

## Typography (two fonts only)

The site uses exactly **two typefaces**. Do not introduce a third font anywhere — including chart axes, legends, annotations, tooltips, or bind controls.

| Font | CSS token | Used for |
|------|-----------|----------|
| **Playfair Display** | `--font-display` | Hero headline, section number, section title only |
| **Source Sans 3** | `--font-body` | Everything else: body copy, block titles, chart text, axes, legends, annotations, filters, footer |

Both are loaded from Google Fonts in `index.html`. Source Sans 3 must include weights **300, 400, 600, 700** and **italic 400/600** (annotations and bold axis titles need them).

### Type scale (HTML)

| Level | Element | Font | Size | Weight |
|-------|---------|------|------|--------|
| 1 | Hero headline (`.hero-title`) | Playfair Display | clamp(36–62px) | 900 |
| 2 | Section headline (`.section-title`) | Playfair Display | clamp(22–30px) | 700 |
| 3 | **Chart block title** (`.chart-header__title`) | Source Sans 3 | **clamp(19–22px)** | **700** |
| 4 | Narration (`.chart-lede__col`) | Source Sans 3 | 15px | 400 |
| 5 | Vega panel title (in-spec sub-chart label) | Source Sans 3 | 12px | bold |

Chart block titles must sit clearly **above** narration prose (level 4). Do not set block titles at 16px or lower — that reads as body copy.

### What is *not* a title

These use **Source Sans 3**, not Playfair:

- HTML block titles (`.chart-header__title`)
- Vega panel titles, axis titles, legend titles
- Annotation callouts
- Hero stat numbers and narration `<strong>` highlights
- Vega bind labels (`Show:`, decade filters, etc.)

---

## Block titles (HTML only)

Every figure block title lives in HTML, never in Vega-Lite. This keeps titles left-aligned with prose regardless of whether the chart embed is full-width, centred, or split.

| Figure | Title text |
|--------|------------|
| 1.1 Dot map | Every shark incident in Australia, 1791 to 2022 |
| 1.2 Choropleth | Volume vs danger by state |
| 1.3 Timeline | Shark incidents per decade, 1790s to 2020s |
| 2.1 Species sankey | Which shark should you actually fear? |
| 2.2 Species size | Most incidents does not mean the biggest shark |
| 3.1 Activity risk | Activity risk, volume vs fatality rate |
| 3.2 Radial clock | Peak hour is 4pm, not dawn |
| 4.1 Gender isotype | Who gets attacked (gender isotype) |
| 4.2 Age mirror ridge | Age distribution by outcome |
| 5.1 Comparison maps | NSW vs California dot maps |
| 5.2 Outcome comparison | Outcome comparison by region |

### Block title styling

| Property | Value |
|----------|-------|
| Font | Source Sans 3 |
| Size | `clamp(19px, 2.4vw, 22px)` |
| Weight | 700 |
| Colour | `#000000` |
| Line height | 1.25 |
| Alignment | left (matches prose) |

**HTML** (required on every `.chart-block`):

```html
<div class="chart-header">
  <div class="chart-header__title">Main title</div>
</div>
```

CSS lives in `index.html` under `.chart-header` / `.chart-header__title`.

Do **not** put block titles in Vega specs. Do **not** add subtitle lines under block titles. Context belongs in the `chart-lede` below the chart (15px — see type scale).

### Panel title (Vega only, sub-chart labels)

Used on choropleth maps, activity butterfly columns, and comparison map panel labels. **Not** the same as the block title.

| Property | Value |
|----------|-------|
| Font | Source Sans 3 |
| Font size | 12px |
| Weight | bold |
| Colour | `#1a2530` |
| Anchor | `middle` for centred columns (choropleth, activity centre); `start` for left-aligned panels |

```json
"title": {
  "text": "Panel label",
  "font": "Source Sans 3",
  "fontSize": 12,
  "fontWeight": "bold",
  "color": "#1a2530",
  "anchor": "middle"
}
```

Do **not** duplicate block-title properties (`fontSize: 16`, etc.) on panel titles.

---

## Vega / Vega-Lite typography

Block titles are **not** in Vega. Panel titles, axis titles, legend titles, and annotation text marks all use **Source Sans 3**.

### Required `config` baseline (every `.vg.json`)

```json
"config": {
  "title": { "font": "Source Sans 3" },
  "text": { "font": "Source Sans 3" },
  "view": { "stroke": "transparent" },
  "axis": { "labelFont": "Source Sans 3", "titleFont": "Source Sans 3" },
  "legend": {
    "labelFont": "Source Sans 3",
    "titleFont": "Source Sans 3",
    "titleFontWeight": "bold",
    "orient": "bottom",
    "direction": "horizontal",
    "titleOrient": "top",
    "titleAnchor": "start",
    "titleAlign": "left"
  }
}
```

**HTML legends** use `.chart-block-legend`: title in `.chart-block-legend__title`, items in `.chart-block-legend__items` (never title inline with swatches).

### Text marks (annotations, labels)

Always set the font explicitly on text marks — do not rely on defaults:

```json
"mark": {
  "type": "text",
  "font": "Source Sans 3",
  "fontSize": 11,
  "fontStyle": "italic"
}
```

For raw **Vega** specs (`species_sankey.vg.json`, `species_size_icons.vg.json`), set font in `encode.update`:

```json
"font": { "value": "Source Sans 3" }
```

`index.html` also merges a shared `chartFontConfig` at embed time so axis/legend/title defaults stay consistent even if a spec omits them.

---

## Prose below charts

| Element | Style | Spacing |
|---------|-------|---------|
| `.chart-header` | block title above chart | `margin-bottom: 6px` |
| `.chart-block-legend` | HTML legend below chart | `margin: 4px 0 2px` |
| `.chart-block-legend` (comparison maps) | outcome key below comparison maps | same stacked layout as other HTML legends |
| `.vega-embed form.vega-bindings`, `.comparison-map-filters` | filters below legend | `margin: 0 0 8px` |
| `.chart-lede` | 15px, `--text-mid`, **2px solid `--ocean` top border** | `margin-top: 4px`, `padding-top: 8px` |

All chart blocks use the same tight spacing above the blue separator (no separate “default” vs “tighter” tiers).

Under `chart-block--split-maps`, lede uses **full card width** (`max-width: none`).

---

## Interactive controls (filters & binds)

### Placement

Vertical order inside each chart block:

```
Chart (SVG/canvas — includes in-chart legend if present)
Legend (HTML only, when not drawn in-chart — e.g. comparison maps)
Filters / Vega binds
chart-lede
```

- **Filters always sit below the legend**, never above the chart.
- Vega `form.vega-bindings` uses flex `order: 2` so binds render under the chart even when vega-embed inserts the form first in the DOM.
- HTML filters (`.comparison-map-filters`) follow `.chart-block-legend` in the markup.

### Alignment

- **Left-aligned** with the block title and prose — `justify-content: flex-start`, `align-self: flex-start`, `width: 100%`.
- Do not centre filter rows under centred chart embeds.

Shared CSS: `.vega-embed form.vega-bindings` and `.comparison-map-filters` in `index.html`.

### Rules

| Rule | Detail |
|------|--------|
| Input type | Always `<select>` / Vega `bind.input: "select"` |
| Avoid | Radio buttons for mode or filter toggles |
| Alignment | Left-aligned; full width of the chart column |
| Order | Below chart (and below HTML legend when one exists) |
| Bottom padding | 12px when binds sit below chart; 4px when no binds (choropleth panels) |
| Label prefix | `"Filter by decade: "`, `"Show: "`, etc. — short and consistent |
| Font | Source Sans 3, 13px (`var(--font-body)`) |

### HTML pattern (comparison maps)

```html
<div class="vis-wrap">…maps…</div>
<div class="chart-block-legend" aria-label="Outcome legend">…</div>
<form class="comparison-map-filters">…</form>
<div class="chart-lede">…</div>
```

Hide duplicate Vega binds when using HTML filters: `.chart-block--comparison-maps .vega-embed form.vega-bindings { display: none }`.

---

## Annotations (timeline, maps, and ridge charts)

### Typography and colour

All callout labels use the same neutral slate style (see `decade_timeline.vg.json`):

| Property | Value |
|----------|-------|
| Font | Source Sans 3 |
| Font size | 11px |
| Font style | italic |
| Colour | `#2c3e50` |
| Line breaks | `"lineBreak": "\n"` on the mark; two short lines max |
| Clip | `"clip": false` on text marks |

Annotations are **never** coloured to match the series they describe — the legend carries series colour. Do not repeat legend labels (e.g. “Fatal”, “Survived”) as on-chart text.

### Do

- Anchor labels to **real data coordinates** (x + y at the point being discussed)
- Offset with **`dx` / `dy`** from that anchor (e.g. `baseline: "bottom"`, `dy: -6` above a peak; `baseline: "top"`, `dy: 8` below a trough)
- Use **short two-line labels** with `\n` and `"lineBreak": "\n"`
- Set `"clip": false` on text marks and `"view": { "clip": false }` in config when labels sit near edges
- Add **top/bottom padding** in the spec when labels sit above or below peaks
- Use `align: "right"` when a label sits near the right edge so text grows leftward, not off the canvas
- Give the y-axis extra headroom above the highest data value

### Don't

- Float labels in margin whitespace with `scale: null` pixel coordinates
- Place annotations at fake x values outside the data domain (e.g. `Decade: 2035`)
- Use `"limit"` on text marks — it truncates with ellipsis and looks broken
- Extend the x-axis domain just to create “whitespace” for callouts
- Rely on margin positioning without padding/headroom — labels get clipped by the view
- Duplicate legend entries as on-chart row labels

### Reference copy

| Chart | Anchor | Text |
|-------|--------|------|
| Timeline count | 2010 peak | `231 incidents\nin the 2010s` |
| Timeline count | 1940 dip | `WW2 kept people\noff the beaches` |
| Timeline rate | 1800 spike | `Very few people\nback then` |
| Timeline rate | ~2000s | `Fairly steady\nsince federation` |
| Age ridge fatal | age 16 on ridge | `Fatal peak\n16 years` |
| Age ridge survived | age 17 on ridge | `Survived peak\n17 years` |

---

## vegaEmbed defaults

**Always use SVG.** Canvas bakes in system fallback fonts (e.g. Segoe UI on Windows) before web fonts load, so chart text will not match body copy even when the spec says Source Sans 3.

```javascript
const chartFontConfig = {
  config: {
    axis: { labelFont: "Source Sans 3", titleFont: "Source Sans 3" },
    legend: {
      labelFont: "Source Sans 3",
      titleFont: "Source Sans 3",
      titleFontWeight: "bold",
      orient: "bottom",
      direction: "horizontal",
      titleOrient: "top",
      titleAnchor: "start",
      titleAlign: "left",
    },
    title: { font: "Source Sans 3" },
    text: { font: "Source Sans 3" },
  },
};

const embedOpts = { actions: false, renderer: "svg", ...chartFontConfig };
```

### Font loading (required)

Preload Source Sans 3 **before** calling `vegaEmbed`. Vega does not wait for fonts on its own:

```javascript
async function loadChartFonts() {
  const faces = [
    '300 16px "Source Sans 3"',
    '400 16px "Source Sans 3"',
    '600 16px "Source Sans 3"',
    '700 16px "Source Sans 3"',
    'italic 400 16px "Source Sans 3"',
    'italic 600 16px "Source Sans 3"',
  ];
  await Promise.all(faces.map((face) => document.fonts.load(face)));
  await document.fonts.ready;
}

async function embedCharts() {
  await loadChartFonts();
  // vegaEmbed calls…
}
```

Google Fonts link uses `display=block` for Source Sans 3 so body text and charts do not flash with a fallback first.

### CSS fallback for SVG text

```css
.vega-embed svg text {
  font-family: var(--font-body) !important;
}

.vega-embed form.vega-bindings {
  font-family: var(--font-body);
}
```

---

## Checklist before shipping a new chart

- [ ] Typography: only Playfair on section/hero titles; Source Sans 3 everywhere else
- [ ] Vega `config` includes `title.font` and `text.font`; text marks set `"font": "Source Sans 3"`
- [ ] `renderer: "svg"` on every embed; fonts preloaded before `vegaEmbed`
- [ ] Block title is HTML `.chart-header` only (no Vega block `title`)
- [ ] Block title uses level-3 type scale (clamp 19–22px, weight 700) — visibly larger than 15px lede
- [ ] Panel titles use 12px bold `#1a2530`, not block-title styling
- [ ] Correct `chart-block--*` classes on the HTML wrapper
- [ ] Chart width matches pattern (full container / 1000px fixed centred / 1000px fixed left / grid panel)
- [ ] Left edge of title, plot, controls, and prose align visually (or chart is intentionally centred per Pattern C)
- [ ] No excessive gap between chart bottom and blue `chart-lede` separator
- [ ] Filters left-aligned, below chart (and below HTML legend when present)
- [ ] Filters use `<select>`, not radios
- [ ] Geographic charts: fixed projection scale, `autosize: pad` only
- [ ] Side-by-side maps: separate HTML containers + separate specs, not fragile `hconcat`
- [ ] Annotations: no `limit`, no clip, anchored to data, two-line copy where needed
- [ ] Card `overflow: visible` if anything extends past the plot bounds

---

## File map

| Figure | HTML classes | Vega spec(s) |
|--------|--------------|--------------|
| 1.1 Dot map | `split-maps` + `dot-map` | `charts/section-1/dot_map.vg.json` |
| 1.2 Choropleth | `split-maps` + `choropleth` | `charts/section-1/state_choropleth_rate.vg.json`, `charts/section-1/state_choropleth_fatal.vg.json` |
| 1.3 Timeline | `split-maps` + `timeline` | `charts/section-1/decade_timeline.vg.json` |
| 2.1 Species sankey | `split-maps` + `sankey` | `charts/section-2/species_sankey.vg.json` |
| 2.2 Species size | `split-maps` + `species-size` | `charts/section-2/species_size_icons.vg.json` |
| 3.1 Activity risk | `split-maps` + `activity` | `charts/section-3/activity_risk.vg.json` |
| 3.2 Radial clock | `split-maps` + `radial-clock` | `charts/section-3/radial_time_clock.vg.json` |
| 4.1 Gender isotype | `split-maps` + `gender-isotype` | `charts/section-4/gender_isotype.vg.json` |
| 4.2 Age mirror ridge | `split-maps` + `age-ridge` | `charts/section-4/age_mirror_ridge.vg.json` |
| 5.1 Comparison maps | `split-maps` + `comparison-maps` | `charts/section-5/nsw_dot_map.vg.json`, `charts/section-5/ca_dot_map.vg.json` |
| 5.2 Outcome comparison | `split-maps` + `outcome-comparison` | `charts/section-5/outcome_comparison.vg.json` |

**Gender isotype (Figure 4.1):** Pattern C centred embed. Icon paths in `assets/icons/` (see `assets/icons/README.md`). Wrangle with `scripts/wrangle_gender_isotype.py` → `data/wrangled_data/gender_isotype.csv`.

```json
"width": 1000,
"height": 292,
"padding": { "top": 8, "left": 8, "right": 12, "bottom": 8 },
"config": {
  "view": { "stroke": "transparent", "clip": false }
}
```

**HTML legends** below the chart (same `.chart-block-legend` pattern as timeline — do not draw legends in Vega):

```html
<div class="vis-wrap">
  <div id="vis-gender-isotype"></div>
  <div class="gender-isotype-legends">
    <div class="chart-block-legend">…Outcome…</div>
    <div class="chart-block-legend">…Icon (20×28px sample icons + “= 10 incidents”)…</div>
  </div>
</div>
```

1. **Outcome** — Fatal (`#c0392b`), Injured (`#e67e22`), Uninjured (`#7f8c8d`) using `.legend-dot`.
2. **Icon** — male **or** female sample pictograms from `assets/icons/`; do not use text alone for the scale.

**Age mirror ridge (Figure 4.2):** Pattern C centred embed. Wrangle with `scripts/wrangle_age_ridge.py` → `data/wrangled_data/age_records.csv`. Density transform lives inside the main area layer. Peak callouts use data-anchored text (same typography as timeline annotations — see **Annotations** section).

```json
"width": 1000,
"height": 360,
"padding": { "top": 36, "left": 8, "right": 12, "bottom": 28 },
"config": {
  "view": { "stroke": "transparent", "clip": false }
}
```

CSS for all of the above lives in `index.html` under the **CHART WRAPPERS** section.
