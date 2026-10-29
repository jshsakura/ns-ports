#!/usr/bin/env python3
"""
Port Recipe: The Legend of Zelda: A Link to the Past (snesrev/zelda3, Switch build)

  python3 build.py zelda3-ko --rom <folder with your zelda3_assets.dat> [--variant ko|original] [--zip] [--deploy <homebrew dir>]

  original: upstream snesrev/zelda3 at a pinned commit, built for Switch.
  ko:       the same plus patches/zelda3-ko.patch (Korean dialogue rendering: 16px variable-width glyphs).

The Korean glyph/dialogue tables are generated from the Korean patch outside this repository and baked into
zelda3_assets.dat; supply that file (and the stock one for `original`) in the --rom folder. No ROM or asset is
included here. Building needs Docker (devkitPro image).
"""
import argparse
import os
import shutil
import subprocess
import sys

VARIANTS = ("ko", "original")
PORT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(PORT_DIR))
REGISTER = os.path.join(ROOT_DIR, "tools", "port_register.py")
SRC = os.path.join(PORT_DIR, "src")
UPSTREAM, COMMIT = "https://github.com/snesrev/zelda3.git", "a23632a"
IMAGE = "devkitpro/devkita64:latest"


def run(cmd, cwd=None):
    print("[*]", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def fetch(variant):
    if not os.path.isdir(os.path.join(SRC, ".git")):
        run(["git", "clone", "--quiet", UPSTREAM, SRC])
    run(["git", "checkout", "--quiet", "--force", COMMIT], cwd=SRC)
    run(["git", "clean", "-qfd"], cwd=SRC)
    if variant == "ko":
        run(["git", "apply", "--whitespace=nowarn", os.path.join(PORT_DIR, "patches", "zelda3-ko.patch")], cwd=SRC)
    shutil.copyfile(os.path.join(PORT_DIR, "ref", "zelda3.nacp"), os.path.join(SRC, "zelda3.nacp"))


def compile_nro():
    run(["docker", "run", "--rm", "-v", SRC + ":/src", "-v", os.path.join(PORT_DIR, "scripts") + ":/scripts",
         IMAGE, "sh", "/scripts/build-switch.sh"])
    os.makedirs(os.path.join(PORT_DIR, "in"), exist_ok=True)
    shutil.copyfile(os.path.join(SRC, "zelda3.nro"), os.path.join(PORT_DIR, "in", "zelda3.nro"))


def build(args):
    own = argparse.ArgumentParser(prog="build.py zelda3-ko")
    own.add_argument("--skip-build", action="store_true", help="reuse in/zelda3.nro")
    own.add_argument("--dry-run", action="store_true")
    opt = own.parse_args(getattr(args, "extra", []))
    variant = getattr(args, "variant", None) or "ko"
    if not opt.skip_build:
        if args.no_docker:
            print("[!] The build runs in Docker; --no-docker is not supported (use --skip-build).", file=sys.stderr)
            return 1
        fetch(variant)
        compile_nro()
    out = args.deploy or os.path.join(PORT_DIR, "dist", "switch")
    cmd = [sys.executable, REGISTER, os.path.join(PORT_DIR, "port.json"), "--variant", variant]
    if args.rom:
        cmd += ["--data", args.rom]
    if opt.dry_run:
        cmd.append("--dry-run")
    ret = subprocess.call(cmd, env=dict(os.environ, NS_PORTS_OUT=out))
    if ret == 0 and args.zip and not opt.dry_run:
        shutil.make_archive(os.path.join(PORT_DIR, "dist", "zelda3-" + variant), "zip", out)
        print("[*] zip:", os.path.join(PORT_DIR, "dist", "zelda3-%s.zip" % variant))
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", help="folder containing your zelda3_assets.dat")
    parser.add_argument("--variant", choices=VARIANTS)
    parser.add_argument("--zip", action="store_true")
    parser.add_argument("--no-docker", action="store_true")
    parser.add_argument("--deploy")
    a, rest = parser.parse_known_args()
    a.extra = rest
    sys.exit(build(a))
