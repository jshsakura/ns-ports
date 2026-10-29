#!/usr/bin/env python3
"""
Port Recipe: The Legend of Zelda: The Wind Waker HD (centollOS/SwitchWakerHD, assemble)

  python3 build.py wwhd --rom <WiiU 덤프 루트(code/, content/, meta/ 가 보이는 폴더)> [--variant ko|original] [--zip] [--deploy <homebrew 폴더>]

ports/wwhd/in/ 준비물 (배치표는 README.md):
  wwhd.nro                     SwitchWakerHD 빌드 NRO
  permanent_2d_UsEnglish.pack  한글 패치의 2d 팩(한국어 텍스트 주입본)
  Title_00.szs                 한글 패치의 타이틀 화면 레이아웃

ko 판은 언어 설정과 상관없이 한글이 뜨도록 세 언어 슬롯(UsEnglish/JpJapanese/EuEnglish)에
같은 팩을 넣는다(실기 검증된 배포본과 동일 구성). original 은 패치 없이 원본 그대로 조립한다.
저장소에는 NRO 와 한글 패치 산출물을 담지 않는다(클린룸).
"""
import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile

PORT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(PORT_DIR))
IN = os.path.join(PORT_DIR, "in")
ICON = os.path.join(PORT_DIR, "icon.jpg")  # 선택. 256x256 JPEG 를 두면 앱 아이콘으로 쓴다
TITLE = "젤다의 전설 바람의 지휘봉 HD"  # 실기 검증된 배포본의 NACP 이름과 같다
VARIANTS = ("ko", "original")

# 한글 패치 배치표: 조립 결과 game/ 안 경로. pack 하나가 두 언어 슬롯에 같이 들어간다.
# EuEnglish 슬롯은 실기 검증본에 없는 파일이라 다루지 않는다(미국판 언어 선택에 안 쓰임).
KO_SLOTS = [
    ("permanent_2d_UsEnglish.pack", "game/content/Common/Pack/permanent_2d_UsEnglish.pack"),
    ("permanent_2d_JpJapanese.pack", "game/content/Common/Pack/permanent_2d_JpJapanese.pack"),
    ("Title_00.szs", "game/content/Common/Layout/Title_00.szs"),
]
KO_INPUTS = ("Title_00.szs",)  # 사용자가 in/ 에 받아 두는 파일
# 한글 pack 은 저장소의 차이 패치(patches/)를 덤프의 UsFrench.pack(원본 그대로) 위에 적용해 만든다.
# in/ 에 permanent_2d_UsEnglish.pack 을 직접 두면 그것을 우선 쓴다.
PACK_PATCH = os.path.join(PORT_DIR, "patches", "permanent_2d_UsEnglish.xdelta")
PACK_BASE = "content/Common/Pack/permanent_2d_UsFrench.pack"
DUMP_SKIP = ("content/Common/Pack/permanent_2d_EuEnglish.pack",)  # 검증본 구성에 없는 덤프 파일

sys.path.insert(0, os.path.join(ROOT_DIR, "tools"))
import port_register as pr  # noqa: E402  (retitle_nro / register / load_config 재사용)


def ko_pack(dump, dry):
    """한글 pack 바이트를 돌려준다. in/ 에 직접 둔 파일이 우선이고, 없으면 덤프 UsFrench.pack 에 차이 패치를 적용한다."""
    own = os.path.join(IN, "permanent_2d_UsEnglish.pack")
    if os.path.exists(own):
        return open(own, "rb").read()
    base = os.path.join(dump, PACK_BASE)
    if not os.path.exists(base) or not os.path.exists(PACK_PATCH):
        print("[!] 한글 pack 을 만들 수 없습니다: 덤프의 %s 또는 patches/ 가 없습니다." % PACK_BASE, file=sys.stderr)
        return None
    if not shutil.which("xdelta3"):
        print("[!] xdelta3 가 필요합니다 (예: sudo apt install xdelta3).", file=sys.stderr)
        return None
    if dry:
        return b""
    with tempfile.TemporaryDirectory() as t:
        out = os.path.join(t, "pack")
        r = subprocess.run(["xdelta3", "-d", "-s", base, PACK_PATCH, out], capture_output=True, text=True)
        if r.returncode != 0:
            print("[!] 패치 적용 실패(덤프가 USA v0 원본이 아닐 수 있습니다):", r.stderr.strip(), file=sys.stderr)
            return None
        return open(out, "rb").read()


