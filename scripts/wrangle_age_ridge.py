"""Build incident-level age records for the mirrored age ridge (Figure 4.2)."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
IN_PATH = ROOT / "data" / "base_data" / "locdat2.txt"
OUT_PATH = ROOT / "data" / "wrangled_data" / "age_records.csv"

VALID_INJURIES = {"fatal", "injured", "uninjured"}


def parse_age(raw: str) -> float | None:
    text = (raw or "").strip()
    if not text:
        return None
    try:
        age = float(text)
    except ValueError:
        return None
    if age < 0 or age > 100:
        return None
    return age


def main() -> None:
    out_rows = []

    with IN_PATH.open(encoding="utf-8", errors="replace") as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            injury = (row.get("Victim.injury") or "").strip().lower()
            if injury not in VALID_INJURIES:
                continue

            age = parse_age(row.get("Victim.age", ""))
            if age is None:
                continue

            out_rows.append(
                {
                    "Victim.age": age,
                    "Victim.injury": injury,
                    "outcome_group": "fatal" if injury == "fatal" else "survived",
                }
            )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["Victim.age", "Victim.injury", "outcome_group"]
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(out_rows)

    fatal = sum(1 for r in out_rows if r["outcome_group"] == "fatal")
    survived = len(out_rows) - fatal
    print(f"Wrote {len(out_rows)} age records to {OUT_PATH} ({fatal} fatal, {survived} survived)")


if __name__ == "__main__":
    main()
