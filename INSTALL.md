# Install / 설치

Every port is built and installed the same way. 모든 포트의 설치법은 같습니다.

## What you need / 공통 준비물

| Need | Why |
| --- | --- |
| Python 3.8+ | runs `build.py` and the assembler |
| Docker (devkitPro image) | only for ports built from source (`source` below) |
| git | fetches upstream sources at pinned commits |
| **Your own game data** | no ROM or game file is included in this project |
| A Nintendo Switch with custom firmware | to run the result (`sd:/switch/<id>/`) |

## Steps / 순서

```bash
git clone https://github.com/jshsakura/ns-ports.git && cd ns-ports
python3 build.py <port-id> --rom <your game data> --variant ko        # Korean edition
python3 build.py <port-id> --rom <your game data> --variant original  # stock edition
```
Add `--zip` for a zip, or `--deploy <homebrew folder>` to assemble straight into a CookingFoil library.
Copy the result to `sd:/switch/<id>/` and launch it from the homebrew menu.

- `source`: the recipe fetches the upstream project, applies our patches and builds the NRO in Docker.
- `assemble`: you provide the built NRO; the tool lays our settings and your data around it.
- `--variant` is accepted by every port. A port that does not tell the two apart yet says so and uses its default.

## Per port / 포트별 필요한 것

| Port | Game data you provide | Kind | NRO | Upstream |
| --- | --- | --- | --- | --- |
| `caesar3` | Caesar 3 PC 설치 데이터 | assemble | place your built `caesar3.nro` in `ports/caesar3/in/` | - |
| `cannonball` | OutRun 아케이드 ROM 세트 | assemble | place your built `cannonball.nro` in `ports/cannonball/in/` | Thorhax/Cannonball-NX-Modern |
| `cnc` | C&C Gold .MIX 파일 및 영상 에셋 | assemble | place your built `vanillatd.nro` in `ports/cnc/in/` | - |
| `cstrike` | 정품 cstrike/ 및 valve/ 데이터 | source | built on your machine | FWGS/xash3d-fwgs |
| `devilutionx` | DIABDAT.MPQ (원작 PC CD 데이터) | assemble | place your built `devilutionx.nro` in `ports/devilutionx/in/` | - |
| `doom64` | doom64.wad, doomsnd.sf2 | assemble | place your built `doom64ex.nro` in `ports/doom64/in/` | - |
| `dragonball-z-rpg` | 게임 에셋 | assemble | place your built `DragonballZrpg.nro` in `ports/dragonball-z-rpg/in/` | white-axe/mkxp-z |
| `fallout1` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout1.nro` in `ports/fallout1/in/` | - |
| `fallout2` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout2.nro` in `ports/fallout2/in/` | - |
| `fheroes2` | HOMM2 원작 게임 데이터 (HEROES2/DATA) | assemble | place your built `fheroes2.nro` in `ports/fheroes2/in/` | ihhub/fheroes2 |
| `ge007` | baserom.j.z64 (일본판 순정 ROM) | source (separate repo) | built on your machine | - |
| `half-life` | valve/ 폴더 (원작 PC 게임 데이터) | assemble | place your built `half-life.nro` in `ports/half-life/in/` | FWGS/xash3d-fwgs |
| `jak1` | Jak 1 PS2 ISO | assemble | place your built `jak1.nro` in `ports/jak1/in/` | fildicio/jak-project-switch |
| `jak2` | Jak 2 PS2 ISO (정발판) | assemble | place your built `jak2.nro` in `ports/jak2/in/` | fildicio/jak-project-switch |
| `jak3` | Jak 3 PS2 ISO (정발판) | assemble | place your built `jak3.nro` in `ports/jak3/in/` | fildicio/jak-project-switch |
| `jazz` | 원작 PC 설치 데이터 (Source/) | assemble | place your built `jazz.nro` in `ports/jazz/in/` | - |
| `openrct2` | RCT2 설치 파일 | assemble | place your built `openrct2.nro` in `ports/openrct2/in/` | rsn8887/OpenRCT2 |
| `openttd` | 오픈 그래픽/사운드 베이스셋 | assemble | place your built `openttd.nro` in `ports/openttd/in/` | rsn8887/OpenTTD |
| `pokemon-survivor-burst` | 게임 데이터 리소스 | assemble | place your built `pokemon-survivor-burst.nro` in `ports/pokemon-survivor-burst/in/` | - |
| `redalert` | Red Alert CD1/CD2 .MIX 파일 | assemble | place your built `vanillara.nro` in `ports/redalert/in/` | - |
| `sm64-hd` | N64 ROM (baserom.us.z64) | assemble | place your built `sm64-hd.nro` in `ports/sm64-hd/in/` | - |
| `sonic-cd` | Data.rsdk (Steam/모바일 리마스터 데이터) | assemble | place your built `scd2011.nro` in `ports/sonic-cd/in/` | - |
| `sonic1` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s12013.nro` in `ports/sonic1/in/` | heyjoeway/Sonic-1-2-2013-Decompilation |
| `sonic2` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s22013.nro` in `ports/sonic2/in/` | heyjoeway/Sonic-1-2-2013-Decompilation |
| `starcraft64` | StarCraft 64 (USA) ROM (.z64) | assemble | place your built `starcraft64.nro` in `ports/starcraft64/in/` | - |
| `war1gus` | DATA.WAR 등 DOS/Mac 원작 데이터 | assemble | place your built `war1gus.nro` in `ports/war1gus/in/` | Thorhax/War1gus-NX-Modern |
| `wargus` | Warcraft II BNE CD 데이터 | assemble | place your built `wargus.nro` in `ports/wargus/in/` | Thorhax/Wargus-NX-Modern |
| `wwhd` | 게임 데이터 | assemble | place your built `wwhd.nro` in `ports/wwhd/in/` | - |
| `zelda-mm-hd` | mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json | assemble | place your built `zelda-mm-hd.nro` in `ports/zelda-mm-hd/in/` | - |
| `zelda-oot-hd` | oot.o2r, soh.o2r, mods/OoT_Reloaded_Korean_Pretendard_HD.o2r, shipofharkinian.json | assemble | place your built `zelda-oot-hd.nro` in `ports/zelda-oot-hd/in/` | - |
| `zelda3-ko` | zelda3_assets.dat | source | built on your machine | snesrev/zelda3 |

Upstream is the project the port is based on (blank when not recorded yet). This table is generated by `tools/gen_install.py` from `ports.json`; edit that file, not this one.
