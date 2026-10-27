# Sly Cooper 1 (Korean disc) extractor

Runs ProjectCane's own ISO extractor on Linux, so the game data can be prepared on a PC
instead of on the Switch. The Korean disc (`SCKA_200.04`) is not the USA layout, so the
extractor sources are patched on the fly with the Korean tables and routed through the
Japanese/PAL path.

Nothing from the game or from upstream is stored here. You bring the ISO and the upstream sources.

## Use

```
git clone --branch 0.5.0 https://github.com/NaGaa95/ProjectCane ProjectCane-src
CANE_SRC=$PWD/ProjectCane-src tools/sly1_extract/build.sh
tools/sly1_extract/build/cane-extract <Korean ISO> <output folder>
python3 build.py sly1 --rom <output folder> --deploy <homebrew folder>
```

Requires `g++` (C++20) and zlib headers. `kr_patch_sources.py` fails loudly if upstream changes.
The output is labelled NTSC-J with a single language slot because ProjectCane 0.5.0 has no Korean region.
The game reads its data from the folder where the NRO sits, so the output goes next to `ProjectCane.nro`.
