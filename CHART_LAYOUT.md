# Chart layout & alignment guide

This document captures the layout conventions used in Section 1 of the dashboard. Follow it when adding or refactoring charts so every figure lines up with its title, controls, and prose below.

---

## Core principle: one vertical column

Every chart block should read as a single aligned column inside the white card:

```
┌─ chart-block (card) ─────────────────────────────┐
│  Title (left-aligned)                              │
│  Chart / controls                                │
│  ─────────── ocean separator ───────────         │
│  chart-lede (takeaway prose)                     │
│  ─────────── light separator ───────────         │
│  chart-caption (figure label + methods)          │
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
  <p class="chart-caption">…</p>
</div>
```

### Layout modifier classes

| Class | Use for | Behaviour |
|-------|---------|-----------|
| `chart-block--split-maps` | All Section 1 full-width figures | Prose (`chart-lede`, `chart-caption`) uses full card width (`max-width: none`). Base `overflow: visible`. |
| `chart-block--dot-map` | Figure 1.1 dot map | Chart container stretches to **full card width**. |
| `chart-block--choropleth` | Figure 1.2 state maps | Two-column grid, each panel `width: 100%`. Tighter gap before prose (see spacing). |
| `chart-block--timeline` | Figure 1.3 decade timeline | Chart embed max **1000px** wide, centred. `overflow: visible` on embed wrappers so annotations are not clipped. |
| `chart-block--species` | Figure 2.1 species bubble | hconcat embed max **1000px** wide, **left-aligned** with title and prose. |
| `chart-block--length-beeswarm` | Figure 2.2 length beeswarm | Chart embed max **1000px** wide, **centred** in the card. |
| `chart-block--activity` | Figure 3.1 activity butterfly | hconcat embed max **1000px** wide, **centred** in the card. |
| `chart-block--radial-clock` | Figure 3.2 radial time clock | Square embed max **560px** wide, **centred** in the card. |
| `chart-block--gender-isotype` | Figure 4.1 gender isotype | Chart embed max **1000px** wide, **centred** in the card. |

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

**Controls:** `<select>` dropdowns (not radio buttons). Bottom padding ~12px is enough room for binds.

**Legend:** In-chart, bottom-left on the map canvas (outcome key also appears in the page-level legend bar).

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

**Shared block title** lives in HTML (`.chart-header`), styled to match Vega `config.title`:

- Title: 16px, `#000000`, Source Sans 3, font-weight 600

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

**Spacing to prose:** `chart-block--choropleth .chart-lede` uses reduced top margin (12px / 14px padding) — no large gap between legends and the blue separator.

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

### Pattern C variant — Fixed-width centred chart (Figures 1.3, 2.2, 3.1)

Use when the chart is narrower than the card. The embed is centred; prose below still spans the full card width.

**HTML classes:** `chart-block--split-maps` plus `chart-block--timeline`, `chart-block--length-beeswarm`, or `chart-block--activity`.

**CSS:** `.vis-wrap { justify-content: center }`, embed wrapper `max-width: 1000px`, `.vega-embed { align-items: center }`.

**Length beeswarm (Figure 2.2):** same HTML header pattern as every other figure. Only the beeswarm embed is centred.

**Vega-Lite (single chart, `length_beeswarm.vg.json`):**

```json
"width": 1000,
"height": 340,
"padding": { "top": 28, "left": 8, "right": 12, "bottom": 12 }
```

Single-panel layout with three outcome bands (fatal / injured / uninjured). Window transform stacks dots vertically within each 0.25&nbsp;m length bin; stack spacing scales to band height. Species filter uses `bind.input: "select"`.

**Vega-Lite (hconcat butterfly, `activity_risk.vg.json`):**

```json
"width": 1000,
"height": 380,
"padding": { "bottom": 4 },
"autosize": { "type": "pad", "contains": "padding", "resize": true }
```

Panel widths inside hconcat must sum to the top-level width (activity: 385 + 180 + 435 = 1000).

**Radial time clock (Figure 3.2):** square centred embed, not full 1000px width.

```json
"width": 560,
"height": 560,
"padding": { "top": 12, "bottom": 48 },
"config": {
  "view": { "stroke": "transparent", "clip": false }
}
```

