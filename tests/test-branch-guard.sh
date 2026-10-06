#!/bin/bash
# branch-guard.sh에 훅 입력을 넣어 종료 코드를 확인한다(0 통과, 2 차단).
# 임시 레포를 만들어 쓰고 끝나면 지운다. 실행: bash tests/test-branch-guard.sh

hook="$(cd "$(dirname "$0")/.." && pwd)/plugins/plate/hooks/branch-guard.sh"
tmp=$(mktemp -d) && trap 'rm -rf "$tmp"' EXIT
repo="$tmp/repo"
mkdir -p "$repo" "$tmp/norepo"
git -C "$repo" init -q -b main
git -C "$repo" -c user.name=t -c user.email=t@t commit -q --allow-empty -m init

fail=0
t() { # 이름, 기대 종료 코드, 훅 입력(JSON)
  printf '%s' "$3" | bash "$hook" >/dev/null 2>&1
  local got=$?
  if [ "$got" = "$2" ]; then echo "ok    $1"; else echo "FAIL  $1 (기대 $2, 실제 $got)"; fail=1; fi
}
edit() { jq -nc --arg t "$1" --arg f "$2" --arg s "${3:-sess-A}" '{tool_name:$t,session_id:$s,cwd:"/",tool_input:{file_path:$f}}'; }
cmd() { jq -nc --arg c "$1" --arg d "$2" --arg s "${3:-sess-A}" '{tool_name:"Bash",session_id:$s,cwd:$d,tool_input:{command:$c}}'; }

echo "== main, 승인 없음 =="
t "Write: 레포 안"                2 "$(edit Write "$repo/a.md")"
t "Edit: 레포 안"                 2 "$(edit Edit "$repo/a.md")"
t "Write: 아직 없는 하위 폴더"    2 "$(edit Write "$repo/new/deep/a.md")"
t "Write: 레포 밖"                0 "$(edit Write "$tmp/norepo/a.md")"
t "git commit"                    2 "$(cmd 'git commit -m x' "$repo")"
t "add && commit 연결"            2 "$(cmd 'cd . && git add -A && git commit -q -m y' "$repo")"
t "git -C <경로> commit"          2 "$(cmd "git -C $repo commit -m x" "$repo")"
t "줄바꿈 뒤 git commit"          2 "$(cmd $'git add -A\ngit commit -m x' "$repo")"
t "git status"                    0 "$(cmd 'git status --short' "$repo")"
t "git log --grep commit"         0 "$(cmd 'git log --grep commit' "$repo")"
t "git commit-tree"               0 "$(cmd 'git commit-tree HEAD^{tree}' "$repo")"
t "ls"                            0 "$(cmd 'ls -la' "$repo")"
t "git commit: 레포 밖"           0 "$(cmd 'git commit -m x' "$tmp/norepo")"

echo "== main, 세션 승인 =="
echo sess-A >"$repo/.git/plate-main-ok"
t "승인한 세션의 Write"           0 "$(edit Write "$repo/a.md" sess-A)"
t "승인한 세션의 git commit"      0 "$(cmd 'git commit -m x' "$repo" sess-A)"
t "다른 세션은 여전히 차단"       2 "$(edit Write "$repo/a.md" sess-B)"
rm "$repo/.git/plate-main-ok"

echo "== 다른 브랜치, detached HEAD =="
git -C "$repo" switch -q -c feat
t "작업 브랜치의 Write"           0 "$(edit Write "$repo/a.md")"
t "작업 브랜치의 git commit"      0 "$(cmd 'git commit -m x' "$repo")"
git -C "$repo" switch -q --detach
t "detached HEAD"                 0 "$(edit Write "$repo/a.md")"

[ "$fail" = 0 ] && echo "모두 통과" || echo "실패 있음"
exit $fail
