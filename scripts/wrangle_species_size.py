"""Build species size summary CSV aligned with the sankey chart grouping."""

import csv
import statistics
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOT_PATH = ROOT / "data" / "wrangled_data" / "dot_map.csv"
LENGTH_PATH = ROOT / "data" / "wrangled_data" / "length_beeswarm.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "species_size.csv"

SANKEY_SPECIES = [
    "White Shark",
    "Tiger Shark",
    "Wobbegong",
    "Bull Shark",
    "Whaler Shark",
    "Other",
]
TOP5 = set(SANKEY_SPECIES) - {"Other"}


def sankey_species(name: str) -> str:
    return name if name in TOP5 else "Other"


def median(values: list[float]) -> float | None:
    return statistics.median(values) if values else None


def mean(values: list[float]) -> float | None:
    return statistics.mean(values) if values else None


def main() -> None:
    counts: Counter[str] = Counter()
    with DOT_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            counts[sankey_species(row["Species.clean"])] += 1

    lengths: dict[str, list[float]] = defaultdict(list)
    with LENGTH_PATH.open(encoding="utf-8") as f:
        for row in csv.DictReader(f):
            lengths[sankey_species(row["Species.clean"])].append(
                float(row["Shark.length.m"])
            )

    out_rows = []
    for order, species in enumerate(SANKEY_SPECIES):
        length_vals = lengths[species]
        out_rows.append(
            {
                "species": species,
                "count": counts[species],
                "median_length": median(length_vals),
                "mean_length": mean(length_vals),
                "length_count": len(length_vals),
                "species_order": order,
            }
        )

    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "species",
                "count",
                "median_length",
                "mean_length",
                "length_count",
                "species_order",
            ],
        )
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {OUT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
