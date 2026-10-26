# run의 본문 넘기기와 고칠 phase 규칙을 고친다

## 목표
run이 `gh`로 본문을 넘기는 네 곳(PR 열기, PR 댓글, 이슈 만들기, 이슈 댓글)이 `--body-file`을 써서 bash 3.2와 권한 검사에서 깨지지 않는다(#10). run이 쓰는 고칠 phase는 파일 목록이 TODO와 맞고(#8), 통과 조건이 앞선 회고들의 재현과 같은 뿌리의 꼴까지 본다(#4).

## 범위 밖
- 회고 쪽 규칙(어긋남에서 고칠 쪽을 적는 것). `004-retro-phase`에서 한다
- 고침 task(`NNN-fixes`)의 꼴을 바꾸는 것. 테스트 먼저와 읽을 것을 고칠 phase에 맞춰 정하는 규칙은 그대로 따라온다
- `docs/TOOLS.md`에 적힌 옛 명령의 꼴. 그때 본 사실이라 고치지 않는다

## 완료 조건
1. tasks 완료 조건 6이 참이다.
   - 확인: `grep -n -- '--body ' plugins/plate/skills/run/SKILL.md`가 아무것도 내지 않는다
   - 확인: `grep -c -- '--body-file' plugins/plate/skills/run/SKILL.md`가 `4` 이상이고, "PR을 연다" 3·4번과 "이슈를 올린다" 3·4번을 하나씩 읽어 네 곳 모두 `--body-file`이다
   - 확인: `grep -n '"\$(' plugins/plate/skills/run/SKILL.md`가 네 곳의 줄을 내지 않는다
2. tasks 완료 조건 7이 참이다.
   - 확인: `plugins/plate/skills/run/SKILL.md`의 8번 본문과 고칠 phase 양식을 읽어 셋이 하나씩 있다. 파일 목록에는 TODO가 고치는 파일만 두고 쓰기 전에 TODO 글과 대어 본다. 통과 조건에 앞선 회고 절들(회고 1~K)이 적은 재현을 모두 다시 돌린다. 고친 코드에서 같은 뿌리의 꼴을 찾아 테스트로 남긴다
3. `docs/ARCHITECTURE.md`에서 고칠 phase와 PR·이슈의 본문을 적은 줄이 바뀐 run과 어긋나지 않는다.
   - 확인: `grep -n '고칠 phase\|PR의 본문\|이슈' docs/ARCHITECTURE.md`가 낸 줄을 하나씩 읽어 바뀐 run과 어긋나는 줄이 없다

## 결정
- 본문을 넘기는 네 곳을 모두 `--body-file`로 바꾼다. 이유: 이슈 본문에도 백틱이 많아 같은 식으로 깨진다
