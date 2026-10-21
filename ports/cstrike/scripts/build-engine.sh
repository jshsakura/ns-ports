#!/bin/bash
# 컨테이너 안에서 FWGS 엔진을 --nswitch 로 빌드한다 (xash3d-fwgs/scripts/gha/build_nswitch_docker.sh 에서 엔진 부분만).
set -e
cd /work/xash3d-fwgs
git config --global --add safe.directory '*'
export PORTLIBS_ROOT=${DEVKITPRO}/portlibs
export PATH=${DEVKITPRO}/tools/bin:${DEVKITPRO}/devkitA64/bin:$PATH
export TOOL_PREFIX=aarch64-none-elf-
export CC=${TOOL_PREFIX}gcc CXX=${TOOL_PREFIX}g++ AR=${TOOL_PREFIX}gcc-ar RANLIB=${TOOL_PREFIX}gcc-ranlib
export PORTLIBS_PREFIX=${DEVKITPRO}/portlibs/switch
export PATH=$PORTLIBS_PREFIX/bin:$PATH
export ARCH="-march=armv8-a+crc+crypto -mtune=cortex-a57 -mtp=soft -fPIC -ftls-model=local-exec"
export CFLAGS="${ARCH} -O2 -ffunction-sections -fdata-sections"
export CXXFLAGS="${CFLAGS}"
export CPPFLAGS="-D__SWITCH__ -I${PORTLIBS_PREFIX}/include -isystem ${DEVKITPRO}/libnx/include"
export LDFLAGS="${ARCH} -L${PORTLIBS_PREFIX}/lib -L${DEVKITPRO}/libnx/lib"
export LIBS="-lnx"
[ -e /usr/bin/python ] || ln -s /usr/bin/python3 /usr/bin/python
make -C /work/libsolder install
dkp-pacman -R --noconfirm switch-libssh2 switch-mbedtls || true
rm -rf build pkgtemp
./waf configure -T release --nswitch ${GAMEDIR:+--gamedir=$GAMEDIR}
./waf build install --destdir=/work/out/${ENGINE_OUT:-engine} -v
echo BUILD-ENGINE-OK
chown -R "${HOST_UID:-0}:${HOST_GID:-0}" /work/out /work/xash3d-fwgs /work/libsolder 2>/dev/null || true
