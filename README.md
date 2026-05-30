# FIT2179 Data Visualisation 2 — Shark Incidents in Australia

## Topic

This visualisation explores shark incidents in Australia from 1791 to 2022, with a secondary comparison against California (USA). The goal is to move beyond the *Jaws*-driven public narrative and build a data-informed picture of where, when, and under what circumstances shark incidents occur — and who is actually at risk.

The visualisation is structured in five sections:

1. **Setting the Scene** — Geography and scale of Australian shark incidents
2. **Which Shark?** — Species breakdown by frequency, lethality, and size
3. **Where, When, and What Were You Doing?** — Time, season, activity, and body region
4. **Who Gets Attacked?** — Victim demographics
5. **Australia vs California** — International comparison

---

## Data Sources

### Primary — Australian Shark Incident Database (ASID)

- **URL:** https://github.com/cjabradshaw/AustralianSharkIncidentDatabase/tree/main/data
- **Coverage:** 1,203 Australian shark incidents, 1791–2022
- **Key fields:** Latitude, Longitude, State, Species, Shark length, Activity, Injury severity, Body part, Gender, Age, Time of day, Provoked/Unprovoked

---

## Charts Produced

| File | Chart | Status |
|------|-------|--------|
| `dot_map.vg.json` | Dot map — every incident plotted by location, filterable by decade | ✅ Done |
| `state_choropleth.vg.json` | Choropleth — total incidents vs fatality rate by state, toggle between views | ✅ Done |

---

## Notes

- Raw source files are in `data/base_data/`
- Processed CSVs for charts are in `data/wrangled_data/`
- TopoJSON files (`australia.json`, `australia_states.json`) are in `data/topojson/`, sourced from Natural Earth via Mapshaper
- State join key uses `iso_3166_2` field from the TopoJSON, stripping the `AU-` prefix to match CSV abbreviations
- Field names containing dots (e.g. `Victim.injury`) are escaped as `Victim\\.injury` in Vega-Lite specs to avoid property path parsing issues

---

## Running Locally

```bash
cd your_project_folder
python3 -m http.server 8000
```

Then open `http://localhost:8000/index.html` in your browser.

Do not open `index.html` directly from the file explorer (`file://`); charts need HTTP so Vega can load CSV and TopoJSON.

## GitHub Pages

The repo includes a `.nojekyll` file so GitHub Pages serves the project as static files. Without it, Jekyll can swallow the `data/` folder and every chart 404s (SVG height becomes `NaN`).

Enable Pages from the **main** branch, folder **/ (root)**. The site URL will be:

`https://<username>.github.io/FIT2179-Data-Visualisation-2/`

Open that URL (not a raw `github.com/.../blob/...` link). Chart specs load data from `data/wrangled_data/` and `data/topojson/` at the site root.
