"""Build incident-level CSV for the length beeswarm chart (Figure 2.2)."""

import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOC_PATH = ROOT / "data" / "base_data" / "locdat2.txt"
DOT_PATH = ROOT / "data" / "wrangled_data" / "dot_map.csv"
OUT_PATH = ROOT / "data" / "wrangled_data" / "length_beeswarm.csv"

SPECIES_MAP = {
    "white shark": "White Shark",
    "tiger shark": "Tiger Shark",
    "wobbegong": "Wobbegong",
    "bull shark": "Bull Shark",
    "whaler shark": "Whaler Shark",
    "bronze whaler shark": "Bronze Whaler",
    "grey nurse shark": "Grey Nurse",
    "grey reef shark": "Grey Reef",
    "whitetip reef shark": "Whitetip Reef",
    "hammerhead shark": "Hammerhead",
    "blacktip reef shark": "Blacktip Reef",
    "dusky shark": "Dusky Shark",
    "galapagos shark": "Galapagos Shark",
    "broadnose sevengill shark": "Other",
    "sevengill shark": "Other",
    "shortfin mako shark": "Other",
    "silvertip shark": "Other",
    "blind shark": "Other",
    "dogfish": "Other",
    "lemon shark": "Lemon Shark",
}


def clean_species(raw: str, dot_lookup: dict) -> str:
    key = (
        raw["Incident.year"],
        raw["State"],
        raw["Latitude"],
        raw["Longitude"],
        raw["Victim.injury"],
    )
    if key in dot_lookup:
        return dot_lookup[key]
    name = raw.get("Shark.common.name", "").strip().lower()
    if not name:
        return "Unknown"
    return SPECIES_MAP.get(name, "Other")


def decade(year: str) -> str:
    y = int(year)
    return str((y // 10) * 10)


def main() -> None:
    with DOT_PATH.open(encoding="utf-8") as f:
        dot_rows = list(csv.DictReader(f))

    dot_lookup = {
        (
            r["Incident.year"],
            r["State"],
            r["Latitude"],
            r["Longitude"],
            r["Victim.injury"],
        ): r["Species.clean"]
        for r in dot_rows
    }

    out_rows = []
    with LOC_PATH.open(encoding="utf-8") as f:
        for raw in csv.DictReader(f, delimiter="\t"):
            length_raw = raw.get("Shark.length.m", "").strip()
            if not length_raw:
                continue
            try:
                length = float(length_raw)
            except ValueError:
                continue
            if length <= 0 or length > 12:
                continue

            injury = raw["Victim.injury"].strip().lower()
            if injury not in {"fatal", "injured", "uninjured"}:
                continue

            out_rows.append(
                {
                    "Shark.length.m": f"{length:.2f}",
                    "Victim.injury": injury,
                    "Species.clean": clean_species(raw, dot_lookup),
                    "State": raw["State"],
                    "Incident.year": raw["Incident.year"],
                    "Decade": decade(raw["Incident.year"]),
                }
            )

    out_rows.sort(
        key=lambda r: (
            float(r["Shark.length.m"]),
            r["Victim.injury"],
            r["Incident.year"],
        )
    )

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "Shark.length.m",
                "Victim.injury",
                "Species.clean",
                "State",
                "Incident.year",
                "Decade",
            ],
        )
        writer.writeheader()
        writer.writerows(out_rows)

    print(f"Wrote {len(out_rows)} rows to {OUT_PATH}")


if __name__ == "__main__":
    main()
