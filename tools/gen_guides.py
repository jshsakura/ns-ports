#!/usr/bin/env python3
"""각 ports/<id>/README.md 맨 위에 '필요한 파일 + 명령어' 블록을 넣거나 갱신한다 (ports.json + slots.json 기준)."""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEGIN, END = "<!-- quick:begin -->", "<!-- quick:end -->"
sys.path.insert(0, ROOT)
import build  # noqa: E402  (칸 목록과 안내 문구를 build.py 와 똑같이 쓴다)

ports = json.load(open(os.path.join(ROOT, "ports.json"), encoding="utf-8"))


def block(p):
    pid = p["id"]
    slots = build.load_slots(pid)
    custom = os.path.join(ROOT, "ports", pid, "quick.md")  # 직접 쓴 안내가 있으면 그것을 맨 위에 쓴다
    if os.path.exists(custom):
        return "\n".join([BEGIN, open(custom, encoding="utf-8").read().rstrip(), END, ""])
    lines = [BEGIN, "## 필요한 파일과 명령어", ""]
    if slots is None:
        lines += ["이 포트는 소스부터 빌드하거나 전용 레시피를 씁니다. 필요한 것: %s" % (p.get("required_assets") or "게임 데이터"), ""]
    else:
        if not any(sl["path"] == "icon.jpg" for sl in slots):
            slots = slots + [build.ICON_SLOT]
        lines += ["**1. 받아서 둘 것**", "", "| 놓을 위치 | 무엇 | 구하는 곳 |", "| :--- | :--- | :--- |"]
        for sl in slots:
            tag = (" (한글 판만)" if sl.get("variant") == "ko" else "") + (" (선택)" if sl.get("optional") else "")
            lines.append("| `ports/%s/%s` | %s%s | %s |" % (pid, sl["path"], sl["what"], tag, (sl.get("get") or "-").replace("|", "/")))
        lines += ["", "**2. 이미지**: 앱 아이콘(`icon.jpg`, 256x256 JPEG)만 쓰이고 없으면 NRO 의 기본 아이콘을 씁니다. 이미지는 저장소에 없으니 필요하면 직접 구해 위 위치에 두세요. 배너와 스크린샷은 다루지 않습니다.", "",
                  "**3. 확인하고 실행**", "", "```", "python3 build.py guide %s    # 빈 칸과 구하는 곳 확인" % pid, "python3 build.py %s --rom <내 게임 데이터 폴더> --zip" % pid, "```"]
        prof = build._port_json(pid) or {}
        if prof.get("release"):
            lines += ["", "NRO 는 구하지 않아도 됩니다. `in/` 에 없으면 %s 릴리스 %s 에서 받아 sha256 을 확인하고 씁니다." % (prof["release"]["repo"], prof["release"]["tag"])]
    if p.get("origin") or p.get("upstream"):
        lines.append("")
        if p.get("origin"):
            lines.append("- 원 프로젝트: %s" % p["origin"])
        if p.get("upstream"):
            lines.append("- 스위치 포트 소스: %s" % p["upstream"])
    lines += [END, ""]
    return "\n".join(lines)


for p in ports:
    f = os.path.join(ROOT, "ports", p["id"], "README.md")
    if not os.path.isdir(os.path.dirname(f)):
        continue
    old = open(f, encoding="utf-8").read() if os.path.exists(f) else "# %s\n" % p.get("name", p["id"])
    if BEGIN in old:
        a, b = old.index(BEGIN), old.index(END) + len(END)
        new = old[:a] + block(p).rstrip("\n") + old[b:]
    else:
        head, _, rest = old.partition("\n")
        new = head + "\n\n" + block(p) + "\n" + rest.lstrip("\n")
    if new != old:
        open(f, "w", encoding="utf-8").write(new)
