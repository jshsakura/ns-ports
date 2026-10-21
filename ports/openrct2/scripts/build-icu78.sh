#!/bin/sh
# Cross-builds ICU 78.1 for the Switch (the original port ships ICU 78) and commits it as openrct2-builder:icu78.
set -e
cd "$(dirname "$0")"
docker rm -f icu78-build >/dev/null 2>&1 || true
docker run --name icu78-build -v "$PWD:/w" -w /w openrct2-builder:full sh -c '
set -e
rm -rf src host sw && mkdir src host sw && tar xzf icu4c-78.1-sources.tgz -C src
cd host && ../src/icu/source/runConfigureICU Linux >/dev/null && make -j$(nproc) >/dev/null 2>&1 && cd ..
cd sw
export PATH=/opt/devkitpro/devkitA64/bin:$PATH
F="-march=armv8-a+crc+crypto -mtune=cortex-a57 -mtp=soft -fPIE -O2 -D__SWITCH__ -D_GNU_SOURCE -DU_HAVE_STRTOD_L=0 -DU_USING_ICU_NAMESPACE=0"
CC=aarch64-none-elf-gcc CXX=aarch64-none-elf-g++ AR=aarch64-none-elf-ar RANLIB=aarch64-none-elf-ranlib \
CFLAGS="$F" CXXFLAGS="$F -std=gnu++17" \
../src/icu/source/configure --host=aarch64-none-elf --with-cross-build=/w/host --prefix=/opt/devkitpro/portlibs/switch \
  --enable-static --disable-shared --disable-tools --disable-extras --disable-tests --disable-samples --disable-icuio --disable-layoutex >/dev/null
make -j$(nproc) 2>&1 | tail -3
make install >/dev/null 2>&1
ls -la /opt/devkitpro/portlibs/switch/lib/libicudata.a'
docker commit icu78-build openrct2-builder:icu78 >/dev/null
docker rm icu78-build >/dev/null
