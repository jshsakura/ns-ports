#!/bin/bash
# 컨테이너 안에서: 없는 시스템 헤더를 빈 shim 으로 채워 가며 regamedll 의 한 파일이 컴파일될 때까지 반복한다.
cd /work && bash /work/scripts/build-cs.sh > /dev/null 2>&1
for i in $(seq 1 25); do
  out=$(cmake --build /work/build-cs --target regamedll -- -k 0 2>&1)
  miss=$(echo "$out" | grep -oE "fatal error: [^:]+: No such file" | sed -E 's/fatal error: ([^:]+): .*/\1/' | sort -u)
  [ -z "$miss" ] && break
  for h in $miss; do mkdir -p "/work/scripts/shim/$(dirname $h)"; [ -e "/work/scripts/shim/$h" ] || echo "/* shim: 스위치 newlib 에 없는 헤더 */" > "/work/scripts/shim/$h"; echo "shim+ $h"; done
done
echo "$out" | grep -E "error" | sed -E 's/^[^ ]*(error:.*)/\1/' | sort | uniq -c | sort -rn | head -15
