#!/usr/bin/env python3
"""
Port Recipe: GoldenEye 007 (Nintendo Switch Native Port)
Repository: https://github.com/jshsakura/goldeneye-007-switch
"""

import os
import sys
import subprocess
import shutil

PORT_DIR = os.path.dirname(os.path.abspath(__file__))
PATCH_PATH = os.path.join(PORT_DIR, "patches", "ge007_korean.bps")
REPO_URL = "https://github.com/jshsakura/goldeneye-007-switch.git"

def build(args):
    print("=" * 60)
    print("  [RECIPE] GoldenEye 007 (NX Native Port)")
    print("=" * 60)

    work_dir = os.path.join(PORT_DIR, "src")
    if not os.path.exists(work_dir):
        # Check if /tmp/ge_pcport exists locally
        if os.path.exists("/tmp/ge_pcport/.git"):
            print("[*] Linking to existing local source checkout (/tmp/ge_pcport)...")
            work_dir = "/tmp/ge_pcport"
        else:
            print(f"[*] Cloning repository from {REPO_URL}...")
            subprocess.run(["git", "clone", REPO_URL, work_dir], check=True)

    build_script = os.path.join(work_dir, "build_switch.py")
    if not os.path.exists(build_script):
        print(f"[!] Error: {build_script} not found!", file=sys.stderr)
        return 1

    cmd = [sys.executable, build_script]
    if args.rom:
        cmd.extend(["--rom", args.rom])
    if args.zip:
        cmd.append("--zip")
    if args.no_docker:
        cmd.append("--no-docker")

    ret = subprocess.run(cmd, cwd=work_dir)
    if ret.returncode != 0:
        return ret.returncode

    # Optional deploy to destination
    if args.deploy:
        target_dir = os.path.join(args.deploy, "ge007")
        src_dist = os.path.join(work_dir, "dist", "switch", "ge007")
        if os.path.exists(src_dist):
            print(f"[*] Deploying to {target_dir}...")
            shutil.copytree(src_dist, target_dir, dirs_exist_ok=True)
            print("[*] Deployment complete!")

    return 0

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", help="Path to GoldenEye 007 ROM")
    parser.add_argument("--zip", action="store_true", help="Create distribution zip")
    parser.add_argument("--no-docker", action="store_true")
    parser.add_argument("--deploy", help="Directory to deploy to (e.g. /mnt/.../homebrew/)")
    sys.exit(build(parser.parse_args()))
