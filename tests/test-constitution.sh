#!/bin/bash
# constitution.sh가 플러그인의 AGENTS.md를 그대로 출력하는지, 그 크기가 SessionStart 상한(10,000자) 안인지 확인한다.
# 실행: bash tests/test-constitution.sh

root="$(cd "$(dirname "$0")/.." && pwd)/plugins/plate"

fail=0
t() { # 이름, 종료 코드(0이면 통과)
  if [ "$2" = 0 ]; then echo "ok    $1"; else echo "FAIL  $1"; fail=1; fi
}

out=$(bash "$root/hooks/constitution.sh" </dev/null)
t "종료 코드 0" $?
[ "$out" = "$(cat "$root/AGENTS.md")" ]
t "출력이 AGENTS.md와 같다" $?
[ "$(wc -m <"$root/AGENTS.md")" -lt 10000 ]
t "AGENTS.md가 10,000자 미만" $?
jq -e '.hooks.SessionStart[].hooks[].command | select(test("constitution\\.sh"))' "$root/hooks/hooks.json" >/dev/null
t "hooks.json의 SessionStart에 배선됨" $?

[ "$fail" = 0 ] && echo "모두 통과" || echo "실패 있음"
exit $fail
