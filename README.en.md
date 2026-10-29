# NS Ports Hub (ns-ports)

Personal notes from my own tests of running old games on the Nintendo Switch as native ports with Korean localisation.
This is a record of what I tried, not a service or a release. Ports I have checked on a real console are marked as verified in the status column; the rest are recipes or not yet checked. Each port folder lists which
file went where under what name; `build.py` is a small helper that packs them into a homebrew folder the same way.
No game data, NRO or patched assets are included, and nothing is fetched for you.

> [!IMPORTANT]
> **You must supply your own game files.** This repository and its releases contain no ROMs, no game data and no
> copyrighted art. See [Legal](#legal).

## Per-port guides

Requirements for every port are in [INSTALL.md](INSTALL.md); the Korean localisation method itself lives in each
`ports/<id>/README.md`. Example, Wind Waker HD ([guide](ports/wwhd/README.md)):

| File you provide | Where to put it |
| --- | --- |
| SwitchWakerHD build NRO | `ports/wwhd/in/wwhd.nro` |
| Korean patch `permanent_2d_UsEnglish.pack` | `ports/wwhd/in/permanent_2d_UsEnglish.pack` |
| Korean patch `Title_00.szs` | `ports/wwhd/in/Title_00.szs` |

```bash
python3 build.py wwhd --rom /path/to/wwhd-dump --zip                   # Korean edition
python3 build.py wwhd --rom /path/to/wwhd-dump --variant original --zip  # stock edition
```

`--rom` points at the Wii U dump root where `content/` is visible. Python 3 is enough for assembly;
ports marked `source` in INSTALL.md build their NRO in Docker (devkitPro image), and GoldenEye 007 uses its own
builder repo that BPS-patches your `baserom.j.z64`.

`python3 build.py guide <id>` lists what to get, where to put it and which command to run: the empty input slots with where to get each, the image note, then the build command. The same check runs before every build. Slots come from `ports/<id>/slots.json`, or from `port.json` and `ports.json` when that file is absent.

Images: none are shipped. Only the app icon is used (optional): put your own 256x256 JPEG at `ports/<id>/icon.jpg`, otherwise the NRO's own icon is kept. Banners and screenshots are not handled here.

## Use your own files (new port)

If you already have a built `.nro`, an icon and your game data:

```bash
python3 build.py new mygame "My Game" --nro mygame.nro --icon icon.jpg
python3 build.py mygame --rom /path/to/game-data --zip
```
Put files that must be laid over the game data into `ports/mygame/overlay/`.
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
