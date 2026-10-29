#!/usr/bin/env python3
"""각 ports/<id>/README.md 맨 위에 '필요한 파일 + 명령어' 블록을 넣거나 갱신한다 (ports.json + slots.json 기준)."""
import json
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEGIN, END = "<!-- quick:begin -->", "<!-- quick:end -->"
ports = json.load(open(os.path.join(ROOT, "ports.json"), encoding="utf-8"))


def block(p):
    pid = p["id"]
    d = os.path.join(ROOT, "ports", pid)
    lines = [BEGIN, "## 필요한 파일과 명령어", ""]
    sp = os.path.join(d, "slots.json")
    if os.path.exists(sp):
        lines += ["| 넣을 위치 | 파일 |", "| :--- | :--- |"]
        for s in json.load(open(sp, encoding="utf-8")):
            lines.append("| `ports/%s/%s` | %s%s |" % (pid, s["path"], s["what"], " (한글 판만)" if s.get("variant") == "ko" else ""))
    else:
        lines.append("필요한 것: %s" % (p.get("required_assets") or "게임 데이터"))
        lines.append("NRO: `ports/%s/in/%s`" % (pid, p.get("nro", pid + ".nro")))
    if p.get("origin") or p.get("upstream"):
        lines.append("")
        if p.get("origin"):
            lines.append("- 원 프로젝트: %s" % p["origin"])
        if p.get("upstream"):
            lines.append("- 스위치 포트 소스: %s" % p["upstream"])
    lines += ["", "```", "python3 build.py check %s    # 빈 칸 확인" % pid, "python3 build.py %s --zip" % pid, "```", END, ""]
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