- CSS caps embed at `max-width: 560px` and centres it in the card
- Use `arc` marks with explicit `theta`/`theta2` wedge angles plus `radius` encoding (not `outerRadius`, which is dropped in v6)
- Dual rings need `"resolve": { "scale": { "radius": "independent" } }` on the layer stack
- **Must use `renderer: "svg"`** in vegaEmbed; canvas does not draw radius-encoded arcs
- Clock labels use calculated pixel `x`/`y` with `scale: null`, not polar `theta`/`radius` on text
- Hour label positions: `angle = (Hour + 0.5) / 24 * 2π − π/2`, then `x = 280 + r·sin(angle)`, `y = 280 − r·cos(angle)`
- Split bold text into a separate text layer (v6 drops `encoding.fontWeight`)
- `Show:` select toggles outer (total) and inner (fatal) ring opacity

**Spacing to prose:** same tighter lede margin as choropleth and timeline (12px / 14px).

---

### Pattern D — Fixed-width left-aligned hconcat (Figure 2.1: species bubble)

Use for multi-panel charts where the left panel should line up with the block title and prose.

**HTML classes:** `chart-block--split-maps chart-block--species`

**CSS:** `.vis-wrap { justify-content: flex-start }`, embed wrapper `max-width: 1000px`, `.vega-embed { align-items: flex-start }`.

**Vega-Lite (`species_bubble.vg.json`):**

```json
"width": 1000,
"height": 380,
"padding": { "bottom": 4 },
"autosize": { "type": "pad", "contains": "padding", "resize": true }
```

Panel widths: 620 + 380 = 1000. Shared click-to-highlight selection stays in one spec (do not split into separate embeds).

Panel sub-titles use the **panel title** tier (see below). Inside-bubble species names use plain `#000000` text, no stroke.

---

## Block titles (HTML only)

Every figure block title lives in HTML, never in Vega-Lite. This keeps titles left-aligned with prose regardless of whether the chart embed is full-width, centred, or split.

| Figure | Title text |
|--------|------------|
| 1.1 Dot map | Every shark incident in Australia, 1791 to 2022 |
| 1.2 Choropleth | Volume vs danger by state |
| 1.3 Timeline | Shark incidents per decade, 1790s to 2020s |
| 2.1 Species bubble | Which shark should you actually fear? |
| 2.2 Length beeswarm | Under 2 metres, no recorded fatalities |
| 3.1 Activity risk | Activity risk, volume vs fatality rate |
| 3.2 Radial clock | Peak hour is 4pm, not dawn |
| 4.1 Gender isotype | Nine in ten victims are male |

### Block title styling

| Property | Value |
|----------|-------|
| Font | Source Sans 3 |
| Size | 16px |
| Weight | 600 |
| Colour | `#000000` |
| Alignment | left (matches prose) |

**HTML** (required on every `.chart-block`):

```html
<div class="chart-header">
  <div class="chart-header__title">Main title</div>
</div>
```

CSS lives in `index.html` under `.chart-header` / `.chart-header__title`.

Do **not** put block titles in Vega specs. Do **not** add subtitle lines under block titles. Context belongs in the `chart-lede` below the chart.

### Panel title (Vega only, sub-chart labels)

Used on choropleth maps, species bubble panels, and activity butterfly columns. **Not** the same as the block title.

| Property | Value |
|----------|-------|
| Font size | 12px |
| Weight | bold |
| Colour | `#1a2530` |
| Anchor | `middle` for centred columns (choropleth, activity centre); `start` for left-aligned panels (species bubble) |

```json
"title": {
  "text": "Panel label",
  "fontSize": 12,
  "fontWeight": "bold",
  "color": "#1a2530",
  "anchor": "start"
}
```

Do **not** duplicate block-title properties (`fontSize: 16`, etc.) on panel titles.

---

## Vega-Lite typography

Block titles are **not** in Vega. Only panel titles, axis titles, and legend titles use Vega `title` properties.

Shared `config` baseline (no `config.title`):

```json
"config": {
  "view": { "stroke": "transparent" },
  "axis": { "labelFont": "Source Sans 3", "titleFont": "Source Sans 3" },
  "legend": { "labelFont": "Source Sans 3", "titleFont": "Source Sans 3" }
}
```

---

## Prose below charts

| Element | Style | Default spacing |
|---------|-------|-----------------|
| `.chart-lede` | 15px, `--text-mid`, **2px solid `--ocean` top border** | `margin-top: 22px`, `padding-top: 18px` |
| `.chart-caption` | 13px, `--text-light`, 1px light top border | `margin-top: 14px`, `padding-top: 12px` |

**Tighter spacing** (charts with bottom legends or fixed-width embeds):

```css
.chart-block--choropleth .chart-lede,
.chart-block--timeline .chart-lede,
.chart-block--species .chart-lede,
.chart-block--length-beeswarm .chart-lede,
.chart-block--activity .chart-lede,
.chart-block--radial-clock .chart-lede,
.chart-block--gender-isotype .chart-lede {
  margin-top: 12px;
  padding-top: 14px;
}
```

