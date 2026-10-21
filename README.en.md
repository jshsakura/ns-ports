# NS Ports Hub (ns-ports)

Native Nintendo Switch ports of classic games with Korean localisation, motion (gyro) aiming and a one-command build.
Each port is a recipe: it fetches the upstream project at a pinned commit, applies our patches, builds it,
and assembles a ready-to-copy folder around **your own game data**.

> [!IMPORTANT]
> **You must supply your own game files.** This repository and its releases contain no ROMs, no game data and no
> copyrighted art. See [Legal](#legal).

## Quick start

```bash
git clone https://github.com/jshsakura/ns-ports.git && cd ns-ports
python3 build.py --list                                      # what is available
python3 build.py cstrike --rom /path/to/your/cstrike-valve-data --variant original --zip
```
Needs Python 3 and, for ports built from source, Docker (devkitPro image). Output goes to `ports/<id>/dist/`.
`--variant ko` builds the Korean edition, `--variant original` the stock edition.
Copy the result to `sd:/switch/<id>/` and launch it from the homebrew menu.

## Use your own files (new port)

If you already have a built `.nro`, an icon and your game data:

```bash
python3 build.py new mygame "My Game" --nro mygame.nro --icon icon.jpg
python3 build.py mygame --rom /path/to/game-data --zip
```
Put files that must be laid over the game data into `ports/mygame/overlay/`. Add `--deploy <homebrew folder>` to assemble
straight into a [CookingFoil](https://github.com/jshsakura/oc-cookingfoil) library (the app is registered through the server API
when `ns-ports.config.json` has the server address and a token file; see `ns-ports.config.example.json`).
A port that needs building from source gets a `ports/<id>/recipe.py`; `ports/cstrike` is a complete example.

## Counter-Strike 1.6

Modern Xash3D FWGS + cs16-client with touch, controller and gyro controls, bots, voice chat (headset), Korean UI and input.
Details, controls and known limits: [ports/cstrike/README.md](ports/cstrike/README.md) and `ports/cstrike/release/README-global.txt`.
Tested on a Switch Lite only.

## Legal

Code in this repository is MIT licensed. Patches to upstream projects stay under the upstream licences
(Xash3D FWGS is GPLv3). Counter-Strike and Half-Life are trademarks of Valve Corporation; this project is not affiliated
with or endorsed by Valve, Nintendo or any publisher.

## AI disclosure

This project was developed with AI coding agents (Claude Code), directed by one person in their spare time.
