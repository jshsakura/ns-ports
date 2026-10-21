#!/usr/bin/env python3
"""
NS Ports Hub - Master Build & Management CLI
Curated collection of classic game native ports for NS / Horizon OS.
"""

import os
import sys
import json
import argparse
import importlib.util
import shutil
import subprocess

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
PORTS_JSON = os.path.join(ROOT_DIR, "ports.json")

def load_ports():
    if not os.path.exists(PORTS_JSON):
        return []
    with open(PORTS_JSON, "r", encoding="utf-8") as f:
        return json.load(f)

def list_ports():
    ports = load_ports()
    print("=" * 85)
    print(f"  {'ID':<16} {'TITLE':<32} {'KOR':<6} {'GYRO':<6} {'STATUS'}")
    print("=" * 85)
    for p in ports:
        pid = p.get("id", "")
        name = p.get("name", "")
        if len(name) > 30:
            name = name[:28] + ".."
        kor = "O" if p.get("korean") else "-"
        gyro = "O" if p.get("motion_controls") else "-"
        status = p.get("status", "planned")
        recipe_exists = os.path.exists(os.path.join(ROOT_DIR, "ports", pid, "recipe.py"))
        if status == "verified":
            mark = "[VERIFIED]"
        elif status == "boot-ok":
            mark = "[BOOT-OK]"
        elif recipe_exists:
            mark = "[RECIPE]"
        else:
            mark = f"[{status}]"
        print(f"  {pid:<16} {name:<32} {kor:<6} {gyro:<6} {mark}")
    print("=" * 85)
    print(f"Total: {len(ports)} ports registered in catalogue.")
    print("Usage: python3 build.py <port-id> [options]")

REGISTER = os.path.join(ROOT_DIR, "tools", "port_register.py")


