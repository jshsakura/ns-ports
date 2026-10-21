set -e
export DEVKITPRO=/opt/devkitpro PATH=/opt/devkitpro/devkitA64/bin:/opt/devkitpro/tools/bin:/opt/devkitpro/portlibs/switch/bin:$PATH
cd /src; mkdir -p /tmp/o
ARCH="-march=armv8-a+crc+crypto -mtune=cortex-a57 -mtp=soft -fPIE"
CF="-g -O2 -ffunction-sections -Wno-parentheses -w -std=gnu11 $ARCH -D__SWITCH__ -DSTBI_NO_THREAD_LOCALS -I/opt/devkitpro/libnx/include $(aarch64-none-elf-pkg-config --cflags sdl2)"
SRCS="$(ls *.c snes/*.c) third_party/gl_core/gl_core_3_1.c third_party/opus-1.3.1-stripped/opus_decoder_amalgam.c"
for f in $SRCS; do echo "$CF -c $f -o /tmp/o/$(basename ${f%.c}).o"; done | xargs -P8 -I{} sh -c "aarch64-none-elf-gcc {}"
aarch64-none-elf-g++ -specs=/opt/devkitpro/libnx/switch.specs -g $ARCH /tmp/o/*.o -L/opt/devkitpro/libnx/lib $(aarch64-none-elf-pkg-config --libs sdl2) -lnx -lm -o /src/zelda3.elf
elf2nro /src/zelda3.elf /src/zelda3.nro --icon=/src/platform/switch/icon.jpg --nacp=/src/zelda3.nacp
