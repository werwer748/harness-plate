# 회고

## 회고 1

**확인**
- 작업 트리의 스킬 줄을 붙인 맡기는 글이 세션의 스킬과 작업 트리의 `SKILL.md`를 둘 다 "그 절차를 따른다"로 가리키고, 둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다 (`plugins/plate/skills/run/SKILL.md:47`)
  - `plugins/plate/skills/run/SKILL.md:47`(낱말 "작업 트리의 스킬 줄")을 읽음 → 붙이는 줄의 글 자체가 `작업 트리의 {경로}를 읽어 그 절차를 따른다. 불러 온 스킬의 본문과 다르면 이 파일을 따른다.`이다. 통과
- 로컬 설정 파일 `.claude/settings.local.json`이 커밋하지 않은 변경으로 잡혀 실행마다 묻게 된다. `.gitignore`에 그 파일을 더한다 (`.gitignore`)
  - `git check-ignore .claude/settings.local.json` → `.claude/settings.local.json`(종료 코드 0). 통과
- tasks 완료 조건 1, 2, 3, 4, 5, 6, 7, 8이 참이다.
  - `plugins/plate/skills/plan/SKILL.md` 6번을 읽음 → 저장소 밖 경로, 읽을 것의 명령을 돌려 봄, 가져올 값이 기록에 있는지, 푸시·권한·인증이 막히는지(막히면 사용자의 단계로 결정에 적기)가 저마다 따로 된 항목이다. 통과
  - 같은 파일의 절대 규칙 3과 6번을 함께 읽음 → 절대 규칙 3이 "확인 명령은 미리 돌려 보지 않고 적는다. 읽을 것에 적는 명령은 6번의 점검에서 돌려 보되, 읽기만 하는 명령만"이라 6번의 읽을 것 명령 점검과 어긋나지 않는다. 통과
  - "조건" 절과 6번을 따로 읽음 → "조건"에 다른 phase의 확인 글을 옮겨 적고 가리킴만 두지 않는다는 줄, 6번에 통과 조건이 다른 phase의 확인을 가리키기만 하면 옮겨 적도록 고친다는 줄이 저마다 있다. 통과
  - "조건" 절을 읽음 → 도구가 실제로 내는 필드나 줄로 적기, 금지 `grep`을 대상 줄로 좁히기, 견줄 커밋이나 시점 적기의 세 줄이 하나씩 있다. 통과
  - "TODO" 절, 양식의 `phase-N.md` TODO 줄, 6번을 하나씩 읽음 → "TODO" 첫 항목이 자리와 바뀜의 종류(더해진다, 바뀐다, 지워진다)를 결과로 적게 하고 예도 그와 맞으며, 양식 TODO 줄이 `{무엇이 어느 자리에 어떻게(더해진다, 바뀐다, 지워진다) 바뀌는지}`이고, 6번에 다른 스킬의 낱말을 그 낱말 절과 대어 보는 줄이 있다. 통과
  - `grep -n '작업 트리의 스킬 줄' plugins/plate/skills/run/SKILL.md` → 4번(:109), 5번(:125), 7번(:147), "코드 평가를 맡긴다"(:265), "하네스 eval을 맡긴다"(:275) 다섯 곳 모두 "tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨으면" 조건과 "다른 글을 더하지 않는다는 규칙의 예외" 글이 있다. 통과
  - `plugins/plate/skills/review/SKILL.md`의 낱말 절(:32-36), 0번의 git 레포가 아닐 때(:52), PR 모드 절(:173), 평가 절 양식의 대상(:212-218)과 적는 규칙(:270)을 읽음 → 결과물인 마크다운을 넣고 절이 없으면 `.md`를 빼며, PR 모드는 기준 브랜치의 `docs/ARCHITECTURE.md`에서 읽는다는 것과 저마다 맞는다. 통과
  - `grep -rn '바뀐 코드 파일' plugins/plate docs README.md` 가운데 review 밖 → `docs/ARCHITECTURE.md:82`와 `docs/tasks/` 아래의 계획·기록 줄뿐이고, 읽어 보니 바뀐 낱말과 어긋나는 줄이 없다. 통과
  - `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83-- \`plugins/plate/skills/*/SKILL.md\``. 통과
  - `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.13.0",`. 통과
  - `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.903s`, `OK`. 통과
  - `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 grep(`작업 트리`, `reload-plugins`, `그 절차를 따른다`, `settings.local`, `gitignore`)하고 걸린 줄을 읽음 → `ARCHITECTURE.md:44`(작업 트리의 스킬 줄 예외), `:47`(`.gitignore`의 `__pycache__`), `:81-83`, `TOOLS.md:84`(새 줄 꼴과 같음)가 바뀐 동작과 맞고, PRD, ADR, README에는 어긋나는 줄이 없다. 통과
- 명령 절
  - 빌드: 없음
  - 린트: 없음
  - 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 15.903s`, `OK`. 통과

**문제**
- 없음

**판정**: 통과
