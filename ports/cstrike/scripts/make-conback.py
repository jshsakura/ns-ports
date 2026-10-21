#!/usr/bin/env python3
"""Build the loading-screen background (gfx/shell/conback.bmp, 1280x960) from a wide hero image.

  make-conback.py <hero image> <output.bmp>

The engine stretches this bitmap to 4:3 and shows only the lower 720 rows, so the 16:9 picture goes in
the lower 720 rows and the top 240 rows are filled with its mirrored top edge. The picture is darkened
so the loading text stays readable. Output is a 24-bit BMP.
"""
import sys

from PIL import Image, ImageEnhance, ImageOps

W, H, FULL = 1280, 720, 960
DARKEN = 0.55


def main(src, dst):
    im = Image.open(src).convert("RGB")
    im = im.resize((round(im.width * H / im.height), H), Image.BILINEAR)
    left = (im.width - W) // 2
    im = ImageEnhance.Brightness(im.crop((left, 0, left + W, H))).enhance(DARKEN)
    out = Image.new("RGB", (W, FULL))
    out.paste(im, (0, FULL - H))
    out.paste(ImageOps.flip(im.crop((0, 0, W, FULL - H))), (0, 0))
    out.save(dst, format="BMP")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
