"""Build unit-grid positions for the gender isotype (Figure 4.1)."""

import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_PATH = ROOT / "data" / "wrangled_data" / "gender_outcome.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "gender_isotype.csv"

OUTCOME_ORDER = {"fatal": 0, "injured": 1, "uninjured": 2}
GENDER_ORDER = {"male": 0, "female": 1}
UNITS_PER_ICON = 10
# Wider male grid → fewer rows (less vertical height). Female = one row of 13.
UNITS_WIDE = {"male": 35, "female": 13}
def icon_ext(gender: str) -> str:
    if (ROOT / "assets" / "icons" / f"{gender}-icon.png").exists():
        return "png"
    return "svg"


def icon_url(gender: str, injury: str) -> str:
    return f"assets/icons/{gender}-{injury}.{icon_ext(gender)}"


def icons_for_count(count: int) -> int:
    if count <= 0:
        return 0
    return max(1, round(count / UNITS_PER_ICON))


def main() -> None:
    rows = list(csv.DictReader(IN_PATH.open(encoding="utf-8")))
    groups: dict[str, list[dict]] = defaultdict(list)

    for row in rows:
        gender = row["Victim.gender"]
        injury = row["Victim.injury"]
        count = int(row["count"])
        n_icons = icons_for_count(count)
        for _ in range(n_icons):
            groups[gender].append(
                {
                    "Victim.gender": gender,
                    "Victim.injury": injury,
                    "source_count": count,
                    "incidents_per_icon": UNITS_PER_ICON,
                    "icon_url": icon_url(gender, injury),
                    "gender_row": GENDER_ORDER[gender],
                }
            )

    out_rows = []
    for gender in sorted(groups, key=lambda g: GENDER_ORDER[g]):
        band = sorted(
            groups[gender],
            key=lambda r: OUTCOME_ORDER[r["Victim.injury"]],
        )
        units_wide = UNITS_WIDE[gender]
        for idx, row in enumerate(band):
            row["unit_col"] = idx % units_wide
            row["unit_row"] = idx // units_wide
            row["unit_idx"] = idx
            out_rows.append(row)

    fieldnames = [
        "Victim.gender",
        "Victim.injury",
        "source_count",
        "incidents_per_icon",
        "icon_url",
        "gender_row",
        "unit_col",
        "unit_row",
        "unit_idx",
    ]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} icon rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
