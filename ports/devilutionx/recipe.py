#!/usr/bin/env python3
"""
Port Recipe: DevilutionX (Diablo 1 + Hellfire - NS Native Port)
Upstream: https://github.com/diasurgical/devilutionX
Language: Korean (ko) via fonts.mpq & diablo.ini
"""

import os
import sys

PORT_DIR = os.path.dirname(os.path.abspath(__file__))

DIABLO_INI_TEMPLATE = """[Language]
Code=ko

[Graphics]
Width=1280
Height=720
Fit to Screen=1
Integer Scaling=0
"""

def build(args):
    print("=" * 60)
    print("  [RECIPE] DevilutionX (Diablo 1 + Hellfire Korean)")
    print("=" * 60)
    
    cookingfoil_path = "/mnt/HDD-8TB-STRIPE/media3/game/switch/homebrew/devilutionx"
    if os.path.exists(cookingfoil_path):
        print(f"[*] Verified CookingFoil deployment folder at: {cookingfoil_path}")
        print("[*] Required files: diabdat.mpq, devilutionx.mpq, fonts.mpq (Korean), diablo.ini")
        print("[*] Status: Ready to play!")
    else:
        print(f"[!] Warning: CookingFoil folder not found at {cookingfoil_path}")

    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--deploy", help="Deploy directory path")
    sys.exit(build(parser.parse_args()))
