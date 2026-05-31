# FIT2179 Data Visualisation 2 — Shark Incidents in Australia

**Author:** Christopher Valensio Darsono  
**Unit:** FIT2179 Data Visualisation 2, Semester 1 2026  
**Submitted:** 31 May 2026

## Live site

[https://chrisvaldar.github.io/FIT2179-Data-Visualisation-2/](https://chrisvaldar.github.io/FIT2179-Data-Visualisation-2/)

Open the GitHub Pages URL above (not a raw `github.com/.../blob/...` link). Charts load CSV and TopoJSON from the site root.

## Topic

This visualisation explores shark incidents in Australia from 1791 to 2022, with a secondary comparison against California (USA) from 1950 to 2022. The goal is to move beyond the *Jaws*-driven public narrative and build a data-informed picture of where, when, and under what circumstances shark incidents occur, and who is actually at risk.

The page is organised in five sections:

1. **Setting the scene** — Geography, volume, and trends over time
2. **Which shark?** — Species by frequency, lethality, and size
3. **Where, when, and what were you doing?** — Activity and time of day
4. **Who gets attacked?** — Victim demographics
5. **Australia vs California** — International comparison (NSW vs California)

Hand-drawn sketch: [`dv2_sketch.pdf`](dv2_sketch.pdf)

---

## Data sources

### Primary — Australian Shark Incident Database (ASID)

- **URL:** [github.com/cjabradshaw/AustralianSharkIncidentDatabase](https://github.com/cjabradshaw/AustralianSharkIncidentDatabase)
- **Coverage:** 1,203 Australian incidents, 1791–2022
- **Key fields:** Latitude, Longitude, State, Species, Shark length, Activity, Injury severity, Gender, Age, Time of day, Provoked/Unprovoked

### Secondary — California Shark Incident Database

- **URL:** [data.ca.gov — Shark Incident Database, California](https://data.ca.gov/dataset/shark-incident-database-california)
- **Coverage:** White shark incidents in California, 1950–2022 (202 incidents in the NSW comparison subset)
- **Used for:** Section 5 dot maps and outcome comparison against New South Wales

Raw source files are in `data/base_data/`. Processed CSVs for charts are in `data/wrangled_data/`. TopoJSON (`australia.json`, `australia_states.json`) is in `data/topojson/`, sourced from Natural Earth via Mapshaper.

---

## Charts on the page

Ten chart blocks, twelve Vega/Vega-Lite specs in `charts/`:

| Section | Chart | Spec(s) | Idiom |
|---------|-------|---------|-------|
| 1.1 | Dot map + decade timeline | `section-1/dot_map.vg.json` | Brushed dot map with stacked area timeline (vconcat) |
| 1.2 | State choropleths | `state_choropleth_rate.vg.json`, `state_choropleth_fatal.vg.json` | Side-by-side choropleths (volume vs fatality rate) |
| 2.1 | Species Sankey | `section-2/species_sankey.vg.json` | Sankey (species → outcome) |
| 2.2 | Species size icons | `section-2/species_size_icons.vg.json` | Custom icon strip (length vs incident count) |
| 3.1 | Activity risk | `section-3/activity_risk.vg.json` | Butterfly lollipop (count vs fatality rate) |
| 3.2 | Time-of-day clock | `section-3/radial_time_clock.vg.json` | Dual radial bar (total vs fatal by hour) |
| 4.1 | Gender isotype | `section-4/gender_isotype.vg.json` | Pictogram / isotype grid |
| 4.2 | Age ridge | `section-4/age_mirror_ridge.vg.json` | Mirrored ridge (fatal vs survived by age) |
| 5.1 | NSW vs CA maps | `section-5/nsw_dot_map.vg.json`, `ca_dot_map.vg.json` | Paired filterable dot maps |
| 5.2 | Outcome comparison | `section-5/outcome_comparison.vg.json` | Grouped bar (per capita vs raw count toggle) |

See [`charts/README.md`](charts/README.md) for the full file listing.

---

## Project structure

```
index.html              Main storytelling page (Vega-Embed)
charts/                 Vega-Lite and Vega JSON specs by section
data/
  base_data/            Raw ASID and California source files
  wrangled_data/        Processed CSVs for charts
  topojson/             Australia country and state boundaries
scripts/                Python data-wrangling scripts
assets/                 Icons, hero image, fonts references
dv2_sketch.pdf          Hand-drawn design sketch (assignment requirement)
```

---

## Running locally

```bash
cd FIT2179-Data-Visualisation-2
python -m http.server 8000
```

Then open [http://localhost:8000/index.html](http://localhost:8000/index.html).

Do not open `index.html` directly from the file explorer (`file://`); charts need HTTP so Vega can load CSV and TopoJSON.

---

## GitHub Pages

The repo includes a `.nojekyll` file so GitHub Pages serves the project as static files. Without it, Jekyll can ignore the `data/` folder and charts will 404.

Enable Pages from the **main** branch, folder **/ (root)**.

---

## Technical notes

- **No npm.** Vega 5, Vega-Lite 6, and Vega-Embed 6 load from jsDelivr in `index.html`. Data wrangling uses Python in `scripts/`.
- **Field names with dots** (e.g. `Victim.injury`) are escaped as `Victim\\.injury` in specs to avoid property-path parsing errors.
- **State join key:** `iso_3166_2` in TopoJSON, stripping the `AU-` prefix to match CSV state abbreviations.
- **AI tools:** Cursor and Claude were used to help build chart specifications and draft on-page narrative text (disclosed in the page footer).

---

## Repository

[github.com/Chrisvaldar/FIT2179-Data-Visualisation-2](https://github.com/Chrisvaldar/FIT2179-Data-Visualisation-2)
