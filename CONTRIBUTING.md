# Contributing / 기여 안내

Add a port by opening a pull request that contains `ports/<id>/` (and one entry in `ports.json`):

- `port.json` (profile), `README.md`, `patches/` for upstream changes, `overlay*/` for files laid over the game data.
- A `recipe.py` only if the port must be built from source (pin upstream commits; see `ports/cstrike/recipe.py`).
- **No** ROMs, game data, copyrighted art, built binaries, IP addresses, personal paths or tokens. Untracked helpers
  such as `ns-ports.config.json` and `favorites.txt` stay out of git.
- Check the whole diff for IPv4 addresses, e-mail addresses and long hex strings before pushing.

포트 추가는 `ports/<id>/` 와 `ports.json` 항목 하나를 담은 PR 로 받습니다. 게임 데이터, 롬, 저작권 이미지, 빌드 산출물,
IP 와 개인 경로, 토큰은 넣지 않습니다. 푸시 전에 diff 에서 IP, 이메일, 긴 16진 문자열을 확인해 주세요.

## Images and other assets you cannot redistribute / 재배포가 애매한 에셋
Do not commit them. Put a link in `port.json` and the assembler downloads and verifies it on the user's machine:
`"icon_url": "...", "icon_sha256": "..."` for the app icon, or `"downloads": [{"url": "...", "sha256": "...", "dest": "path/in/package"}]`.
Credit the author in the port README. 링크만 두고, 받는 쪽에서 내려받아 해시를 확인합니다.

## Where a port lives / 포트가 있어야 할 곳
Everything lives in this repository, as patches, overlays and a recipe on top of a pinned upstream. The one exception is a
port that is a full source tree of its own (today only `ge007`, a decompilation with its own history): it keeps its own repository
and `ports/<id>/recipe.py` just clones it, so the install steps stay identical.
업스트림에 패치를 얹는 포트는 전부 이 저장소에 두고, 자체 소스 트리를 통째로 가진 포트(지금은 `ge007` 하나)만 별도 저장소로 두고 레시피로 연결합니다.
