"""Build NSW incident points for the Section 5 state comparison map (1950+)."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_PATH = ROOT / "data" / "wrangled_data" / "dot_map.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "nsw_dot_map.csv"

FIELDNAMES = [
    "Incident.year",
    "Latitude",
    "Longitude",
    "Victim.injury",
    "Activity.clean",
    "Location",
    "Decade",
]


def decade_for_year(year: int) -> int:
    return (year // 10) * 10


def main() -> None:
    out_rows = []

    with IN_PATH.open(encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row.get("State") != "NSW":
                continue

            year = int(row["Incident.year"])
            if year < 1950:
                continue

            out_rows.append(
                {
                    "Incident.year": year,
                    "Latitude": row["Latitude"],
                    "Longitude": row["Longitude"],
                    "Victim.injury": row["Victim.injury"],
                    "Activity.clean": row["Activity.clean"],
                    "Location": row["Location"],
                    "Decade": decade_for_year(year),
                }
            )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} NSW incidents (1950+) to {OUT_PATH}")


if __name__ == "__main__":
    main()
