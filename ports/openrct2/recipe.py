#!/usr/bin/env python3
"""
Port Recipe: OpenRCT2 (Nintendo Switch, Korean build)

  python3 build.py openrct2 --rom <folder with your RollerCoaster Tycoon 2 files> [--variant ko|original] [--zip] [--deploy <homebrew dir>]

  original: the Wander-Eule/OpenRCT2-Switch fork at a pinned commit, built as is (font-less, DISABLE_TTF).
  ko:       the same plus patches/korean-switch.patch (embedded Korean TrueType font, ko-KR strings, Switch locale handling).

The build runs in a devkitPro container that also needs ICU 78 and libzip (scripts/Dockerfile, scripts/build-icu78.sh);
set OPENRCT2_BUILDER to an existing image that has them. Game data is never included.
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
UPSTREAM, COMMIT = "https://github.com/Wander-Eule/OpenRCT2-Switch.git", "7d4673d8b2"
IMAGE = os.environ.get("OPENRCT2_BUILDER", "openrct2-builder:full")


def run(cmd, cwd=None):
    print("[*]", " ".join(cmd))
    subprocess.run(cmd, cwd=cwd, check=True)


def fetch(variant):
    if not os.path.isdir(os.path.join(SRC, ".git")):
        run(["git", "clone", "--quiet", UPSTREAM, SRC])
    run(["git", "checkout", "--quiet", "--force", COMMIT], cwd=SRC)
    run(["git", "clean", "-qfd"], cwd=SRC)
    if variant == "ko":
        run(["git", "apply", "--whitespace=nowarn", os.path.join(PORT_DIR, "patches", "korean-switch.patch")], cwd=SRC)
        shutil.copyfile(os.path.join(PORT_DIR, "assets", "NanumBarunGothic.ttf"), os.path.join(SRC, "resources", "font.ttf"))


def compile_nro(variant):
    have = subprocess.run(["docker", "image", "inspect", IMAGE], capture_output=True).returncode == 0
    if not have:
        print("[!] builder image %s not found. Build it from scripts/Dockerfile (+ scripts/build-icu78.sh) or set OPENRCT2_BUILDER." % IMAGE, file=sys.stderr)
        sys.exit(1)
    flag = "" if variant == "ko" else "-DDISABLE_TTF=ON "
    os.makedirs(os.path.join(SRC, "build-switch"), exist_ok=True)
    run(["docker", "run", "--rm", "-v", SRC + ":/source", "-w", "/source/build-switch", IMAGE, "sh", "-c",
         "cmake %s-DCMAKE_TOOLCHAIN_FILE=/opt/devkitpro/cmake/Switch.cmake /source >/dev/null && make -j$(nproc)" % flag])
    os.makedirs(os.path.join(PORT_DIR, "in"), exist_ok=True)
    shutil.copyfile(os.path.join(SRC, "build-switch", "openrct2.nro"), os.path.join(PORT_DIR, "in", "openrct2.nro"))


def build(args):
    own = argparse.ArgumentParser(prog="build.py openrct2")
    own.add_argument("--skip-build", action="store_true", help="reuse in/openrct2.nro")
    own.add_argument("--dry-run", action="store_true")
    opt = own.parse_args(getattr(args, "extra", []))
    variant = getattr(args, "variant", None) or "ko"
    if not opt.skip_build:
        if args.no_docker:
            print("[!] The build runs in Docker; --no-docker is not supported (use --skip-build).", file=sys.stderr)
            return 1
        fetch(variant)
        compile_nro(variant)
    out = args.deploy or os.path.join(PORT_DIR, "dist", "switch")
    cmd = [sys.executable, REGISTER, os.path.join(PORT_DIR, "port.json"), "--variant", variant]
    if args.rom:
        cmd += ["--data", args.rom]
    if opt.dry_run:
        cmd.append("--dry-run")
    ret = subprocess.call(cmd, env=dict(os.environ, NS_PORTS_OUT=out))
    if ret == 0 and args.zip and not opt.dry_run:
        shutil.make_archive(os.path.join(PORT_DIR, "dist", "openrct2-" + variant), "zip", out)
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom")
    parser.add_argument("--variant", choices=VARIANTS)
    parser.add_argument("--zip", action="store_true")
    parser.add_argument("--no-docker", action="store_true")
    parser.add_argument("--deploy")
    a, rest = parser.parse_known_args()
    a.extra = rest
    sys.exit(build(a))
