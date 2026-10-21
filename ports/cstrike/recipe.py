#!/usr/bin/env python3
"""
Port Recipe: Counter-Strike 1.6 (Xash3D FWGS + cs16-client, Korean/global builds)

Same flow as the other native ports:
  python3 build.py cstrike --rom <your cstrike/valve data folder> [--variant ko|original] [--zip] [--deploy <homebrew dir>]

  1. fetch   upstream sources at pinned commits into ports/cstrike/src and apply patches/
  2. build   engine and game code in the devkitPro container (docker)
  3. assemble binaries + overlays + your game data into dist/switch/<id>/
  4. --zip   pack it, --deploy copy it into a homebrew folder (CookingFoil layout)

The game data is yours: it is hard-linked, never uploaded or committed.
Options and defaults can also live in ns-ports.config.json (see ns-ports.config.example.json).
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
DIST = os.path.join(PORT_DIR, "dist")

# repo -> (url, commit, subdir). Submodules are initialised recursively.
UPSTREAM = [
    ("xash3d-fwgs", "https://github.com/FWGS/xash3d-fwgs.git", "03a396e"),
    ("cs16-client", "https://github.com/Velaron/cs16-client.git", "9778fec"),
    ("libsolder", "https://github.com/fgsfdsfgs/libsolder.git", "36e5f31"),
]
# patch file -> directory (relative to src/) it applies in
PATCHES = [
    ("xash3d-fwgs.patch", "xash3d-fwgs"),
    ("mainui.patch", "xash3d-fwgs/3rdparty/mainui"),
    ("cs16-client.patch", "cs16-client"),
    ("regamedll.patch", "cs16-client/3rdparty/ReGameDLL_CS"),
    ("yapb.patch", "cs16-client/3rdparty/yapb"),
]
DOCKER_IMAGE = "devkitpro/devkita64:latest"


def run(cmd, cwd=None, check=True):
    print("[*]", " ".join(cmd))
    return subprocess.run(cmd, cwd=cwd, check=check)


def fetch():
    os.makedirs(SRC, exist_ok=True)
    for name, url, commit in UPSTREAM:
        d = os.path.join(SRC, name)
        if os.path.isdir(os.path.join(d, ".git")):
            continue
        run(["git", "clone", "--quiet", url, d])
        run(["git", "checkout", "--quiet", commit], cwd=d)
        run(["git", "submodule", "update", "--init", "--recursive", "--quiet"], cwd=d)
    marker = os.path.join(SRC, ".patched")
    if os.path.exists(marker):
        return
    for patch, sub in PATCHES:
        # the cs16-client patch also records a dirty submodule pointer; skip gitlinks
        run(["git", "apply", "--whitespace=nowarn", "--exclude=3rdparty/ReGameDLL_CS",
             os.path.join(PORT_DIR, "patches", patch)], cwd=os.path.join(SRC, sub))
    open(marker, "w").write("ok\n")


def docker_build(script):
    uid, gid = str(os.getuid()), str(os.getgid())
    run(["docker", "run", "--rm", "-e", "HOST_UID=" + uid, "-e", "HOST_GID=" + gid,
         "-v", SRC + ":/work", "-v", os.path.join(PORT_DIR, "out") + ":/work/out",
         "-v", os.path.join(PORT_DIR, "scripts") + ":/work/scripts", "-w", "/work",
         DOCKER_IMAGE, "bash", "/work/scripts/" + script])


def build(args):
    own = argparse.ArgumentParser(prog="build.py cstrike")
    own.add_argument("--skip-build", action="store_true", help="reuse binaries in out/")
    own.add_argument("--dry-run", action="store_true")
    own.add_argument("--no-register", action="store_true")
    opt = own.parse_args(getattr(args, "extra", []))

    if not opt.skip_build:
        if args.no_docker:
            print("[!] The devkitPro build runs in Docker; --no-docker is not supported (use --skip-build).", file=sys.stderr)
            return 1
        fetch()
        os.makedirs(os.path.join(PORT_DIR, "out"), exist_ok=True)
        docker_build("build-engine.sh")
        docker_build("build-cs.sh")

    out = args.deploy or os.path.join(DIST, "switch")
    cmd = [sys.executable, REGISTER, os.path.join(PORT_DIR, "port.json")]
    if getattr(args, "variant", None):
        cmd += ["--variant", args.variant]
    if args.rom:
        cmd += ["--data", args.rom]
    if opt.dry_run:
        cmd.append("--dry-run")
    if opt.no_register or not args.deploy:
        cmd.append("--no-register")
    env = dict(os.environ, COOK_HOMEBREW_DIR=out)
    ret = subprocess.call(cmd, env=env)
    if ret == 0 and args.zip and not opt.dry_run:
        shutil.make_archive(os.path.join(DIST, "cstrike"), "zip", out)
        print("[*] zip:", os.path.join(DIST, "cstrike.zip"))
    return ret


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", help="your cstrike/valve game data folder")
    parser.add_argument("--zip", action="store_true")
    parser.add_argument("--no-docker", action="store_true")
    parser.add_argument("--deploy", help="homebrew folder to assemble into (registers via the server API when configured)")
    a, rest = parser.parse_known_args()
    a.extra = rest
    sys.exit(build(a))