def new_port(argv):
    """python3 build.py new <id> "<title>" [--nro 파일] [--icon 파일] : 파일만 있으면 바로 쓰는 포트 뼈대를 만든다."""
    import shutil
    ap = argparse.ArgumentParser(prog="build.py new")
    ap.add_argument("id")
    ap.add_argument("title", help="목록에 보일 이름, 예: '게임 이름 (Game Name)'")
    ap.add_argument("--nro", help="이미 빌드된 NRO 파일 (ports/<id>/in/ 으로 복사)")
    ap.add_argument("--icon", help="아이콘 JPEG (ports/<id>/ 으로 복사)")
    ap.add_argument("--reason", default="", help="게임 데이터가 필요한 이유(앱 설명에 쓰임)")
    a = ap.parse_args(argv)
    d = os.path.join(ROOT_DIR, "ports", a.id)
    if os.path.exists(os.path.join(d, "port.json")):
        print(f"[!] ports/{a.id}/port.json 이 이미 있습니다.", file=sys.stderr)
        return 1
    os.makedirs(os.path.join(d, "in"), exist_ok=True)
    os.makedirs(os.path.join(d, "overlay"), exist_ok=True)
    icon = "icon.jpg"
    if a.icon:
        shutil.copyfile(a.icon, os.path.join(d, icon))
    if a.nro:
        shutil.copyfile(a.nro, os.path.join(d, "in", a.id + ".nro"))
    profile = {"id": a.id, "title": a.title, "reason": a.reason or f"{a.title} 게임 데이터가 함께 있어야 실행됩니다",
               "base": ".", "icon": icon, "nro": {"src": f"in/{a.id}.nro", "out": f"{a.id}.nro"},
               "overlays": ["overlay"], "files": []}
    with open(os.path.join(d, "port.json"), "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(d, ".gitignore"), "w") as f:
        f.write("in/\ndist/\n")
    with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
        f.write(f"# {a.title}\n\n준비물: `in/{a.id}.nro`(빌드된 NRO), `icon.jpg`, 내 게임 데이터 폴더.\n"
                f"덮어쓸 파일은 `overlay/` 에 같은 구조로 넣고, 따로 둘 파일은 `port.json` 의 `files` 에 적는다.\n\n"
                f"```\npython3 build.py {a.id} --rom <게임 데이터> --deploy <homebrew 폴더>\n```\n")
    ports = load_ports()
    if not any(p.get("id") == a.id for p in ports):
        ports.append({"id": a.id, "name": a.title, "category": "", "engine": "", "status": "planned", "korean": False,
                      "motion_controls": False, "description": "", "required_assets": "내 게임 데이터", "nro": a.id + ".nro"})
        with open(PORTS_JSON, "w", encoding="utf-8") as f:
            json.dump(ports, f, ensure_ascii=False, indent=2)
            f.write("\n")
    print(f"[*] ports/{a.id}/ 를 만들었습니다. 빠진 것: " + ", ".join(
        x for x, ok in (("NRO(in/)", a.nro), ("아이콘", a.icon)) if not ok) or "없음")
    print(f"[*] 다음: python3 build.py {a.id} --rom <게임 데이터> --deploy <homebrew 폴더>")
    return 0


def generic_build(port_id, args):
    """recipe.py 가 없고 port.json 만 있는 포트: 파일을 조립해 homebrew 폴더에 반영한다."""
    cmd = [sys.executable, REGISTER, os.path.join(ROOT_DIR, "ports", port_id, "port.json")]
    if args.rom:
        cmd += ["--data", args.rom]
    if not args.deploy:
        cmd.append("--no-register")
    extra = getattr(args, "extra", [])
    cmd += [x for x in extra if x in ("--dry-run", "--no-register")]
    env = dict(os.environ)
    out = args.deploy or os.path.join(ROOT_DIR, "ports", port_id, "dist", "switch")
    env["COOK_HOMEBREW_DIR"] = out
    ret = subprocess.call(cmd, env=env)
    if ret == 0 and args.zip:
        shutil.make_archive(os.path.join(ROOT_DIR, "ports", port_id, "dist", port_id), "zip", out)
        print("[*] zip 을 ports/%s/dist/ 에 만들었습니다." % port_id)
    return ret


def run_port(port_id, extra_args):
    recipe_path = os.path.join(ROOT_DIR, "ports", port_id, "recipe.py")
    if not os.path.exists(recipe_path) and os.path.exists(os.path.join(ROOT_DIR, "ports", port_id, "port.json")):
        parser = argparse.ArgumentParser(prog=f"build.py {port_id}")
        parser.add_argument("--rom", help="내 게임 데이터 폴더")
        parser.add_argument("--zip", action="store_true")
        parser.add_argument("--deploy", help="homebrew 폴더")
        args, unknown = parser.parse_known_args(extra_args)
        args.extra = unknown
        return generic_build(port_id, args)
    if not os.path.exists(recipe_path):
        print(f"[!] No recipe implemented for '{port_id}' yet.", file=sys.stderr)
        print(f"[*] Check 'ports.json' for required assets and upstream sources.", file=sys.stderr)
        return 1

    spec = importlib.util.spec_from_file_location("recipe", recipe_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    parser = argparse.ArgumentParser(prog=f"build.py {port_id}")
    parser.add_argument("--rom", help="Path to required ROM file")
    parser.add_argument("--zip", action="store_true", help="Create zip package")
    parser.add_argument("--no-docker", action="store_true", help="Do not use Docker")
    parser.add_argument("--deploy", help="Deploy directory path")
    args, unknown = parser.parse_known_args(extra_args)
    args.extra = unknown  # port-specific options a recipe parses itself

    return module.build(args)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-l", "--list", "list"):
        list_ports()
        return 0

    port_id = sys.argv[1]
    if port_id == "new":
        return new_port(sys.argv[2:])
    if port_id in ("-h", "--help"):
        print("NS Ports Hub CLI")
        print("Commands:")
        print("  python3 build.py --list                 List all ports")
        print("  python3 build.py <port-id> [options]    Build a specific port")
        print("  python3 build.py new <id> \"<title>\" [--nro F] [--icon F]   Scaffold a port from files you already have")
        return 0

    return run_port(port_id, sys.argv[2:])

if __name__ == "__main__":
    sys.exit(main())
