# Phase 1: tasks 끝의 문제를 고친다

**목표**: task 머리의 완료 조건에 적힌 것을 모두 고친다.

**테스트 먼저**: 아니오 — `.md`와 `.gitignore`만 고쳐 테스트가 보는 코드의 동작이 바뀌지 않는다

**읽을 것**
- `docs/tasks/review.md`의 `## 평가 1` 절
- `docs/tasks/eval.md`의 `## eval 1` 절
- `plugins/plate/skills/run/SKILL.md`
- `.gitignore`
- `docs/PRD.md`
- `docs/ARCHITECTURE.md`
- `docs/ADR.md`
- `docs/TOOLS.md`

**TODO**
- [x] 작업 트리의 스킬 줄을 붙인 맡기는 글이 세션의 스킬과 작업 트리의 `SKILL.md`를 둘 다 "그 절차를 따른다"로 가리키고, 둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다 (`plugins/plate/skills/run/SKILL.md`)
- [x] 로컬 설정 파일 `.claude/settings.local.json`이 커밋하지 않은 변경으로 잡혀 실행마다 묻게 된다. `.gitignore`에 그 파일을 더한다 (`.gitignore`)

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 확인: 완료 조건의 확인을 모두 돌린다

## 한 일
- 작업 트리의 스킬 줄을 붙인 맡기는 글이 …둘이 다를 때 작업 트리 쪽을 따르라는 말이 띄운 에이전트가 받는 글에 없다: run의 낱말 "작업 트리의 스킬 줄"이 정한 줄의 꼴이 `작업 트리의 {경로}를 읽어 그 절차를 따른다. 불러 온 스킬의 본문과 다르면 이 파일을 따른다.`로 바뀌었다. 같은 줄의 꼴을 옮겨 적은 `docs/TOOLS.md:84`도 같은 꼴로 바꿨다 (`plugins/plate/skills/run/SKILL.md`, `docs/TOOLS.md`)
- 로컬 설정 파일 `.claude/settings.local.json`이 …`.gitignore`에 그 파일을 더한다: `.gitignore` 끝에 `.claude/settings.local.json` 줄이 더해졌다 (`.gitignore`)

