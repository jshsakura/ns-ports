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
| `sly1` | 슬라이 쿠퍼 1 PS2 ISO (미국/유럽/일본판, SD 카드에 두면 앱이 직접 풀어 줍니다) | assemble | place `ProjectCane.nro` as `ports/sly1/in/sly1.nro` | NaGaa95/ProjectCane 0.5.0, downloaded |
| `nfsmw` | Xbox 360 NTSC-K 디스크의 game_root 와 nfsmw_shaders.nfsp | assemble | place `nfsmw-nx-kor.nro` as `ports/nfsmw/in/nfsmw.nro` | StevensND/nfsmw-nx v1.0.0, downloaded |
| `cannonball` | OutRun 아케이드 ROM 세트 | assemble | place your built `cannonball.nro` in `ports/cannonball/in/` | Thorhax/Cannonball-NX-Modern v1.08-nx, downloaded |
| `cnc` | C&C Gold .MIX 파일 및 영상 에셋 | assemble | place your built `vanillatd.nro` in `ports/cnc/in/` | - |
| `cstrike` | 정품 cstrike/ 및 valve/ 데이터 | source | built on your machine | FWGS/xash3d-fwgs |
| `devilutionx` | DIABDAT.MPQ (원작 PC CD 데이터) | assemble | place your built `devilutionx.nro` in `ports/devilutionx/in/` | diasurgical/DevilutionX 1.5.5, downloaded |
| `doom64` | doom64.wad, doomsnd.sf2 | assemble | place your built `doom64ex.nro` in `ports/doom64/in/` | fgsfdsfgs/Doom64EX v0.2.0-nx, downloaded |
| `dragonball-z-rpg` | 게임 에셋 | assemble | place your built `DragonballZrpg.nro` in `ports/dragonball-z-rpg/in/` | white-axe/mkxp-z libretro 2.4.2, downloaded |
| `fallout1` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout1.nro` in `ports/fallout1/in/` | - |
| `fallout2` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout2.nro` in `ports/fallout2/in/` | - |
| `fheroes2` | HOMM2 원작 게임 데이터 (HEROES2/DATA) | assemble | place your built `fheroes2.nro` in `ports/fheroes2/in/` | ihhub/fheroes2 |
| `ge007` | baserom.j.z64 (일본판 순정 ROM) | source (separate repo) | built on your machine | - |
| `half-life` | valve/ 폴더 (원작 PC 게임 데이터) | assemble | place your built `half-life.nro` in `ports/half-life/in/` | FWGS/xash3d-fwgs 4211 |
| `jak1` | Jak 1 PS2 ISO | assemble | place your built `jak1.nro` in `ports/jak1/in/` | fildicio/jak-project-switch |
| `jak2` | Jak 2 PS2 ISO (정발판) | assemble | place your built `jak2.nro` in `ports/jak2/in/` | fildicio/jak-project-switch |
| `jak3` | Jak 3 PS2 ISO (정발판) | assemble | place your built `jak3.nro` in `ports/jak3/in/` | fildicio/jak-project-switch |
| `jazz` | 원작 PC 설치 데이터 (Source/) | assemble | place your built `jazz.nro` in `ports/jazz/in/` | deathkiller/jazz2 3.8.0, downloaded |
| `openbor` | OpenBOR .pak 게임 팩 | assemble | place your built `OpenBOR.nro` in `ports/openbor/in/` | SylphiaWindy/openbor switch-v26.0919.1, downloaded |
| `openrct2` | RCT2 설치 파일 | source | built on your machine | Wander-Eule/OpenRCT2-Switch 7d4673d8b2 + Korean patch, built |
| `openttd` | 오픈 그래픽/사운드 베이스셋 | assemble | place your built `openttd.nro` in `ports/openttd/in/` | rsn8887/OpenTTD v1.07-switch, downloaded |
| `pokemon-survivor-burst` | 게임 데이터 리소스 | assemble | place your built `pokemon-survivor-burst.nro` in `ports/pokemon-survivor-burst/in/` | - |
| `redalert` | Red Alert CD1/CD2 .MIX 파일 | assemble | place your built `vanillara.nro` in `ports/redalert/in/` | - |
| `sonic-cd` | Data.rsdk (Steam/모바일 리마스터 데이터) | assemble | place your built `scd2011.nro` in `ports/sonic-cd/in/` | heyjoeway/Sonic-CD-11-Decompilation 1.3.0, downloaded |
| `sonic1` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s12013.nro` in `ports/sonic1/in/` | heyjoeway/Sonic-1-2-2013-Decompilation 1.3.0rev1, downloaded |
| `sonic2` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s22013.nro` in `ports/sonic2/in/` | heyjoeway/Sonic-1-2-2013-Decompilation 1.3.0rev1, downloaded |
| `starcraft64` | StarCraft 64 (USA) ROM (.z64) | assemble | place your built `starcraft64.nro` in `ports/starcraft64/in/` | gabryboy12-ai/StarCraft64-NX v0.5, built |
| `war1gus` | DATA.WAR 등 DOS/Mac 원작 데이터 | assemble | place your built `war1gus.nro` in `ports/war1gus/in/` | Thorhax/War1gus-NX-Modern v3.3.3-nx, downloaded |
| `wargus` | Warcraft II BNE CD 데이터 | assemble | place your built `wargus.nro` in `ports/wargus/in/` | Thorhax/Wargus-NX-Modern v3.3.2-nx.2, downloaded |
| `wwhd` | 게임 데이터 | assemble | place your built `wwhd.nro` in `ports/wwhd/in/` | centollOS/SwitchWakerHD 9a57081, built |
| `zelda-mm-hd` | mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json | assemble | place your built `zelda-mm-hd.nro` in `ports/zelda-mm-hd/in/` | - |
| `zelda-oot-hd` | oot.o2r, soh.o2r, mods/OoT_Reloaded_Korean_Pretendard_HD.o2r, shipofharkinian.json | assemble | place your built `zelda-oot-hd.nro` in `ports/zelda-oot-hd/in/` | - |
| `zelda3-ko` | zelda3_assets.dat | source | built on your machine | snesrev/zelda3 |

Upstream is the project and version the port is based on, and whether the NRO was downloaded or built (recovered from our old work logs; `-` when not recorded). This table is generated by `tools/gen_install.py` from `ports.json`; edit that file, not this one.
