# DO NOT RUN THIS SCRIPT ON THE CALCULATOR! It is meant to be run on a PC to extract the bitmaps from the source code and save them as JSON and PBM files for use in scripts where exact character bitmap pixel widths are required for custom label alignment.

import json
import math
from pathlib import Path

from casioplot.characters import large, medium, small

try:
    from casioplot import getkey
except ImportError:
    getkey = None


TABLES = {
    "small": small,
    "medium": medium,
    "large": large,
}


def glyph_to_bits(glyph_rows):
    return [[1 if px == "X" else 0 for px in row] for row in glyph_rows]


def save_json(table_name, table, out_dir):
    chars = sorted(table.keys(), key=ord)
    glyph_h = max(len(table[ch]) for ch in chars)
    glyph_w = max(len(table[ch][0]) for ch in chars)

    data = {
        "name": table_name,
        "glyph_width": glyph_w,
        "glyph_height": glyph_h,
        "glyph_count": len(chars),
        "characters": [
            {
                "char": ch,
                "codepoint": ord(ch),
                "w": len(table[ch][0]),
                "h": len(table[ch]),
                "rows": list(table[ch]),
                "bits": glyph_to_bits(table[ch]),
            }
            for ch in chars
        ],
    }

    path = out_dir / f"{table_name}.json"
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")


def build_atlas(table, columns=16, padding=1):
    chars = sorted(table.keys(), key=ord)
    cell_h = max(len(table[ch]) for ch in chars)
    cell_w = max(len(table[ch][0]) for ch in chars)

    rows = math.ceil(len(chars) / columns)
    atlas_w = padding + columns * (cell_w + padding)
    atlas_h = padding + rows * (cell_h + padding)

    pixels = [[0 for _ in range(atlas_w)] for _ in range(atlas_h)]
    metadata = []

    for i, ch in enumerate(chars):
        col = i % columns
        row = i // columns
        x0 = padding + col * (cell_w + padding)
        y0 = padding + row * (cell_h + padding)

        glyph = table[ch]
        glyph_h = len(glyph)
        glyph_w = len(glyph[0])
        for y, line in enumerate(glyph):
            for x, px in enumerate(line):
                if px == "X":
                    pixels[y0 + y][x0 + x] = 1

        metadata.append(
            {
                "char": ch,
                "codepoint": ord(ch),
                "x": x0,
                "y": y0,
                "w": glyph_w,
                "h": glyph_h,
            }
        )

    return pixels, metadata


def save_pbm(path, pixels):
    h = len(pixels)
    w = len(pixels[0]) if h else 0

    with path.open("w", encoding="ascii") as f:
        f.write("P1\n")
        f.write(f"{w} {h}\n")
        for row in pixels:
            f.write(" ".join(str(v) for v in row))
            f.write("\n")


def save_atlas(table_name, table, out_dir):
    pixels, metadata = build_atlas(table)

    pbm_path = out_dir / f"{table_name}_atlas.pbm"
    save_pbm(pbm_path, pixels)

    meta_path = out_dir / f"{table_name}_atlas_meta.json"
    meta_path.write_text(json.dumps(metadata, indent=2), encoding="utf-8")


def wait_for_exit():
    if getkey is not None:
        getkey()
    else:
        input("\nPress any key to exit: ")


def main():
    out_dir = Path("assets/casioplot_font")
    out_dir.mkdir(parents=True, exist_ok=True)

    for name, table in TABLES.items():
        save_json(name, table, out_dir)
        save_atlas(name, table, out_dir)

    print("Extracted bitmaps to", out_dir)
    wait_for_exit()


main()
