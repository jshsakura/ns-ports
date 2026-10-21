#!/usr/bin/env python3
"""
Port Recipe: Counter-Strike 1.6 (Xash3D FWGS + cs16-client, Korean/global builds)

Assembles the built binaries and overlays into a CookingFoil-style folder.
Building the binaries themselves is described in BUILD.md (devkitPro container).
"""
import argparse
import os
import subprocess
import sys

PORT_DIR = os.path.dirname(os.path.abspath(__file__))
REGISTER = os.path.join(os.path.dirname(os.path.dirname(PORT_DIR)), "tools", "port_register.py")


def build(args):
    own = argparse.ArgumentParser(prog="build.py cstrike")
    own.add_argument("--variant", default="ko", choices=["ko", "en"], help="ko: Korean, en: stock/global")
    own.add_argument("--data", help="your own cstrike/valve game data folder (hard-linked)")
    own.add_argument("--dry-run", action="store_true")
    own.add_argument("--no-register", action="store_true")
    opt = own.parse_args(getattr(args, "extra", []))
    cmd = [sys.executable, REGISTER, os.path.join(PORT_DIR, "port.json"), "--variant", opt.variant]
    if opt.data:
        cmd += ["--data", opt.data]
    if opt.dry_run:
        cmd.append("--dry-run")
    if opt.no_register:
        cmd.append("--no-register")
    env = dict(os.environ)
    if args.deploy:
        env["COOK_HOMEBREW_DIR"] = args.deploy
    return subprocess.call(cmd, env=env)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--deploy", help="homebrew folder to assemble into (COOK_HOMEBREW_DIR)")
    a, rest = parser.parse_known_args()
    a.extra = rest
    sys.exit(build(a))
