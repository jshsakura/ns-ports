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
        recipe_exists = any(os.path.exists(os.path.join(ROOT_DIR, "ports", pid, f)) for f in ("recipe.py", "port.json"))
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
    if a.icon:
        shutil.copyfile(a.icon, os.path.join(d, "icon.jpg"))
    if a.nro:
        shutil.copyfile(a.nro, os.path.join(d, "in", a.id + ".nro"))
    profile = {"id": a.id, "title": a.title, "reason": a.reason or f"{a.title} 게임 데이터가 함께 있어야 실행됩니다",
               "base": ".", "nro": {"src": f"in/{a.id}.nro", "out": f"{a.id}.nro"},
               "overlays": ["overlay"], "files": []}
    with open(os.path.join(d, "port.json"), "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(d, "slots.json"), "w", encoding="utf-8") as f:
        json.dump([{"path": f"in/{a.id}.nro", "what": "빌드된 NRO"}], f, ensure_ascii=False, indent=2)
        f.write("\n")
    with open(os.path.join(d, ".gitignore"), "w") as f:
        f.write("in/\ndist/\nicon.jpg\n")
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
    data = args.rom or (os.path.join(ROOT_DIR, "ports", port_id, "in", "data")
                        if os.path.isdir(os.path.join(ROOT_DIR, "ports", port_id, "in", "data")) else None)
    if data:
        cmd += ["--data", data]
    if args.variant:
        cmd += ["--variant", args.variant]
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


def _port_json(port_id):
    path = os.path.join(ROOT_DIR, "ports", port_id, "port.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return None


def load_slots(port_id):
    """칸 목록. slots.json 이 있으면 그것, 없으면 port.json 과 ports.json 에서 NRO 와 게임 데이터 칸을 만든다."""
    path = os.path.join(ROOT_DIR, "ports", port_id, "slots.json")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    prof = _port_json(port_id)
    if prof is None or os.path.exists(os.path.join(ROOT_DIR, "ports", port_id, "recipe.py")):
        return None
    meta = next((p for p in load_ports() if p.get("id") == port_id), {})
    up = meta.get("upstream")
    return [
        {"path": prof["nro"]["src"], "what": "스위치용 NRO",
         "get": f"{up} 의 릴리스를 받거나 직접 빌드" if up else "직접 빌드한 NRO"},
        {"path": "in/data", "what": meta.get("required_assets") or "게임 데이터",
         "get": "내가 가진 정품 데이터 (--rom <폴더> 로 따로 줘도 된다)"},
    ]


ICON_SLOT = {"path": "icon.jpg", "what": "앱 아이콘 (256x256 JPEG)", "optional": True, "kind": "image",
             "get": "직접 구하거나 만든다. 없으면 NRO 에 든 아이콘을 그대로 쓴다"}


def _filled(path):
    return os.path.isdir(path) and bool(os.listdir(path)) or os.path.isfile(path)


def check_slots(port_id, variant=None, quiet_ok=False, rom=None):
    """칸마다 파일이 있는지 보고 비어 있는 칸과 구하는 곳을 알려 준다. 빠진 필수 칸이 없으면 True."""
    slots = load_slots(port_id)
    if slots is None:
        print(f"[*] {port_id}: 이 포트는 소스부터 빌드하거나 전용 레시피를 씁니다. ports/{port_id}/README.md 를 보세요.")
        return True
    if not any(sl["path"] == ICON_SLOT["path"] for sl in slots):
        slots = slots + [ICON_SLOT]
    port_dir = os.path.join(ROOT_DIR, "ports", port_id)
    missing = []
    for sl in slots:
        if sl.get("variant") and variant and sl["variant"] != variant:
            continue
        if rom and sl["path"].startswith("in/data"):  # --rom 으로 데이터 폴더를 따로 줬으면 in/data 칸은 보지 않는다
            continue
        have = _filled(os.path.join(port_dir, sl["path"]))
        if not have and not sl.get("optional"):
            missing.append(sl)
        if have and quiet_ok:
            continue
        mark = "OK  " if have else ("빈칸" if not sl.get("optional") else "선택")
        print(f"  [{mark}] ports/{port_id}/{sl['path']:<38} {sl['what']}")
        if not have and sl.get("get"):
            print(f"         구하는 곳: {sl['get']}")
    if missing:
        print(f"[!] 채울 칸 {len(missing)}개가 비어 있습니다. 위 '구하는 곳'에서 받아 해당 위치에 두고 다시 실행하세요.", file=sys.stderr)
    return not missing


def guide_cmd(argv):
    """python3 build.py guide|check <id> : 무엇을 어디에 두고 어떤 명령을 치는지 순서대로 보여 준다."""
    ids = argv or [p["id"] for p in load_ports() if load_slots(p["id"]) is not None]
    ok = True
    for pid in ids:
        print(f"== {pid}")
        print("1) 받아서 둘 것")
        ok &= check_slots(pid)
        print("2) 이미지: 앱 아이콘만 이 저장소가 쓰고(선택), 배너·스크린샷은 다루지 않습니다.")
        print("   icon.jpg 는 직접 구한 256x256 JPEG 를 위 위치에 두면 되고, 안 두면 NRO 의 기본 아이콘이 나옵니다.")
        print("3) 실행")
        print(f"   python3 build.py {pid} --zip      # 결과: ports/{pid}/dist/switch/{pid}/ 와 {pid}.zip")
    return 0 if ok else 1


check_cmd = guide_cmd


def run_port(port_id, extra_args):
    if "--check" in extra_args:
        return check_cmd([port_id])
    variant = extra_args[extra_args.index("--variant") + 1] if "--variant" in extra_args else None
    rom = extra_args[extra_args.index("--rom") + 1] if "--rom" in extra_args else None
    if not rom:  # ns-ports.config.json 의 data 에 이 포트의 데이터 폴더가 있으면 그것도 데이터를 준 것으로 본다
        sys.path.insert(0, os.path.join(ROOT_DIR, "tools"))
        import port_register
        rom = (port_register.load_config().get("data") or {}).get(port_id)
    if not check_slots(port_id, variant, quiet_ok=True, rom=rom):
        return 1
    recipe_path = os.path.join(ROOT_DIR, "ports", port_id, "recipe.py")
    if not os.path.exists(recipe_path) and os.path.exists(os.path.join(ROOT_DIR, "ports", port_id, "port.json")):
        parser = argparse.ArgumentParser(prog=f"build.py {port_id}")
        parser.add_argument("--rom", help="내 게임 데이터 폴더")
        parser.add_argument("--zip", action="store_true")
        parser.add_argument("--deploy", help="homebrew 폴더")
        parser.add_argument("--variant", help="ko(한국어) 또는 original(원본)")
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
    parser.add_argument("--variant", help="ko (Korean) or original; every port takes it")
    args, unknown = parser.parse_known_args(extra_args)
    if args.variant and not getattr(module, "VARIANTS", None):
        print(f"[!] '{port_id}' 레시피는 아직 --variant 를 구분하지 않습니다. 기본 판으로 진행합니다.", file=sys.stderr)
    args.extra = unknown  # port-specific options a recipe parses itself

    return module.build(args)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-l", "--list", "list"):
        list_ports()
        return 0

    port_id = sys.argv[1]
    if port_id == "new":
        return new_port(sys.argv[2:])
    if port_id in ("check", "guide"):
        return guide_cmd(sys.argv[2:])
    if port_id in ("-h", "--help"):
        print("NS Ports Hub CLI")
        print("Commands:")
        print("  python3 build.py --list                 List all ports")
        print("  python3 build.py <port-id> [options]    Build a specific port")
        print("  python3 build.py guide <id>             What to get, where to put it, which command to run (alias: check)")
        print("  python3 build.py new <id> \"<title>\" [--nro F] [--icon F]   Scaffold a port from files you already have")
        return 0

    return run_port(port_id, sys.argv[2:])

if __name__ == "__main__":
    sys.exit(main())