def build(args):
    own = argparse.ArgumentParser(prog="build.py wwhd")
    own.add_argument("--dry-run", action="store_true")
    own.add_argument("--no-register", action="store_true")
    opt = own.parse_args(getattr(args, "extra", []))
    variant = getattr(args, "variant", None) or "ko"

    nro = os.path.join(IN, "wwhd.nro")
    if not os.path.exists(nro):
        print("[!] %s 이(가) 없습니다. SwitchWakerHD 빌드 NRO 를 그 이름으로 in/ 에 두세요." % nro, file=sys.stderr)
        return 1
    missing = [f for f in KO_INPUTS if not os.path.exists(os.path.join(IN, f))]
    if variant == "ko" and missing:
        print("[!] 한글 판에 필요한 파일이 in/ 에 없습니다: %s" % ", ".join(missing), file=sys.stderr)
        print("[*] 한글 패치 배포본의 permanent_2d_*.pack 과 Title_00.szs 를 ports/wwhd/in/ 에 두세요.", file=sys.stderr)
        print("[*] 원본 그대로 조립하려면 --variant original 을 쓰세요.", file=sys.stderr)
        return 1
    if not args.rom or not os.path.isdir(os.path.join(args.rom, "content")):
        print("[!] --rom 에는 content/ 폴더가 보이는 WiiU 덤프 루트(code/, content/, meta/)를 지정하세요.", file=sys.stderr)
        return 1

    out = args.deploy or os.path.join(PORT_DIR, "dist", "switch")
    root = os.path.join(out, "wwhd")
    print("[*] 조립:", root)

    # 1) 게임 데이터: 하드링크로 연결. 한글 패치가 덮어쓸 경로는 빼고 나중에 새 파일로 쓴다(원본 보호).
    skip = {dst for _, dst in KO_SLOTS} if variant == "ko" else set()
    skip |= {"game/" + p for p in DUMP_SKIP}
    n = 0
    for d, _, fs in os.walk(args.rom):
        for f in fs:
            s = os.path.join(d, f)
            r = os.path.relpath(s, args.rom)
            if os.path.join("game", r) in skip:
                continue
            dst = os.path.join(root, "game", r)
            if opt.dry_run:
                n += 1
                continue
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            if not os.path.exists(dst):
                try:
                    os.link(s, dst)
                except OSError:
                    shutil.copyfile(s, dst)
                n += 1
    print(("[예행] " if opt.dry_run else "") + "게임 데이터 %d개" % n)

    # 2) 한글 패치: pack 하나를 세 언어 슬롯에 같은 내용으로, szs 는 Layout 에.
    if variant == "ko":
        pack = ko_pack(args.rom, opt.dry_run)
        if pack is None:
            return 1
        szs = open(os.path.join(IN, "Title_00.szs"), "rb").read()
        for slot, dst_rel in KO_SLOTS:
            data = pack if slot.endswith(".pack") else szs
            print(("[예행] " if opt.dry_run else "") + "한글 패치 %s -> %s" % (slot, dst_rel))
            if not opt.dry_run:
                dst = os.path.join(root, dst_rel)
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                open(dst, "wb").write(data)

    if not opt.dry_run:
        # 3) NRO: 이름 교체(ASET 이 없으면 있는 그대로 복사). 아이콘 오류는 아래 try 에 가려지지 않게 먼저 검사한다.
        if os.path.exists(ICON):
            pr.check_icon(ICON)
        try:
            open(os.path.join(root, "wwhd.nro"), "wb").write(pr.retitle_nro(nro, ICON if os.path.exists(ICON) else None, TITLE))
        except SystemExit:
            print("[*] NRO 에 ASET 이 없어 그대로 복사합니다.")
            shutil.copyfile(nro, os.path.join(root, "wwhd.nro"))
        # 4) 폴더 매니페스트 (실기 검증본과 같은 내용)
        manifest = {"nro": "wwhd.nro", "mode": "folder",
                    "reason": "게임 데이터가 함께 있어야 실행됩니다", "rules": [], "excluded": [],
                    "own_metadata": False}
        with open(os.path.join(root, ".cookingfoil.json"), "w", encoding="utf-8") as f:
            json.dump(manifest, f, ensure_ascii=False, separators=(",", ":"))

    if args.zip and not opt.dry_run:
        os.makedirs(os.path.join(PORT_DIR, "dist"), exist_ok=True)
        shutil.make_archive(os.path.join(PORT_DIR, "dist", "wwhd"), "zip", out)
        print("[*] zip:", os.path.join(PORT_DIR, "dist", "wwhd.zip"))
    if args.deploy and not opt.no_register and not opt.dry_run:
        cfg = pr.load_config()
        if cfg.get("cook_url") and not os.environ.get("COOK_URL"):
            os.environ["COOK_URL"] = cfg["cook_url"]
        tf = cfg.get("token_file")
        if tf and os.path.exists(os.path.expanduser(tf)) and not os.environ.get("COOK_API_TOKEN"):
            os.environ["COOK_API_TOKEN"] = open(os.path.expanduser(tf)).read().strip()
        pr.register("wwhd")
    return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--rom", help="WiiU 덤프 루트(code/, content/, meta/)")
    parser.add_argument("--variant", choices=VARIANTS)
    parser.add_argument("--zip", action="store_true")
    parser.add_argument("--no-docker", action="store_true")
    parser.add_argument("--deploy")
    a, rest = parser.parse_known_args()
    a.extra = rest
    sys.exit(build(a))
