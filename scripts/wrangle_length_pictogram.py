"""Build unit-grid positions for the length pictogram (Figure 2.4)."""

import csv
import math
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_PATH = ROOT / "data" / "wrangled_data" / "length_beeswarm.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "length_pictogram.csv"

OUTCOME_ORDER = {"fatal": 0, "injured": 1, "uninjured": 2}
UNITS_WIDE = 5


def length_band(floor_m: int) -> str:
    return f"{floor_m}–{floor_m + 1} m"


def main() -> None:
    rows = list(csv.DictReader(IN_PATH.open(encoding="utf-8")))
    groups: dict[int, list[dict]] = defaultdict(list)

    for row in rows:
        length_m = float(row["Shark.length.m"])
        floor_m = math.floor(length_m)
        groups[floor_m].append(
            {
                "Shark.length.m": row["Shark.length.m"],
                "Victim.injury": row["Victim.injury"],
                "Species.clean": row["Species.clean"],
                "State": row["State"],
                "Incident.year": row["Incident.year"],
                "length_floor": floor_m,
                "length_band": length_band(floor_m),
            }
        )

    out_rows = []
    for floor_m in sorted(groups):
        band_rows = sorted(
            groups[floor_m],
            key=lambda r: (
                OUTCOME_ORDER[r["Victim.injury"]],
                float(r["Shark.length.m"]),
                r["Incident.year"],
            ),
        )
        for idx, row in enumerate(band_rows):
            row["unit_col"] = idx % UNITS_WIDE
            row["unit_row"] = idx // UNITS_WIDE
            out_rows.append(row)

    fieldnames = [
        "Shark.length.m",
        "Victim.injury",
        "Species.clean",
        "State",
        "Incident.year",
        "length_floor",
        "length_band",
        "unit_col",
        "unit_row",
    ]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
