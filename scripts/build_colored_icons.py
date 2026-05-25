"""Build per-outcome icon files from base male-icon / female-icon (SVG or PNG)."""

import re
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
ICONS = ROOT / "assets" / "icons"

# Match male SVG canvas so every icon renders at the same on-screen size.
CANONICAL_SIZE = (320, 452)

OUTCOMES = {
    "fatal": "#c0392b",
    "injured": "#e67e22",
    "uninjured": "#7f8c8d",
}

FILL_PATTERN = re.compile(
    r'fill="(?:#000000|#000|#ffffff|#fff|black|white)"',
    re.IGNORECASE,
)


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    h = hex_color.lstrip("#")
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def recolor_svg(svg_text: str, color: str) -> str:
    return FILL_PATTERN.sub(f'fill="{color}"', svg_text)


def normalize_png(img: Image.Image) -> Image.Image:
    """Fit any source PNG onto the same canvas as male-icon.svg (320×452)."""
    img = img.convert("RGBA")
    target_w, target_h = CANONICAL_SIZE
    scale = target_h / img.height
    new_w = int(img.width * scale)
    new_h = target_h
    resized = img.resize((new_w, new_h), Image.Resampling.LANCZOS)
    if new_w > target_w:
        left = (new_w - target_w) // 2
        resized = resized.crop((left, 0, left + target_w, target_h))
        return resized
    canvas = Image.new("RGBA", CANONICAL_SIZE, (0, 0, 0, 0))
    canvas.paste(resized, ((target_w - new_w) // 2, 0), resized)
    return canvas


def recolor_png(source: Path, dest: Path, color: str) -> None:
    rgb = hex_to_rgb(color)
    img = normalize_png(Image.open(source))
    pixels = img.load()
    for y in range(img.height):
        for x in range(img.width):
            r, g, b, a = pixels[x, y]
            if a > 12:
                pixels[x, y] = (rgb[0], rgb[1], rgb[2], a)
    img.save(dest, format="PNG")


def base_path(gender: str) -> Path | None:
    png = ICONS / f"{gender}-icon.png"
    svg = ICONS / f"{gender}-icon.svg"
    if png.exists():
        return png
    if svg.exists():
        return svg
    return None


def build_for_gender(gender: str) -> None:
    source = base_path(gender)
    if source is None:
        print(f"Skip {gender}: no {gender}-icon.png or {gender}-icon.svg")
        return

    ext = source.suffix.lower()
    for outcome, color in OUTCOMES.items():
        out = ICONS / f"{gender}-{outcome}{ext}"
        if ext == ".png":
            recolor_png(source, out, color)
        else:
            template = source.read_text(encoding="utf-8")
            out.write_text(recolor_svg(template, color), encoding="utf-8")
        print(f"Wrote {out}")


def main() -> None:
    for gender in ("male", "female"):
        build_for_gender(gender)
    print("Done.")


if __name__ == "__main__":
    main()
