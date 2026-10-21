#!/bin/bash
# 컨테이너 안에서 cs16-client(서버 로직 ReGameDLL_CS, 클라이언트, 봇)를 스위치용으로 크로스 빌드한다.
cd /work/cs16-client
git config --global --add safe.directory '*'
${DEVKITPRO}/devkitA64/bin/aarch64-none-elf-gcc -c -O2 -fPIC -D_GNU_SOURCE -isystem ${DEVKITPRO}/libnx/include /work/scripts/switch_stubs.c -o /work/build-stubs.o || exit 1
rm -rf /work/build-cs && mkdir -p /work/build-cs
cmake -S . -B /work/build-cs -G Ninja -DCMAKE_TOOLCHAIN_FILE=/work/scripts/switch-toolchain.cmake \
  -DCMAKE_BUILD_TYPE=Release -DBUILD_MAINUI=OFF -DNO_YAPB=ON -DCMAKE_INSTALL_PREFIX=/work/out/cs \
  && cmake --build /work/build-cs --parallel $(nproc) -v
echo "BUILD-CS-EXIT=$?"
chown -R "${HOST_UID:-0}:${HOST_GID:-0}" /work/build-cs /work/out /work/cs16-client 2>/dev/null || true
