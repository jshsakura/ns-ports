#!/usr/bin/env python3
"""Build the 1280x720 main-menu background (gfx/shell/splash.bmp) from a wide hero image.

  make-splash.py <hero image> <output.bmp>

The image is mirrored (so the dark side sits under the menu text), scaled to a height of 720 and cropped
to the left 1280 columns. Output is a 24-bit BMP, which is what the engine's menu loader reads.
"""
import sys

from PIL import Image, ImageOps

W, H = 1280, 720


def main(src, dst):
    im = ImageOps.mirror(Image.open(src).convert("RGB"))
    im = im.resize((round(im.width * H / im.height), H), Image.BILINEAR).crop((0, 0, W, H))
    im.save(dst, format="BMP")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
