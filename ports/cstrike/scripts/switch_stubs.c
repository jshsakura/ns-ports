/* 엔진 NRO 가 내보내지 않는 libc 심볼의 대체 구현. 게임 .so 마다 정적으로 들어간다.
 * 확인 방법: nm -D --undefined-only <so> 와 nm -D --defined-only src/xash3d-fwgs/build/engine/xash 를 comm 으로 비교.
 * 파일 접근 계열은 "없는 것으로 응답" 하는 임시 구현이다. dl* 은 shim/dlfcn.h 가 solder_dl* 로 잇고, ctype 은 엔진이 내보낸다. */
#include <stdio.h>
#include <errno.h>
#include <stdarg.h>
#include <stddef.h>
#include <wchar.h>


int isdigit(int c) { return c >= '0' && c <= '9'; }
#undef feof
int feof(FILE *f) { return (f->_flags & 0x20) != 0; }


int creat(const char *p, unsigned m) { (void)p; (void)m; errno = ENOSYS; return -1; }
int getppid(void) { return 1; }
int getpid(void) { return 1; }
int access(const char *p, int m) { (void)p; (void)m; errno = ENOENT; return -1; }
int unlink(const char *p) { (void)p; errno = ENOENT; return -1; }
int mkstemp(char *t) { (void)t; errno = ENOSYS; return -1; }
long sysconf(int n) { (void)n; return -1; }
int fnmatch(const char *p, const char *s, int f) { (void)p; (void)s; (void)f; return 1; }
int vswprintf(wchar_t *s, size_t n, const wchar_t *f, va_list a) { (void)s; (void)n; (void)f; (void)a; return -1; }
