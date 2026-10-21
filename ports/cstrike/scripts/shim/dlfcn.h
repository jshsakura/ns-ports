/* devkitA64 의 newlib 에는 dlfcn.h 가 없다. 엔진 NRO 가 내보내는 solder_dl* 로 연결한다. */
#pragma once
#define SOLDER_LIBDL_COMPAT
#include <solder.h>
#undef dladdr
#define dladdr(x, y) solder_dladdr((void *)(x), (y))
