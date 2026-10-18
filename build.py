#!/usr/bin/env python3
"""
Retro NX Ports Hub - Master Build & Management CLI
Curated collection of classic game native ports for NX / Horizon OS.
"""

import os
import sys
import json
import argparse
import importlib.util

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
        mark = "[RECIPE]" if recipe_exists else f"[{status}]"
        print(f"  {pid:<16} {name:<32} {kor:<6} {gyro:<6} {mark}")
    print("=" * 85)
    print(f"Total: {len(ports)} ports registered in catalogue.")
    print("Usage: python3 build.py <port-id> [options]")

def run_port(port_id, extra_args):
    recipe_path = os.path.join(ROOT_DIR, "ports", port_id, "recipe.py")
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

    return module.build(args)

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-l", "--list", "list"):
        list_ports()
        return 0

    port_id = sys.argv[1]
    if port_id in ("-h", "--help"):
        print("Retro NX Ports Hub CLI")
        print("Commands:")
        print("  python3 build.py --list                 List all ports")
        print("  python3 build.py <port-id> [options]    Build a specific port")
        return 0

    return run_port(port_id, sys.argv[2:])

if __name__ == "__main__":
    sys.exit(main())
