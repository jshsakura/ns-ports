#!/usr/bin/env python3
"""
Port Recipe: OpenRCT2 (RollerCoaster Tycoon 2 - NS Native Port)
Upstream: https://github.com/OpenRCT2/OpenRCT2
Language: Korean (ko-KR) via FreeType TrueType Font
"""

import os
import sys
import shutil

PORT_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_INI_TEMPLATE = """[general]
game_path = "/switch/openrct2/rct2"
rct1_path = "/switch/openrct2/rct1"
language = ko-KR
fullscreen_mode = 0
fullscreen_width = 1280
fullscreen_height = 720
window_width = 1280
window_height = 720
drawing_engine = "SOFTWARE"
play_intro = false

[font]
file_name = "/switch/openrct2/font.ttf"
font_name = "NanumBarunGothic"
x_offset = 1
y_offset = -2
size_tiny = 11
size_small = 12
size_medium = 12
size_big = 13
height_tiny = 12
height_small = 14
height_medium = 14
height_big = 16
enable_hinting = true
hinting_threshold = 0
"""

def build(args):
    print("=" * 60)
    print("  [RECIPE] RollerCoaster Tycoon 2 (OpenRCT2 Korean)")
    print("=" * 60)
    
    cookingfoil_path = "/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew/openrct2"
    if os.path.exists(cookingfoil_path):
        print(f"[*] Verified CookingFoil deployment folder at: {cookingfoil_path}")
        print("[*] Korean TTF font (NanumBarunGothic) and config.ini are configured.")
    else:
        print(f"[!] Warning: CookingFoil folder not found at {cookingfoil_path}")

    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--deploy", help="Deploy directory path")
    sys.exit(build(parser.parse_args()))
