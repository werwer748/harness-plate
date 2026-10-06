#!/bin/bash
# branch-guard — PreToolUse(Edit|Write|NotebookEdit|Bash)
# 막는 실패: 의도하지 않은 채 기본 브랜치(main·master)에서 작업하고 커밋하는 것.
#   2026-10-04 세션 8d4fb7ce에서 두 번째 커밋이 묻지 않고 main에 올라갔다.
# 동작: 기본 브랜치에서 레포 안 파일을 고치거나 `git commit`을 하려 하면 막고,
#   브랜치를 만들지 사용자에게 묻게 한다. 사용자가 기본 브랜치에서 하겠다고 하면
#   <git-dir>/plate-main-ok에 세션 ID를 적어 그 세션에서만 통과시킨다.
# 한계: Bash는 `git commit`만 보고(셸로 파일을 쓰는 것은 막지 않는다) 레포를 cwd로 판단한다.

input=$(cat)
session=$(jq -r '.session_id // empty' <<<"$input")

if [ "$(jq -r '.tool_name // empty' <<<"$input")" = "Bash" ]; then
  jq -r '.tool_input.command // empty' <<<"$input" |
    grep -Eq '(^|[;&|([:space:]])git([[:space:]]+-[cC][[:space:]]+[^[:space:]]+)*[[:space:]]+commit([[:space:]]|$)' || exit 0
  dir=$(jq -r '.cwd // empty' <<<"$input")
else
  # 고칠 파일이 있는 레포를 본다. 새 폴더에 쓰는 경우에는 이미 있는 상위 폴더까지 올라간다.
  dir=$(dirname "$(jq -r '.tool_input.file_path // .tool_input.notebook_path // empty' <<<"$input")")
  while [ ! -d "$dir" ] && [ "$dir" != "/" ]; do dir=$(dirname "$dir"); done
fi

# 레포 밖이거나 detached HEAD면 통과한다.
branch=$(git -C "$dir" symbolic-ref --short -q HEAD 2>/dev/null) || exit 0
case "$branch" in main | master) ;; *) exit 0 ;; esac

ok="$(git -C "$dir" rev-parse --absolute-git-dir)/plate-main-ok"
[ -n "$session" ] && [ "$(cat "$ok" 2>/dev/null)" = "$session" ] && exit 0

cat >&2 <<EOF
branch-guard: 지금 '$branch' 브랜치다. 이 작업을 위한 브랜치를 만들지 사용자에게 먼저 물어라(AskUserQuestion).
- 만든다고 하면: git switch -c <브랜치 이름> 을 실행한 뒤 다시 시도한다.
- $branch 에서 하겠다고 하면: echo $session > "$ok" 을 실행한 뒤 다시 시도한다(이 세션에서만 통한다).
사용자에게 묻지 않고 위 파일을 만들지 않는다.
EOF
exit 2
