# tasks 끝의 문제를 고친다

## 목표
tasks 끝의 코드 평가와 하네스 eval에서 고치기로 한 것을 모두 고친다.

## 범위 밖
- 코드 평가와 하네스 eval을 다시 하는 것
- plate 자체의 하네스 고칠 거리를 고치는 것. 이슈로 올리고 plate 저장소에서 고친다

## 완료 조건
1. 작업 트리의 스킬 줄을 붙인 맡기는 글이 세션의 스킬과 작업 트리의 `SKILL.md`를 둘 다 "그 절차를 따른다"로 가리키고, 둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다 (`plugins/plate/skills/run/SKILL.md:47`)
   - 확인: `plugins/plate/skills/run/SKILL.md`의 낱말 "작업 트리의 스킬 줄"을 읽어, 붙이는 줄의 글 자체에 불러 온 스킬의 본문과 다르면 작업 트리의 파일을 따른다는 말이 있다
2. 로컬 설정 파일 `.claude/settings.local.json`이 커밋하지 않은 변경으로 잡혀 실행마다 묻게 된다. `.gitignore`에 그 파일을 더한다 (`.gitignore`)
   - 확인: `git check-ignore .claude/settings.local.json`이 그 경로를 낸다
3. tasks 완료 조건 1, 2, 3, 4, 5, 6, 7, 8이 참이다.
   - 확인: `plugins/plate/skills/plan/SKILL.md`의 6번을 읽어 네 점검이 하나씩 따로 있다. 하나라도 없으면 실패
   - 확인: 같은 파일의 절대 규칙 3과 6번을 함께 읽어, 읽을 것의 명령은 돌려 보고 확인 명령은 돌려 보지 않는다는 것이 서로 어긋나지 않게 적혀 있다
   - 확인: plan의 "조건" 절과 6번을 따로 읽어 두 줄이 저마다 있다
   - 확인: plan의 "조건" 절을 읽어 세 줄이 하나씩 있다. 하나라도 없으면 실패
   - 확인: plan의 "TODO" 절, 양식의 `phase-N.md` TODO 줄, 6번을 하나씩 읽어 세 곳이 저마다 위의 것을 적는다
   - 확인: `plugins/plate/skills/run/SKILL.md`의 4번, 5번, 7번, "코드 평가를 맡긴다", "하네스 eval을 맡긴다"를 하나씩 읽어 다섯 곳 모두에 그 줄을 붙이는 조건과 예외가 있다. 한 곳이라도 없으면 실패
   - 확인: `plugins/plate/skills/review/SKILL.md`의 낱말 절, 0번의 git 레포가 아닐 때의 줄, PR 모드 절, 평가 절 양식의 대상을 하나씩 읽어 네 곳이 저마다 위의 것과 맞는다
   - 확인: `grep -rn '바뀐 코드 파일' plugins/plate docs README.md`가 낸 줄 가운데 review 밖의 것을 하나씩 읽어, 바뀐 낱말과 어긋나는 줄이 없다
   - 확인: `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md`가 그 절과 `plugins/plate/skills/*/SKILL.md` 경로를 낸다
   - 확인: `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json`의 두 줄이 모두 `0.13.0`
   - 확인: `claude plugin validate .`의 마지막 줄이 `✔ Validation passed`
   - 확인: `python3 -m unittest discover -s tests`가 `OK`
   - 확인: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 따로 읽어, 이 tasks가 바꾼 동작(plan의 초안 전 점검, run이 넘기는 작업 트리 경로, review의 결과물인 마크다운)과 어긋나는 줄이 없다

## 결정
- 없음
