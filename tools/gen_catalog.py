#!/usr/bin/env python3
"""README.md 의 포트 카탈로그 표를 ports.json 에서 만든다. 상태 칸은 ports.json 의 status 그대로다."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BEGIN, END = "<!-- catalog:begin -->", "<!-- catalog:end -->"
STATUS = {"verified": ("🎯", "실기 확인", 0), "boot-ok": ("🟡", "기동 확인", 1),
          "active": ("📦", "레시피 정리", 2), "planned": ("🧪", "기기 시험 전", 3)}


def links(p):
    pid, d = p["id"], os.path.join(ROOT, "ports", p["id"])
    out = ["[가이드](ports/%s/README.md)" % pid]
    if os.path.exists(os.path.join(d, "BUILD.md")):
        out.append("[빌드](ports/%s/BUILD.md)" % pid)
    if os.path.exists(os.path.join(d, "recipe.py")):
        out.append("[레시피](ports/%s/recipe.py)" % pid)
    if str(p.get("repository", "")).startswith("http"):
        out.append("[빌더 저장소](%s)" % p["repository"])
    if p.get("upstream"):
        out.append("[포트 소스](%s)" % p["upstream"])
    if p.get("origin"):
        out.append("[원 프로젝트](%s)" % p["origin"])
    return " · ".join(out)


def table(ports):
    rows = ["| ID | 타이틀 | 장르 / 원작 | 한글 | 자이로 | 상태 | 바로가기 |", "| :--- | :--- | :--- | :---: | :---: | :--- | :--- |"]
    for p in sorted(ports, key=lambda p: (STATUS[p["status"]][2], p["id"])):
        icon, label, _ = STATUS[p["status"]]
        rows.append("| `%s` | %s | %s | %s | %s | %s %s | %s |" % (
            p["id"], p["name"], p["category"], "✅" if p.get("korean") else "➖",
            "✅" if p.get("motion_controls") else "➖", icon, label, links(p)))
    return "\n".join(rows)


def main():
    ports = json.load(open(os.path.join(ROOT, "ports.json"), encoding="utf-8"))
    path = os.path.join(ROOT, "README.md")
    s = open(path, encoding="utf-8").read()
    head = "## 🎮 포트 카탈로그 (전체 %d종)" % len(ports)
    body = ("%s\n\n> 상태는 `ports.json` 의 `status` 를 그대로 옮긴 것이고 이 표는 `tools/gen_catalog.py` 가 만듭니다. "
            "🎯 는 실기에서 확인한 것, 🟡 는 켜지는 것까지, 📦 는 레시피만 정리한 것, 🧪 는 아직 기기에서 안 해 본 것입니다. "
            "빌더 저장소가 따로 있는 포트는 **빌더 저장소** 링크가 있습니다.\n\n%s\n%s\n%s\n" % (head, BEGIN, table(ports), END))
    if BEGIN in s:
        s = re.sub(re.escape(BEGIN) + ".*?" + re.escape(END), lambda m: BEGIN + "\n" + table(ports) + "\n" + END, s, flags=re.S)
        s = re.sub(r"## 🎮 포트 카탈로그 \(.*?\)", head, s)
    else:
        a = s.index("## 🎮 포트 카탈로그")
        b = s.index("\n---\n", a)
        s = s[:a] + body + s[b:]
    open(path, "w", encoding="utf-8").write(s)


if __name__ == "__main__":
    main()
