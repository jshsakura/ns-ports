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
Add `--zip` for a zip.
Copy the result to `sd:/switch/<id>/` and launch it from the homebrew menu.

- `source`: the recipe fetches the upstream project, applies our patches and builds the NRO in Docker.
- `assemble`: you provide the built NRO; the tool lays our settings and your data around it.
- `--variant` is accepted by every port. A port that does not tell the two apart yet says so and uses its default.

## Per port / 포트별 필요한 것

| Port | Game data you provide | Kind | NRO | Upstream |
| --- | --- | --- | --- | --- |
| `0ad` | 0ad-0.28.0 데이터 (data/) | assemble | place your built `0ad.nro` in `ports/0ad/in/` | souldbminerr/0ad-switch |
| `avp-gold` | AvP Gold / Classic 2000 PC 게임 데이터 | assemble | place your built `avp.nro` in `ports/avp-gold/in/` | Thorhax/AvP-Gold-NX-Modern v2026-nx, downloaded |
| `caesar3` | Caesar 3 PC 설치 데이터 | assemble | place your built `caesar3.nro` in `ports/caesar3/in/` | bvschaik/julius |
| `cannonball` | OutRun 아케이드 ROM 세트 | assemble | place your built `cannonball.nro` in `ports/cannonball/in/` | Thorhax/Cannonball-NX-Modern v1.08-nx, downloaded |
| `cnc` | C&C Gold .MIX 파일 및 영상 에셋 | assemble | place your built `vanillatd.nro` in `ports/cnc/in/` | TheAssemblyArmada/Vanilla-Conquer |
| `cstrike` | 정품 cstrike/ 및 valve/ 데이터 | source | built on your machine | FWGS/xash3d-fwgs |
| `dantes-inferno` | Xbox 360 디스크 game 폴더(bigfile0.viv, bigfile1.viv, default.xex, default.xexp 타이틀 업데이트 2)와 dante_shaders.dslib, shadercache_dksh.bin | assemble | place your built `dantes-inferno-nx.nro` in `ports/dantes-inferno/in/` | VasilkovND/dantes-inferno-nx v1.1.0, built |
| `daytona-usa` | MAME Model 2 daytona.zip (Rev A) 롬 | assemble | place your built `Daytona.nro` in `ports/daytona-usa/in/` | Thorhax/Daytona-NX-Modern v1.1.0, downloaded |
| `devilutionx` | DIABDAT.MPQ (원작 PC CD 데이터) | assemble | place your built `devilutionx.nro` in `ports/devilutionx/in/` | diasurgical/DevilutionX 1.5.5, downloaded |
| `doom` | 자체 무료 IWAD 포함 (상용 IWAD 추가 지원) | assemble | place your built `gzdoom_launcher.nro` in `ports/doom/in/` | fgsfdsfgs/gzdoom nx4.11pre-2, downloaded |
| `doom64` | doom64.wad, doomsnd.sf2 | assemble | place your built `doom64ex.nro` in `ports/doom64/in/` | fgsfdsfgs/Doom64EX v0.2.0-nx, downloaded |
| `doukutsu-rs` | Cave Story 게임 데이터 (data/) | assemble | place your built `doukutsu-rs.nro` in `ports/doukutsu-rs/in/` | - |
| `dragonball-z-rpg` | 게임 에셋 | assemble | place your built `DragonballZrpg.nro` in `ports/dragonball-z-rpg/in/` | white-axe/mkxp-z libretro 2.4.2, downloaded |
| `fallout1` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout1.nro` in `ports/fallout1/in/` | alexbatalov/fallout1-ce |
| `fallout2` | master.dat, critter.dat (PC판 데이터) | assemble | place your built `fallout2.nro` in `ports/fallout2/in/` | alexbatalov/fallout2-ce |
| `fheroes2` | HOMM2 원작 게임 데이터 (HEROES2/DATA) | assemble | place your built `fheroes2.nro` in `ports/fheroes2/in/` | ihhub/fheroes2 |
| `futari` | Xbox 360판 벌레공주 두 사람 게임 데이터 | assemble | place your built `futari-nx.nro` in `ports/futari/in/` | ChanseyIsTheBest/futari-nx v1.0.3, downloaded |
| `ge007` | baserom.j.z64 (일본판 순정 ROM) | source (separate repo) | built on your machine | - |
| `half-life` | valve/ 폴더 (원작 PC 게임 데이터) | assemble | place your built `half-life.nro` in `ports/half-life/in/` | FWGS/xash3d-fwgs 4211 |
| `hurrican` | data/, lang/ | assemble | place your built `hurrican.nro` in `ports/hurrican/in/` | rsn8887/Hurrican |
| `jak1` | Jak 1 PS2 ISO | assemble | place your built `jak1.nro` in `ports/jak1/in/` | fildicio/jak-project-switch |
| `jak2` | Jak 2 PS2 ISO (정발판) | assemble | place your built `jak2.nro` in `ports/jak2/in/` | fildicio/jak-project-switch |
| `jak3` | Jak 3 PS2 ISO (정발판) | assemble | place your built `jak3.nro` in `ports/jak3/in/` | fildicio/jak-project-switch |
| `jazz` | 원작 PC 설치 데이터 (Source/) | assemble | place your built `jazz.nro` in `ports/jazz/in/` | deathkiller/jazz2 3.8.0, downloaded |
| `marathon-recomp` | Xbox 360판 소닉 06 디스크 데이터 | assemble | place your built `MarathonRecomp.nro` in `ports/marathon-recomp/in/` | ChanseyIsTheBest/MarathonRecomp-NX 1.0.3, downloaded |
| `masseffect` | Xbox 360판 매스 이펙트 1 게임 데이터 | assemble | place your built `masseffect-nx.nro` in `ports/masseffect/in/` | nebadasSwifty/masseffect-nx v0.2.1, downloaded |
| `nfsmw` | Xbox 360 NTSC-K 디스크의 game_root 폴더와 셰이더 파일(nfsmw_shaders.nfsp) | assemble | place your built `nfsmw-nx.nro` in `ports/nfsmw/in/` | StevensND/nfsmw-nx v1.0.0, downloaded |
| `nzportable` | 자체 무료 데이터 포함 (독립 실행형) | assemble | place your built `nzportable.nro` in `ports/nzportable/in/` | nzp-team/nzportable v2.0.0, downloaded |
| `openbor` | OpenBOR .pak 게임 팩 | assemble | place your built `OpenBOR.nro` in `ports/openbor/in/` | SylphiaWindy/openbor switch-v26.0919.1, downloaded |
| `openmw` | Morrowind Data Files (Morrowind.esm 등) | assemble | place your built `openmw.nro` in `ports/openmw/in/` | fgsfdsfgs/openmw 0.46.0-nx4, downloaded |
| `openrct2` | RCT2 설치 파일 | source | built on your machine | Wander-Eule/OpenRCT2-Switch 7d4673d8b2 + Korean patch, built |
| `openttd` | 오픈 그래픽/사운드 베이스셋 | assemble | place your built `openttd.nro` in `ports/openttd/in/` | rsn8887/OpenTTD v1.07-switch, downloaded |
| `opentyrian` | 자체 무료 풀버전 데이터 포함 | assemble | place your built `opentyrian.nro` in `ports/opentyrian/in/` | theflippedbit/opentyrian-nx v1.0.0, downloaded |
| `pokemmo` | GBA/NDS 포켓몬 롬 (FireRed, Emerald, Platinum, Black/White) | assemble | place your built `pokemmo.nro` in `ports/pokemmo/in/` | Petit-Prince-dev/PokeMMO-NX v1.1.4, downloaded |
| `pokemon-survivor-burst` | 원작자 배포본 게임 폴더 (Audio/, Data/, Fonts/, Graphics/, Plugins/, lib/) | assemble | place your built `pokemon-survivor-burst.nro` in `ports/pokemon-survivor-burst/in/` | randygil/rgss-switch |
| `project8` | Xbox 360판 토니 호크 프로젝트 8 게임 데이터 | assemble | place your built `project8-sw.nro` in `ports/project8/in/` | R-drg/project8-sw v1.0.0, downloaded |
| `pvz` | Plants vs. Zombies PC판 main.pak | assemble | place your built `pvz.nro` in `ports/pvz/in/` | HayatoG/PvZ-Portable v2026.07.02, downloaded |
| `redalert` | Red Alert CD1/CD2 .MIX 파일 | assemble | place your built `vanillara.nro` in `ports/redalert/in/` | TheAssemblyArmada/Vanilla-Conquer |
| `ro` | 라그나로크 클라이언트 데이터(data.grf, rdata.grf)와 접속 설정(login.ini) | assemble | place your built `ragnarok.nro` in `ports/ro/in/` | - |
| `sa2` | Xbox 360판 소닉 어드벤처 2 게임 데이터 | assemble | place your built `sa2-nx.nro` in `ports/sa2/in/` | ChanseyIsTheBest/sa2-nx v1.0.3.1, downloaded |
| `sh1` | PS1 사일런트 힐 1 롬 데이터 | assemble | place your built `silent-hill.nro` in `ports/sh1/in/` | ChaykaDed/silent-hill-decomp-nx 1.2.0, downloaded |
| `sh2` | 사일런트 힐 2 PC판(Enhanced Edition) 설치본 | assemble | place your built `sh2.nro` in `ports/sh2/in/` | cutarev/sh2-nx v1.02, downloaded |
| `sh3` | 사일런트 힐 3 PC판 설치본 | assemble | place your built `sh3.nro` in `ports/sh3/in/` | cutarev/sh3-nx v0.06, downloaded |
| `sh4` | 사일런트 힐 4 GOG PC판 설치본 | assemble | place your built `sh4.nro` in `ports/sh4/in/` | 72ak/sh4-nx v0.1, downloaded |
| `sly1` | 슬라이 쿠퍼 1 PS2 ISO (미국 SCUS-971.98, 유럽 SCES-509.17, 일본 SCPS-150.36 중 하나) | assemble | place your built `ProjectCane.nro` in `ports/sly1/in/` | NaGaa95/ProjectCane 0.5.0, downloaded |
| `sonic-cd` | Data.rsdk (Steam/모바일 리마스터 데이터) | assemble | place your built `scd2011.nro` in `ports/sonic-cd/in/` | heyjoeway/Sonic-CD-11-Decompilation 1.3.0, downloaded |
| `sonic-fighters` | MAME Model 2 sfight.zip 롬 | assemble | place your built `sonic_the_fighters.nro` in `ports/sonic-fighters/in/` | boraeskicioglu/sonic_the_fighters_nx 0.8.3, downloaded |
| `sonic1` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s12013.nro` in `ports/sonic1/in/` | heyjoeway/Sonic-1-2-2013-Decompilation 1.3.0rev1, downloaded |
| `sonic2` | Data.rsdk (모바일 2013 리마스터 데이터) | assemble | place your built `s22013.nro` in `ports/sonic2/in/` | heyjoeway/Sonic-1-2-2013-Decompilation 1.3.0rev1, downloaded |
| `space-cadet` | Windows 3D Pinball 사운드 및 테이블 데이터 | assemble | place your built `SpaceCadetPinball.nro` in `ports/space-cadet/in/` | averne/SpaceCadetPinball-NX 1.1.1-NX3, downloaded |
| `srb2` | 자체 무료 풀버전 데이터 포함 | assemble | place your built `srb2switch22.nro` in `ports/srb2/in/` | P-AS/srb2-switch v2.2.13, downloaded |
| `starcraft64` | StarCraft 64 (USA) ROM (.z64) | assemble | place your built `starcraft64.nro` in `ports/starcraft64/in/` | gabryboy12-ai/StarCraft64-NX v0.5, built |
| `supermariowar` | 자체 무료 풀버전 데이터 포함 | assemble | place your built `smw.nro` in `ports/supermariowar/in/` | retronx-team/supermariowar-nx 2.0.0-nx5, downloaded |
| `supertux2` | 게임 데이터 (data/) | assemble | place your built `supertux2.nro` in `ports/supertux2/in/` | - |
| `supertuxkart` | SuperTuxKart-1.5 데이터 (data/) | assemble | place your built `supertuxkart.nro` in `ports/supertuxkart/in/` | - |
| `torchlight` | Xbox 360판 토치라이트 게임 데이터 | assemble | place your built `torchlight-nx.nro` in `ports/torchlight/in/` | liartes/torchlight-nx v1.0.2, downloaded |
| `undertale-yellow` | Undertale Yellow 무료 게임 데이터 | assemble | place your built `UndertaleYellow.nro` in `ports/undertale-yellow/in/` | NalienDev/Undertale-Yellow-NX v1.0, downloaded |
| `vcmi` | HOMM3 Data 및 Maps 폴더 | assemble | place your built `vcmi.nro` in `ports/vcmi/in/` | NaGaa95/vcmi_nx 1.8.0-R2, downloaded |
| `vf2` | MAME Model 2 vf2.zip 롬 | assemble | place your built `VF2.nro` in `ports/vf2/in/` | Thorhax/VF2-NX-Modern v1.1.0, downloaded |
| `virtual-on` | MAME Model 2 von.zip 롬 | assemble | place your built `Virtual-On.nro` in `ports/virtual-on/in/` | Thorhax/Virtual-On-NX v1.2.0, downloaded |
| `war1gus` | DATA.WAR 등 DOS/Mac 원작 데이터 | assemble | place your built `war1gus.nro` in `ports/war1gus/in/` | Thorhax/War1gus-NX-Modern v3.3.3-nx, downloaded |
| `wargus` | Warcraft II BNE CD 데이터 | assemble | place your built `wargus.nro` in `ports/wargus/in/` | Thorhax/Wargus-NX-Modern v3.3.2-nx.2, downloaded |
| `wwhd` | WiiU 덤프 루트(code/, content/, meta/)와 한글 패치 파일(permanent_2d_UsEnglish.pack, Title_00.szs) | assemble | place your built `wwhd.nro` in `ports/wwhd/in/` | centollOS/SwitchWakerHD 9a57081, built |
| `zelda-mm-hd` | mm.o2r, 2ship.o2r, mods/MM_Reloaded_v11.0.3_HD.o2r, 2ship2harkinian.json | assemble | place your built `zelda-mm-hd.nro` in `ports/zelda-mm-hd/in/` | 2ship2harkinian/2ship2harkinian |
| `zelda-olb` | 자체 무료 데이터 포함 | assemble | place your built `ZeldaOLB.nro` in `ports/zelda-olb/in/` | worthis/ZeldaOLB-new-engine 1.1.1, downloaded |
| `zelda-oot-hd` | oot.o2r, soh.o2r, mods/OoT_Reloaded_Korean_Pretendard_HD.o2r, shipofharkinian.json | assemble | place your built `zelda-oot-hd.nro` in `ports/zelda-oot-hd/in/` | HarbourMasters/Shipwright |
| `zelda-roth` | 자체 무료 데이터 포함 | assemble | place your built `ZeldaROTH.nro` in `ports/zelda-roth/in/` | worthis/ZeldaROTH-new-engine 1.1.4, downloaded |
| `zelda3-ko` | zelda3_assets.dat | source | built on your machine | snesrev/zelda3 |
| `zelda3t` | data/ (images, maps, musics, sounds, texts) | assemble | place your built `zelda3t.nro` in `ports/zelda3t/in/` | worthis/Zelda3T |

Upstream is the project and version the port is based on, and whether the NRO was downloaded or built (recovered from our old work logs; `-` when not recorded). This table is generated by `tools/gen_install.py` from `ports.json`; edit that file, not this one.
