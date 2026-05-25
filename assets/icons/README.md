# Gender isotype icons (Figure 4.1)

## Base files (you edit)

| File | Format |
|------|--------|
| `male-icon.svg` or `male-icon.png` | Male source |
| `female-icon.svg` or `female-icon.png` | Female source |

Dark silhouette on **transparent** background. One file per gender.

**Important:** male and female sources must share the same canvas proportions. Male SVGs use **320×452**; PNG sources are auto-normalized to that size when you run `build_colored_icons.py`. A square PNG (e.g. 512×512) will render larger in Vega even if the chart sets the same `width`/`height`.

## Generate coloured versions

```bash
python scripts/build_colored_icons.py
python scripts/wrangle_gender_isotype.py
```

Creates six files using the **same extension** as the base (e.g. PNG in → `female-fatal.png`, SVG in → `male-fatal.svg`):

- `{gender}-fatal` — `#c0392b`
- `{gender}-injured` — `#e67e22`
- `{gender}-uninjured` — `#7f8c8d`

Hard refresh the browser (Ctrl+F5) after regenerating.