## 확인 결과
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/run/SKILL.md:47`을 읽음 → 붙이는 줄의 글 자체에 "불러 온 스킬의 본문과 다르면 이 파일을 따른다."가 있다. 통과
  - 완료 조건 2: `git check-ignore .claude/settings.local.json` → `.claude/settings.local.json`. 통과
  - 완료 조건 3, plan 6번의 네 점검: `plugins/plate/skills/plan/SKILL.md:98`, `:99`, `:100`, `:101`을 읽음 → 저장소 밖 경로, 읽을 것의 명령, 가져올 값, 푸시·권한·인증 점검이 하나씩 따로 있다. 통과
  - 완료 조건 3, 절대 규칙 3과 6번: `plan/SKILL.md:18`과 `:99`를 함께 읽음 → 확인 명령은 미리 돌리지 않고, 읽을 것의 명령은 6번에서 읽기만 하는 것만 돌린다로 갈려 어긋나지 않는다. 통과
  - 완료 조건 3, 다른 phase의 확인 옮겨 적기: "조건" 절 `plan/SKILL.md:235`와 6번 `:102`를 읽음 → 두 줄이 저마다 있다. 통과
  - 완료 조건 3, "조건"의 세 줄: `plan/SKILL.md:236`, `:237`, `:238`을 읽음 → 도구가 내는 필드나 줄, 금지 `grep`을 대상 줄로 좁힘, 견줄 커밋이나 시점이 하나씩 있다. 통과
  - 완료 조건 3, TODO: "TODO" 절 `plan/SKILL.md:268`, 양식 TODO 줄 `:194`, 6번 `:103`을 읽음 → 268과 194가 자리와 바뀜의 종류를 적고, 103이 다른 스킬의 낱말 절과 대어 보라고 적는다. 통과
  - 완료 조건 3, run의 다섯 곳: `sed -n '109p;125p;147p;265p;275p' plugins/plate/skills/run/SKILL.md | grep -c '작업 트리의 스킬 줄을 붙인다. 이 줄은 다른 글을 더하지 않는다는 규칙의 예외다'` → `5`. 다섯 줄 모두 "tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨으면" 조건을 단다. 통과
  - 완료 조건 3, review의 네 곳: `plugins/plate/skills/review/SKILL.md:32-36`(낱말), `:52`(git 레포가 아닐 때), `:173`(PR 모드가 기준 브랜치에서 읽음), `:215`, `:218`, `:270`(평가 절의 대상)을 읽음 → 결과물인 마크다운을 넣고 절이 없으면 `.md`를 뺀다는 것과 맞는다. 통과
  - 완료 조건 3, `grep -rn '바뀐 코드 파일' plugins/plate docs README.md` → review 밖의 줄은 `docs/ARCHITECTURE.md:82`와 `docs/tasks/` 아래의 계획·기록 줄뿐이고 읽어 보니 바뀐 낱말과 어긋나지 않는다. 통과
  - 완료 조건 3, `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83:- \`plugins/plate/skills/*/SKILL.md\``. 통과
  - 완료 조건 3, `grep -h '"version"' plugins/plate/.claude-plugin/plugin.json plugins/plate/.codex-plugin/plugin.json` → 두 줄 모두 `"version": "0.13.0",`. 통과
  - 완료 조건 3, `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 3, `python3 -m unittest discover -s tests` → `OK`. 통과
  - 완료 조건 3, 맥락 문서: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 보고 `작업 트리`, `reload-plugins`, `새 세션`, `초안`, `결과물인 마크다운`으로 grep → `ARCHITECTURE.md:44`의 스킬 호출 예외와 `:81-83`의 절, `TOOLS.md:84`(이번에 새 줄 꼴로 바꿈), `README.md:25`가 바뀐 동작과 맞고, PRD와 ADR에는 걸리는 줄이 없다. 통과

## 계획과 달라진 점
- TODO에 적힌 파일은 `run/SKILL.md`와 `.gitignore`뿐이지만 `docs/TOOLS.md:84`도 고쳤다. 그 줄이 작업 트리의 스킬 줄의 꼴을 그대로 옮겨 적고 있어, 두지 않으면 완료 조건 3의 맥락 문서 확인(바뀐 동작과 어긋나는 줄이 없다)이 실패한다.

## 남은 것
- 이미 이 세션에서 돌고 있는 run은 고치기 전의 줄 꼴을 쓴다. 바뀐 줄은 다음에 run 본문을 실을 때(새 세션이나 `/reload-plugins`)부터 붙는다.
- 완료 조건 3의 "tasks 완료 조건 1~8"은 tasks 머리를 읽지 않는 이 스킬의 규칙대로 task 머리에 옮겨 적힌 확인만 돌렸다.

## 하네스에서 걸린 것
- task 머리 완료 조건 3이 "tasks 완료 조건 1, 2, …, 8이 참이다"로 tasks 머리를 가리키는데, phase 스킬은 tasks 머리를 읽지 않는다. 아래 확인 글이 옮겨 적혀 있어 그것으로 돌렸지만, 확인 글의 "네 점검", "세 줄", "위의 것"이 무엇인지는 task 머리만으로 알 수 없어 `docs/tasks/review.md` 평가 1의 완료 조건 절(읽을 것에 든 곳)에서 찾았다.

## 확인 1

**통과 조건**
- task 머리의 완료 조건이 모두 참이다.
  - 완료 조건 1: `plugins/plate/skills/run/SKILL.md:47`(낱말 "작업 트리의 스킬 줄")을 읽음 → 붙이는 줄의 글 자체가 `작업 트리의 {경로}를 읽어 그 절차를 따른다. 불러 온 스킬의 본문과 다르면 이 파일을 따른다.`이다. 통과
  - 완료 조건 2: `git check-ignore .claude/settings.local.json` → `.claude/settings.local.json`(종료 코드 0). 통과
  - 완료 조건 3, plan 6번의 네 점검(`docs/tasks/plan.md` 완료 조건 1의 뜻): `plugins/plate/skills/plan/SKILL.md` 6번을 읽음 → 저장소 밖 경로(:99), 읽을 것의 명령을 돌려 봄(:100), 가져올 값이 기록에 있는지(:101), 푸시·권한·인증이 막히는지와 결정에 사용자의 단계로 적기(:102)가 하나씩 따로 있다. 통과
  - 완료 조건 3, 절대 규칙 3과 6번: `plan/SKILL.md:18`과 6번을 함께 읽음 → 절대 규칙 3이 확인 명령은 미리 돌리지 않고 읽을 것의 명령은 6번에서 읽기만 하는 것만 돌린다고 적어, 6번(:100)과 어긋나지 않는다. 통과
  - 완료 조건 3, "조건"과 6번의 두 줄: "조건" 절에 다른 phase의 확인 글을 옮겨 적고 가리킴만 두지 않는다는 줄, 6번에 통과 조건이 다른 phase를 가리키면 옮겨 적도록 고친다는 줄이 저마다 있다. 통과
  - 완료 조건 3, "조건"의 세 줄: 도구가 실제로 내는 필드나 줄로 적기, 금지 `grep`을 대상 줄로 좁히기, 견줄 커밋이나 시점 적기가 하나씩 있다. 통과
  - 완료 조건 3, TODO 세 곳: "TODO" 절 첫 항목이 자리와 바뀜의 종류(더해진다, 바뀐다, 지워진다)를 적게 하고 예도 그와 맞으며, 양식의 TODO 줄이 `{무엇이 어느 자리에 어떻게(더해진다, 바뀐다, 지워진다) 바뀌는지}`이고, 6번에 다른 스킬의 낱말을 그 낱말 절과 대어 보는 줄이 있다. 통과
  - 완료 조건 3, run의 다섯 곳: `grep -n '작업 트리의 스킬 줄' plugins/plate/skills/run/SKILL.md` → 4번(:109), 5번(:125), 7번(:147), "코드 평가를 맡긴다"(:265), "하네스 eval을 맡긴다"(:275) 다섯 곳 모두 "tasks 커밋이 그 스킬의 `SKILL.md`를 바꿨으면" 조건과 "다른 글을 더하지 않는다는 규칙의 예외" 글이 있다. 통과
  - 완료 조건 3, review의 네 곳: `plugins/plate/skills/review/SKILL.md` 낱말(:32-36), git 레포가 아닐 때(:52), PR 모드(:173), 평가 절 양식과 적는 규칙(:215-218, :270)을 읽음 → 결과물인 마크다운을 넣고 절이 없으면 `.md`를 빼며 PR 모드는 기준 브랜치에서 읽는다는 것과 저마다 맞는다. 통과
  - 완료 조건 3, `grep -rn '바뀐 코드 파일' plugins/plate docs README.md` 가운데 review 밖 → `docs/ARCHITECTURE.md:82`와 `docs/tasks/` 아래 계획·기록 줄뿐이고, 읽어 보니 바뀐 낱말과 어긋나는 줄이 없다. 통과
  - 완료 조건 3, `grep -n -A3 '^## 결과물인 마크다운' docs/ARCHITECTURE.md` → `81:## 결과물인 마크다운`, `83-- \`plugins/plate/skills/*/SKILL.md\``. 통과
  - 완료 조건 3, `grep -h '"version"' …plugin.json` 두 개 → 두 줄 모두 `"version": "0.13.0",`. 통과
  - 완료 조건 3, `claude plugin validate .` → 마지막 줄 `✔ Validation passed`. 통과
  - 완료 조건 3, `python3 -m unittest discover -s tests` → `Ran 99 tests`, `OK`. 통과
  - 완료 조건 3, 맥락 문서: `docs/PRD.md`, `docs/ARCHITECTURE.md`, `docs/ADR.md`, `docs/TOOLS.md`, `README.md`를 문서마다 grep(`작업 트리`, `reload-plugins`, `초안`, `결과물인 마크다운`, `review`, `점검`)하고 걸린 줄을 읽음 → `ARCHITECTURE.md:44`, `:51`, `:73`, `:81-83`, `TOOLS.md:82`, `:84`(새 줄 꼴과 같음), `README.md:25`가 바뀐 동작과 맞고, PRD와 ADR에는 어긋나는 줄이 없다. 통과

**명령**
- 빌드: 없음
- 린트: 없음
- 테스트: `python3 -m unittest discover -s tests` → `Ran 99 tests in 14.324s`, `OK`. 통과

**실패**
- 없음

**하네스에서 걸린 것**
- task 머리 완료 조건 3의 확인 글("네 점검", "세 줄", "위의 것")이 무엇을 가리키는지 task 머리만으로는 알 수 없어, 그 뜻을 `docs/tasks/plan.md`의 완료 조건 1~6에서 읽고 판정했다.

**판정**: 통과
