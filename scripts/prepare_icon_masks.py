"""Convert black silhouette PNGs to white masks so Vega can tint by outcome colour."""

from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "assets" / "icons"

FILES = ["male-icon.png", "female-icon.png"]


def to_white_mask(path: Path) -> None:
    img = Image.open(path).convert("RGBA")
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a > 8:
                pixels[x, y] = (255, 255, 255, a)
    img.save(path)


def main() -> None:
    for name in FILES:
        path = ICONS / name
        if not path.exists():
            raise FileNotFoundError(path)
        to_white_mask(path)
        print(f"Prepared tint mask: {path}")


if __name__ == "__main__":
    main()