Under `chart-block--split-maps`, lede and caption use **full card width** (`max-width: none`), not the old 820px cap.

---

## Interactive controls

| Rule | Detail |
|------|--------|
| Input type | Always `<select>` / Vega `bind.input: "select"` |
| Avoid | Radio buttons for mode or filter toggles |
| Bottom padding | 12px when binds sit below chart; 4px when no binds (choropleth panels) |
| Label prefix | `"Filter by decade: "`, `"Show: "`, etc. — short and consistent |

---

## Annotations (timeline and maps)

### Do

- Anchor labels to **real data coordinates** (decade + y value at that point)
- Use **short two-line labels** with `\n` and `"lineBreak": "\n"`
- Set `"clip": false` on text marks and `"view": { "clip": false }` in config when labels sit near edges
- Add **top/right padding** in the spec when labels sit above peaks or near the right edge
- Use `align: "right"` at the 2010 peak so text grows leftward, not off the right edge
- Give the y-axis extra headroom above the highest data value

### Don't

- Place annotations at fake x values outside the data domain (e.g. `Decade: 2035`)
- Use `"limit"` on text marks — it truncates with ellipsis and looks broken
- Extend the x-axis domain just to create “whitespace” for callouts
- Rely on margin positioning without padding/headroom — labels get clipped by the view

### Current timeline labels (reference copy)

| Mode | Anchor | Text |
|------|--------|------|
| Count | 2010 peak | `231 incidents\nin the 2010s` |
| Count | 1940 dip | `WW2 kept people\noff the beaches` |
| Rate | 1800 spike | `Very few people\nback then` |
| Rate | ~2000s | `Fairly steady\nsince federation` |

---

## vegaEmbed defaults

```javascript
const embedOpts = { actions: false, renderer: "canvas" };

// Choropleth panels only:
const choroplethOpts = { ...embedOpts, renderer: "svg" };
```

---

## Checklist before shipping a new chart

- [ ] Block title is HTML `.chart-header` only (no Vega block `title`)
- [ ] Panel titles use 12px bold `#1a2530`, not block-title styling
- [ ] Correct `chart-block--*` classes on the HTML wrapper
- [ ] Chart width matches pattern (full container / 1000px fixed centred / 1000px fixed left / grid panel)
- [ ] Left edge of title, plot, controls, and prose align visually (or chart is intentionally centred per Pattern C)
- [ ] No excessive gap between chart bottom and blue `chart-lede` separator
- [ ] Filters use `<select>`, not radios
- [ ] Geographic charts: fixed projection scale, `autosize: pad` only
- [ ] Side-by-side maps: separate HTML containers + separate specs, not fragile `hconcat`
- [ ] Annotations: no `limit`, no clip, anchored to data, two-line copy where needed
- [ ] Card `overflow: visible` if anything extends past the plot bounds

---

## File map

| Figure | HTML classes | Vega spec(s) |
|--------|--------------|--------------|
| 1.1 Dot map | `split-maps` + `dot-map` | `dot_map.vg.json` |
| 1.2 Choropleth | `split-maps` + `choropleth` | `state_choropleth_rate.vg.json`, `state_choropleth_fatal.vg.json` |
| 1.3 Timeline | `split-maps` + `timeline` | `decade_timeline.vg.json` |
| 2.1 Species bubble | `split-maps` + `species` | `species_bubble.vg.json` |
| 2.2 Length beeswarm | `split-maps` + `length-beeswarm` | `length_beeswarm.vg.json` |
| 2.3 Length ridgeline | `split-maps` + `length-ridgeline` | `length_ridgeline.vg.json` |
| 2.4 Length pictogram | `split-maps` + `length-pictogram` | `length_pictogram.vg.json` |
| 3.1 Activity risk | `split-maps` + `activity` | `activity_risk.vg.json` |
| 3.2 Radial clock | `split-maps` + `radial-clock` | `radial_time_clock.vg.json` |
| 4.1 Gender isotype | `split-maps` + `gender-isotype` | `gender_isotype.vg.json` |

**Gender isotype (Figure 4.1):** Pattern C centred embed. Icon paths in `assets/icons/` (see `assets/icons/README.md`). Wrangle with `scripts/wrangle_gender_isotype.py` → `data/wrangled_data/gender_isotype.csv`.

```json
"width": 1000,
"height": 360,
"padding": { "top": 8, "left": 8, "right": 12, "bottom": 8 },
"config": {
  "view": { "stroke": "transparent", "clip": false }
}
```

CSS for all of the above lives in `index.html` under the **CHART WRAPPERS** section.
