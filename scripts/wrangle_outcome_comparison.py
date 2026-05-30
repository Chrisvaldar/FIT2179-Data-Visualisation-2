"""NSW vs California outcome counts (1950+) with population-normalised rates."""

import csv
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NSW_PATH = ROOT / "data" / "wrangled_data" / "nsw_dot_map.csv"
CA_PATH = ROOT / "data" / "wrangled_data" / "ca_dot_map.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "outcome_comparison.csv"

OUTCOMES = ("fatal", "injured", "uninjured")

# 2021 populations — NSW matches state_choropleth.csv; CA from US Census Bureau.
POPULATION = {
    "NSW": 8_166_369,
    "California": 39_237_836,
}


def counts_for(path: Path) -> Counter:
    c: Counter = Counter()
    with path.open(encoding="utf-8", newline="") as f:
        for row in csv.DictReader(f):
            injury = row["Victim.injury"]
            if injury in OUTCOMES:
                c[injury] += 1
    return c


def main() -> None:
    region_counts = {
        "NSW": counts_for(NSW_PATH),
        "California": counts_for(CA_PATH),
    }

    rows = []
    for region, counter in region_counts.items():
        pop = POPULATION[region]
        total = sum(counter[o] for o in OUTCOMES)
        for outcome in OUTCOMES:
            count = counter[outcome]
            rows.append(
                {
                    "region": region,
                    "outcome": outcome,
                    "count": count,
                    "population": pop,
                    "rate_per_million": round(count / pop * 1_000_000, 2),
                    "pct_within_region": round(100 * count / total, 1) if total else 0,
                    "region_total": total,
                }
            )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
        "region",
        "outcome",
        "count",
        "population",
        "rate_per_million",
        "pct_within_region",
        "region_total",
    ]
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    for region, counter in region_counts.items():
        total = sum(counter.values())
        print(f"{region}: {dict(counter)} (total {total})")
    print(f"Wrote {len(rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
