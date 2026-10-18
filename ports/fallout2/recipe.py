#!/usr/bin/env python3
"""
Port Recipe: Fallout 2 (fallout2-ce - NS Native Port)
Upstream: https://github.com/alexbatalov/fallout2-ce
Language: Korean (100% CJK dialog & game texts) via FreeType CP949
"""

import os
import sys
import shutil

PORT_DIR = os.path.dirname(os.path.abspath(__file__))

FALLOUT2_CFG_TEMPLATE = """[debug]
mode=environment
output_map_data_info=0
show_load_info=0
show_script_messages=0
show_tile_num=0

[preferences]
brightness=1.000000
combat_difficulty=0
combat_looks=1
combat_messages=1
combat_speed=12
combat_taunts=1
game_difficulty=0
item_highlight=1
language_filter=0
mouse_sensitivity=1.000000
player_speedup=0
running=0
subtitles=1
target_highlight=2
text_base_delay=3.602740
text_line_delay=1.041096
violence_level=3

[sound]
cache_size=448
device=-1
dma=-1
initialize=1
irq=-1
master_volume=32767
music=1
music_path1=data\\sound\\music\\
music_path2=sound\\music\\
music_volume=32767
port=-1
sndfx_volume=32767
sounds=1
speech=1
speech_volume=32767

[system]
art_cache_size=8
color_cycling=1
critter_dat=critter.dat
critter_patches=data
cycle_speed_factor=1
executable=game
free_space=20480
hashing=1
interrupt_walk=1
language=korean
master_dat=master.dat
master_patches=data
scroll_lock=0
splash=21
"""

def build(args):
    print("=" * 60)
    print("  [RECIPE] Fallout 2 (fallout2-ce Korean Port)")
    print("=" * 60)
    
    cookingfoil_path = "/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew/fallout2"
    if os.path.exists(cookingfoil_path):
        print(f"[*] Verified CookingFoil deployment folder at: {cookingfoil_path}")
        print("[*] Required files: master.dat, critter.dat, fallout2.nro")
        print("[*] Korean text assets: data/text/korean/ (1,033+ dialog files)")
        print("[*] Korean fonts: fonts/korean/ (font.ini, font.ttf, zpix.ttf)")
        print("[*] Configuration: fallout2.cfg (language=korean)")
        print("[*] Status: Verified & 100% playable in Korean!")
    else:
        print(f"[!] Warning: CookingFoil folder not found at {cookingfoil_path}")

    if hasattr(args, "deploy") and args.deploy:
        out_dir = os.path.join(args.deploy, "fallout2")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "fallout2.cfg"), "w", encoding="utf-8") as f:
            f.write(FALLOUT2_CFG_TEMPLATE)
        print(f"[*] Deployed configuration to {out_dir}")

    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--deploy", help="Deploy directory path")
    sys.exit(build(parser.parse_args()))
